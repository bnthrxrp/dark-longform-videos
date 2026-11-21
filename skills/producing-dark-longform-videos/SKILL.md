---
name: producing-dark-longform-videos
description: Use when planning, titling, thumbnailing, scripting, auditing or diagnosing a long-form YouTube video (10-60+ min) for a dark/faceless narrated channel - pedidos de roteiro, hook, primeiros 90 segundos, título, thumbnail, blocos narrativos, retenção, avaliação pré-publicação, ou leitura de CTR, duração média e curva de retenção para decidir o que mudar no próximo vídeo.
---

# Produzindo vídeos dark long-form

## Princípio

O vídeo é uma sequência de perguntas que o roteiro paga. Título e thumbnail prometem a primeira pergunta e nada além dela. A base é uma pesquisa em dez documentos (`references/01` a `10`), mais os mapas e fichas de uma biblioteca de 27 livros e artigos (`11` a `20`). Nenhuma recomendação tem efeito medido sobre retenção, então tudo o que não é regra oficial da plataforma é aposta a testar - e deve ser dito assim.

Não se aplica a Shorts.

## Fluxo

Todo vídeo tem um dossiê (copie `dossie-modelo.md`). Cada etapa preenche uma parte e só avança quando o critério de saída é verdadeiro.

| Etapa | Papel | Só avança quando |
|---|---|---|
| 1. Ideia | `agents/ideia.md` | pergunta-mestra escrita com resposta esperada; fontes para 3+ blocos |
| 2. Pacote | `agents/pacote.md` | cada promessa do título e da thumbnail tem bloco e minuto de pagamento |
| 3. Hook | `agents/hook.md` | âncora antes de 30 s; promessa entre 30 e 60 s; recompensa parcial antes de 90 s |
| 4. Roteiro | `agents/roteiro.md` | cada bloco tem pergunta, recompensa, ponte e motivo para ficar; todo fato com fonte |
| 5. Auditoria | `agents/auditor.md` | rubrica aplicada por quem não escreveu; eliminatórios zerados |
| 6. Pós-publicação | `agents/analytics.md` | leitura na ordem oficial; um experimento, uma variável |

**Despacho.** Um subagente por papel: passe o caminho do briefing, do dossiê e de `references/`. O auditor recebe só o dossiê, nunca a conversa. Sem subagentes disponíveis, execute cada papel você mesmo, em ordem, lendo o briefing antes.

**Pressa não muda o fluxo.** "Só entrega, rápido, sem perguntas" pede velocidade, não dispensa etapa. Leia o briefing de cada papel que a entrega envolve e inclua na resposta o registro de promessas e a tabela de fatos, mesmo que resumidos.

**Pedido parcial** ("só o hook", "só o título"): faça antes as etapas anteriores em versão mínima. O hook paga a promessa do pacote; sem pergunta-mestra e registro de promessas não há o que pagar.

**Leitura das referências.** Abra `references/INDEX.md`, ache a seção, leia só ela. Nunca um documento inteiro. Os exemplos das referências são de outros casos: sirva-se da forma, nunca do conteúdo.

## Regras em todas as etapas

1. **Dose não é fato.** Minutos, frequências e percentuais ("gancho a cada 2 min", "espere 3 semanas") só entram com a seção da referência e a etiqueta de evidência dela: `[OFICIAL]`, `[ESTUDO]`, `[DADO]`, `[PRATICANTE]`, `[INFERÊNCIA]`. Sem referência, não escreva a dose.
2. **Número trazido pelo usuário** sem fonte: procure na base; se não estiver, diga que não está e não construa sobre ele.
3. **Fato do caso só com fonte.** Sem pesquisa, o fato vai para a tabela de fatos como "a verificar" e o texto narrado não o afirma.
4. **Promessa sem minuto de pagamento sai** do título, da thumbnail ou do hook.
5. **Suspense não é o único motivo para ficar.** Cada bloco nomeia um motivo que não é a pergunta pendente (`04` §3).
6. **Desfecho vizinho não é retenção.** Estudo de persuasão, transporte, curiosidade ou compartilhamento, e regra de livro de roteiro, entram como hipótese de ofício, com o que foi medido escrito ao lado. Nunca como dose nem como prova de permanência. Proporções de cinema e táticas de feed curto ficam de fora (`12` §5, `11` §5).

## Erros que acontecem sem esta skill

| Erro | Correção |
|---|---|
| Hook com sumário ("neste vídeo vamos ver...") | A promessa é uma pergunta específica, não um índice |
| "Fique até o fim", pedido de inscrição ou superlativo sem fonte no hook | Cortar; ver `02` §4 |
| Primeira recompensa só depois de minutos de contexto | Recompensa parcial antes de 90 s; contexto depois dela |
| "Termine cada bloco com suspense" | Bloco fecha com recompensa e ponte |
| Pergunta de trivia como gancho | A pergunta do hook é a pergunta-mestra ou parte dela |
| Cinco dicas genéricas após um vídeo fraco | Auditar a promessa do pacote, ler a curva, propor um experimento |
| Concluir que a thumbnail é melhor porque o CTR subiu | CTR só se compara na mesma origem de tráfego; ver `08` §5 |

## Sinais de que você está pulando a skill

- "O pedido é de entrega direta, não preciso dos briefings."
- Respondeu sem abrir o briefing do papel da etapa (inclusive em pergunta de Analytics).
- Título ou hook entregue sem registro de promessas.
- Ponte, pagamento ou frase copiados de um exemplo das referências.
- Dose escrita sem a seção de onde veio.
- Ponte ou gancho que afirma algo sobre o caso sem linha na tabela de fatos.

Qualquer um deles: volte ao briefing do papel.

Depois de editar um documento em `references/`, rode `python scripts/build_index.py`.
