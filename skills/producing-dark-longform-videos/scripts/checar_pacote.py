#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida a skill antes de publicar e, se pedido, monta o zip para upload.

Uso:
    python scripts/checar_pacote.py [--zip SAIDA.zip] [--dir PASTA_DA_SKILL] [--forcar]

Cada checagem imprime OK, ERRO ou AVISO. Código de saída 0 se não houver ERRO, 1 se houver.

Checa:
  1. SKILL.md: frontmatter YAML (parse simples), name = nome da pasta e só [a-z0-9-],
     description começando com "Use when", frontmatter com menos de 1024 caracteres.
  2. Caminhos entre crases nos .md (agents/, references/, scripts/, dossie-modelo.md) existem.
  3. Citações "NN §X" apontam para seção que existe (usa o parser de scripts/build_index.py).
  4. references/INDEX.md está atualizado (regerado em memória, numa cópia temporária).
  5. Cada script de scripts/ responde a --help sem erro (numa cópia temporária, com timeout,
     para que um script sem --help que execute a tarefa não altere a skill).
  6. Palavras: SKILL.md (aviso acima de 700) e cada briefing em agents/ (aviso acima de 900).
  7. Arquivos indesejados: __pycache__, .pyc, .DS_Store, .whl, arquivos acima de 2 MB e o que
     parece segredo (tokens de API, chaves privadas).
  8. Com --zip: monta o zip com a pasta da skill na raiz (formato aceito pelo upload do claude.ai).
     Sem ERRO, o zip sai; com ERRO, só com --forcar (lixo que o zip exclui não conta).

Só usa a biblioteca padrão (Python 3.10+). Não altera a skill: o que precisa executar roda
numa cópia em diretório temporário.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True  # importar build_index não pode criar __pycache__ na skill

# ---------------------------------------------------------------------------
# Configuração (fácil de editar)
# ---------------------------------------------------------------------------

MAX_FRONTMATTER = 1024        # caracteres do bloco de frontmatter, delimitadores incluídos
MAX_PALAVRAS_SKILL = 700
MAX_PALAVRAS_BRIEFING = 900
MAX_BYTES_ARQUIVO = 2 * 1024 * 1024
TIMEOUT_HELP_S = 20

NOMES_LIXO = {".DS_Store", "Thumbs.db", ".gitignore", ".gitattributes"}
DIRS_LIXO = {"__pycache__", ".git", ".idea", ".vscode", ".pytest_cache", ".mypy_cache", "node_modules"}
EXT_LIXO = {".pyc", ".pyo", ".whl", ".zip", ".swp", ".bak", ".tmp"}

# Padrões de segredo. Exigem um corpo longo depois do prefixo, para não acusar texto que apenas
# cita o prefixo (e para este arquivo não se acusar).
SEGREDOS = {
    "chave Anthropic": re.compile(r"sk-ant-[A-Za-z0-9_\-]{16,}"),
    "chave estilo OpenAI": re.compile(r"\bsk-[A-Za-z0-9]{32,}"),
    "token GitHub": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}"),
    "token GitHub (fine-grained)": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "token Apify": re.compile(r"apify_api_[A-Za-z0-9]{16,}"),
    "chave AWS": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "chave Google": re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}"),
    "token Slack": re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}"),
    "chave privada": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY"),
    "atribuição de segredo": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|token|password|senha)\b\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{20,}['\"]"),
}

# Caminhos citados entre crases.
RE_CRASES = re.compile(r"`([^`\n]+)`")
RE_CAMINHO = re.compile(
    r"(?<![\w/.\-])((?:agents|references|scripts)/[\w*.\-]+|dossie-modelo\.md|INDEX\.md"
    r"|\d{2}_[\w*]+\.md|[\w\-]+\.py)(?![\w/\-])")
RE_REF_DOC = re.compile(
    r"(?P<doc>(?<![\w/.])\d{2}(?:_[a-z0-9_]+(?:\.md)?)?)`?(?=[ ,(]*§)|§§?\s*(?P<sec>\d+(?:\.\d+)*)")


# ---------------------------------------------------------------------------
# Relatório
# ---------------------------------------------------------------------------

class Relatorio:
    def __init__(self) -> None:
        self.n = {"OK": 0, "ERRO": 0, "AVISO": 0}
        self.sanaveis = 0  # ERROs que o zip resolve sozinho (lixo que ele exclui)

    def _p(self, nivel: str, msg: str) -> None:
        self.n[nivel] += 1
        print(f"{nivel:<5} {msg}")

    def ok(self, msg: str) -> None:
        self._p("OK", msg)

    def erro(self, msg: str, excluido_no_zip: bool = False) -> None:
        self._p("ERRO", msg)
        if excluido_no_zip:
            self.sanaveis += 1

    def aviso(self, msg: str) -> None:
        self._p("AVISO", msg)

    def secao(self, titulo: str) -> None:
        print(f"\n== {titulo}")


def lixo_do_nome(rel: Path) -> str | None:
    """Motivo pelo qual um caminho relativo não deve ir para o pacote, ou None."""
    partes = rel.parts
    for p in partes[:-1]:
        if p in DIRS_LIXO:
            return f"pasta {p}"
    nome = rel.name
    if nome in NOMES_LIXO:
        return nome
    if rel.suffix.lower() in EXT_LIXO:
        return f"extensão {rel.suffix.lower()}"
    if nome.startswith("._"):
        return "resíduo do macOS"
    return None


def arquivos(raiz: Path):
    """Todos os arquivos sob raiz (caminho relativo), sem seguir links simbólicos de pasta."""
    for p in sorted(raiz.rglob("*")):
        if p.is_file() and not p.is_symlink():
            yield p.relative_to(raiz)
        elif p.is_symlink():
            yield p.relative_to(raiz)


# ---------------------------------------------------------------------------
# 1. Frontmatter
# ---------------------------------------------------------------------------

def parse_frontmatter(texto: str):
    """Devolve (bloco_bruto, dict, erro). Parse simples de 'chave: valor' com continuação por indentação."""
    linhas = texto.split("\n")
    if not linhas or linhas[0].strip() != "---":
        return None, {}, "SKILL.md não começa com '---'"
    fim = None
    for i in range(1, len(linhas)):
        if linhas[i].strip() == "---":
            fim = i
            break
    if fim is None:
        return None, {}, "frontmatter sem '---' de fechamento"
    bloco = "\n".join(linhas[: fim + 1])
    dados: dict[str, str] = {}
    chave = None
    for ln in linhas[1:fim]:
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        if ln[0] in " \t":
            if chave is None:
                return bloco, dados, f"linha indentada sem chave: {ln.strip()[:40]!r}"
            dados[chave] += " " + ln.strip()
            continue
        m = re.match(r"^([A-Za-z_][\w\-]*)\s*:\s*(.*)$", ln)
        if not m:
            return bloco, dados, f"linha fora do formato 'chave: valor': {ln[:50]!r}"
        chave, val = m.group(1), m.group(2).strip()
        if chave in dados:
            return bloco, dados, f"chave repetida: {chave}"
        if val in (">", ">-", "|", "|-"):
            val = ""
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        elif val[:1] in "\"'":
            return bloco, dados, f"aspas não fechadas em {chave}"
        dados[chave] = val
    return bloco, dados, None


def checar_frontmatter(skill: Path, r: Relatorio) -> None:
    r.secao("SKILL.md: frontmatter")
    arq = skill / "SKILL.md"
    if not arq.is_file():
        r.erro("SKILL.md não existe")
        return
    texto = arq.read_text(encoding="utf-8")
    bloco, d, err = parse_frontmatter(texto)
    if err:
        r.erro(f"frontmatter inválido: {err}")
        if bloco is None:
            return
    else:
        r.ok("frontmatter YAML válido (parse simples)")
    nome = d.get("name", "")
    if not nome:
        r.erro("falta 'name'")
    else:
        if nome != skill.name:
            r.erro(f"name '{nome}' difere do nome da pasta '{skill.name}'")
        else:
            r.ok(f"name '{nome}' igual ao nome da pasta")
        if not re.fullmatch(r"[a-z0-9-]+", nome):
            r.erro(f"name '{nome}' tem caracteres fora de [a-z0-9-]")
        elif len(nome) > 64:
            r.erro(f"name tem {len(nome)} caracteres (máximo 64)")
        else:
            r.ok("name usa só [a-z0-9-]")
        if re.search(r"anthropic|claude", nome):
            r.aviso("name contém palavra reservada (anthropic/claude); o upload pode recusar")
    desc = d.get("description", "")
    if not desc:
        r.erro("falta 'description'")
    else:
        if desc.startswith("Use when"):
            r.ok("description começa com 'Use when'")
        else:
            r.erro(f"description não começa com 'Use when' (começa com {desc[:30]!r})")
        if len(desc) > 1024:
            r.erro(f"description tem {len(desc)} caracteres (máximo 1024)")
        if re.search(r"[<>]", desc):
            r.aviso("description contém '<' ou '>'; o upload pode recusar tags")
    if bloco is not None:
        n = len(bloco)
        if n >= MAX_FRONTMATTER:
            r.erro(f"frontmatter tem {n} caracteres (limite: menos de {MAX_FRONTMATTER})")
        else:
            r.ok(f"frontmatter com {n} caracteres (< {MAX_FRONTMATTER})")
    # campos aceitos pela especificação de skills (agentskills.io): os demais geram aviso
    extras = sorted(set(d) - {"name", "description", "license", "allowed-tools", "metadata", "compatibility"})
    if extras:
        r.aviso(f"chaves fora da especificação no frontmatter: {', '.join(extras)}")


# ---------------------------------------------------------------------------
# 2 e 3. Caminhos e citações
# ---------------------------------------------------------------------------

def md_da_skill(skill: Path) -> list[Path]:
    return sorted(p for p in skill.rglob("*.md")
                  if not any(x in DIRS_LIXO for x in p.relative_to(skill).parts))


def resolve_caminho(skill: Path, cit: str) -> list[Path]:
    """Lista os arquivos que o caminho citado designa (vazia se não existe)."""
    if cit == "INDEX.md":
        alvos = [skill / "references" / "INDEX.md"]
    elif re.fullmatch(r"\d{2}_[\w*]+\.md", cit):
        return sorted((skill / "references").glob(cit))
    elif "/" not in cit and cit.endswith(".py"):
        alvos = [skill / "scripts" / cit]
    else:
        alvos = [skill / cit]
    if any("*" in str(a) for a in alvos):
        return sorted(alvos[0].parent.glob(alvos[0].name))
    return [a for a in alvos if a.exists()]


def checar_caminhos(skill: Path, r: Relatorio) -> None:
    r.secao("Caminhos citados entre crases")
    total, falhas = 0, 0
    for md in md_da_skill(skill):
        rel = md.relative_to(skill)
        em_ref = rel.parts[0] == "references"
        in_code = False
        for i, linha in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if linha.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for span in RE_CRASES.findall(linha):
                for cit in RE_CAMINHO.findall(span):
                    total += 1
                    if not resolve_caminho(skill, cit):
                        falhas += 1
                        msg = f"{rel}:{i}: `{cit}` não existe"
                        (r.aviso if em_ref else r.erro)(msg)
    if falhas == 0:
        r.ok(f"{total} caminho(s) citado(s), todos existem")
    # briefings que o SKILL.md não cita
    skill_md = (skill / "SKILL.md").read_text(encoding="utf-8") if (skill / "SKILL.md").is_file() else ""
    for ag in sorted((skill / "agents").glob("*.md")):
        if f"agents/{ag.name}" not in skill_md:
            r.aviso(f"agents/{ag.name} não é citado no SKILL.md")


def carregar_build_index(skill: Path):
    caminho = skill / "scripts" / "build_index.py"
    if not caminho.is_file():
        return None
    spec = importlib.util.spec_from_file_location("build_index_skill", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def secoes_por_doc(bi, skill: Path) -> dict[str, set[str]]:
    secoes = {}
    for p in sorted((skill / "references").glob("[0-9][0-9]_*.md")):
        _, entradas = bi.parse(p)
        secoes[p.name[:2]] = {e["num"] for e in entradas if e["num"]}
    return secoes


def checar_citacoes(skill: Path, bi, r: Relatorio) -> None:
    r.secao("Citações 'NN §X'")
    if bi is None:
        r.erro("scripts/build_index.py ausente: não dá para listar as seções")
        return
    secoes = secoes_por_doc(bi, skill)
    total, falhas = 0, 0
    for md in md_da_skill(skill):
        rel = md.relative_to(skill)
        if rel.name == "INDEX.md":
            continue
        em_ref = rel.parts[0] == "references"
        in_code = False
        for i, linha in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if linha.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            doc, direta = None, False
            for m in RE_REF_DOC.finditer(linha):
                if m.group("doc"):
                    d = m.group("doc")[:2]
                    doc, direta = (d if d in secoes else None), True
                    continue
                if doc is None:
                    continue
                total += 1
                sec = m.group("sec")
                if sec not in secoes[doc]:
                    falhas += 1
                    msg = f"{rel}:{i}: `{doc}` §{sec} não existe"
                    # a citação encadeada ("`10` §3, §4.5") herda o documento: só aviso
                    (r.erro if direta and not em_ref else r.aviso)(msg)
                direta = False
    if falhas == 0:
        r.ok(f"{total} citação(ões) de seção, todas existem")


# ---------------------------------------------------------------------------
# 4. INDEX.md
# ---------------------------------------------------------------------------

def checar_index(skill: Path, bi, r: Relatorio) -> None:
    r.secao("references/INDEX.md")
    atual = skill / "references" / "INDEX.md"
    if bi is None:
        r.erro("scripts/build_index.py ausente")
        return
    if not atual.is_file():
        r.erro("references/INDEX.md não existe: rode build_index.py")
        return
    with tempfile.TemporaryDirectory(prefix="checar_pacote_") as tmp:
        ref_tmp = Path(tmp) / "references"
        ref_tmp.mkdir()
        for p in (skill / "references").glob("*.md"):
            if p.name != "INDEX.md":
                shutil.copy2(p, ref_tmp / p.name)
        original = bi.REF
        bi.REF = ref_tmp
        saida, erros = io.StringIO(), io.StringIO()
        try:
            with contextlib.redirect_stdout(saida), contextlib.redirect_stderr(erros):
                bi.main()
        except SystemExit as e:
            r.erro(f"build_index.py falhou: {str(e.code).strip()[:300]}")
            return
        except Exception as e:  # noqa: BLE001
            r.erro(f"build_index.py levantou {type(e).__name__}: {e}")
            return
        finally:
            bi.REF = original
        novo = (ref_tmp / "INDEX.md").read_text(encoding="utf-8")
    if novo == atual.read_text(encoding="utf-8"):
        r.ok("INDEX.md atualizado")
    else:
        r.aviso("INDEX.md desatualizado: rode `python scripts/build_index.py`")
    for ln in erros.getvalue().splitlines():
        if ln.strip():
            r.aviso(f"build_index: {ln.strip()[:200]}")


# ---------------------------------------------------------------------------
# 5. Scripts --help
# ---------------------------------------------------------------------------

def checar_scripts(skill: Path, r: Relatorio) -> None:
    r.secao("scripts/: --help")
    scripts = sorted((skill / "scripts").glob("*.py"))
    if not scripts:
        r.aviso("nenhum script em scripts/")
        return
    with tempfile.TemporaryDirectory(prefix="checar_pacote_") as tmp:
        copia = Path(tmp) / skill.name
        shutil.copytree(skill, copia,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git"))
        for s in scripts:
            alvo = copia / "scripts" / s.name
            try:
                p = subprocess.run(
                    [sys.executable, "-B", str(alvo), "--help"],
                    capture_output=True, text=True, timeout=TIMEOUT_HELP_S, cwd=copia,
                    stdin=subprocess.DEVNULL,
                    env={**__import__("os").environ, "PYTHONDONTWRITEBYTECODE": "1"})
            except subprocess.TimeoutExpired:
                r.erro(f"{s.name} --help passou de {TIMEOUT_HELP_S}s")
                continue
            if p.returncode != 0:
                ult = (p.stderr.strip().splitlines() or ["sem mensagem"])[-1][:160]
                r.erro(f"{s.name} --help saiu com código {p.returncode}: {ult}")
            elif not any(w in p.stdout.lower() for w in ("usage", "uso:")):
                r.aviso(f"{s.name} --help roda, mas não mostra 'usage': o script provavelmente "
                        f"ignora --help e executa a tarefa (sem argparse)")
            else:
                r.ok(f"{s.name} --help")


# ---------------------------------------------------------------------------
# 6. Palavras
# ---------------------------------------------------------------------------

def checar_palavras(skill: Path, r: Relatorio) -> None:
    r.secao("Contagem de palavras")
    sk = skill / "SKILL.md"
    if sk.is_file():
        n = len(sk.read_text(encoding="utf-8").split())
        if n > MAX_PALAVRAS_SKILL:
            r.aviso(f"SKILL.md tem {n} palavras (aviso acima de {MAX_PALAVRAS_SKILL})")
        else:
            r.ok(f"SKILL.md: {n} palavras")
    for ag in sorted((skill / "agents").glob("*.md")):
        n = len(ag.read_text(encoding="utf-8").split())
        if n > MAX_PALAVRAS_BRIEFING:
            r.aviso(f"agents/{ag.name} tem {n} palavras (aviso acima de {MAX_PALAVRAS_BRIEFING})")
        else:
            r.ok(f"agents/{ag.name}: {n} palavras")


# ---------------------------------------------------------------------------
# 7. Arquivos indesejados e segredos
# ---------------------------------------------------------------------------

def checar_arquivos(skill: Path, r: Relatorio) -> None:
    r.secao("Arquivos indesejados e segredos")
    problemas = 0
    for rel in arquivos(skill):
        caminho = skill / rel
        motivo = lixo_do_nome(rel)
        if motivo:
            problemas += 1
            r.erro(f"{rel}: não deve ir no pacote ({motivo}); o zip o exclui; apague-o",
                   excluido_no_zip=True)
            continue
        if caminho.is_symlink():
            problemas += 1
            r.aviso(f"{rel}: link simbólico; o zip o ignora")
            continue
        tam = caminho.stat().st_size
        if tam > MAX_BYTES_ARQUIVO:
            problemas += 1
            r.erro(f"{rel}: {tam / 1048576:.1f} MB (limite {MAX_BYTES_ARQUIVO // 1048576} MB)")
            continue
        try:
            texto = caminho.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for nome, pat in SEGREDOS.items():
            for i, linha in enumerate(texto.splitlines(), 1):
                if pat.search(linha):
                    problemas += 1
                    r.erro(f"{rel}:{i}: parece {nome} (valor não impresso)")
                    break
    if problemas == 0:
        r.ok("nenhum arquivo indesejado, nenhum arquivo grande, nenhum segredo aparente")


# ---------------------------------------------------------------------------
# 8. Zip
# ---------------------------------------------------------------------------

def montar_zip(skill: Path, destino: Path, r: Relatorio) -> None:
    r.secao(f"Zip: {destino}")
    destino = destino.resolve()
    n, bruto = 0, 0
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists():
        destino.unlink()
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel in arquivos(skill):
            caminho = skill / rel
            if caminho.resolve() == destino or caminho.is_symlink() or lixo_do_nome(rel):
                continue
            z.write(caminho, f"{skill.name}/{rel.as_posix()}")
            n += 1
            bruto += caminho.stat().st_size
    with zipfile.ZipFile(destino) as z:
        nomes = z.namelist()
        if z.testzip() is not None:
            r.erro("zip com entrada corrompida")
            return
    if not all(x.startswith(f"{skill.name}/") for x in nomes) or f"{skill.name}/SKILL.md" not in nomes:
        r.erro(f"zip sem {skill.name}/SKILL.md na raiz da pasta")
        return
    r.ok(f"zip criado: {destino.stat().st_size / 1024:.0f} KB compactado "
         f"({bruto / 1024:.0f} KB bruto), {n} arquivo(s), raiz {skill.name}/")


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Valida a skill antes de publicar e, com --zip, monta o pacote para upload.")
    ap.add_argument("--zip", metavar="SAIDA.zip", help="monta o zip com a pasta da skill na raiz")
    ap.add_argument("--dir", metavar="PASTA", help="pasta da skill (padrão: a que contém este script)")
    ap.add_argument("--forcar", action="store_true", help="monta o zip mesmo com ERRO")
    args = ap.parse_args()

    skill = Path(args.dir).resolve() if args.dir else Path(__file__).resolve().parent.parent
    if not skill.is_dir():
        print(f"ERRO  pasta não existe: {skill}")
        return 1
    print(f"Skill: {skill}")
    r = Relatorio()

    checar_frontmatter(skill, r)
    try:
        bi = carregar_build_index(skill)
    except Exception as e:  # noqa: BLE001
        bi = None
        r.erro(f"não consegui importar scripts/build_index.py: {type(e).__name__}: {e}")
    checar_caminhos(skill, r)
    checar_citacoes(skill, bi, r)
    checar_index(skill, bi, r)
    checar_scripts(skill, r)
    checar_palavras(skill, r)
    checar_arquivos(skill, r)

    if args.zip:
        if r.n["ERRO"] > r.sanaveis and not args.forcar:
            r.secao(f"Zip: {args.zip}")
            r.aviso("zip não gerado porque há ERRO (use --forcar para gerar mesmo assim)")
        else:
            montar_zip(skill, Path(args.zip), r)

    print(f"\nResumo: {r.n['OK']} OK, {r.n['AVISO']} AVISO, {r.n['ERRO']} ERRO")
    return 1 if r.n["ERRO"] else 0


if __name__ == "__main__":
    sys.exit(main())
