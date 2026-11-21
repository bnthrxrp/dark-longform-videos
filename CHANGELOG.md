# Changelog

Formato: uma seção por versão, da mais nova para a mais antiga.

## 2.0.0 (2026-11-21)

Revisão da skill a partir de uma análise de seis frentes e do teste comparativo com juízes de IA
(`references/21_testes_comparativos.md`). O teste mostrou que a skill garantia processo, mas não dizia o
que faz alguém clicar e continuar, e que nenhuma etapa escrevia o texto narrado. A versão 2 ataca isso.
Nenhuma das mudanças abaixo foi medida em audiência.

### Fluxo e princípio
- O fluxo passa de seis para **sete etapas**: ideia, pacote, hook, roteiro, **narração**, auditoria e
  pós-publicação. A narração (`agents/narracao.md`) é nova: escreve o texto narrado bloco a bloco, com
  tamanho calculado por minutos do mapa × ritmo do canal, fonte `[#id]` em cada frase de fato, medição
  por script e fecho pela ponte.
- O **princípio** ganha duas metades: motivo para clicar e continuar (qualidade percebida) e disciplina
  de fato e promessa. Seguir o processo não substitui a primeira.
- Entrega nova: primeiro o texto limpo, pronto para copiar e narrar; depois a base (tabela de fatos,
  registro de promessas, medições). Modo enxuto para pedido parcial ou com pressa.
- `dossie-modelo.md` reorganizado em seções 0 a 9, com canal e voz do narrador, ficha de fatos com
  coluna de cena possível, sinopse, narração e nota de pós-publicação.

### Ideia
- Critério de clicável: anomalia em uma frase, sem o nome do caso, e três perguntas candidatas
  pontuadas por colisão, leigo, imagem e entregável.
- Capacidade para a duração: conta de fatos (afirmações atômicas verificáveis) por minuto, como aviso,
  não como portão. A duração pedida se mantém; blocos sem fato ficam marcados "a pesquisar" e o aviso
  de escopo abre a entrega. A conta é `[INFERÊNCIA]`, a calibrar.
- Tabela de fatos com coluna "cena possível": só o que a fonte traz.

### Pacote
- Ficha de layout da thumbnail (ponto focal, frase de destaque, área segura, nada por cima de nada,
  contraste, tamanho de letra, leitura em 320x180) e checagem de legibilidade por `checar_thumbnail.py`.
- O limite de "3 a 6 palavras" sai: vale o mínimo de palavras que diz a anomalia.
- Famílias de título e alvo de até 70 caracteres. A ressalva de precisão vai para a narração e a
  descrição, não para o título.

### Hook
- Tamanho por **tempo** (80 a 95 s, faixa de palavras derivada do ritmo do canal; 180 a 215 a
  135 palavras por minuto), no lugar do piso fixo de 190 a 230 palavras. Medido por script.
- Uma pergunta central, dita uma vez até 60 s, com no máximo duas perguntas no hook. Sem frase sobre o
  vídeo.
- Fecho em laço aberto específico, sem afirmação seca e sem anúncio.
- Esquema de frases F (fato), I (inferência), R (ritmo) e X (invenção, que sai): a cena vem só da
  coluna "cena possível".
- Quatro estruturas de abertura, escolhidas pela anomalia (o objeto que não deveria existir, a cena
  fria no momento da descoberta, a contagem que não fecha, a pessoa e o último registro dela).

### Roteiro
- O mapa é derivado do caso (cenas da tabela de fatos agrupadas por fronteira de evento), não do molde
  de 30 minutos, com checagem de cópia do molde.
- Sinopse em três tempos (como começa, como anda, como termina).
- Mapa com coluna de **imagem**, motivo para ficar concreto e ponte em forma de pergunta; cheque de
  densidade (fatos verificados contra blocos) e de intervalo sem fato novo (6 min).

### Auditor
- Centrado no espectador: critérios observáveis em vez de conformidade, cada item com trecho citado e
  classe (bloqueia ou corrige).
- Passo 1 por código (`medir_texto.py`, `checar_thumbnail.py`), rastreio de cada detalhe à tabela de
  fatos e cálculo do maior intervalo sem fato novo.
- Registro da direção prevista para retenção e CTR, para o analytics comparar depois.

### Analytics
- Comparação dentro da mesma faixa de duração, não entre durações diferentes.
- Segmentação por origem de tráfego (CTR, intro de 30 s, duração média e curva), não só do CTR.
- Aviso das quebras de contagem de 24/08/2026 e de novembro/2026.
- Ciclo de volta à skill: hipótese, resultado com nível E0 a E3 e "briefing a mudar", com no máximo
  uma mudança por documento por mês.

### Scripts
- `scripts/medir_texto.py`: palavras, frases, tempo, perguntas, frases sobre o vídeo e números e nomes
  fora da ficha de fatos.
- `scripts/checar_thumbnail.py`: texto cortado, sobreposto, contraste e tamanho no feed, com
  renderizador quando houver e checagem estática parcial quando não.
- `scripts/checar_pacote.py`: valida a skill antes de publicar e monta o zip para upload.
- `scripts/build_index.py` reescrito: trilha por papel, cabeçalhos sem número, técnicas e divergências
  dos mapas, e aviso de referência cruzada quebrada.

### Base de referência
- `00_kit_de_bolso.md` novo: doses com etiqueta, aberturas reais do corpus, checklist de thumbnail e
  pontes entre blocos.
- `21_testes_comparativos.md` novo: os testes cegos, a etiqueta `[TESTE-IA]` e os limites do que provam.
- `INDEX.md` com trilha por papel (as seções que cada briefing mais usa).
- Correções na base: referências cruzadas quebradas, fontes erradas, doses sem etiqueta, cortes
  divergentes de `09`, a regra de promessa paga até 40% do tempo reclassificada como relato de
  praticante e os exemplos que ensinavam o que o briefing do hook proíbe.

### Testada com Haiku e corrigida
- Cinco pedidos reais feitos a Claude Haiku 5.5 seguindo a skill (pacote completo, só o hook com
  pressa, narração de um bloco, pergunta de Analytics, auditoria de hook com defeitos plantados) e
  avaliados por um revisor independente.
- Correções que vieram desses testes: capacidade deixou de reduzir a duração sozinha; fecho do hook
  alinhado ao `medir_texto.py`, que avisa quando o fecho não é pergunta; modo enxuto com formato fixo;
  Analytics compara cada vídeo com a própria faixa de duração e responde direto primeiro; citações de
  referência e campos de processo ficam fora do texto que o usuário lê; `checar_thumbnail.py` valida a
  imagem de feed; o objeto da thumbnail precisa ser reconhecível no feed.
- Reteste dos dois pedidos que tinham falhado: o vídeo de 30 min ficou com 30 min e o trecho sem
  material marcado; a leitura de Analytics passou a comparar cada vídeo com a própria faixa de duração.

## 1.x

- **1.2:** segunda leva da biblioteca (12 obras): mapas `18` e `19`, `20_atualizacao_dos_mapas_11_a_16.md`
  e fichas ampliadas em `17`. Correções vindas do teste comparativo com juízes cegos nos briefings de
  hook e de pacote.
- **1.1:** biblioteca de livros e artigos incorporada: mapas `11` a `16` e as fichas de `17`.
- **1.0:** skill com seis etapas (ideia, pacote, hook, roteiro, auditoria, pós-publicação), dossiê e os
  dez documentos da pesquisa (`01` a `10`).
