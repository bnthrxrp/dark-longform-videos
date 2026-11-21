---
name: producing-dark-longform-videos
description: Use when the user asks to create, review or diagnose a long-form (10+ min) video for a dark or faceless narrated YouTube channel: roteiro/script, hook/abertura, título/title, thumbnail/miniatura, ideia/pauta, narração/voiceover, auditoria antes de publicar, ou leitura de Analytics de vídeo longo (retenção, CTR, curva). Not for Shorts.
license: MIT
---

# Produzindo vídeos dark long-form

Base em `references/`: ache a seção em `references/INDEX.md` e leia só ela. `00_kit_de_bolso.md` traz doses, aberturas reais, checklist de thumbnail e pontes. Fora a regra oficial, nada tem efeito medido sobre retenção.

## Princípio

Duas metades; nenhuma substitui a outra.

1. **Motivo para clicar e para continuar.** O espectador não conhece o caso. Clica por uma cena concreta ou uma anomalia de uma frase. Fica por uma pergunta central paga aos poucos, com os fatos mais estranhos cedo (guarde a explicação) e frases que soam como fala. Primeira frase que serviria a qualquer vídeo do tema: refaça.
2. **Disciplina de fato e promessa.** Só se afirma o que tem fonte. Só se promete o que o vídeo paga.

## Fluxo

| Etapa | Briefing | Entrega |
|---|---|---|
| 1. Ideia | `agents/ideia.md` | pergunta-mestra, tabela de fatos |
| 2. Pacote | `agents/pacote.md` | título, thumbnail, promessas |
| 3. Hook | `agents/hook.md` | 80 a 95 s (180 a 215 palavras a 135/min) |
| 4. Roteiro | `agents/roteiro.md` | sinopse, mapa de blocos |
| 5. Narração | `agents/narracao.md` | texto narrado completo |
| 6. Auditoria | `agents/auditor.md` | publicar ou corrigir |
| 7. Pós-publicação | `agents/analytics.md` | leitura da curva, um experimento |

Leia o briefing antes da etapa; o critério de saída fica no fim. O projeto vive no dossiê (`dossie-modelo.md`, `## 0` a `## 9`). Vídeo publicado não ganha dossiê: peça capítulos e curva.

Subagente só na auditoria, com o dossiê e sem a conversa. Sem subagente, passada separada, com "auditoria própria, não independente".

## Entrega

Primeiro o texto limpo, pronto para copiar e narrar, sem tabela, etiqueta, citação de referência nem comentário de processo. Só `[VERIFICAR]` pode ficar, e sai antes de narrar. Se algo muda o que foi pedido, abra com uma linha de aviso de escopo e a decisão do usuário. Não encurte a duração sozinho: marque os blocos sem fato "a pesquisar" (`agents/ideia.md`). Depois, a base compacta: fatos, promessas, medições. Auditoria: lista numerada por classe (Bloqueia, Corrige), uma linha por defeito, sem tabela.

**Modo enxuto** (pedido parcial ou com pressa): sem dossiê, mesmo critério. Formato fixo: aviso de escopo (se houver) no topo; o texto; depois, no máximo: medição (1 linha), pergunta-mestra (1), fatos usados por id (1), promessas e onde pagam (1 por promessa), pendências (1). Fora, salvo pedido: grafias, "o que não entra", abertura alternativa, códigos H-NN, títulos descartados. A pergunta-mestra passa no teste: um fato de uma linha não a responde. Da ficha do usuário valem `fatos`, `tema`, `anomalia` e `incertos` (só atribuído); `cuidados` restringe.

## Medir por código

Não conte de cabeça. Rode na pasta da skill:

- `python scripts/medir_texto.py hook.txt --tipo hook --fatos fatos.txt`: palavras, segundos (`--wpm 135`), frases sobre o vídeo, perguntas, fecho, números fora da ficha (um fato por linha). Blocos: `--tipo bloco`.
- `python scripts/checar_thumbnail.py thumb.svg --titulo "TÍTULO" --png thumb.png`: legibilidade do SVG 1280x720; grava `thumb_feed.png` (320x180). Abra os dois.
- Título: `python -c "print(len('TÍTULO'))"`.

Sem como rodar: "não medi".

## Regras

1. **Fato do caso só com fonte.** Sem pesquisa, entra como "a verificar" e a narração não o afirma. Memória não é fonte. Número do usuário sem fonte: procure na base; se não houver, diga e não construa sobre ele.
2. **Promessa sem bloco e minuto de pagamento** sai do título, da thumbnail e do hook.
3. **Dose** (minutos, frequências, percentuais) só com origem e etiqueta: `[OFICIAL]` `[ESTUDO]` `[DADO]` `[PRATICANTE]` `[INFERÊNCIA]` `[TESTE-IA]`. `[TESTE-IA]` = juízes de IA em teste cego, não audiência (`21` §1).
4. **Desfecho vizinho não é retenção.** Estudo de persuasão ou compartilhamento e regra de livro de roteiro são hipótese, nunca dose nem prova de permanência.
5. **Exemplos das referências** servem pela forma, não pelo conteúdo. Pedido "direto" não dispensa o briefing nem o registro de promessas.

Após editar `references/`, rode `python scripts/build_index.py`.
