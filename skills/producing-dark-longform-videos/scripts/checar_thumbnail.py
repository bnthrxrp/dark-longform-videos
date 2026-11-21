#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checa uma thumbnail desenhada em SVG (viewBox 1280x720).

Uso:
    python scripts/checar_thumbnail.py THUMB.svg [--titulo "..."] [--png SAIDA.png] [--json]

Saída: PASSOU ou FALHOU, com a lista de problemas e onde estão. Código de saída 0 (passou),
1 (falhou) ou 2 (arquivo ilegível). Só precisa de Python 3.10+; ganha medidas reais se houver
um renderizador, tentado nesta ordem:
  1. Python `playwright` (com Chromium instalado);
  2. pacote node `playwright` (via `node -e`);
  3. `cairosvg` (renderiza o fundo; as caixas de texto continuam estimadas);
  4. nenhum: checagem estática do SVG (PARCIAL; o relatório avisa).

Com renderizador, cada <text> é medido no DOM (caixa real das letras, pixels de tinta),
renderizado sozinho e comparado com o fundo. A medição depende das fontes instaladas na
máquina: Arial Black ou Impact podem cair em outra fonte e mudar larguras.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

# ---------------------------------------------------------------------------
# Limiares (fáceis de editar)
# ---------------------------------------------------------------------------

LARGURA, ALTURA = 1280, 720
FEED_L, FEED_A = 320, 180
MARGEM_SEGURA = 0.05            # 5% de cada lado (64 px na largura, 36 px na altura)
TOLERANCIA_BORDA_PX = 1.5       # quanto passar da borda antes de acusar corte
TOLERANCIA_SEGURA_PX = 2.0      # idem para a área segura
TOLERANCIA_SEGURA_LEVE_PX = 8.0 # invasão da margem até este valor vira só aviso (x=60 em vez de 64)
LETRA_MIN_FEED_PX = 11          # altura de letra mínima no feed 320x180 (~44 px em 1280)
LETRA_APOIO_MIN_FEED_PX = 7     # texto de apoio: abaixo disto (28 px em 1280) bloqueia; entre 7 e 11, só aviso
LETRA_PRINCIPAL_MIN_PX = 80     # aviso: frase principal com menos que isto (1/9 da altura)
CONTRASTE_MIN = 3.0             # razão WCAG mínima entre texto e fundo
PX_BAIXO_MIN = 120              # pixels de letra com contraste < 2:1 (ex.: uma letra metade fora da placa)
OPACIDADE_DECORATIVO = 0.4      # texto com opacidade menor é tratado como marca-d'água
LIMITE_FORMA_MIN, LIMITE_FORMA_MAX = 0.08, 0.92   # fração das amostras sobre uma forma para avisar
SOBREPOSICAO_MIN_PX = 30        # pixels de tinta em comum entre dois textos para acusar
ENCOSTADOS_MIN_PX = 60          # pixels de um texto a menos de 8 px de outro (aviso)
OCULTO_MIN_PX = 25              # pixels de letra cobertos por forma desenhada depois do texto
PALAVRAS_AVISO = 8              # aviso (não bloqueia) acima disto; a mediana de breakouts é 5
SELO_DIRETA_PX = 210            # canto inferior direito reservado ao selo de duração
SELO_BAIXO_PX = 90

STOPWORDS = set("""a o as os um uma uns umas de do da dos das em no na nos nas por pelo pela pelos pelas
para pra com sem sob sobre ate ao aos e ou mas que se nem entre apos contra desde perante ante num numa
nuns numas dum duma deste desta destes destas neste nesta nestes nestas nesse nessa esse essa este esta
isso isto ele ela eles elas seu sua seus suas lhe""".split())


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def sem_acento(s: str) -> str:
    return "".join(unicodedata.normalize("NFD", c)[0] for c in s)


def palavras_de(s: str) -> list[str]:
    return [t for t in re.findall(r"[\wÀ-ÿ'’]+", s) if any(c.isalnum() for c in t)]


def palavras_conteudo(s: str) -> set[str]:
    return {sem_acento(p).lower().strip("'’") for p in palavras_de(s)} - STOPWORDS - {""}


def lum_srgb(r: float, g: float, b: float) -> float:
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def razao(l1: float, l2: float) -> float:
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def fmt(x: float, casas: int = 1) -> str:
    return f"{x:.{casas}f}".replace(".", ",")


def lugar(caixa: list[float]) -> str:
    """Descreve a posição da caixa na imagem em palavras."""
    cx, cy = (caixa[0] + caixa[2]) / 2, (caixa[1] + caixa[3]) / 2
    h = "esquerda" if cx < LARGURA / 3 else "direita" if cx > 2 * LARGURA / 3 else "centro"
    v = "alto" if cy < ALTURA / 3 else "baixo" if cy > 2 * ALTURA / 3 else "meio"
    return f"{v}/{h}"


def letras_curtas(s: str, limite: int = 12) -> str:
    return s if len(s) <= limite else s[:limite] + "…"


def rotulo(t: dict, limite: int = 28) -> str:
    s = t["texto"]
    return '"' + (s if len(s) <= limite else s[: limite - 1] + "…") + '"'


def cx(c: list[float]) -> str:
    return f"x {c[0]:.0f}-{c[2]:.0f}, y {c[1]:.0f}-{c[3]:.0f}"


# ---------------------------------------------------------------------------
# SVG: leitura e análise estática
# ---------------------------------------------------------------------------

CORES_NOMEADAS = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "yellow": (255, 255, 0),
    "gold": (255, 215, 0), "orange": (255, 165, 0), "gray": (128, 128, 128), "grey": (128, 128, 128),
    "silver": (192, 192, 192), "blue": (0, 0, 255), "green": (0, 128, 0), "lime": (0, 255, 0),
    "navy": (0, 0, 128), "purple": (128, 0, 128), "crimson": (220, 20, 60), "ivory": (255, 255, 240),
    "beige": (245, 245, 220), "tan": (210, 180, 140), "brown": (165, 42, 42), "maroon": (128, 0, 0),
    "cyan": (0, 255, 255), "aqua": (0, 255, 255), "pink": (255, 192, 203), "whitesmoke": (245, 245, 245),
    "lightgray": (211, 211, 211), "lightgrey": (211, 211, 211), "darkgray": (169, 169, 169),
    "dimgray": (105, 105, 105), "gainsboro": (220, 220, 220), "tomato": (255, 99, 71),
}


def parse_cor(s: str | None):
    if not s:
        return None
    s = s.strip().lower()
    if s in CORES_NOMEADAS:
        return CORES_NOMEADAS[s]
    m = re.fullmatch(r"#([0-9a-f]{3})", s)
    if m:
        return tuple(int(c * 2, 16) for c in m.group(1))
    m = re.fullmatch(r"#([0-9a-f]{6})(?:[0-9a-f]{2})?", s)
    if m:
        h = m.group(1)
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
    m = re.fullmatch(r"rgba?\(([^)]+)\)", s)
    if m:
        p = [x for x in re.split(r"[ ,/]+", m.group(1)) if x]
        try:
            v = []
            for x in p[:3]:
                v.append(round(float(x[:-1]) * 2.55) if x.endswith("%") else round(float(x)))
            return tuple(v)
        except ValueError:
            return None
    return None


def _local(tag: str) -> str:
    return tag.split("}")[-1] if "}" in tag else tag


def _estilo(el: ET.Element, css: dict) -> dict:
    """Propriedades de apresentação do elemento: regras CSS por tag/classe, atributo, style=."""
    props: dict[str, str] = {}
    tag = _local(el.tag)
    for seletor in (tag, *("." + c for c in (el.get("class") or "").split())):
        props.update(css.get(seletor, {}))
    for k, v in el.attrib.items():
        props[_local(k)] = v
    if el.get("style"):
        for decl in el.get("style").split(";"):
            if ":" in decl:
                k, v = decl.split(":", 1)
                props[k.strip()] = v.strip()
    return props


def _css_de(root: ET.Element) -> dict:
    css: dict[str, dict] = {}
    for el in root.iter():
        if _local(el.tag) == "style" and el.text:
            for sel, corpo in re.findall(r"([^{}]+)\{([^}]*)\}", el.text):
                props = {}
                for decl in corpo.split(";"):
                    if ":" in decl:
                        k, v = decl.split(":", 1)
                        props[k.strip()] = v.strip()
                for s in sel.split(","):
                    css.setdefault(s.strip(), {}).update(props)
    return css


def _num(v, padrao=0.0):
    if v is None:
        return padrao
    m = re.match(r"\s*(-?\d*\.?\d+(?:e-?\d+)?)", str(v))
    return float(m.group(1)) if m else padrao


def _lista_num(v):
    return [float(x) for x in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", v or "")]


def _mat_mul(a, b):
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
            a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
            a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5])


def _parse_transform(s: str | None):
    m = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    for nome, args in re.findall(r"(\w+)\s*\(([^)]*)\)", s or ""):
        v = _lista_num(args)
        if nome == "translate":
            t = (1, 0, 0, 1, v[0] if v else 0, v[1] if len(v) > 1 else 0)
        elif nome == "scale":
            sx = v[0] if v else 1
            t = (sx, 0, 0, v[1] if len(v) > 1 else sx, 0, 0)
        elif nome == "matrix" and len(v) == 6:
            t = tuple(v)
        elif nome == "rotate" and v:
            a = math.radians(v[0])
            c, s_ = math.cos(a), math.sin(a)
            t = (c, s_, -s_, c, 0, 0)
            if len(v) == 3:
                t = _mat_mul(_mat_mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        else:
            continue
        m = _mat_mul(m, t)
    return m


def _aplicar(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def largura_estimada(texto: str, fs: float, familia: str, negrito: bool, espaco: float) -> float:
    """Largura aproximada de uma linha em caixa de texto sem fonte real (estimativa)."""
    fam = (familia or "").lower()
    k = 1.0
    if "black" in fam:
        k = 1.12
    elif "impact" in fam:
        k = 0.82
    elif "mono" in fam or "courier" in fam:
        return len(texto) * (0.6 * fs + espaco)
    elif "serif" in fam and "sans" not in fam or "georgia" in fam or "times" in fam:
        k = 0.97
    if negrito and "black" not in fam and "impact" not in fam:
        k *= 1.04
    w = 0.0
    for c in texto:
        if c == " ":
            w += 0.28
        elif c.isupper():
            w += 0.68
        elif c.isdigit():
            w += 0.56
        elif c in ".,;:!'|·":
            w += 0.28
        elif c in "mwMW":
            w += 0.82
        elif c in "il":
            w += 0.24
        elif c.isalpha():
            w += 0.55
        else:
            w += 0.50
    return w * fs * k + espaco * len(texto)


def analisar_estatico(svg_txt: str) -> dict:
    """Lê o SVG com a biblioteca padrão e estima as caixas de texto (APROXIMADO)."""
    root = ET.fromstring(svg_txt)
    css = _css_de(root)
    vb = _lista_num(root.get("viewBox"))
    info = {
        "viewBox": " ".join(f"{v:g}" for v in vb) if vb else None,
        "largura_attr": root.get("width"),
        "altura_attr": root.get("height"),
    }
    escala = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    if len(vb) == 4 and vb[2] and vb[3]:
        escala = (LARGURA / vb[2], 0, 0, ALTURA / vb[3], -vb[0] * LARGURA / vb[2], -vb[1] * ALTURA / vb[3])
    textos: list[dict] = []
    formas: list[dict] = []
    contador = [0]
    defs: dict[str, ET.Element] = {el.get("id"): el for el in root.iter() if el.get("id")}

    def anda(el: ET.Element, heranca: dict, mat, em_defs: bool):
        tag = _local(el.tag)
        props = dict(heranca)
        est = _estilo(el, css)
        for k in ("font-size", "font-family", "font-weight", "fill", "stroke", "stroke-width", "text-anchor",
                  "letter-spacing", "opacity", "fill-opacity", "font-style"):
            if k in est:
                props[k] = est[k]
        m2 = _mat_mul(mat, _parse_transform(el.get("transform")))
        if tag in ("defs", "symbol", "clipPath", "mask", "pattern", "marker", "filter", "linearGradient",
                   "radialGradient"):
            return
        if tag == "text":
            tx = _texto_estatico(el, props, m2, css, len(textos))
            tx["ordem"] = contador[0]
            contador[0] += 1
            textos.append(tx)
            return
        if tag in ("rect", "circle", "ellipse", "polygon", "polyline", "path", "line", "image"):
            f = _forma_estatica(el, props, m2, est)
            if f:
                f["ordem"] = contador[0]
                formas.append(f)
            contador[0] += 1
        for filho in el:
            anda(filho, props, m2, em_defs)

    anda(root, {"font-size": "16"}, escala, False)
    info["textos"] = [t for t in textos if t["texto"].strip()]
    info["formas"] = formas
    info["gradientes"] = {i: el for i, el in defs.items() if _local(el.tag) in ("linearGradient", "radialGradient")}
    return info


def _forma_estatica(el, props, m, est) -> dict | None:
    tag = _local(el.tag)
    fill = props.get("fill", "black") if "fill" in est or "fill" in props else "black"
    if tag in ("line", "polyline") and "fill" not in props:
        fill = "none"
    box = None
    try:
        if tag == "rect":
            x, y, w, h = _num(el.get("x")), _num(el.get("y")), _num(el.get("width")), _num(el.get("height"))
            pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        elif tag == "circle":
            cx_, cy_, r = _num(el.get("cx")), _num(el.get("cy")), _num(el.get("r"))
            pts = [(cx_ - r, cy_ - r), (cx_ + r, cy_ + r)]
        elif tag == "ellipse":
            cx_, cy_, rx, ry = _num(el.get("cx")), _num(el.get("cy")), _num(el.get("rx")), _num(el.get("ry"))
            pts = [(cx_ - rx, cy_ - ry), (cx_ + rx, cy_ + ry)]
        elif tag in ("polygon", "polyline"):
            v = _lista_num(el.get("points"))
            pts = list(zip(v[0::2], v[1::2]))
        elif tag == "line":
            pts = [(_num(el.get("x1")), _num(el.get("y1"))), (_num(el.get("x2")), _num(el.get("y2")))]
        elif tag == "image":
            x, y, w, h = _num(el.get("x")), _num(el.get("y")), _num(el.get("width")), _num(el.get("height"))
            pts = [(x, y), (x + w, y + h)]
        else:
            return None  # path: caixa não estimada sem interpretar os comandos
    except (ValueError, TypeError):
        return None
    if not pts:
        return None
    pts = [_aplicar(m, px, py) for px, py in pts]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    box = [min(xs), min(ys), max(xs), max(ys)]
    return {"tag": tag, "caixa": box, "fill": fill,
            "opacidade": _num(props.get("opacity"), 1.0) * _num(props.get("fill-opacity"), 1.0),
            "retangular": tag in ("rect", "image")}


def _texto_estatico(el, props, m, css, idx) -> dict:
    fs = _num(props.get("font-size"), 16.0)
    fam = props.get("font-family", "sans-serif")
    peso = str(props.get("font-weight", "normal")).lower()
    negrito = peso in ("bold", "bolder") or (peso.isdigit() and int(peso) >= 600)
    ancora = props.get("text-anchor", "start")
    espaco = _num(props.get("letter-spacing"), 0.0)
    rot = abs(m[1]) > 0.01 or abs(m[2]) > 0.01
    escala = math.hypot(m[0], m[1])
    # linhas: texto direto + tspans (cada tspan com x/y/dy abre linha própria)
    x0 = _lista_num(el.get("x"))
    y0 = _lista_num(el.get("y"))
    x, y = (x0[0] if x0 else 0.0), (y0[0] if y0 else 0.0)
    dx0 = _lista_num(el.get("dx"))
    x += dx0[0] if dx0 else 0.0
    dy0 = _lista_num(el.get("dy"))
    y += dy0[0] if dy0 else 0.0
    linhas: list[dict] = []
    atual = {"txt": "", "x": x, "y": y, "fs": fs, "anc": ancora, "esp": espaco, "neg": negrito, "fam": fam}
    text_length = _num(el.get("textLength"), 0.0) or None
    linhas.append(atual)

    def percorre(nodo, pr_fs, pr_anc, pr_neg, pr_esp, pr_fam):
        nonlocal atual
        if nodo.text:
            atual["txt"] += re.sub(r"\s+", " ", nodo.text)
        for filho in nodo:
            if _local(filho.tag) == "tspan":
                est = _estilo(filho, css)
                f_fs = _num(est.get("font-size"), pr_fs)
                f_anc = est.get("text-anchor", pr_anc)
                p = str(est.get("font-weight", "")).lower()
                f_neg = pr_neg if not p else (p in ("bold", "bolder") or (p.isdigit() and int(p) >= 600))
                f_esp = _num(est.get("letter-spacing"), pr_esp)
                f_fam = est.get("font-family", pr_fam)
                nx, ny = _lista_num(filho.get("x")), _lista_num(filho.get("y"))
                ndx, ndy = _lista_num(filho.get("dx")), _lista_num(filho.get("dy"))
                if nx or ny or ndy:
                    atual = {"txt": "", "x": nx[0] if nx else atual["x"], "y": (ny[0] if ny else atual["y"]) + (ndy[0] if ndy else 0.0),
                             "fs": f_fs, "anc": f_anc, "esp": f_esp, "neg": f_neg, "fam": f_fam}
                    linhas.append(atual)
                else:
                    atual["fs"] = max(atual["fs"], f_fs)
                percorre(filho, f_fs, f_anc, f_neg, f_esp, f_fam)
            if filho.tail:
                atual["txt"] += re.sub(r"\s+", " ", filho.tail)

    percorre(el, fs, ancora, negrito, espaco, fam)
    caixas = []
    textos_linhas = []
    for ln in linhas:
        txt = ln["txt"].strip()
        if not txt:
            continue
        w = (text_length if text_length and len(linhas) == 1 else largura_estimada(txt, ln["fs"], ln["fam"], ln["neg"], ln["esp"]))
        if ln["anc"] == "middle":
            ini = ln["x"] - w / 2
        elif ln["anc"] == "end":
            ini = ln["x"] - w
        else:
            ini = ln["x"]
        acento = bool(re.search(r"[ÁÀÂÃÉÊÍÓÔÕÚÜ]", txt))
        desc = bool(re.search(r"[gjpqyçQ,;]", txt))
        topo = ln["y"] - ln["fs"] * (0.93 if acento else 0.73)
        base = ln["y"] + ln["fs"] * (0.21 if desc else 0.02)
        pts = [_aplicar(m, ini, topo), _aplicar(m, ini + w, topo), _aplicar(m, ini, base), _aplicar(m, ini + w, base)]
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        caixas.append([min(xs), min(ys), max(xs), max(ys)])
        textos_linhas.append(txt)
    if caixas:
        caixa = [min(c[0] for c in caixas), min(c[1] for c in caixas), max(c[2] for c in caixas), max(c[3] for c in caixas)]
    else:
        caixa = [0, 0, 0, 0]
    fs_max = max((ln["fs"] for ln in linhas if ln["txt"].strip()), default=fs)
    fs_min = min((ln["fs"] for ln in linhas if ln["txt"].strip()), default=fs)
    return {
        "indice": idx,
        "texto": " ".join(textos_linhas),
        "palavras": len(palavras_de(" ".join(textos_linhas))),
        "fontPx": fs_max * escala,
        "fontPxMin": fs_min * escala,
        "caixa": caixa,
        "linhas_caixas": caixas,
        "fill": props.get("fill", "black"),
        "stroke": props.get("stroke", "none"),
        "stroke_width": _num(props.get("stroke-width"), 0.0) * escala,
        "rot": rot,
        "opacidade": _num(props.get("opacity"), 1.0) * _num(props.get("fill-opacity"), 1.0),
        "estimado": True,
    }


def _cor_de_fill(fill: str | None, gradientes: dict):
    cores = _cores_do_fill(fill, gradientes)
    if not cores:
        return None
    return tuple(sum(c[i] for c in cores) // len(cores) for i in range(3))


def _cores_do_fill(fill: str | None, gradientes: dict) -> list[tuple]:
    """Cores possíveis de um preenchimento: a cor sólida, ou todas as paradas do gradiente."""
    c = parse_cor(fill)
    if c:
        return [c]
    m = re.match(r"url\(#([^)]+)\)", fill or "")
    if m and m.group(1) in gradientes:
        cores = []
        for st in gradientes[m.group(1)].iter():
            if _local(st.tag) == "stop":
                cc = parse_cor(_estilo(st, {}).get("stop-color"))
                if cc:
                    cores.append(cc)
        return cores
    return []


def fundo_estatico(t: dict, info: dict) -> list[list[tuple]]:
    """Para cinco pontos da caixa do texto, as cores possíveis do que está atrás, olhando só formas
    simples (rect, circle, ellipse, polygon, line) desenhadas antes do texto. A última forma que cobre o ponto
    vence; gradiente vira o conjunto das suas paradas; forma translúcida deixa o que havia antes como possível."""
    c = t["caixa"]
    pontos = [((c[0] + c[2]) / 2, (c[1] + c[3]) / 2), (c[0] + 2, (c[1] + c[3]) / 2),
              (c[2] - 2, (c[1] + c[3]) / 2), ((c[0] + c[2]) / 2, c[1] + 2), ((c[0] + c[2]) / 2, c[3] - 2)]
    saida = []
    for px, py in pontos:
        cores: list[tuple] = []
        for f in info["formas"]:
            if f["ordem"] > t["ordem"] or f["tag"] in ("line", "polyline", "image"):
                continue
            b = f["caixa"]
            if not (b[0] <= px <= b[2] and b[1] <= py <= b[3]):
                continue
            if f["tag"] in ("circle", "ellipse"):
                ex, ey = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
                rx, ry = (b[2] - b[0]) / 2 or 1, (b[3] - b[1]) / 2 or 1
                if ((px - ex) / rx) ** 2 + ((py - ey) / ry) ** 2 > 1:
                    continue
            novas = _cores_do_fill(f["fill"], info["gradientes"])
            if not novas:
                continue
            if f["opacidade"] >= 0.95 and not str(f["fill"]).startswith("url("):
                cores = novas
            else:
                cores = cores + novas if cores else novas
        saida.append(cores)
    return saida


# ---------------------------------------------------------------------------
# PNG puro (para o caminho com cairosvg, sem Pillow)
# ---------------------------------------------------------------------------

def ler_png(dados: bytes):
    """Decodifica PNG 8 bits (RGB, RGBA, cinza) sem dependências. Devolve (w, h, canais, bytearray)."""
    try:
        from PIL import Image  # type: ignore
        import io
        im = Image.open(io.BytesIO(dados)).convert("RGBA")
        return im.size[0], im.size[1], 4, bytearray(im.tobytes())
    except Exception:
        pass
    assert dados[:8] == b"\x89PNG\r\n\x1a\n"
    pos = 8
    idat = b""
    w = h = depth = ctype = 0
    while pos < len(dados):
        n, tipo = struct.unpack(">I4s", dados[pos:pos + 8])
        corpo = dados[pos + 8:pos + 8 + n]
        pos += 12 + n
        if tipo == b"IHDR":
            w, h, depth, ctype, _c, _f, inter = struct.unpack(">IIBBBBB", corpo)
        elif tipo == b"IDAT":
            idat += corpo
        elif tipo == b"IEND":
            break
    canais = {0: 1, 2: 3, 4: 2, 6: 4}[ctype]
    if depth != 8 or inter:
        raise ValueError("PNG não suportado")
    raw = zlib.decompress(idat)
    stride = w * canais
    out = bytearray(h * stride)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        f = raw[p]
        linha = bytearray(raw[p + 1:p + 1 + stride])
        p += 1 + stride
        if f == 1:
            for i in range(canais, stride):
                linha[i] = (linha[i] + linha[i - canais]) & 255
        elif f == 2:
            for i in range(stride):
                linha[i] = (linha[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                a = linha[i - canais] if i >= canais else 0
                linha[i] = (linha[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = linha[i - canais] if i >= canais else 0
                b = prev[i]
                c = prev[i - canais] if i >= canais else 0
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                linha[i] = (linha[i] + pr) & 255
        out[y * stride:(y + 1) * stride] = linha
        prev = linha
    return w, h, canais, out


# ---------------------------------------------------------------------------
# Renderizadores
# ---------------------------------------------------------------------------

# Roda DENTRO da página (Chromium). Mede cada <text> no DOM e por pixels: renderiza o SVG sem
# texto (fundo), cada texto isolado (por cima de tudo e no lugar original) e compara.
JS_ANALISE = r"""
async (opts) => {
  const W = 1280, H = 720;
  const svg = document.querySelector('svg');
  if (!svg) return {erro: 'sem elemento <svg>'};
  svg.setAttribute('width', String(W)); svg.setAttribute('height', String(H));
  const LUT = new Float32Array(256);
  for (let i = 0; i < 256; i++) { const c = i / 255; LUT[i] = c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  const lum = (r, g, b) => 0.2126 * LUT[r] + 0.7152 * LUT[g] + 0.0722 * LUT[b];
  const ratio = (a, b) => (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
  const hex = (r, g, b) => '#' + [r, g, b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const parseCor = (s) => { const m = /rgba?\(([^)]+)\)/.exec(s || ''); if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return {r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1}; };
  const pct = (arr, q) => { if (!arr.length) return null; const s = Float32Array.from(arr).sort(); return s[Math.min(s.length - 1, Math.floor(q * s.length))]; };

  const IGN = 'defs,symbol,clipPath,mask,pattern,marker,filter,linearGradient,radialGradient';
  const cand = Array.from(svg.querySelectorAll('text')).filter(el => !el.closest(IGN));
  const itens = [];
  for (const el of cand) {
    const partes = [];
    const tw0 = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let n0;
    while ((n0 = tw0.nextNode())) { const t0 = n0.data.replace(/\s+/g, ' ').trim(); if (t0) partes.push(t0); }
    const txt = partes.join(' ');   // um espaço entre tspans/linhas
    if (!txt) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    let op = 1;
    for (let e = el; e && e !== document.body; e = e.parentElement) { const o = parseFloat(getComputedStyle(e).opacity); if (!isNaN(o)) op *= o; }
    if (op < 0.05) continue;
    if ((cs.fill === 'none' || parseFloat(cs.fillOpacity) === 0) && cs.stroke === 'none') continue;
    el.setAttribute('data-ck', String(itens.length));
    itens.push({el, txt, cs, opac: op * (isNaN(parseFloat(cs.fillOpacity)) ? 1 : parseFloat(cs.fillOpacity))});
  }
  const LIMITE = 40;
  const truncado = itens.length > LIMITE;
  if (truncado) itens.length = LIMITE;

  // ---- geometria por letra (Range por caractere + métricas reais da fonte via canvas) ----
  const ctx0 = document.createElement('canvas').getContext('2d');
  function geometria(it) {
    const chars = [];
    const tw = document.createTreeWalker(it.el, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = tw.nextNode())) {
      const par = n.parentElement; const pcs = getComputedStyle(par);
      const ctm = par.getScreenCTM(); if (!ctm) continue;
      const esc = Math.hypot(ctm.a, ctm.b);
      const rot = Math.abs(ctm.b) > 0.01 || Math.abs(ctm.c) > 0.01;
      const fsU = parseFloat(pcs.fontSize); const fontPx = fsU * esc;
      ctx0.font = `${pcs.fontStyle} ${pcs.fontWeight} ${fsU}px ${pcs.fontFamily}`;
      const cache = {};
      for (let i = 0; i < n.data.length; i++) {
        const ch = n.data[i]; if (/\s/.test(ch)) continue;
        const q = document.createRange(); q.setStart(n, i); q.setEnd(n, i + 1);
        const rc = q.getClientRects(); if (!rc.length) continue;
        const r = rc[0]; if (r.width === 0 && r.height === 0) continue;
        let m = cache[ch];
        if (!m) { const mm = ctx0.measureText(ch);
          m = cache[ch] = {a: mm.actualBoundingBoxAscent, d: mm.actualBoundingBoxDescent, l: mm.actualBoundingBoxLeft, rr: mm.actualBoundingBoxRight, fa: mm.fontBoundingBoxAscent}; }
        let x0, x1, y0, y1, base;
        if (rot) { x0 = r.left; x1 = r.right; y0 = r.top; y1 = r.bottom; base = r.bottom; }
        else { base = r.top + m.fa * esc; y0 = base - m.a * esc; y1 = base + m.d * esc; x0 = r.left - m.l * esc; x1 = r.left + m.rr * esc; }
        chars.push({c: ch, x0, x1, y0, y1, base, fontPx, rot});
      }
    }
    return chars;
  }
  function linhasDe(chars) {
    const ord = chars.slice().sort((a, b) => a.base - b.base);
    const grupos = [];
    for (const c of ord) {
      const g = grupos.find(g => c.rot || g.rot ? true : Math.abs(g.base - c.base) <= 0.35 * c.fontPx);
      if (g) { g.chars.push(c); } else grupos.push({base: c.base, rot: c.rot, chars: [c]});
    }
    return grupos.map(g => {
      g.chars.sort((a, b) => a.x0 - b.x0);
      return {x0: Math.min(...g.chars.map(c => c.x0)), x1: Math.max(...g.chars.map(c => c.x1)),
              y0: Math.min(...g.chars.map(c => c.y0)), y1: Math.max(...g.chars.map(c => c.y1)),
              texto: g.chars.map(c => c.c).join(''), chars: g.chars};
    }).sort((a, b) => a.y0 - b.y0);
  }
  function excesso(chars, xmin, ymin, xmax, ymax, tol) {
    const o = {esq: 0, dir: 0, topo: 0, base: 0, letras: {esq: '', dir: '', topo: '', base: ''}};
    for (const c of chars) {
      if (xmin - c.x0 > tol) { o.esq = Math.max(o.esq, xmin - c.x0); o.letras.esq += c.c; }
      if (c.x1 - xmax > tol) { o.dir = Math.max(o.dir, c.x1 - xmax); o.letras.dir += c.c; }
      if (ymin - c.y0 > tol) { o.topo = Math.max(o.topo, ymin - c.y0); o.letras.topo += c.c; }
      if (c.y1 - ymax > tol) { o.base = Math.max(o.base, c.y1 - ymax); o.letras.base += c.c; }
    }
    return o;
  }

  // ---- renderização por variantes (SVG -> imagem -> canvas) ----
  async function render(mod, w = W, h = H, fundo = '#ffffff') {
    const clone = svg.cloneNode(true);
    clone.setAttribute('width', String(w)); clone.setAttribute('height', String(h));
    clone.removeAttribute('style');
    mod(clone);
    const xml = new XMLSerializer().serializeToString(clone);
    const img = new Image();
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(xml);
    await img.decode();
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const x = c.getContext('2d', {willReadFrequently: true});
    x.fillStyle = fundo; x.fillRect(0, 0, w, h);
    x.drawImage(img, 0, 0, w, h);
    return x.getImageData(0, 0, w, h).data;
  }
  const textosDe = (c) => Array.from(c.querySelectorAll('text'));
  const modFundo = (c) => textosDe(c).forEach(t => t.remove());
  const modIso = (k, topo) => (c) => {
    for (const t of textosDe(c)) {
      if (t.getAttribute('data-ck') !== String(k)) t.remove();
    }
    if (topo) {
      const t = c.querySelector(`text[data-ck="${k}"]`);
      if (!t) return;
      const cadeia = []; for (let e = t.parentElement; e && e !== c; e = e.parentElement) cadeia.unshift(e);
      let cur = c;
      for (const a of cadeia) { const n = a.cloneNode(false); n.removeAttribute('id'); cur.appendChild(n); cur = n; }
      const copia = t.cloneNode(true); copia.removeAttribute('id'); cur.appendChild(copia);
      t.remove();
    }
  };

  const GEOM = 'path,rect,circle,ellipse,line,polyline,polygon,image,use,foreignObject';
  // só o texto k, sem nenhuma forma desenhada (fundo do canvas define a cor atrás)
  const modSoTexto = (k) => (c) => {
    modIso(k, false)(c);
    for (const e of Array.from(c.querySelectorAll(GEOM))) if (!e.closest(IGN)) e.style.display = 'none';
  };
  const bg = await render(modFundo);
  const ar = W * H;

  // ---- por texto ----
  const resultados = [];
  const mascaras = [];
  for (let k = 0; k < itens.length; k++) {
    const it = itens[k];
    const chars = geometria(it);
    const linhas = linhasDe(chars);
    const cs = it.cs;
    let fontMin = Infinity, fontMax = 0;
    for (const c of chars) { fontMin = Math.min(fontMin, c.fontPx); fontMax = Math.max(fontMax, c.fontPx); }
    const geo = chars.length ? [Math.min(...chars.map(c => c.x0)), Math.min(...chars.map(c => c.y0)),
                                Math.max(...chars.map(c => c.x1)), Math.max(...chars.map(c => c.y1))] : [0, 0, 0, 0];
    const fora = excesso(chars, 0, 0, W, H, 1.5);
    const seguro = excesso(chars, W * 0.05, H * 0.05, W * 0.95, H * 0.95, 2);
    // linhas do mesmo texto que se tocam
    const colisoes = [];
    for (let a = 0; a < linhas.length; a++) for (let b = a + 1; b < linhas.length; b++) {
      let n = 0; const cx = [];
      for (const ca of linhas[a].chars) for (const cb of linhas[b].chars) {
        const iw = Math.min(ca.x1, cb.x1) - Math.max(ca.x0, cb.x0), ih = Math.min(ca.y1, cb.y1) - Math.max(ca.y0, cb.y0);
        if (iw > 1 && ih > 1.5) { n++; if (cx.length < 3) cx.push(ca.c + cb.c); }
      }
      if (n) colisoes.push({a: linhas[a].texto, b: linhas[b].texto, pares: n, letras: cx});
    }
    // pixels: cobertura da letra (independe da cor), render por cima de tudo e no lugar original
    const isoW = await render(modSoTexto(k), W, H, '#ffffff');
    const isoB = await render(modSoTexto(k), W, H, '#000000');
    const alfa = new Float32Array(ar);
    let amax = 0;
    for (let i = 0, p = 0; i < ar; i++, p += 4) {
      const d = Math.abs(isoW[p] - isoB[p]) + Math.abs(isoW[p + 1] - isoB[p + 1]) + Math.abs(isoW[p + 2] - isoB[p + 2]);
      const a = 1 - d / 765; alfa[i] = a; if (a > amax) amax = a;
    }
    const top = await render(modIso(k, true));
    const inpl = await render(modIso(k, false));
    const mask = new Uint8Array(ar);
    let nink = 0, minx = W, miny = H, maxx = -1, maxy = -1;
    const core = [];
    const lim = Math.max(0.05, amax);
    for (let i = 0; i < ar; i++) {
      const a = alfa[i];
      if (a >= 0.5 * lim && a > 0.04) {
        mask[i] = 1; nink++;
        const x = i % W, y = (i / W) | 0;
        if (x < minx) minx = x; if (x > maxx) maxx = x; if (y < miny) miny = y; if (y > maxy) maxy = y;
        if (a >= 0.85 * lim) core.push(i);
      }
    }
    // oculto: tinta que existiria por cima de tudo, mas some no lugar original (forma desenhada depois)
    let oculto = 0;
    for (const i of core) {
      const p = i * 4;
      const dt = Math.abs(top[p] - bg[p]) + Math.abs(top[p + 1] - bg[p + 1]) + Math.abs(top[p + 2] - bg[p + 2]);
      if (dt < 90) continue;
      const d = Math.abs(inpl[p] - bg[p]) + Math.abs(inpl[p + 1] - bg[p + 1]) + Math.abs(inpl[p + 2] - bg[p + 2]);
      if (d < 0.35 * dt) oculto++;
    }
    // contraste por pixel de núcleo, como o espectador vê (render no lugar original)
    const razoes = []; const rs = [], gs = [], bs = [], rb = [], gb = [], bb = [];
    const passo = Math.max(1, Math.floor(core.length / 20000));
    for (let j = 0; j < core.length; j += passo) {
      const p = core[j] * 4;
      razoes.push(ratio(lum(inpl[p], inpl[p + 1], inpl[p + 2]), lum(bg[p], bg[p + 1], bg[p + 2])));
      rs.push(inpl[p]); gs.push(inpl[p + 1]); bs.push(inpl[p + 2]); rb.push(bg[p]); gb.push(bg[p + 1]); bb.push(bg[p + 2]);
    }
    const med = (a) => pct(a, 0.5);
    const corTexto = rs.length ? [med(rs), med(gs), med(bs)] : null;
    const corFundo = rb.length ? [med(rb), med(gb), med(bb)] : null;
    const fracBaixo = razoes.length ? razoes.filter(r => r < 3).length / razoes.length : null;
    const pxBaixo2 = razoes.filter(r => r < 2).length * passo, pxBaixo3 = razoes.filter(r => r < 3).length * passo;
    const fill = parseCor(cs.fill), stroke = parseCor(cs.stroke);
    const escEl = (() => { const m = it.el.getScreenCTM(); return m ? Math.hypot(m.a, m.b) : 1; })();
    const sw = parseFloat(cs.strokeWidth) * escEl;
    const contorno = !!(stroke && cs.stroke !== 'none' && sw >= 2 && parseFloat(cs.strokeOpacity) > 0.5);
    let razaoFillStroke = null;
    if (contorno && fill) razaoFillStroke = ratio(lum(fill.r, fill.g, fill.b), lum(stroke.r, stroke.g, stroke.b));
    // formas sob e sobre o texto (hit-test em amostras do núcleo)
    const sob = {}, acima = {};
    const amostras = Math.min(core.length, 150);
    for (let j = 0; j < amostras; j++) {
      const i = core[Math.floor(j * core.length / amostras)];
      const x = (i % W) + 0.5, y = ((i / W) | 0) + 0.5;
      const pilha = document.elementsFromPoint(x, y);
      const pos = pilha.findIndex(e => e.closest && e.closest('text') === it.el);
      if (pos < 0) continue;
      pilha.forEach((e, idx) => {
        if (e === svg || e.closest('text') || !(e instanceof SVGGraphicsElement)) return;
        const bb2 = e.getBoundingClientRect();
        if (bb2.width * bb2.height >= 0.6 * ar) return; // fundo
        const nome = e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.getAttribute('fill') ? ' fill=' + e.getAttribute('fill') : '');
        const alvo = idx < pos ? acima : sob;
        alvo[nome] = (alvo[nome] || 0) + 1;
      });
    }
    const topN = (o) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, 3).map(([n, c]) => ({forma: n, amostras: c, de: amostras}));
    const rotulosCaixa = nink ? [minx, miny, maxx + 1, maxy + 1] : geo;
    resultados.push({
      k, texto: it.txt, palavras: it.txt.split(/\s+/).filter(w => /[\p{L}\p{N}]/u.test(w)).length,
      fontPx: fontMax, fontPxMin: isFinite(fontMin) ? fontMin : 0, peso: cs.fontWeight, familia: cs.fontFamily,
      opacidade: it.opac, fill: cs.fill, stroke: cs.stroke, contorno, razaoFillStroke,
      caixaGeom: geo, caixa: rotulosCaixa, inkPx: nink,
      linhas: linhas.map(l => ({texto: l.texto, caixa: [l.x0, l.y0, l.x1, l.y1]})),
      fora, seguro, colisoes,
      contraste: {mediano: pct(razoes, 0.5), pior: pct(razoes, 0.1), fracBaixo, pxBaixo2, pxBaixo3, nucleo: core.length, corTexto: corTexto && hex(...corTexto), corFundo: corFundo && hex(...corFundo)},
      ocultoFrac: nink ? oculto / nink : 0, ocultoPx: oculto,
      sob: topN(sob), acima: topN(acima),
    });
    mascaras.push({mask, minx, miny, maxx, maxy});
  }
  // ---- sobreposição e encostamento entre textos ----
  const pares = [];
  const R = 8;
  for (let a = 0; a < mascaras.length; a++) for (let b = a + 1; b < mascaras.length; b++) {
    const A = mascaras[a], B = mascaras[b];
    if (A.maxx < 0 || B.maxx < 0) continue;
    const x0 = Math.max(A.minx, B.minx) - R, x1 = Math.min(A.maxx, B.maxx) + R, y0 = Math.max(A.miny, B.miny) - R, y1 = Math.min(A.maxy, B.maxy) + R;
    if (x1 < x0 || y1 < y0) continue;
    const cx0 = Math.max(0, x0), cx1 = Math.min(W - 1, x1), cy0 = Math.max(0, y0), cy1 = Math.min(H - 1, y1);
    const rw = cx1 - cx0 + 1, rh = cy1 - cy0 + 1;
    // A dilatada por R pixels dentro da região (máximo separável)
    const h = new Uint8Array(rw * rh), d = new Uint8Array(rw * rh);
    for (let y = 0; y < rh; y++) for (let x = 0; x < rw; x++) {
      if (!A.mask[(cy0 + y) * W + cx0 + x]) continue;
      for (let k = Math.max(0, x - R); k <= Math.min(rw - 1, x + R); k++) h[y * rw + k] = 1;
    }
    for (let y = 0; y < rh; y++) for (let x = 0; x < rw; x++) {
      if (!h[y * rw + x]) continue;
      for (let k = Math.max(0, y - R); k <= Math.min(rh - 1, y + R); k++) d[k * rw + x] = 1;
    }
    let n = 0, perto = 0, ix0 = W, iy0 = H, ix1 = -1, iy1 = -1;
    for (let y = 0; y < rh; y++) for (let x = 0; x < rw; x++) {
      const i = (cy0 + y) * W + cx0 + x;
      if (!B.mask[i]) continue;
      if (A.mask[i]) { n++; const X = cx0 + x, Y = cy0 + y; if (X < ix0) ix0 = X; if (X > ix1) ix1 = X; if (Y < iy0) iy0 = Y; if (Y > iy1) iy1 = Y; }
      else if (d[y * rw + x]) perto++;
    }
    if (n > 0 || perto > 0) pares.push({a, b, px: n, perto, caixa: n ? [ix0, iy0, ix1 + 1, iy1 + 1] : [cx0, cy0, cx1 + 1, cy1 + 1]});
  }
  // ---- feed 320x180 ----
  const FW = 320, FH = 180, E = W / FW;
  const feed = await render(() => {}, FW, FH);
  const lumF = new Float32Array(FW * FH);
  for (let i = 0, p = 0; i < FW * FH; i++, p += 4) lumF[i] = lum(feed[p], feed[p + 1], feed[p + 2]);
  mascaras.forEach((M, k) => {
    const r = resultados[k];
    if (!r.inkPx) { r.feed = {sumiu: true, nucleo: 0, contraste: null}; return; }
    const fx0 = Math.max(0, Math.floor(M.minx / E) - 5), fx1 = Math.min(FW - 1, Math.floor(M.maxx / E) + 5);
    const fy0 = Math.max(0, Math.floor(M.miny / E) - 5), fy1 = Math.min(FH - 1, Math.floor(M.maxy / E) + 5);
    let nuc = 0, somaN = 0, nb = 0, somaB = 0;
    for (let fy = fy0; fy <= fy1; fy++) for (let fx = fx0; fx <= fx1; fx++) {
      let cov = 0;
      for (let dy = 0; dy < E; dy++) { const y = fy * E + dy; for (let dx = 0; dx < E; dx++) cov += M.mask[y * W + fx * E + dx]; }
      cov /= (E * E);
      const L = lumF[fy * FW + fx];
      if (cov >= 0.6) { nuc++; somaN += L; } else if (cov === 0) { nb++; somaB += L; }
    }
    r.feed = {nucleo: nuc, sumiu: nuc === 0, contraste: nuc && nb ? ratio(somaN / nuc, somaB / nb) : null};
  });
  return {viewBox: svg.getAttribute('viewBox'), textos: resultados, pares, truncado,
          nTextosNoSvg: cand.length};
}
"""

# Script node (executado com `node -e`): mesma análise, com o playwright do node.
JS_NODE = r"""
const fs = require('fs');
const {chromium} = require('playwright');
(async () => {
  const job = JSON.parse(fs.readFileSync(process.argv[1], 'utf8'));
  const analisar = %(analise)s;
  const b = await chromium.launch();
  try {
    const p = await b.newPage({viewport: {width: 1280, height: 720}});
    await p.route('**/*', r => { const u = r.request().url(); (u.startsWith('data:') || u.startsWith('about:')) ? r.continue() : r.abort(); });
    const svg = fs.readFileSync(job.svg, 'utf8');
    await p.setContent('<!doctype html><html><body style="margin:0;background:#fff">' + svg + '</body></html>');
    const res = await p.evaluate(analisar, {});
    if (job.png) await p.screenshot({path: job.png, clip: {x: 0, y: 0, width: 1280, height: 720}});
    if (job.feed) {
      const pf = await b.newPage({viewport: {width: 320, height: 180}});
      await pf.route('**/*', r => { const u = r.request().url(); (u.startsWith('data:') || u.startsWith('about:')) ? r.continue() : r.abort(); });
      await pf.setContent('<!doctype html><html><body style="margin:0;background:#fff">' + fs.readFileSync(job.feedSvg, 'utf8') + '</body></html>');
      await pf.screenshot({path: job.feed, clip: {x: 0, y: 0, width: 320, height: 180}});
    }
    process.stdout.write('\nRESULTADO_JSON:' + JSON.stringify(res) + '\n');
  } finally { await b.close(); }
})().catch(e => { process.stderr.write(String(e && e.stack || e) + '\n'); process.exit(3); });
"""


def limpar_svg(svg_txt: str) -> tuple[str, list[str]]:
    """Remove declaração XML e <script>/atributos on*; devolve o SVG seguro para embutir."""
    avisos = []
    s = re.sub(r"<\?xml[^>]*\?>", "", svg_txt)
    s = re.sub(r"<!DOCTYPE[^>]*>", "", s, flags=re.I)
    if re.search(r"<script\b", s, re.I):
        avisos.append("o SVG tem <script>; removido antes de renderizar (a skill proíbe script)")
        s = re.sub(r"<script\b.*?</script>", "", s, flags=re.I | re.S)
    s = re.sub(r"\son\w+\s*=\s*(\"[^\"]*\"|'[^']*')", "", s, flags=re.I)
    return s.strip(), avisos


def _achar_chromium() -> list[str]:
    """Procura binários de Chromium já baixados (outras versões do playwright, cache comum)."""
    raizes = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH", ""), os.path.expanduser("~/.cache/ms-playwright"),
              "/opt/pw-browsers", "/ms-playwright"]
    achados: list[str] = []
    for raiz in raizes:
        if not raiz or not os.path.isdir(raiz):
            continue
        for raiz_dir, dirs, arquivos in os.walk(raiz):
            if raiz_dir[len(raiz):].count(os.sep) > 4:
                dirs[:] = []
                continue
            for nome in arquivos:
                if nome in ("chrome", "headless_shell", "chrome-headless-shell"):
                    caminho = os.path.join(raiz_dir, nome)
                    if os.access(caminho, os.X_OK) and "ffmpeg" not in caminho:
                        achados.append(caminho)
    return sorted(achados, reverse=True)


def svg_para_feed(svg: str) -> str:
    """SVG pronto para renderizar em 320x180: garante viewBox e troca width/height.

    Sem viewBox, mudar width/height só recorta o canto superior esquerdo em vez de reduzir.
    """
    m = re.search(r"<svg\b[^>]*>", svg, re.I)
    if not m:
        return svg
    tag = m.group(0)
    def attr(nome: str) -> str | None:
        a = re.search(r"\s" + nome + r"\s*=\s*(\"([^\"]*)\"|'([^']*)')", tag, re.I)
        return (a.group(2) if a.group(2) is not None else a.group(3)) if a else None
    larg = re.match(r"\s*([0-9.]+)", attr("width") or "")
    alt = re.match(r"\s*([0-9.]+)", attr("height") or "")
    vb = attr("viewBox")
    novo = re.sub(r"\s(width|height)\s*=\s*(\"[^\"]*\"|'[^']*')", "", tag, flags=re.I)
    extra = f' width="{FEED_L}" height="{FEED_A}"'
    if not vb:
        extra += f' viewBox="0 0 {larg.group(1) if larg else LARGURA} {alt.group(1) if alt else ALTURA}"'
    novo = novo[:-1].rstrip("/") + extra + ">"
    return svg.replace(tag, novo, 1)


def validar_feed(png: str, feed: str) -> list[dict]:
    """Confere o feed contra o PNG cheio reduzido; se divergir, regera o feed e avisa.

    Foi visto um feed quebrado (recorte do canto, quase preto) com RESULTADO: PASSOU.
    Sem PIL não há como comparar: o aviso manda abrir a imagem.
    """
    try:
        from PIL import Image  # type: ignore
    except Exception:
        return [{"tipo": "feed_nao_validado", "texto": "PIL ausente: o feed não foi comparado com o PNG cheio; "
                 "abra o arquivo de feed e confira que mostra a thumbnail inteira", "onde": ""}]
    try:
        cheio = Image.open(png).convert("RGB")
        ref = cheio.resize((FEED_L, FEED_A), Image.LANCZOS)
        atual = Image.open(feed).convert("RGB")
        from PIL import ImageStat  # type: ignore
        media = lambda im: ImageStat.Stat(im.convert("L")).mean[0]
        ok = atual.size == (FEED_L, FEED_A) and abs(media(atual) - media(ref)) <= 12
        if ok:
            # compara também uma grade 4x4 de blocos, para pegar recorte com média parecida
            for gy in range(4):
                for gx in range(4):
                    caixa = (gx * 80, gy * 45, gx * 80 + 80, gy * 45 + 45)
                    if abs(media(atual.crop(caixa)) - media(ref.crop(caixa))) > 40:
                        ok = False
        if not ok:
            ref.save(feed)
            return [{"tipo": "feed_invalido", "texto": "FEED INVÁLIDO: o feed do navegador não correspondia ao PNG "
                     "cheio (recorte ou imagem quase vazia); foi regerado reduzindo o PNG. Abra-o e confira", "onde": feed}]
    except Exception as e:
        return [{"tipo": "feed_nao_validado", "texto": f"não consegui validar o feed ({type(e).__name__}); "
                 "abra o arquivo e confira", "onde": ""}]
    return []


# Fontes que o sistema substitui por outra de mesmas métricas: não vale avisar.
EQUIVALENTES = {"arial": "liberation sans", "helvetica": "liberation sans", "times new roman": "liberation serif",
                "courier new": "liberation mono"}
GENERICAS = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "inherit", "initial"}


def fontes_ausentes(svg: str) -> list[dict]:
    """Avisa quando a primeira fonte pedida não existe no sistema (o renderizador usa outra)."""
    fc = shutil.which("fc-match")
    if not fc:
        return []
    vistas: set[str] = set()
    avisos = []
    for m in re.finditer(r"font-family\s*[=:]\s*[\"']?([^;\"'>]+(?:'[^']*')?[^;\"'>]*)", svg, re.I):
        primeira = m.group(1).split(",")[0].strip().strip("\"'")
        if not primeira or primeira.lower() in GENERICAS or primeira in vistas:
            continue
        vistas.add(primeira)
        try:
            r = subprocess.run([fc, "-f", "%{family}", primeira], capture_output=True, text=True, timeout=10)
        except (subprocess.TimeoutExpired, OSError):
            continue
        achada = r.stdout.strip()
        if achada and primeira.lower() not in achada.lower().split(",") \
                and EQUIVALENTES.get(primeira.lower()) != achada.lower().split(",")[0]:
            avisos.append({"tipo": "fonte_ausente", "texto": f"a fonte pedida \"{primeira}\" não existe neste "
                           f"renderizador (cai em \"{achada.split(',')[0]}\"): larguras e peso são aproximados; "
                           "o texto pode ficar mais largo ou mais fino no arquivo final", "onde": ""})
    return avisos


def render_python_playwright(svg: str, png: str | None, feed: str | None):
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception:
        return None, "python playwright não instalado"
    ultimo = ""
    try:
        with sync_playwright() as p:
            b = None
            tentativas: list[str | None] = [None] + _achar_chromium()[:3]
            for exe in tentativas:
                try:
                    b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
                    break
                except Exception as e:
                    ultimo = str(e).splitlines()[0][:110] if str(e) else type(e).__name__
            if b is None:
                return None, f"python playwright sem Chromium utilizável ({ultimo})"
            try:
                pg = b.new_page(viewport={"width": LARGURA, "height": ALTURA})
                pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("data:", "about:")) else r.abort())
                pg.set_content('<!doctype html><html><body style="margin:0;background:#fff">' + svg + "</body></html>")
                res = pg.evaluate(JS_ANALISE, {})
                if png:
                    pg.screenshot(path=png, clip={"x": 0, "y": 0, "width": LARGURA, "height": ALTURA})
                if feed:
                    # página nova, com o SVG reescrito em 320x180: sem corrida de layout nem recorte
                    pf = b.new_page(viewport={"width": FEED_L, "height": FEED_A})
                    pf.route("**/*", lambda r: r.continue_() if r.request.url.startswith(("data:", "about:")) else r.abort())
                    pf.set_content('<!doctype html><html><body style="margin:0;background:#fff">' + svg_para_feed(svg) + "</body></html>")
                    pf.screenshot(path=feed, clip={"x": 0, "y": 0, "width": FEED_L, "height": FEED_A})
                return res, "playwright (Python) + Chromium"
            finally:
                b.close()
    except Exception as e:  # sandbox, falha no meio da análise etc.
        return None, f"python playwright falhou: {str(e).splitlines()[0][:120] if str(e) else type(e).__name__}"


def render_node_playwright(svg: str, png: str | None, feed: str | None):
    node = shutil.which("node")
    if not node:
        return None, "node não encontrado"
    with tempfile.TemporaryDirectory(prefix="chk_thumb_") as d:
        svg_path = os.path.join(d, "t.svg")
        job_path = os.path.join(d, "job.json")
        Path(svg_path).write_text(svg, encoding="utf-8")
        feed_svg_path = os.path.join(d, "f.svg")
        Path(feed_svg_path).write_text(svg_para_feed(svg), encoding="utf-8")
        Path(job_path).write_text(json.dumps({"svg": svg_path, "feedSvg": feed_svg_path, "png": png, "feed": feed}), encoding="utf-8")
        script = JS_NODE % {"analise": JS_ANALISE}
        try:
            r = subprocess.run([node, "-e", script, job_path], capture_output=True, text=True, timeout=120, cwd=d)
        except (subprocess.TimeoutExpired, OSError) as e:
            return None, f"node playwright falhou: {type(e).__name__}"
        if r.returncode != 0:
            msg = (r.stderr or "").strip().splitlines()
            return None, "node playwright indisponível: " + (msg[0][:140] if msg else f"código {r.returncode}")
        m = re.search(r"RESULTADO_JSON:(.*)", r.stdout)
        if not m:
            return None, "node playwright sem resultado"
        return json.loads(m.group(1)), "playwright (node) + Chromium"


def render_cairosvg(svg: str, png: str | None, feed: str | None, estatico: dict):
    """Com cairosvg: PNG real e amostragem do fundo (sem texto); caixas de texto estimadas."""
    try:
        import cairosvg  # type: ignore
    except Exception:
        return None, "cairosvg não instalado"
    try:
        if png:
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=png, output_width=LARGURA, output_height=ALTURA)
        if feed:
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=feed, output_width=FEED_L, output_height=FEED_A)
        # fundo sem texto, em meia resolução (decodificação em Python puro é lenta)
        raiz = ET.fromstring(svg)
        for pai in list(raiz.iter()):
            for filho in list(pai):
                if _local(filho.tag) == "text":
                    pai.remove(filho)
        ET.register_namespace("", "http://www.w3.org/2000/svg")
        sem_texto = ET.tostring(raiz, encoding="unicode")
        dados = cairosvg.svg2png(bytestring=sem_texto.encode("utf-8"), output_width=LARGURA // 2, output_height=ALTURA // 2)
        w, h, canais, px = ler_png(dados)
        return {"png_fundo": (w, h, canais, px)}, "cairosvg (fundo renderizado; caixas de texto estimadas)"
    except Exception as e:
        return None, f"cairosvg falhou: {str(e).splitlines()[0][:120] if str(e) else type(e).__name__}"


def contraste_por_pixels(t: dict, fundo) -> dict | None:
    """Contraste entre a cor de preenchimento do texto e os pixels do fundo dentro da caixa (cairosvg)."""
    w, h, canais, px = fundo
    cor = parse_cor(t.get("fill"))
    if not cor:
        return None
    c = t["caixa"]
    x0, x1 = max(0, int(c[0] / 2)), min(w - 1, int(c[2] / 2))
    y0, y1 = max(0, int(c[1] / 2)), min(h - 1, int(c[3] / 2))
    if x1 <= x0 or y1 <= y0:
        return None
    lt = lum_srgb(*cor)
    razoes = []
    for y in range(y0, y1 + 1):
        base = y * w * canais
        for x in range(x0, x1 + 1):
            i = base + x * canais
            if canais >= 3:
                r, g, b = px[i], px[i + 1], px[i + 2]
            else:
                r = g = b = px[i]
            razoes.append(razao(lt, lum_srgb(r, g, b)))
    if not razoes:
        return None
    razoes.sort()
    return {"mediano": razoes[len(razoes) // 2], "pior": razoes[int(len(razoes) * 0.1)],
            "fracBaixo": sum(1 for r in razoes if r < CONTRASTE_MIN) / len(razoes)}


# ---------------------------------------------------------------------------
# Avaliação
# ---------------------------------------------------------------------------

def avaliar_renderizado(res: dict) -> tuple[list[dict], list[dict]]:
    problemas: list[dict] = []
    avisos: list[dict] = []
    todos = res["textos"]
    ts = [t for t in todos if (t.get("opacidade") or 1.0) >= OPACIDADE_DECORATIVO]
    for t in todos:
        t["decorativo"] = t not in ts

    def P(tipo, texto, onde, **extra):
        problemas.append({"tipo": tipo, "texto": texto, "onde": onde, **extra})

    def A(tipo, texto, onde="", **extra):
        avisos.append({"tipo": tipo, "texto": texto, "onde": onde, **extra})

    for t in todos:
        if t["decorativo"]:
            A("texto_decorativo", f"{rotulo(t)} tem opacidade {t['opacidade']:.2f}; tratado como marca-d'água e fora das "
              "checagens de contraste, tamanho e área segura", f"{lugar(t['caixa'])}")
    fonte_max = max((t["fontPx"] for t in ts), default=0)
    for t in ts:
        nome = rotulo(t)
        caixa = t["caixa"]
        onde = f"{nome} ({lugar(caixa)}; {cx(caixa)})"
        f, s = t["fora"], t["seguro"]
        t["principal"] = t["fontPx"] >= 0.6 * fonte_max
        # cortado pela borda
        lados = []
        for lado, nome_lado in (("esq", "esquerda"), ("dir", "direita"), ("topo", "superior"), ("base", "inferior")):
            if f[lado] > TOLERANCIA_BORDA_PX:
                lados.append(f"borda {nome_lado}: {f[lado]:.0f} px fora (letras \"{letras_curtas(f['letras'][lado])}\")")
        if lados:
            P("texto_cortado", "texto passa da borda da imagem e é cortado: " + "; ".join(lados), onde)
        else:
            seg = []
            leve = True
            for lado, nome_lado in (("esq", "esquerda"), ("dir", "direita"), ("topo", "superior"), ("base", "inferior")):
                if s[lado] > TOLERANCIA_SEGURA_PX:
                    seg.append(f"{s[lado]:.0f} px dentro da margem {nome_lado} (letras \"{letras_curtas(s['letras'][lado])}\")")
                    if s[lado] > TOLERANCIA_SEGURA_LEVE_PX:
                        leve = False
            if seg:
                texto = (f"texto invade a margem de {int(MARGEM_SEGURA * 100)}% ({LARGURA * MARGEM_SEGURA:.0f} px nas laterais, "
                         f"{ALTURA * MARGEM_SEGURA:.0f} px em cima e embaixo): " + "; ".join(seg))
                if leve:
                    A("margem_apertada", texto + f" (até {TOLERANCIA_SEGURA_LEVE_PX} px: só aviso)", onde)
                else:
                    P("fora_da_area_segura", texto, onde)
        # tamanho no feed
        feed_px = t["fontPxMin"] * FEED_L / LARGURA
        t["_feed_px"] = feed_px
        if t["inkPx"] == 0:
            P("texto_invisivel", "nenhum pixel de tinta: texto sem cor visível (cor igual ao fundo ou fora da imagem)", onde)
        elif feed_px < LETRA_MIN_FEED_PX:
            texto = (f"letra de {t['fontPxMin']:.0f} px vira {feed_px:.1f} px no feed 320x180 "
                     f"(mínimo {LETRA_MIN_FEED_PX} px, ou {LETRA_MIN_FEED_PX * LARGURA / FEED_L:.0f} px em 1280)")
            if t["principal"] or feed_px < LETRA_APOIO_MIN_FEED_PX:
                P("letra_pequena_no_feed", texto + ("" if t["principal"] else f"; mesmo como apoio, abaixo de {LETRA_APOIO_MIN_FEED_PX} px"), onde)
            else:
                A("apoio_pequeno_no_feed", texto + " (texto de apoio: só aviso; a ficha pede 40 px ou mais)", onde)
        elif t["feed"].get("sumiu"):
            P("texto_some_no_feed", "o traço some no feed 320x180 (menos de 1 pixel de núcleo)", onde)
        # contraste
        c = t["contraste"]
        compensado = bool(t["contorno"] and (t.get("razaoFillStroke") is None or t["razaoFillStroke"] >= CONTRASTE_MIN))
        if t["inkPx"] and c["mediano"] is not None:
            t["_contraste"] = max(c["mediano"], t["razaoFillStroke"] or 0) if compensado else c["mediano"]
            nota = f" (contorno compensa: texto/contorno {fmt(t['razaoFillStroke'])}:1)" if compensado and t.get("razaoFillStroke") else ""
            if compensado:
                pass
            elif c["mediano"] < CONTRASTE_MIN:
                P("contraste_baixo", f"contraste {fmt(c['mediano'])}:1 entre texto {c['corTexto']} e fundo {c['corFundo']} "
                  f"(mínimo {fmt(CONTRASTE_MIN, 0)}:1)", onde, sob=[x["forma"] for x in t["sob"]])
            elif (c["pxBaixo2"] or 0) >= PX_BAIXO_MIN:
                P("parte_do_texto_some", f"{c['pxBaixo2']} px de letra ({c['pxBaixo2'] / max(1, c['nucleo']) * 100:.0f}%) ficam sobre "
                  f"fundo com contraste < 2:1 (pior região {fmt(c['pior'])}:1; mediana {fmt(c['mediano'])}:1); formas atrás: "
                  + (", ".join(x["forma"] for x in t["sob"]) or "gradiente do fundo")
                  + "; texto escuro sobre fundo escuro ou claro sobre claro nessa parte", onde)
        # coberto por forma por cima
        if t["inkPx"] and t["ocultoPx"] >= OCULTO_MIN_PX:
            P("coberto_por_forma", f"{t['ocultoPx']} px das letras ({t['ocultoFrac'] * 100:.0f}%) ficam atrás de outra forma "
              f"(desenhada depois do texto): " + (", ".join(x["forma"] for x in t["acima"]) or "forma não identificada"), onde)
        for col in t["colisoes"]:
            P("linhas_coladas", f"as linhas \"{col['a']}\" e \"{col['b']}\" se tocam ({col['pares']} pares de letras, "
              f"ex.: {', '.join(col['letras'])}); aumente a entrelinha", onde)
    for par in res["pares"]:
        a, b = todos[par["a"]], todos[par["b"]]
        if a["decorativo"] or b["decorativo"]:
            continue
        if par["px"] >= SOBREPOSICAO_MIN_PX:
            P("textos_sobrepostos", f"{rotulo(a)} e {rotulo(b)} se sobrepõem ({par['px']} px de tinta em comum)",
              f"{cx(par['caixa'])} ({lugar(par['caixa'])})")
        elif par["perto"] >= ENCOSTADOS_MIN_PX:
            A("textos_encostados", f"{rotulo(a)} e {rotulo(b)} ficam a menos de 8 px um do outro ({par['perto']} px de "
              "letra); abra mais a entrelinha", f"{cx(par['caixa'])} ({lugar(par['caixa'])})")
    # avisos
    total = sum(t["palavras"] for t in ts)
    if total > PALAVRAS_AVISO:
        A("muito_texto", f"{total} palavras no texto da thumbnail (aviso acima de {PALAVRAS_AVISO}; a mediana de breakouts é 5). "
          "Não bloqueia: o que perdeu nos testes foi texto cortado, sobreposto ou ilegível.")
    if ts:
        principal = max(ts, key=lambda t: t["fontPx"])
        if principal["fontPx"] < LETRA_PRINCIPAL_MIN_PX:
            A("frase_principal_pequena", f"a maior letra tem {principal['fontPx']:.0f} px; a ficha pede pelo menos "
              f"{LETRA_PRINCIPAL_MIN_PX} px (1/9 da altura) para a frase principal", f"{rotulo(principal)}")
    com_problema = {p["onde"].split(" (")[0] for p in problemas}
    for t in ts:
        c = t["caixa"]
        if c[2] > LARGURA - SELO_DIRETA_PX and c[3] > ALTURA - SELO_BAIXO_PX:
            A("selo_de_duracao", "texto no canto inferior direito, onde o selo de duração do YouTube cobre a imagem",
              f"{rotulo(t)} ({cx(c)})")
        if rotulo(t) in com_problema:
            continue
        for sob in t["sob"]:
            parte = sob["amostras"] / max(1, sob["de"])
            if LIMITE_FORMA_MIN <= parte <= LIMITE_FORMA_MAX:
                A("texto_cruza_forma", f"texto cruza o contorno de <{sob['forma']}> ({parte * 100:.0f}% das amostras sobre ela; "
                  "contraste ok, mas confirme que não cobre o objeto principal)", rotulo(t))
                break
    if res.get("truncado"):
        A("muitos_textos", "mais de 40 elementos <text>: só os 40 primeiros foram medidos")
    vb = res.get("viewBox")
    try:
        if vb and [float(x) for x in re.split(r"[ ,]+", vb.strip())] != [0, 0, 1280, 720]:
            A("viewbox", f"viewBox \"{vb}\" não é \"0 0 1280 720\"; as medidas usam a imagem renderizada em 1280x720")
    except ValueError:
        pass
    return problemas, avisos


def avaliar_estatico(info: dict, fundo_cairo=None) -> tuple[list[dict], list[dict], list[dict]]:
    """Checagem sem DOM: caixas ESTIMADAS a partir de font-size, x/y, text-anchor e largura média por caractere.
    Conservadora: só acusa o que as cores declaradas ou o fundo renderizado sustentam."""
    problemas: list[dict] = []
    avisos: list[dict] = []
    ts = info["textos"]

    def P(tipo, texto, onde, **extra):
        problemas.append({"tipo": tipo, "texto": texto, "onde": onde, **extra})

    def A(tipo, texto, onde="", **extra):
        avisos.append({"tipo": tipo, "texto": texto, "onde": onde, **extra})

    def opac(t):
        return t.get("opacidade", 1.0)

    fonte_max = max((t["fontPx"] for t in ts), default=0)
    mx, my = LARGURA * MARGEM_SEGURA, ALTURA * MARGEM_SEGURA
    for t in ts:
        c = t["caixa"]
        nome = rotulo(t)
        onde = f"{nome} ({lugar(c)}; {cx(c)}, estimado)"
        t["principal"] = t["fontPx"] >= 0.6 * fonte_max
        if t["rot"]:
            A("rotacionado", "texto rotacionado: caixa aproximada", nome)
        sai = []
        if c[0] < -TOLERANCIA_BORDA_PX:
            sai.append(f"esquerda {-c[0]:.0f} px")
        if c[2] > LARGURA + TOLERANCIA_BORDA_PX:
            sai.append(f"direita {c[2] - LARGURA:.0f} px")
        if c[1] < -TOLERANCIA_BORDA_PX:
            sai.append(f"topo {-c[1]:.0f} px")
        if c[3] > ALTURA + TOLERANCIA_BORDA_PX:
            sai.append(f"base {c[3] - ALTURA:.0f} px")
        if sai:
            P("texto_cortado", "texto estimado passa da borda e seria cortado: " + "; ".join(sai), onde)
        else:
            dentro = []
            piores = 0.0
            for rotulo_lado, valor in (("esquerda", mx - c[0]), ("direita", c[2] - (LARGURA - mx)),
                                       ("topo", my - c[1]), ("base", c[3] - (ALTURA - my))):
                if valor > TOLERANCIA_SEGURA_PX:
                    dentro.append(f"{rotulo_lado} {valor:.0f} px")
                    piores = max(piores, valor)
            if dentro:
                texto = "texto estimado invade a margem de 5%: " + "; ".join(dentro)
                if piores <= TOLERANCIA_SEGURA_LEVE_PX:
                    A("margem_apertada", texto + f" (até {TOLERANCIA_SEGURA_LEVE_PX:.0f} px: só aviso)", onde)
                else:
                    P("fora_da_area_segura", texto, onde)
        feed_px = t["fontPxMin"] * FEED_L / LARGURA
        if feed_px < LETRA_MIN_FEED_PX:
            texto = f"letra de {t['fontPxMin']:.0f} px vira {feed_px:.1f} px no feed 320x180 (mínimo {LETRA_MIN_FEED_PX} px)"
            if t["principal"] or feed_px < LETRA_APOIO_MIN_FEED_PX:
                P("letra_pequena_no_feed", texto, onde)
            else:
                A("apoio_pequeno_no_feed", texto + " (texto de apoio: só aviso)", onde)
        # contraste, só quando há base: pixels do fundo (cairosvg) ou fundo declarado sem ambiguidade
        contorno = t.get("stroke") not in (None, "none") and t.get("stroke_width", 0) >= 2
        cor_t = parse_cor(t.get("fill")) if not str(t.get("fill", "")).startswith("url(") else _cor_de_fill(t["fill"], info["gradientes"])
        if contorno or cor_t is None or opac(t) < OPACIDADE_DECORATIVO:
            continue
        lt = lum_srgb(*cor_t)
        if fundo_cairo:
            ct = contraste_por_pixels(t, fundo_cairo)
            if ct:
                t["_contraste"] = ct["mediano"]
                if ct["mediano"] < CONTRASTE_MIN:
                    P("contraste_baixo", f"contraste {fmt(ct['mediano'])}:1 entre o texto e os pixels do fundo sob a caixa "
                      f"(fundo renderizado sem texto; mínimo {fmt(CONTRASTE_MIN, 0)}:1)", onde)
                elif ct["fracBaixo"] >= 0.35 and ct["pior"] < 2.0:
                    A("contraste_parcial", f"{ct['fracBaixo'] * 100:.0f}% da caixa tem fundo com contraste < 3:1 "
                      f"(pior {fmt(ct['pior'])}:1); pode haver letra sobre região de cor parecida", onde)
        else:
            fundos = fundo_estatico(t, info)
            medidas = []
            for opcoes in fundos:
                if opcoes:
                    medidas.append(max(razao(lt, lum_srgb(*f)) for f in opcoes))  # melhor caso do ponto
            if len(medidas) >= 3:
                medidas.sort()
                t["_contraste"] = medidas[len(medidas) // 2]
                if medidas[len(medidas) // 2] < CONTRASTE_MIN:
                    P("contraste_baixo", f"contraste estimado {fmt(medidas[len(medidas) // 2])}:1 (cor do texto contra as formas "
                      f"declaradas atrás; mínimo {fmt(CONTRASTE_MIN, 0)}:1)", onde)
                elif medidas[0] < 2.0:
                    A("contraste_parcial", f"parte da caixa tem contraste estimado {fmt(medidas[0])}:1 contra as formas atrás", onde)
    for i in range(len(ts)):
        for j in range(i + 1, len(ts)):
            a, b = ts[i], ts[j]
            if opac(a) < OPACIDADE_DECORATIVO or opac(b) < OPACIDADE_DECORATIVO:
                continue
            achou = False
            for ca in a["linhas_caixas"] or [a["caixa"]]:
                for cb in b["linhas_caixas"] or [b["caixa"]]:
                    iw = min(ca[2], cb[2]) - max(ca[0], cb[0])
                    ih = min(ca[3], cb[3]) - max(ca[1], cb[1])
                    if iw > 3 and ih > 3:
                        P("textos_sobrepostos", f"{rotulo(a)} e {rotulo(b)}: caixas estimadas se sobrepõem em "
                          f"{iw:.0f}x{ih:.0f} px", f"{lugar([ca[0], ca[1], ca[2], ca[3]])}")
                        achou = True
                        break
                if achou:
                    break
    # forma desenhada depois do texto e sobre ele: só aviso (sem pixels não dá para medir)
    for t in ts:
        for f in info["formas"]:
            b = f["caixa"]
            area_f = max(0, b[2] - b[0]) * max(0, b[3] - b[1])
            if area_f >= 0.6 * LARGURA * ALTURA or f["opacidade"] < 0.2 or f["fill"] == "none":
                continue
            c = t["caixa"]
            iw, ih = min(c[2], b[2]) - max(c[0], b[0]), min(c[3], b[3]) - max(c[1], b[1])
            area_t = max(1, (c[2] - c[0]) * (c[3] - c[1]))
            if iw > 0 and ih > 0 and iw * ih >= 0.15 * area_t and f["ordem"] > t["ordem"] and f["tag"] != "line":
                A("forma_sobre_texto", f"<{f['tag']}> desenhado depois do texto cobre {iw * ih / area_t * 100:.0f}% da caixa estimada",
                  rotulo(t))
                break
    total = sum(t["palavras"] for t in ts if opac(t) >= OPACIDADE_DECORATIVO)
    if total > PALAVRAS_AVISO:
        A("muito_texto", f"{total} palavras no texto da thumbnail (aviso acima de {PALAVRAS_AVISO}).")
    if ts:
        principal = max(ts, key=lambda t: t["fontPx"])
        if principal["fontPx"] < LETRA_PRINCIPAL_MIN_PX:
            A("frase_principal_pequena", f"a maior letra tem {principal['fontPx']:.0f} px; a ficha pede pelo menos "
              f"{LETRA_PRINCIPAL_MIN_PX} px", rotulo(principal))
    for t in ts:
        c = t["caixa"]
        if c[2] > LARGURA - SELO_DIRETA_PX and c[3] > ALTURA - SELO_BAIXO_PX:
            A("selo_de_duracao", "texto no canto inferior direito (selo de duração)", f"{rotulo(t)}")
    vb = info.get("viewBox")
    if vb != "0 0 1280 720":
        A("viewbox", f"viewBox {vb!r}: esperado '0 0 1280 720'")
    return problemas, avisos, ts


# ---------------------------------------------------------------------------
# Relatório
# ---------------------------------------------------------------------------

def comparar_titulo(titulo: str | None, textos: list[dict]) -> dict | None:
    if not titulo:
        return None
    t_thumb = " ".join(t["texto"] for t in textos)
    pt, pm = palavras_conteudo(titulo), palavras_conteudo(t_thumb)
    rep = sorted(pt & pm)
    return {"titulo": titulo, "repetidas": rep, "palavras_titulo": len(palavras_de(titulo))}


def montar(svg_path: str, titulo: str | None, png: str | None, usar: str | None) -> tuple[dict, int]:
    bruto = Path(svg_path).read_text(encoding="utf-8", errors="replace")
    svg, avisos_limpeza = limpar_svg(bruto)
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        return {"arquivo": svg_path, "resultado": "FALHOU", "erro": f"SVG inválido: {e}",
                "problemas": [{"tipo": "svg_invalido", "texto": f"SVG não é XML válido: {e}", "onde": ""}],
                "avisos": [], "renderizador": "nenhum (SVG não pôde ser lido)", "parcial": False, "textos": [],
                "palavras_texto": 0, "titulo": None, "tentativas_sem_sucesso": []}, 1

    feed = None
    if png:
        base, ext = os.path.splitext(png)
        feed = f"{base}_feed{ext or '.png'}"
        Path(png).parent.mkdir(parents=True, exist_ok=True)

    estatico = analisar_estatico(svg)
    res = None
    como = None
    tentativas: list[str] = []
    ordem = [usar] if usar else ["playwright-python", "playwright-node", "cairosvg"]
    for r in ordem:
        if r == "playwright-python":
            res, como = render_python_playwright(svg, png, feed)
        elif r == "playwright-node":
            res, como = render_node_playwright(svg, png, feed)
        elif r == "cairosvg":
            res, como = render_cairosvg(svg, png, feed, estatico)
        if res is not None:
            break
        tentativas.append(como)
    out: dict = {"arquivo": svg_path, "svg_viewbox": estatico.get("viewBox"), "tentativas_sem_sucesso": tentativas}
    if res is not None and "erro" in res:
        tentativas.append(res["erro"])
        res = None
    if res is not None and "textos" in res:
        out["renderizador"] = como
        out["parcial"] = False
        problemas, avisos = avaliar_renderizado(res)
        out["textos"] = res["textos"]
        out["sobreposicoes"] = res["pares"]
        out["palavras_texto"] = sum(t["palavras"] for t in res["textos"] if not t.get("decorativo"))
        textos_cmp = [t for t in res["textos"] if not t.get("decorativo")]
        if png:
            out["png"] = png
            out["png_feed"] = feed
    else:
        fundo = res["png_fundo"] if res and "png_fundo" in res else None
        problemas, avisos, ts = avaliar_estatico(estatico, fundo)
        out["renderizador"] = como if fundo else "nenhum (checagem estática do SVG)"
        out["parcial"] = True
        out["textos"] = [{k: v for k, v in t.items() if k != "linhas_caixas"} for t in ts]
        out["palavras_texto"] = sum(t["palavras"] for t in ts)
        textos_cmp = ts
        if png and fundo:
            out["png"], out["png_feed"] = png, feed
        elif png:
            avisos.append({"tipo": "sem_png", "texto": "sem renderizador: o PNG não foi gerado", "onde": ""})
    for a in avisos_limpeza:
        avisos.append({"tipo": "svg", "texto": a, "onde": ""})
    if png and feed and out.get("png_feed") and os.path.exists(png) and os.path.exists(feed):
        avisos.extend(validar_feed(png, feed))
    if not out["parcial"]:
        avisos.extend(fontes_ausentes(svg))
    if not out["textos"]:
        avisos.append({"tipo": "sem_texto", "texto": "nenhum <text> visível encontrado (texto convertido em caminho "
                       "não é medido; as palavras contam 0)", "onde": ""})
    cmp_t = comparar_titulo(titulo, textos_cmp)
    out["titulo"] = cmp_t
    if cmp_t and cmp_t["repetidas"]:
        avisos.append({"tipo": "palavras_repetidas", "texto": "palavras de conteúdo repetidas entre título e thumbnail: "
                       + ", ".join(cmp_t["repetidas"]) + ". Se foi decisão (frase citada do caso), anote no pacote; "
                       "senão troque na thumbnail.", "onde": ""})
    out["problemas"] = problemas
    out["avisos"] = avisos
    out["resultado"] = "FALHOU" if problemas else "PASSOU"
    return out, (1 if problemas else 0)


def relatorio(o: dict) -> str:
    L = [f"CHECAGEM DE THUMBNAIL: {o['arquivo']}"]
    L.append(f"Renderizador: {o['renderizador']}")
    if o.get("parcial"):
        L.append("ATENÇÃO: CHECAGEM PARCIAL. Sem renderizador completo, as caixas de texto são ESTIMADAS "
                 "(font-size, x/y, text-anchor e largura média por caractere) e o contraste vem das cores declaradas ou "
                 "do fundo renderizado. Não mede sobreposição real com figuras, nem corte por fonte diferente. "
                 "Para medir de verdade: instale `playwright` (pip) com Chromium, ou o pacote node `playwright`.")
        for t in o.get("tentativas_sem_sucesso", []):
            L.append(f"  (tentativa: {t})")
    elif o.get("tentativas_sem_sucesso"):
        for t in o["tentativas_sem_sucesso"]:
            L.append(f"  (tentado antes, sem sucesso: {t}; o renderizador acima funcionou e a checagem é completa)")
    L.append("")
    L.append(f"Texto na thumbnail: {o.get('palavras_texto', 0)} palavras em {len(o.get('textos', []))} bloco(s)")
    for i, t in enumerate(o.get("textos", []), 1):
        caixa = t["caixa"]
        extra = []
        fpx = t.get("fontPxMin") or t.get("fontPx") or 0
        extra.append(f"letra {fpx:.0f} px (feed {fpx * FEED_L / LARGURA:.1f} px)")
        c = t.get("_contraste")
        if c is None and t.get("contraste", {}).get("mediano") is not None:
            c = t["contraste"]["mediano"]
        if c is not None:
            extra.append(f"contraste {fmt(c)}:1")
        L.append(f"  {i}. {rotulo(t, 40)}  {cx(caixa)}  | " + ", ".join(extra))
    if o.get("titulo"):
        rep = o["titulo"]["repetidas"]
        L.append(f"Título: \"{o['titulo']['titulo']}\" ({o['titulo']['palavras_titulo']} palavras)")
        L.append("  palavras repetidas entre título e thumbnail: " + (", ".join(rep) if rep else "nenhuma"))
    if o.get("png"):
        L.append(f"PNG salvo: {o['png']} (feed 320x180: {o['png_feed']})")
    L.append("")
    if o["problemas"]:
        L.append(f"PROBLEMAS ({len(o['problemas'])}):")
        for i, p in enumerate(o["problemas"], 1):
            L.append(f"  {i}. [{p['tipo']}] {p['texto']}")
            if p.get("onde"):
                L.append(f"       onde: {p['onde']}")
    else:
        L.append("PROBLEMAS: nenhum")
    if o["avisos"]:
        L.append(f"AVISOS ({len(o['avisos'])}; não bloqueiam):")
        for p in o["avisos"]:
            suf = f" ({p['onde']})" if p.get("onde") else ""
            L.append(f"  - [{p['tipo']}] {p['texto']}{suf}")
    L.append("")
    sufixo = " (checagem parcial)" if o.get("parcial") else ""
    L.append(f"RESULTADO: {o['resultado']}{sufixo}")
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Checa uma thumbnail SVG 1280x720: texto cortado, sobreposto, contraste, tamanho no feed.")
    ap.add_argument("svg", help="arquivo SVG da thumbnail")
    ap.add_argument("--titulo", help="título do vídeo, para achar palavras repetidas")
    ap.add_argument("--png", help="salva o PNG renderizado (e SAIDA_feed.png em 320x180) quando houver renderizador")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    ap.add_argument("--renderizador", choices=("playwright-python", "playwright-node", "cairosvg", "nenhum"),
                    help="força um renderizador (padrão: tenta em ordem)")
    args = ap.parse_args(argv)
    if not Path(args.svg).is_file():
        print(f"erro: arquivo não encontrado: {args.svg}", file=sys.stderr)
        return 2
    usar = None if not args.renderizador else args.renderizador
    try:
        if usar == "nenhum":
            # força estática
            bruto = Path(args.svg).read_text(encoding="utf-8", errors="replace")
            svg, av = limpar_svg(bruto)
            ET.fromstring(svg)
            info = analisar_estatico(svg)
            problemas, avisos, ts = avaliar_estatico(info)
            for a in av:
                avisos.append({"tipo": "svg", "texto": a, "onde": ""})
            cmp_t = comparar_titulo(args.titulo, ts)
            if cmp_t and cmp_t["repetidas"]:
                avisos.append({"tipo": "palavras_repetidas", "texto": "palavras de conteúdo repetidas entre título e thumbnail: "
                               + ", ".join(cmp_t["repetidas"]), "onde": ""})
            o = {"arquivo": args.svg, "renderizador": "nenhum (checagem estática do SVG)", "parcial": True,
                 "textos": [{k: v for k, v in t.items() if k != "linhas_caixas"} for t in ts],
                 "palavras_texto": sum(t["palavras"] for t in ts), "titulo": cmp_t, "problemas": problemas,
                 "avisos": avisos, "tentativas_sem_sucesso": [], "resultado": "FALHOU" if problemas else "PASSOU"}
            codigo = 1 if problemas else 0
        else:
            o, codigo = montar(args.svg, args.titulo, args.png, usar)
    except (ET.ParseError, OSError) as e:
        print(f"erro: SVG ilegível: {e}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(o, ensure_ascii=False, indent=2, default=str))
    else:
        print(relatorio(o))
    return codigo


if __name__ == "__main__":
    sys.exit(main())
