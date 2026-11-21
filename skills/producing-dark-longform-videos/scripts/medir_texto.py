#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mede um texto narrado (hook ou bloco) para o agente que escreve o roteiro.

Uso:
    python scripts/medir_texto.py TEXTO.txt [--fatos FATOS.txt|FATOS.json]
                                  [--wpm 135] [--tipo hook|bloco] [--json]
    cat texto.txt | python scripts/medir_texto.py - --tipo hook

Mede: palavras, frases, segundos estimados, perguntas, frases sobre o próprio vídeo
(metalinguagem) e, com --fatos, números, datas e nomes que não estão na ficha.

Só usa a biblioteca padrão (Python 3.10+). Os resultados são triagem: apontam onde olhar,
não decidem. Quem escreve confere cada alerta contra o texto.

Para estender a lista de metalinguagem, edite PADROES_METALINGUAGEM aqui embaixo ou
crie references/marcadores_slop.json (ver carregar_marcadores).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuração (fácil de editar)
# ---------------------------------------------------------------------------

WPM_PADRAO = 135
HOOK_MIN_S = 80            # janela do hook, em segundos
HOOK_MAX_S = 95
HOOK_MAX_PERGUNTAS = 2     # mais que isso = provável excesso de perguntas centrais

# Padrões de metalinguagem: frases que falam do vídeo, do roteiro ou do espectador em vez
# do caso. As regexes rodam sobre o texto em minúsculas e SEM ACENTOS (por isso "video",
# "proximos"). Para acrescentar um padrão, acrescente uma entrada: "id": {"regex", "nota"}.
PADROES_METALINGUAGEM: dict[str, dict[str, str]] = {
    "neste_video": {
        "regex": r"\b(neste|nesse|deste|desse|este|esse)\s+(video|episodio|documentario|canal)\b",
        "nota": "fala do vídeo em vez do caso",
    },
    "proximos_minutos": {
        "regex": r"\bnos\s+proximos\s+(\w+\s+)?(minutos|instantes|segundos)\b",
        "nota": "promessa de agenda",
    },
    "vamos_verbo": {
        "regex": r"\bvamos\s+(ver|responder|descobrir|separar|entender|comecar|acompanhar|mostrar|"
                 r"analisar|explorar|investigar|mergulhar|conhecer|falar|olhar|contar|reconstruir|"
                 r"percorrer|desvendar|examinar|revisar|explicar|apresentar|voltar|passar|tentar|seguir|"
                 r"abrir|refazer|rever|dissecar|partir)\b",
        "nota": "índice falado ('vamos ver...')",
    },
    "vou_verbo": {
        "regex": r"\bvou\s+(te\s+|lhe\s+|lhes\s+|vos\s+)?(mostrar|explicar|contar|responder|separar|"
                 r"apresentar|detalhar|analisar|provar|revelar|desvendar|reconstruir|percorrer|seguir|"
                 r"abrir|comecar|voltar)\b",
        "nota": "narrador anuncia o que vai fazer",
    },
    "hoje_vamos": {
        "regex": r"\bhoje\s+(vamos|vou|iremos|veremos|voce\s+vai|eu\s+vou)\b",
        "nota": "abertura de aula",
    },
    "fique_ate_o_fim": {
        "regex": r"\b(fique|fica|continue|permaneca)\s+(comigo\s+)?ate\s+o\s+(fim|final)\b|"
                 r"\bate\s+o\s+(fim|final)\s+do\s+video\b",
        "nota": "apelo de retenção",
    },
    "inscreva": {
        "regex": r"\b(se\s+inscreva|inscreva-se|inscrevam-se|deixe\s+(o\s+|seu\s+)?(like|curtida)|"
                 r"ative\s+o\s+sininho|compartilhe\s+(este|esse))\b",
        "nota": "pedido de inscrição ou curtida",
    },
    "a_seguir": {
        # só o uso de roteiro ("a seguir, ...", "veremos a seguir"); "decidiu a seguir para Gênova" é narração
        "regex": r"(^|[.!?…]\s+)a\s+seguir\b|\ba\s+seguir\s*[,:;.!?]|"
                 r"\b(veremos|vemos|vamos\s+ver|vem|mostramos|mostro|conto|explico|falamos|falo)\s+a\s+seguir\b",
        "nota": "transição de roteiro",
    },
    "promessa_futura": {
        "regex": r"\b(mais\s+adiante|mais\s+a\s+frente|daqui\s+a\s+pouco|em\s+instantes|ja\s+ja|"
                 r"logo\s+adiante|ao\s+longo\s+do\s+video|no\s+(final|fim)\s+do\s+video)\b",
        "nota": "adia o pagamento falando do vídeo",
    },
    "precisamos": {
        "regex": r"\b(precisamos|temos\s+que|e\s+preciso)\s+(primeiro\s+)?(entender|ver|voltar|olhar|conhecer|"
                 r"separar|examinar|recuar)\b|\bcomecamos\s+(por|pelo|pela)\b|\bantes\s+de\s+chegar\s+a\s+isso\b",
        "nota": "narrador explica o percurso em vez de seguir o caso",
    },
    "retomada": {
        "regex": r"\b(veremos|voltaremos|chegaremos|retomaremos|descobriremos|responderemos|"
                 r"entenderemos)\b|\bvoltamos\s+(a|ao|aos|as|para)\b",
        "nota": "narrador organiza o percurso",
    },
    "como_vimos": {
        "regex": r"\bcomo\s+(ja\s+)?(vimos|dissemos|explicamos|mencionei|falei|disse\s+antes)\b",
        "nota": "remissão a outra parte do vídeo",
    },
    "neste_capitulo": {
        "regex": r"\b(neste|nesse|no)\s+(capitulo|bloco|trecho|segmento|roteiro)\b",
        "nota": "fala da estrutura do vídeo",
    },
    "esta_historia": {
        "regex": r"\b(esta|essa)\s+(historia|analise|investigacao|aula|serie)\s+(tenta|vai|busca|"
                 r"responde|pretende|procura)\b",
        "nota": "a história se descreve em vez de acontecer",
    },
    "perguntas_guiam": {
        "regex": r"\b(duas|tres|quatro)\s+perguntas\s+(guiam|norteiam|orientam|conduzem|organizam)\b|"
                 r"\bperguntas?\s+que\s+(guia|guiam|norteia|norteiam)\b|"
                 r"\ba\s+pergunta\s+que\s+(este|esse)\s+video\b",
        "nota": "agenda de perguntas anunciada",
    },
}

# Caminho do arquivo opcional de marcadores extras (ao lado da skill: references/).
CAMINHO_MARCADORES_PADRAO = (
    Path(__file__).resolve().parent.parent / "references" / "marcadores_slop.json"
)

MESES = {
    "janeiro": 1, "fevereiro": 2, "marco": 3, "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12,
}

# Abreviações que terminam em ponto sem encerrar a frase (sem acento, minúsculas).
ABREVIACOES = {
    "sr", "sra", "srta", "dr", "dra", "prof", "profa", "st", "sta", "av", "etc", "vs", "ex",
    "cap", "no", "nos", "pag", "pg", "tel", "cel", "gen", "cmdt", "cap", "ten", "sgt", "col",
    "min", "seg", "obs", "ca", "aprox", "dom", "jr", "ltda",
}

# Número seguido destes substantivos conta o próprio vídeo, não o caso: não entra na triagem de fatos.
CONTAGEM_META_RX = re.compile(r"\s+(perguntas?|partes?|coisas|etapas|blocos|minutos|capitulos|pontos|passos)\b")

# Equivalências entre siglas e nomes por extenso, para não acusar "Estados Unidos" quando a
# ficha diz "EUA". Chave e valores sem acento, minúsculos.
ALIASES = {"eua": ["estados", "unidos"], "urss": ["uniao", "sovietica"], "onu": ["nacoes", "unidas"],
           "fbi": ["federal", "bureau"], "nasa": ["aeronautica", "espaco"]}

# Palavras por extenso (para normalizar números nos textos e nas fichas).
_UNIDADES = {"um": 1, "uma": 1, "dois": 2, "duas": 2, "tres": 3, "quatro": 4, "cinco": 5,
             "seis": 6, "sete": 7, "oito": 8, "nove": 9}
_DEZ_A_DEZENOVE = {"dez": 10, "onze": 11, "doze": 12, "treze": 13, "catorze": 14,
                   "quatorze": 14, "quinze": 15, "dezesseis": 16, "dezasseis": 16,
                   "dezessete": 17, "dezassete": 17, "dezoito": 18, "dezenove": 19,
                   "dezanove": 19}
_DEZENAS = {"vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60,
            "setenta": 70, "oitenta": 80, "noventa": 90}
_CENTENAS = {"cem": 100, "cento": 100, "duzentos": 200, "duzentas": 200, "trezentos": 300,
             "trezentas": 300, "quatrocentos": 400, "quatrocentas": 400, "quinhentos": 500,
             "quinhentas": 500, "seiscentos": 600, "seiscentas": 600, "setecentos": 700,
             "setecentas": 700, "oitocentos": 800, "oitocentas": 800, "novecentos": 900,
             "novecentas": 900}
_MIL = {"mil": 1000}
_MILHAO = {"milhao": 10**6, "milhoes": 10**6, "bilhao": 10**9, "bilhoes": 10**9}
_ZERO = {"zero": 0}

_CATEGORIA: dict[str, tuple[str, int]] = {}
for _d, _c in ((_UNIDADES, "u"), (_DEZ_A_DEZENOVE, "t"), (_DEZENAS, "d"), (_CENTENAS, "c"),
               (_MIL, "mil"), (_MILHAO, "mi"), (_ZERO, "z")):
    for _k, _v in _d.items():
        _CATEGORIA[_k] = (_c, _v)

ROMANOS = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


# ---------------------------------------------------------------------------
# Utilidades de texto
# ---------------------------------------------------------------------------

def sem_acento(s: str) -> str:
    """Remove acentos preservando o comprimento (índices do original continuam valendo)."""
    out = []
    for ch in s:
        base = unicodedata.normalize("NFD", ch)[0]
        out.append(base)
    return "".join(out)


def normalizar(s: str) -> str:
    return sem_acento(s).lower()


def eh_palavra(token: str) -> bool:
    """Token separado por espaço que conta como palavra: tem ao menos uma letra ou dígito."""
    return any(c.isalnum() for c in token)


def contar_palavras(s: str) -> int:
    return sum(1 for t in s.split() if eh_palavra(t))


def fmt(x: float, casas: int = 1) -> str:
    return f"{x:.{casas}f}".replace(".", ",")


def trecho_em(texto: str, ini: int, fim: int, folga: int = 55) -> str:
    a = max(0, ini - folga)
    b = min(len(texto), fim + folga)
    s = re.sub(r"\s+", " ", texto[a:b]).strip()
    return ("…" if a > 0 else "") + s + ("…" if b < len(texto) else "")


# ---------------------------------------------------------------------------
# Frases
# ---------------------------------------------------------------------------

class Frase:
    __slots__ = ("texto", "ini", "fim", "palavras", "palavra_inicial", "pergunta")

    def __init__(self, texto: str, ini: int, fim: int):
        self.texto = texto
        self.ini = ini
        self.fim = fim
        self.palavras = contar_palavras(texto)
        self.palavra_inicial = 0
        self.pergunta = bool(re.search(r"\?[\"”’')\]»]*\s*$", texto.rstrip()))


_TERMINADOR = re.compile(r"[.!?…]+[\"”’')\]»]*")


def dividir_frases(texto: str) -> list[Frase]:
    """Divide em frases por pontuação final e por linha em branco. Trata abreviações
    ("Sr.", "D. B. Cooper"), números com ponto ("2.150") e reticências."""
    cortes = [0]
    for m in _TERMINADOR.finditer(texto):
        fim = m.end()
        resto = texto[fim:]
        if resto and not resto[0].isspace():
            continue  # "2.150", "e.g.", "...texto"
        prox = resto.lstrip()
        marca = m.group(0)
        if "?" not in marca and "!" not in marca:
            antes = texto[:m.start()]
            ultima = re.findall(r"[\wÀ-ÿ]+$", antes)
            ultima = ultima[0] if ultima else ""
            if normalizar(ultima) in ABREVIACOES and not marca.startswith(".."):
                continue
            if len(ultima) == 1 and ultima.isupper():
                continue  # inicial: "D. B. Cooper"
            if prox and prox[0].islower():
                continue  # ponto seguido de minúscula: não encerra
        cortes.append(fim)
    cortes.append(len(texto))
    frases: list[Frase] = []
    for a, b in zip(cortes, cortes[1:]):
        trecho = texto[a:b]
        # parágrafos separados por linha em branco também encerram frase
        base = a
        for parte in re.split(r"(\n[ \t]*\n)", trecho):
            if re.fullmatch(r"\n[ \t]*\n", parte or "x"):
                base += len(parte)
                continue
            if parte.strip() and eh_palavra(parte):
                lead = len(parte) - len(parte.lstrip())
                frases.append(Frase(parte.strip(), base + lead, base + len(parte.rstrip())))
            base += len(parte)
    acum = 0
    for f in frases:
        f.palavra_inicial = acum
        acum += f.palavras
    return frases


# ---------------------------------------------------------------------------
# Marcadores (metalinguagem e extras)
# ---------------------------------------------------------------------------

def carregar_marcadores(caminho_json: str | Path | None = None) -> list[dict]:
    """Lê padrões extras de um JSON {"marcadores": [{"id","regex","nota"}]}.

    Se `caminho_json` for None, usa references/marcadores_slop.json ao lado da skill.
    Se o arquivo não existir, devolve lista vazia (segue sem eles). Regex inválida é
    ignorada com aviso no stderr.
    """
    caminho = Path(caminho_json) if caminho_json else CAMINHO_MARCADORES_PADRAO
    if not caminho.is_file():
        return []
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"aviso: não consegui ler {caminho}: {e}", file=sys.stderr)
        return []
    lista = dados.get("marcadores", []) if isinstance(dados, dict) else dados
    saida = []
    for item in lista if isinstance(lista, list) else []:
        if not isinstance(item, dict) or not item.get("regex"):
            continue
        try:
            rx = re.compile(item["regex"], re.IGNORECASE)
        except re.error as e:
            print(f"aviso: regex inválida em {item.get('id', '?')}: {e}", file=sys.stderr)
            continue
        saida.append({"id": str(item.get("id", "marcador")), "regex": rx,
                      "nota": str(item.get("nota", "")), "ascii": item["regex"].isascii()})
    return saida


def achar_metalinguagem(texto: str, frases: list[Frase], wpm: float) -> list[dict]:
    base = normalizar(texto)
    achados = []
    for pid, p in PADROES_METALINGUAGEM.items():
        for m in re.finditer(p["regex"], base):
            achados.append(_achado(pid, p.get("nota", ""), texto, m.start(), m.end(), frases, wpm))
    achados.sort(key=lambda a: a["_ini"])
    return _sem_sobreposicao(achados)


def achar_extras(texto: str, frases: list[Frase], wpm: float, marcadores: list[dict]) -> list[dict]:
    base = normalizar(texto)
    achados = []
    for mk in marcadores:
        spans = {(m.start(), m.end()) for m in mk["regex"].finditer(texto)}
        if mk["ascii"]:
            spans |= {(m.start(), m.end()) for m in mk["regex"].finditer(base)}
        for ini, fim in sorted(spans):
            achados.append(_achado(mk["id"], mk["nota"], texto, ini, fim, frases, wpm))
    achados.sort(key=lambda a: a["_ini"])
    return _sem_sobreposicao(achados)


def _achado(pid: str, nota: str, texto: str, ini: int, fim: int, frases: list[Frase], wpm: float) -> dict:
    pos_palavra = contar_palavras(texto[:ini])
    return {
        "id": pid,
        "nota": nota,
        "trecho": trecho_em(texto, ini, fim),
        "segundos": round(pos_palavra / wpm * 60, 1),
        "_ini": ini,
        "_fim": fim,
    }


def _sem_sobreposicao(achados: list[dict]) -> list[dict]:
    """Mesmo id e mesmo trecho repetido por sobreposição de padrões: mantém o primeiro."""
    saida: list[dict] = []
    ultimo_fim = -1
    for a in achados:
        if a["_ini"] < ultimo_fim:
            continue
        ultimo_fim = a["_fim"]
        saida.append(a)
    for a in saida:
        a.pop("_ini", None)
        a.pop("_fim", None)
    return saida


# ---------------------------------------------------------------------------
# Triagem de fatos (números, datas, nomes)
# ---------------------------------------------------------------------------

_MES_RX = "|".join(MESES)


def _valor_digitos(s: str) -> float:
    """'2.150' -> 2150; '1,5' -> 1.5; '1.701' -> 1701; '10' -> 10."""
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        return float(s.replace(".", ""))
    if re.fullmatch(r"\d{1,3}(\.\d{3})+,\d+", s):
        return float(s.replace(".", "").replace(",", "."))
    s2 = s.replace(",", ".")
    try:
        return float(s2)
    except ValueError:
        return float(re.sub(r"\D", "", s) or 0)


def _romano(s: str) -> int | None:
    s = s.lower()
    if not s or any(c not in ROMANOS for c in s):
        return None
    total = 0
    for i, c in enumerate(s):
        v = ROMANOS[c]
        if i + 1 < len(s) and ROMANOS[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total


def _transicao_ok(anterior: str, atual: str, tem_e: bool) -> bool:
    """Pode a categoria `atual` continuar um número que terminou em `anterior`?
    Categorias: u unidade, t dez a dezenove, d dezena, c centena, mil, mi milhão, z zero."""
    if atual in ("mil", "mi"):
        return anterior in ("u", "t", "d", "c") or (atual == "mil" and anterior == "mi")
    if anterior == "c":
        return atual in ("d", "t", "u") and tem_e
    if anterior == "d":
        return atual == "u" and tem_e
    if anterior in ("mil", "mi"):
        return atual in ("c", "d", "t", "u")
    return False


def _valor_sequencia(palavras: list[str]) -> float:
    """Valor de uma sequência de números por extenso já delimitada."""
    total = 0
    atual = 0
    for p in palavras:
        if p == "e":
            continue
        cat, v = _CATEGORIA[p]
        if cat == "mil":
            total += (atual or 1) * 1000
            atual = 0
        elif cat == "mi":
            total = (total + (atual or 1)) * v
            atual = 0
        else:
            atual += v
    return float(total + atual)


def _extrair_numeros_por_extenso(norm: str, ocupado: list[tuple[int, int]]) -> list[tuple[int, int, float]]:
    """Acha sequências como 'dez', 'cento e quinze', 'mil setecentos e um', 'oitenta milhões'.
    'um/uma' sozinho (artigo) é ignorado."""
    toks = [(m.group(0), m.start(), m.end()) for m in re.finditer(r"[a-z]+", norm)]

    def livre(a, b):
        return not any(a < fb and b > fa for fa, fb in ocupado)

    achados = []
    i = 0
    while i < len(toks):
        w, a, b = toks[i]
        if w not in _CATEGORIA or not livre(a, b):
            i += 1
            continue
        palavras = [w]
        ultima = _CATEGORIA[w][0]
        fim_grupo = b
        j = i + 1
        while j < len(toks):
            w2, a2, b2 = toks[j]
            tem_e = False
            k = j
            if w2 == "e" and j + 1 < len(toks):
                tem_e = True
                k = j + 1
                w2, a2, b2 = toks[k]
            if w2 not in _CATEGORIA or not livre(a2, b2):
                break
            if norm[fim_grupo:a2].strip() not in ("", "e"):
                break
            cat2 = _CATEGORIA[w2][0]
            if not _transicao_ok(ultima, cat2, tem_e):
                break
            palavras.append(w2)
            ultima = cat2
            fim_grupo = b2
            j = k + 1
        if len(palavras) == 1 and w in ("um", "uma"):
            i += 1
            continue
        achados.append((a, fim_grupo, _valor_sequencia(palavras)))
        i = j
    return achados


class Item:
    """Um elemento checável: número, ano, data, sigla ou nome."""
    __slots__ = ("tipo", "valor", "chave", "ini", "fim")

    def __init__(self, tipo: str, valor: str, chave, ini: int, fim: int):
        self.tipo, self.valor, self.chave, self.ini, self.fim = tipo, valor, chave, ini, fim


def extrair_itens(texto: str, frases: list[Frase]) -> list[Item]:
    norm = normalizar(texto)
    itens: list[Item] = []
    ocupado: list[tuple[int, int]] = []

    def marca(a, b):
        ocupado.append((a, b))

    # 1. datas completas e mês+ano
    for m in re.finditer(rf"\b(\d{{1,2}})\s*(?:o|º|°)?\s+de\s+({_MES_RX})(?:\s+de\s+(\d{{4}}))?\b", norm):
        d, mes, ano = int(m.group(1)), MESES[m.group(2)], m.group(3)
        itens.append(Item("data", texto[m.start():m.end()], ("dm", d, mes), m.start(), m.end()))
        if ano:
            itens.append(Item("ano", ano, ("n", float(ano)), m.start(3), m.end(3)))
        marca(m.start(), m.end())
    for m in re.finditer(rf"\b({_MES_RX})\s+de\s+(\d{{4}})\b", norm):
        if any(a <= m.start() < b for a, b in ocupado):
            continue
        mes, ano = MESES[m.group(1)], int(m.group(2))
        itens.append(Item("data", texto[m.start():m.end()], ("my", mes, ano), m.start(), m.end()))
        marca(m.start(), m.end())
    # meses soltos ("em julho", "de junho")
    for m in re.finditer(rf"\b({_MES_RX})\b", norm):
        if any(a <= m.start() < b for a, b in ocupado):
            continue
        itens.append(Item("data", texto[m.start():m.end()], ("m", MESES[m.group(1)]), m.start(), m.end()))
        marca(m.start(), m.end())

    # 2. "século XV"
    for m in re.finditer(r"\bseculo\s+([ivxlc]+)\b", norm):
        v = _romano(m.group(1))
        if v:
            itens.append(Item("número", texto[m.start():m.end()], ("n", float(v)), m.start(), m.end()))
            marca(m.start(), m.end())

    # 3. códigos alfanuméricos (6EQUJ5, MS 408 fica como número + sigla)
    for m in re.finditer(r"\b(?=[a-z0-9]*\d)(?=[a-z0-9]*[a-z])[a-z0-9]{4,}\b", norm):
        if any(a <= m.start() < b for a, b in ocupado):
            continue
        itens.append(Item("código", texto[m.start():m.end()], ("t", m.group(0)), m.start(), m.end()))
        marca(m.start(), m.end())

    # 4. números em dígitos (com sufixo mil/milhões)
    for m in re.finditer(r"(?<![\w.,])\d+(?:[.,]\d+)*(?:\s*(?:º|°|o\b))?(?:\s+(mil|milhao|milhoes|bilhao|bilhoes)\b)?", norm):
        if any(a <= m.start() < b for a, b in ocupado):
            continue
        bruto = re.match(r"\d+(?:[.,]\d+)*", m.group(0)).group(0)
        bruto = bruto.rstrip(".,")
        valor = _valor_digitos(bruto)
        suf = m.group(1)
        if suf:
            valor *= {"mil": 1000}.get(suf, 10**9 if suf.startswith("bilh") else 10**6)
        tipo = "número"
        if (suf is None and re.fullmatch(r"\d{4}", bruto) and 1000 <= valor <= 2100):
            tipo = "ano"
        itens.append(Item(tipo, texto[m.start():m.end()].strip(), ("n", float(valor)), m.start(), m.end()))
        marca(m.start(), m.end())
    # intervalo "157–337" já saiu como dois números (o separador não é dígito)

    # 5. números por extenso
    for a, b, v in _extrair_numeros_por_extenso(norm, ocupado):
        itens.append(Item("número", texto[a:b], ("n", v), a, b))
        marca(a, b)

    # 6. siglas (todas maiúsculas, 2+ letras) e nomes próprios fora do início de frase
    inicios = set()
    for f in frases:
        m = re.search(r"[\wÀ-ÿ]", texto[f.ini:f.fim])
        if m:
            inicios.add(f.ini + m.start())
    for m in re.finditer(r"[A-ZÀ-ÝÇ][\wÀ-ÿ'’]*", texto):
        a, b = m.start(), m.end()
        if any(oa <= a < ob for oa, ob in ocupado):
            continue
        palavra = m.group(0)
        letras = [c for c in palavra if c.isalpha()]
        if len(letras) >= 2 and all(c.isupper() for c in letras):
            itens.append(Item("sigla", palavra, ("t", normalizar(palavra)), a, b))
            continue
        if a in inicios or len(letras) < 2:
            continue  # início de frase não diz se é nome; letra solta ("E, Q, U") também não
        itens.append(Item("nome", palavra, ("t", normalizar(palavra)), a, b))
    itens.sort(key=lambda it: it.ini)
    return itens


def carregar_fatos(caminho: str) -> list[str]:
    p = Path(caminho)
    bruto = p.read_text(encoding="utf-8")
    if p.suffix.lower() == ".json":
        dados = json.loads(bruto)
        if isinstance(dados, dict):
            for chave in ("fatos", "facts", "ficha", "itens"):
                if isinstance(dados.get(chave), list):
                    dados = dados[chave]
                    break
        if not isinstance(dados, list):
            raise ValueError("FATOS.json deve ser uma lista de strings ou de objetos com 'texto' ou 'fato'")
        fatos = []
        for d in dados:
            if isinstance(d, str):
                fatos.append(d)
            elif isinstance(d, dict):
                v = d.get("texto") or d.get("fato") or d.get("text")
                if v:
                    fatos.append(str(v))
        return fatos
    fatos = []
    for linha in bruto.splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        linha = re.sub(r"^(?:[-*•]|\d+[.)])\s+", "", linha)
        fatos.append(linha)
    return fatos


def _prefixo_comum(a: str, b: str) -> int:
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def fora_da_ficha(texto: str, frases: list[Frase], fatos: list[str], wpm: float) -> list[dict]:
    base_fatos = "\n".join(fatos)
    itens_fatos = extrair_itens(base_fatos, dividir_frases(base_fatos))
    numeros_f = {it.chave[1] for it in itens_fatos if it.chave[0] == "n"}
    dm_f = {(it.chave[1], it.chave[2]) for it in itens_fatos if it.chave[0] == "dm"}
    my_f = {(it.chave[1], it.chave[2]) for it in itens_fatos if it.chave[0] == "my"}
    meses_f = {it.chave[1] for it in itens_fatos if it.chave[0] == "m"}
    meses_f |= {m for (_d, m) in dm_f} | {m for (m, _a) in my_f}
    numeros_f |= {float(d) for (d, _m) in dm_f} | {float(a) for (_m, a) in my_f}  # dia e ano de datas
    tokens_f = {normalizar(t) for t in re.findall(r"[\wÀ-ÿ'’]+", base_fatos)}
    for sigla, expansao in ALIASES.items():
        if sigla in tokens_f:
            tokens_f.update(expansao)
        if all(e in tokens_f for e in expansao):
            tokens_f.add(sigla)
    longos_f = [t for t in tokens_f if len(t) >= 5]

    def nome_na_ficha(tok: str) -> bool:
        if tok in tokens_f:
            return True
        if len(tok) < 5:
            return False
        # tolera flexão curta (plural, sufixo): prefixo comum quase do tamanho da menor palavra
        return any(_prefixo_comum(tok, m) >= max(5, min(len(tok), len(m)) - 2) for m in longos_f)

    saida: list[dict] = []
    vistos: dict[tuple, dict] = {}
    norm = normalizar(texto)
    for it in extrair_itens(texto, frases):
        k = it.chave
        if k[0] == "n":
            # contagem do próprio vídeo ("duas perguntas", "três partes", "trinta minutos"): não é fato do caso
            if CONTAGEM_META_RX.match(norm[it.fim:it.fim + 30]):
                continue
            ok = k[1] in numeros_f
        elif k[0] == "dm":
            ok = (k[1], k[2]) in dm_f
        elif k[0] == "my":
            ok = (k[1], k[2]) in my_f or (k[1] in meses_f and float(k[2]) in numeros_f)
        elif k[0] == "m":
            ok = k[1] in meses_f
        elif it.tipo == "nome":
            ok = nome_na_ficha(k[1])
        else:  # sigla ou código
            ok = k[1] in tokens_f
        if ok:
            continue
        chave_unica = (it.tipo, it.valor.lower())
        if chave_unica in vistos:
            vistos[chave_unica]["ocorrencias"] += 1
            continue
        reg = {
            "tipo": it.tipo,
            "valor": it.valor,
            "trecho": trecho_em(texto, it.ini, it.fim),
            "segundos": round(contar_palavras(texto[:it.ini]) / wpm * 60, 1),
            "ocorrencias": 1,
        }
        vistos[chave_unica] = reg
        saida.append(reg)
    return saida


# ---------------------------------------------------------------------------
# Medição principal
# ---------------------------------------------------------------------------

def medir(texto: str, wpm: float = WPM_PADRAO, tipo: str = "bloco",
          fatos: list[str] | None = None, marcadores: list[dict] | None = None) -> dict:
    frases = dividir_frases(texto)
    palavras = contar_palavras(texto)
    segundos = palavras / wpm * 60 if wpm else 0.0
    tamanhos = [f.palavras for f in frases]
    maior = max(frases, key=lambda f: f.palavras) if frases else None
    perguntas = [f for f in frases if f.pergunta]
    primeira = perguntas[0] if perguntas else None
    ultima = frases[-1] if frases else None

    meta = achar_metalinguagem(texto, frases, wpm)
    extras = achar_extras(texto, frases, wpm, marcadores or [])

    res = {
        "tipo": tipo,
        "wpm": wpm,
        "palavras": palavras,
        "frases": len(frases),
        "media_palavras_por_frase": round(sum(tamanhos) / len(tamanhos), 1) if tamanhos else 0.0,
        "maior_frase_palavras": maior.palavras if maior else 0,
        "maior_frase_trecho": (maior.texto if len(maior.texto) <= 120 else maior.texto[:117] + "...") if maior else "",
        "segundos_estimados": round(segundos, 1),
        "perguntas": {
            "total": len(perguntas),
            "primeira_em_segundos": round(primeira.palavra_inicial / wpm * 60, 1) if primeira else None,
            "primeira_na_palavra": primeira.palavra_inicial if primeira else None,
            "primeira_trecho": primeira.texto[:120] if primeira else None,
            "termina_em_pergunta": bool(ultima and ultima.pergunta),
        },
        "ultima_frase": ultima.texto if ultima else "",
        "ultima_frase_palavras": ultima.palavras if ultima else 0,
        "metalinguagem": meta,
        "marcadores_extras": extras,
        "fatos": None,
        "avisos": [],
    }
    if fatos is not None:
        res["fatos"] = {"qtd_fatos": len(fatos), "fora_da_ficha": fora_da_ficha(texto, frases, fatos, wpm)}
    if tipo == "hook":
        res["avisos"] = avisos_hook(res)
    return res


def avisos_hook(r: dict) -> list[str]:
    av = []
    s = r["segundos_estimados"]
    if s < HOOK_MIN_S or s > HOOK_MAX_S:
        lado = "curto" if s < HOOK_MIN_S else "longo"
        alvo_min = round(HOOK_MIN_S / 60 * r["wpm"])
        alvo_max = round(HOOK_MAX_S / 60 * r["wpm"])
        av.append(f"Duração {fmt(s)} s fora de {HOOK_MIN_S}-{HOOK_MAX_S} s (hook {lado} demais; "
                  f"a {r['wpm']:g} palavras por minuto, {alvo_min} a {alvo_max} palavras).")
    n = r["perguntas"]["total"]
    if n > HOOK_MAX_PERGUNTAS:
        av.append(f"{n} perguntas no hook; mais de {HOOK_MAX_PERGUNTAS} sugere mais de uma pergunta "
                  f"central (heurística: confira qual é a pergunta-mestra).")
    if r["metalinguagem"]:
        av.append(f"{len(r['metalinguagem'])} trecho(s) de metalinguagem: o hook fala do vídeo em "
                  f"vez do caso (ver lista).")
    if not r["perguntas"]["termina_em_pergunta"]:
        av.append("Fecho em afirmação: confira se nomeia algo sem resposta; afirmação que encerra o assunto "
                  "solta a tensão (cole a última frase e diga que laço ela abre).")
    return av


# ---------------------------------------------------------------------------
# Saída
# ---------------------------------------------------------------------------

def relatorio(r: dict, nome: str) -> str:
    L = []
    L.append(f"MEDIÇÃO DE TEXTO: {nome}")
    L.append(f"Tipo: {r['tipo']} | ritmo: {r['wpm']:g} palavras por minuto")
    L.append("")
    seg = r["segundos_estimados"]
    L.append(f"Palavras: {r['palavras']}")
    L.append(f"Duração estimada: {fmt(seg)} s ({int(seg // 60)} min {int(round(seg % 60))} s)")
    L.append(f"Frases: {r['frases']} | média {fmt(r['media_palavras_por_frase'])} palavras por frase | "
             f"maior {r['maior_frase_palavras']} palavras")
    if r["maior_frase_trecho"]:
        L.append(f"  maior frase: \"{r['maior_frase_trecho']}\"")
    p = r["perguntas"]
    if p["total"]:
        L.append(f"Perguntas: {p['total']} | a primeira aos {fmt(p['primeira_em_segundos'])} s "
                 f"(palavra {p['primeira_na_palavra']}) | termina em pergunta: "
                 f"{'sim' if p['termina_em_pergunta'] else 'não'}")
        L.append(f"  primeira: \"{p['primeira_trecho']}\"")
    else:
        L.append("Perguntas: 0 | termina em pergunta: não")
    ult = r["ultima_frase"]
    L.append(f"Última frase ({r['ultima_frase_palavras']} palavras): \"{ult[:140]}\"")
    L.append("")
    meta = r["metalinguagem"]
    L.append(f"Metalinguagem (frases sobre o vídeo): {len(meta)}")
    for a in meta:
        L.append(f"  - [{a['id']}] aos {fmt(a['segundos'])} s: \"{a['trecho']}\"")
    if r["marcadores_extras"]:
        L.append("")
        L.append(f"Marcadores extras (lista externa de marcadores): {len(r['marcadores_extras'])}")
        for a in r["marcadores_extras"]:
            nota = f" ({a['nota']})" if a["nota"] else ""
            L.append(f"  - [{a['id']}]{nota} aos {fmt(a['segundos'])} s: \"{a['trecho']}\"")
    if r["fatos"] is not None:
        L.append("")
        fo = r["fatos"]["fora_da_ficha"]
        L.append(f"Possíveis fatos fora da ficha ({r['fatos']['qtd_fatos']} fatos na ficha): {len(fo)}")
        L.append("  TRIAGEM, não veredito: confere números (inclusive por extenso), datas, siglas e nomes "
                 "próprios fora do início de frase.")
        L.append("  Não pega afirmações sem número ou nome, nem inferências ('o navio foi abandonado'), "
                 "nem nome próprio no início da frase.")
        for a in fo:
            rep = f" (x{a['ocorrencias']})" if a["ocorrencias"] > 1 else ""
            L.append(f"  - {a['tipo']} \"{a['valor']}\"{rep} aos {fmt(a['segundos'])} s: \"{a['trecho']}\"")
    if r["tipo"] == "hook":
        L.append("")
        if r["avisos"]:
            L.append(f"AVISOS DO HOOK ({len(r['avisos'])}):")
            for a in r["avisos"]:
                L.append(f"  ! {a}")
        else:
            L.append("Avisos do hook: nenhum (duração, perguntas, metalinguagem e fecho dentro da heurística).")
        L.append(f"(Janela {HOOK_MIN_S}-{HOOK_MAX_S} s; >{HOOK_MAX_PERGUNTAS} perguntas e fecho são heurísticas.)")
    return "\n".join(L)


def ler_texto(caminho: str) -> tuple[str, str]:
    if caminho == "-":
        return sys.stdin.read(), "(stdin)"
    p = Path(caminho)
    bruto = p.read_text(encoding="utf-8", errors="replace")
    if p.suffix.lower() == ".json":
        try:
            d = json.loads(bruto)
        except ValueError:
            return bruto, p.name
        if isinstance(d, dict):
            for chave in ("texto", "hook", "roteiro"):
                if isinstance(d.get(chave), str):
                    return d[chave], f"{p.name}[{chave}]"
        if isinstance(d, str):
            return d, p.name
        raise SystemExit("JSON sem campo 'texto' ou 'hook'.")
    return bruto, p.name


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Mede um texto narrado: palavras, frases, tempo, perguntas, metalinguagem e fatos fora da ficha.")
    ap.add_argument("texto", help="arquivo de texto (ou '-' para ler de stdin)")
    ap.add_argument("--fatos", help="ficha de fatos: .txt (um por linha) ou .json (lista de strings ou de objetos com 'texto'/'fato')")
    ap.add_argument("--wpm", type=float, default=WPM_PADRAO, help=f"palavras por minuto (padrão {WPM_PADRAO})")
    ap.add_argument("--tipo", choices=("hook", "bloco"), default="bloco", help="'hook' ativa os avisos de hook")
    ap.add_argument("--marcadores", help="JSON de marcadores extras (padrão: references/marcadores_slop.json, se existir)")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    ap.add_argument("--estrito", action="store_true", help="código de saída 1 se houver avisos de hook")
    args = ap.parse_args(argv)

    if args.wpm <= 0:
        ap.error("--wpm deve ser positivo")
    try:
        texto, nome = ler_texto(args.texto)
    except OSError as e:
        print(f"erro: não consegui ler {args.texto}: {e}", file=sys.stderr)
        return 2
    if not texto.strip():
        print("erro: texto vazio", file=sys.stderr)
        return 2
    fatos = None
    if args.fatos:
        try:
            fatos = carregar_fatos(args.fatos)
        except (OSError, ValueError) as e:
            print(f"erro: ficha de fatos ilegível: {e}", file=sys.stderr)
            return 2
    marcadores = carregar_marcadores(args.marcadores)
    r = medir(texto, wpm=args.wpm, tipo=args.tipo, fatos=fatos, marcadores=marcadores)
    r["arquivo"] = nome
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(relatorio(r, nome))
    return 1 if (args.estrito and r["avisos"]) else 0


if __name__ == "__main__":
    sys.exit(main())
