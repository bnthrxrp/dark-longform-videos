# Dossiê: [tema]

Data: [aaaa-mm-dd]. Preencha uma seção por etapa, na ordem. Campos curtos: uma linha basta. Os textos entre colchetes mostram a forma do campo; troque-os pelo conteúdo deste vídeo. O critério de saída de cada etapa está no briefing dela.

## 0. Canal
- **Voz do narrador:** [pessoa gramatical, registro, humor sim ou não, tiques proibidos; voz humana ou sintética]
- **Público:** [quem é e o que já sabe do tema]
- **Gênero:** [história real / mistério / documentário / curiosidades]
- **Duração-alvo:** [min]
- **Ritmo:** [palavras por minuto] (padrão 135 se o canal não tiver medida; diga de onde veio)
- **Últimos 2 ou 3 vídeos do canal:** [título e tipo de abertura de cada um, para variar]
- **Material e restrições do usuário:** [ficha de fatos, links, o que não pode aparecer]

## 1. Ideia
- **Base do público:** [o que ele já sabe do tema e qual lacuna percebe]
- **Anomalia em uma frase** (sem o nome do caso): [dois fatos que colidem, ou um fato que nega o esperado]
- **Perguntas candidatas** (3, com nota 0 ou 1 em colisão, leigo, imagem, entregável): [P1: nota] / [P2: nota] / [P3: nota]
- **Pergunta-mestra** (uma frase, específica; no máximo uma secundária): [...]
- **Resposta esperada** e a ressalva, ou, sem resposta pública, a **recompensa entregável**: [...]
- **Capacidade para a duração:** [N afirmações atômicas verificáveis, cerca de X min cada, soma Y min; cobre a duração? sim / não, e então blocos "a pesquisar" com o que falta saber; a duração só muda se o usuário mandar] `[INFERÊNCIA]`
- **Estrutura escolhida** (`05` §4) e por quê: [...]
- **Ângulo** em relação ao que já existe: [...]
- **Riscos:** [pessoas vivas, atribuição de culpa, direito de imagem]

## 2. Tabela de fatos
Nenhum fato entra na narração sem status "verificado". Fato de uma só versão entra como "a verificar", com a atribuição na coluna Fonte ("segundo X").

| id | Fato | Fonte | Status (verificado / a verificar) | Cena possível (o que se vê) |
|---|---|---|---|---|
| F1 | [afirmação curta] | [link ou documento] | [status] | [objeto, lugar, número, gesto; vazio se a fonte não traz] |

## 3. Pacote
- **Títulos candidatos** (famílias diferentes): [A] / [B] / [C]
- **Escolhido** e por quê: [...] ([N] caracteres, medidos)
- **Tensão não resolvida em uma frase:** [...]
- **Descrição da thumbnail:** objeto [...]; frase curta, em linguagem comum (mediana de 5 palavras) [...]; o que fica de fora [...]; arquivo [caminho do SVG]
- **Resultado de `checar_thumbnail.py`:** [PASSOU / problemas e correção feita / não medi]

### Registro de promessas
Promessa sem bloco e minuto de pagamento é retirada.

| Onde (título / thumbnail / hook) | Promessa | Bloco | Minuto | Paga? (marcado na auditoria) |
|---|---|---|---|---|
| [onde] | [o que promete] | [nº] | [min] | |

## 4. Hook
[Texto narrado de 80 a 95 s (cerca de 180 a 215 palavras a 135 palavras/min), contínuo, como será lido em voz alta.]

- **Estrutura(s) usada(s)** (códigos H-NN): [...]
- **Resultado de `medir_texto.py --tipo hook`:** [palavras, segundos no ritmo da seção 0, frases sobre o vídeo, perguntas, números fora da tabela de fatos]
- **Promessas que o hook abre:** [linhas do registro da seção 3]

## 5. Sinopse em três tempos
- **Como começa** (2 a 4 frases): [...]
- **Como anda** (2 a 4 frases): [...]
- **Como termina** (2 a 4 frases): [...]

## 6. Mapa de blocos

| Tempo | Função | Fatos novos (ids) | Ao sair, o espectador sabe ou acha | Motivo para ficar (o que verá ou saberá no próximo bloco) | Imagem | Ponte (pergunta que fica aberta) |
|---|---|---|---|---|---|---|
| [min a min] | [...] | [F1, F2] | [...] | [...] | [documento, mapa, arquivo, reconstituição rotulada ou silêncio; origem e licença] | [...] |

- **Maior intervalo sem fato novo:** [min]

## 7. Narração
Um bloco por subtítulo, no texto que será narrado, com `[#id]` ao fim de cada frase de fato (as marcas ficam no dossiê). Marque o que falta verificar só com `[VERIFICAR]`.

### Bloco 1 ([min a min])
[texto]

- **Resultado de `medir_texto.py --tipo bloco`:** [palavras, tempo estimado contra o do mapa, números e nomes fora da tabela e a resolução de cada um]

Ao fim: total de palavras e tempo total.

## 8. Auditoria
Feita por quem não escreveu o texto, ou declarada como "auditoria própria, não independente".

| Check | Trecho ou minuto | Evidência (frase colada e `#`) | Resultado (passa / corrige / bloqueia) | Ação |
|---|---|---|---|---|
| [check] | [trecho] | ["frase" e id] | [resultado] | [o que muda] |

- **Versão da rubrica e direção prevista** para retenção e CTR: [...]
- **Decisão:** [publicar / corrigir e reauditar]

## 9. Pós-publicação e experimento
- **Hipótese** (falsificável, escrita antes do resultado): [...]
- **Variável única alterada:** [...]
- **Métrica primária** e **de proteção:** [...]
- **Resultado que confirma / que derruba:** [...]
- **Resultado** (janela, origem, faixa de duração, nível E0 a E3): [...]
- **Briefing a mudar** (qual `agents/*.md` e o quê, ou "nenhum"): [...]

| Data da leitura | Janela e faixa de duração | Origem dominante das impressões | CTR (na mesma origem) | Retenção aos 30 s | Duração média | Onde a curva cai (bloco) | Decisão |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
