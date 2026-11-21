#!/usr/bin/env python3
"""Gera references/INDEX.md: os títulos de cada documento com o número da linha, para que
um agente leia só a seção de que precisa (os documentos têm de 40 a 160 mil caracteres)."""
import re
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references"
out = ["# Índice das referências",
       "",
       "Cada linha: `linha  título`. Leia a seção com Read(offset=linha, limit=até o próximo título).",
       "Não leia um documento inteiro: procure aqui a seção e leia só ela.", ""]
for path in sorted(REF.glob("[0-9]*.md")):
    lines = path.read_text().splitlines()
    out.append(f"## {path.name}  ({len(lines)} linhas)")
    hooks = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,3}) (.+)$", line)
        if not m:
            continue
        level, title = len(m.group(1)), m.group(2).strip()
        code = re.match(r"^(H-\d+)\s*[-–—]\s*(.+)$", title)
        if code:  # estruturas de hook: uma linha compacta por estrutura
            hooks.append(f"{i:>5}  {code.group(1)} {code.group(2)}")
            continue
        if level <= 2 or (level == 3 and re.match(r"^\d+\.\d+ ", title)):
            if hooks:
                out += hooks
                hooks = []
            out.append(f"{i:>5}  {'  ' * (level - 1)}{title}")
    out += hooks
    out.append("")
(REF / "INDEX.md").write_text("\n".join(out) + "\n")
print(f"INDEX.md: {len(out)} linhas")
