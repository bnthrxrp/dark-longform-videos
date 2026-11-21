#!/usr/bin/env python3
"""Gera references/INDEX.md.

O índice abre com a trilha por papel (as seções que cada briefing mais usa) e, depois, lista os
títulos de cada documento com a faixa de linhas e o tamanho em palavras, para que o agente leia só
a seção de que precisa. Entram também os cabeçalhos sem número (Desenhos de 10 §3, fichas de 07) e
as técnicas T, as divergências D e os acréscimos N dos mapas.

Uso: python scripts/build_index.py
Depois de rodar, confira os avisos de referência cruzada que o script imprime.
"""
import re
import sys
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references"

# Documentos de consulta de fundo: não precisam ser abertos para escrever.
FUNDO = {"06", "07", "15", "17"}

# Mapas com técnicas (T), divergências (D) e acréscimos (N) em negrito, que entram no índice.
MAPAS = {"11", "12", "13", "14", "15", "16", "18", "19", "20"}

# Documentos em que só entram cabeçalhos de nível 1 e 2 (as fichas de 17 têm 250 subtítulos).
SO_NIVEL_2 = {"17"}

# Trilha por papel: (documento, chave). A chave é um número de seção ("3.2") ou o começo de um
# título ("Mapa 11", "T1"). A primeira ocorrência vale; o script falha se não achar.
TRILHA = [
    ("ideia", "agents/ideia.md", [
        ("00", "1"), ("01", "2.1"), ("01", "4.1"), ("05", "4"), ("01", "8.3"), ("20", "Mapa 11")]),
    ("pacote", "agents/pacote.md", [
        ("00", "3"), ("01", "2.2"), ("03", "2.4"), ("03", "2.8"), ("03", "3.4"), ("03", "5.3")]),
    ("hook", "agents/hook.md", [
        ("00", "2"), ("02", "1"), ("02", "3"), ("02", "4"), ("01", "3.2"), ("20", "Mapa 11")]),
    ("roteiro", "agents/roteiro.md", [
        ("00", "4"), ("05", "4"), ("04", "4"), ("04", "5"), ("12", "3"), ("01", "3.5")]),
    ("narracao", "agents/narracao.md", [
        ("00", "4"), ("16", "3"), ("04", "5"), ("04", "7.4"), ("19", "3"), ("05", "5")]),
    ("auditor", "agents/auditor.md", [
        ("00", "1"), ("09", "1"), ("09", "2"), ("09", "3"), ("09", "5"), ("04", "10")]),
    ("analytics", "agents/analytics.md", [
        ("00", "1"), ("08", "7"), ("08", "5"), ("18", "1"), ("10", "3"), ("10", "4.5")]),
]

BOLD = re.compile(r"^(?:[-*] )?\*\*((?:D-N|N-T|[TDN])\d+)[.:]?\s*(.*?)\*\*\s*(.*)$")
HEAD = re.compile(r"^(#{1,6}) (.+?)\s*$")
HOOK = re.compile(r"^(H-\d+)\s*[-–—]\s*(.+)$")
NUM = re.compile(r"^(\d+(?:\.\d+)*)(?:\.(?=\s)|(?=\s))")


def parse(path):
    """Devolve (linhas, entradas). Entrada: dict(nivel, titulo, ini, num, hook, dup)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    doc = path.name[:2]
    entradas, in_code, last_head_line = [], False, -10
    ultimo_nivel_head = 1
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEAD.match(line)
        if m:
            nivel, titulo = len(m.group(1)), m.group(2).strip()
            if entradas and entradas[-1]["nivel"] == nivel and i - last_head_line <= 2 \
                    and not entradas[-1].get("bold"):
                last_head_line = i  # título duplicado logo abaixo do primeiro: fica o primeiro
                continue
            last_head_line = i
            ultimo_nivel_head = nivel
            if doc in SO_NIVEL_2 and nivel > 2:
                continue
            entradas.append({"nivel": nivel, "titulo": titulo, "ini": i})
            continue
        if doc in MAPAS:
            b = BOLD.match(line)
            if b:
                resto = b.group(2).strip() or b.group(3).strip()
                titulo = f"{b.group(1)}. {resto}"
                if len(titulo) > 90:
                    titulo = titulo[:87].rstrip() + "..."
                entradas.append({"nivel": max(ultimo_nivel_head + 1, 3), "titulo": titulo,
                                 "ini": i, "bold": True})
    # fim da faixa: linha anterior à próxima entrada de nível igual ou menor
    for k, e in enumerate(entradas):
        fim = len(lines)
        for nxt in entradas[k + 1:]:
            if nxt["nivel"] <= e["nivel"]:
                fim = nxt["ini"] - 1
                break
        e["fim"] = fim
        e["pal"] = sum(len(x.split()) for x in lines[e["ini"] - 1:fim])
        h = HOOK.match(e["titulo"])
        e["hook"] = h.groups() if h else None
    # números de seção repetidos no mesmo documento
    vistos = {}
    for e in entradas:
        n = NUM.match(e["titulo"])
        e["num"] = n.group(1) if n else None
        if n and e["nivel"] <= 3 and not e.get("bold"):
            if n.group(1) in vistos:
                e["dup"] = True
            vistos[n.group(1)] = True
    return lines, entradas


def acha(entradas, chave):
    """Primeira entrada cujo número de seção é a chave, ou cujo título começa por ela."""
    for e in entradas:
        if e.get("hook") or e.get("bold"):
            continue
        if re.match(r"^\d", chave):
            if e["num"] == chave and e["nivel"] <= 3:
                return e
        elif e["titulo"].startswith(chave):
            return e
    return None


def main():
    docs = {}
    for path in sorted(REF.glob("[0-9]*.md")):
        docs[path.name[:2]] = (path, *parse(path))

    out = ["# Índice das referências", "",
           "Cada linha: `início-fim  palavras  título`. Leia com Read(offset=início, limit=fim-início+1). "
           "As palavras incluem as subseções. Não leia um documento nem este índice inteiro: use a trilha abaixo ou Grep pelo título.",
           "Comece por `00_kit_de_bolso.md`: doses com etiqueta, aberturas reais, checklist de thumbnail e pontes. "
           "`[TESTE-IA]` está definido em `21_testes_comparativos.md`.", ""]

    # Trilha por papel
    out += ["## Trilha por papel", "",
            "As seções que cada briefing mais usa, na ordem de leitura. Fora delas, procure no índice abaixo.", ""]
    erros = []
    for papel, briefing, itens in TRILHA:
        out.append(f"**{papel}** (`{briefing}`)")
        for doc, chave in itens:
            if doc not in docs:
                erros.append(f"{papel}: documento {doc} não existe")
                continue
            path, lines, entradas = docs[doc]
            e = acha(entradas, chave)
            if not e:
                erros.append(f"{papel}: não achei {doc} {chave}")
                continue
            sec = f"§{e['num']} " if e["num"] else ""
            nome = NUM.sub("", e["titulo"]).lstrip(". ") if e["num"] else e["titulo"]
            out.append(f"- `{path.name}` {sec}{nome} (linhas {e['ini']}-{e['fim']}, {e['pal']} pal.)")
        out.append("")
    if erros:
        sys.exit("Trilha quebrada:\n" + "\n".join(erros))

    out += ["## Consulta de fundo", "",
            "`06`, `07`, `15` e `17` são consulta de fundo, não precisa abrir para escrever. Servem à "
            "rastreabilidade: os números de `06` entram via `01` e `02`; `07` e `17` guardam as fichas "
            "de onde saíram os mapas `11` a `16` e `18` a `20`.", ""]

    # Listagem por documento
    for doc, (path, lines, entradas) in docs.items():
        total = sum(len(x.split()) for x in lines)
        nota = "  consulta de fundo, não precisa abrir para escrever" if doc in FUNDO else ""
        out.append(f"## {path.name}  ({len(lines)} linhas, {total} palavras){'  -' if nota else ''}{nota}")
        hooks = []
        for e in entradas:
            if e["hook"]:  # estruturas de hook: uma linha compacta por estrutura
                hooks.append(f"{e['ini']:>5}-{e['fim']:<5} {e['pal']:>5}p  {e['hook'][0]} {e['hook'][1]}")
                continue
            if hooks:
                out += hooks
                hooks = []
            marca = "  [nº repetido: cite pelo título]" if e.get("dup") else ""
            out.append(f"{e['ini']:>5}-{e['fim']:<5} {e['pal']:>5}p  {'  ' * (e['nivel'] - 1)}{e['titulo']}{marca}")
        out += hooks
        out.append("")

    (REF / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"INDEX.md: {len(out)} linhas")
    checa_referencias(docs)


def checa_referencias(docs):
    """Avisa de referências cruzadas `NN §X` que apontam para seção inexistente."""
    secoes = {d: {e["num"] for e in ents if e["num"]} for d, (_, _, ents) in docs.items()}
    pat = re.compile(r"`?\b(0[1-9]|1\d|2[01])\b`?(?:_[a-z_]+(?:\.md)?)?[ ,]*\(?§§?\s*(\d+(?:\.\d+)?)")
    avisos = []
    for doc, (path, lines, _) in docs.items():
        for i, line in enumerate(lines, 1):
            for m in pat.finditer(line):
                alvo, sec = m.group(1), m.group(2)
                if alvo in secoes and sec not in secoes[alvo]:
                    avisos.append(f"{path.name}:{i}: `{alvo}` §{sec} não existe")
    for a in avisos:
        print("AVISO", a, file=sys.stderr)
    print(f"Referências cruzadas: {len(avisos)} aviso(s).")


if __name__ == "__main__":
    import sys
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print("Uso: python scripts/build_index.py\n"
              "Regera references/INDEX.md a partir dos cabeçalhos de references/*.md e confere as\n"
              "referências cruzadas (NN §X). Rode depois de editar qualquer documento em references/.")
        sys.exit(0)
    main()
