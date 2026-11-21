# Testes comparativos: com a skill e sem ela

Este arquivo guarda o histórico dos testes cegos que mediram a skill contra o mesmo pedido feito sem ela. Os briefings citam só a etiqueta `[TESTE-IA]` e mandam vir aqui para saber o quanto confiar nela.

## 1. A etiqueta `[TESTE-IA]`

`[TESTE-IA]` = preferência de juízes de IA em teste cego, não audiência. A etiqueta marca o resultado de um teste cego em que juízes de IA ordenaram textos e thumbnails. Não mede clique, retenção nem satisfação. Mede o que um modelo de linguagem prefere ler e se a entrega cumpre um processo.

Regras de uso:
- Escreva `[TESTE-IA]` ao lado de qualquer número ou regra que venha deste arquivo.
- Não misture com `[DADO]`. Na base, `[DADO]` quer dizer número observado no corpus de 38 vídeos ou nas fichas. Aqui o "dado" são ordenações de modelos.
- Nenhuma heurística daqui vira critério de bloqueio sozinha. Vira aposta de estilo, a ser confirmada com a curva do próprio canal (`10` §3, §4).

## 2. Como o teste foi montado

- **Pedido.** O mesmo para todos os braços: título, thumbnail em SVG, primeira tela, texto dos primeiros 90 s e mapa de blocos, a partir da mesma ficha de fatos (6 a 7 fatos por tema, redigida pelo orquestrador a partir de conhecimento geral).
- **Braços.** Sem skill; v1 (só a pesquisa, dez documentos); v2 (+ 1ª leva da biblioteca); v3 (+ 2ª leva da biblioteca); v4 (v3 com as correções de `hook.md` e `pacote.md` depois da 1ª rodada). A skill de cada braço foi lida do histórico do git. O gerador foi um modelo pequeno (Haiku).
- **Temas.** 12 casos: 8 na 1ª rodada (Mary Celeste, Passo Dyatlov, Roanoke, Voo 19, Tunguska, D. B. Cooper, Homem de Somerton, Manuscrito Voynich) e mais 4 reservados na 2ª (Amelia Earhart, Hinterkaifeck, Sinal Wow, Praga da Dança).
- **Juízes.** Três agentes Opus por rodada, cegos ao braço, com letras embaralhadas. Ordenaram hooks (só o texto) e pacotes (thumbnail em 320×180 mais título) em separado, com um motivo escrito. Um painel Haiku (5 juízes, 8 temas) deu segunda opinião. Um auditor cego aplicou critérios observáveis a cada entrega.
- **Volume.** 120 ordenações Opus (60 de hook e 60 de pacote), 52 entregas únicas.

## 3. Rodada 1: a skill perdeu

8 temas, 3 juízes Opus, 24 ordenações por quesito. Primeiros lugares `[TESTE-IA]`:

| Braço | Hook: 1º / último | Pacote: 1º / último |
|---|---|---|
| Sem skill | 21 / 0 | 13 / 0 |
| v1 só pesquisa | 0 / 7 | 5 / 5 |
| v2 + 1ª leva | 3 / 14 | 6 / 6 |
| v3 + 2ª leva | 0 / 3 | 0 / 13 |

O painel Haiku, com 5 juízes por tema, também deu o hook ao texto sem skill (27 de 40 primeiros lugares). No pacote ele ficou dividido (sem skill 11, v2 13, v1 9, v3 7), o que sugere que a derrota do pacote dependia do juiz.

**O que os juízes escreveram.** Percentuais das duas rodadas somadas (60 motivos por quesito), como ordem de grandeza:
- Hooks que perdem: "aula" ou metalinguagem em 38% dos últimos lugares e em 0 dos 60 primeiros; "curto ou raso" em 38%; "seco, verbete, cronológico" em 32%; "chega tarde ao mistério" em 13%.
- Hooks que ganham: cena viva em 47% dos primeiros; fecho com pergunta, gancho ou virada em 47%; ritmo em 23%; fatos fortes e caso completo em 18%; peso humano em 17%.
- Pacotes que perdem: texto ilegível, cortado ou sobreposto em 40% dos últimos; título genérico em 30%; thumbnail confusa em 25%; imagem vaga em 25%.
- Pacotes que ganham: número ou fato de contraste na thumbnail em 52%; imagem que conta a história em 32%; título forte em 30%; pergunta em 18%.

Os hooks da skill saíam com 137 a 155 palavras (mediana por braço), contra 199,5 do texto sem skill. Foi essa a correção principal: hook curto, que parava antes do melhor momento. As correções entraram em `agents/hook.md` e `agents/pacote.md` e formaram o braço v4.

## 4. Rodada 2: a correção empatou

12 temas, 3 juízes Opus novos, 36 ordenações por quesito. Braços: sem skill, v3 (a skill anterior) e v4 (corrigida). Primeiros lugares `[TESTE-IA]`:

| Braço | Hook: 1º / último | Pacote: 1º / último |
|---|---|---|
| Sem skill | 18 / 3 | 18 / 3 |
| v3 skill anterior | 0 / 31 | 1 / 26 |
| v4 skill corrigida | 18 / 2 | 17 / 7 |

Nos 4 temas novos, v4 ficou à frente: hook 7 a 5 e pacote 9 a 3 sobre o texto sem skill. Nos 8 originais, o hook foi 13 a 11 para o texto sem skill, e o pacote 15 a 8.

Por tema, o resultado é 6 a 6 entre v4 e sem skill nos dois quesitos. v4 ganhou onde há sequência de atos com gente em risco (voo, sequestro, dança, viagem, explosão). O texto sem skill ganhou onde a anomalia é um objeto ou documento parado (manuscrito, Tamám Shud, sinal, navio vazio) e simplesmente abria mostrando o objeto. Essa leitura é inferência sobre 12 casos.

O que só a skill entrega, segundo o auditor: promessa do título com minuto de pagamento (12 de 12 contra 0), registro de promessas (12 de 12 contra 0) e blocos com motivo para ficar além da pergunta (88% contra 0%). Esses critérios de processo não separaram o primeiro do último lugar: cumprir o processo não custou nem rendeu preferência de leitor.

## 5. Efeitos colaterais

- **Detalhe de cena fora da ficha.** O auditor marcou 8 de 52 entregas, todas nos 4 temas novos: sem skill 4 de 4, v3 1 de 4, v4 3 de 4. Nos 8 originais, nenhuma. Os casos são inferências ou ambientação leves ("numa fazenda isolada na Baviera", "a mata ficava logo atrás dela"). A varredura dos 52 hooks não achou nome nem número inventado. Os juízes não viram a ficha e nenhum dos 120 motivos fala de fidelidade, então o teste não mediu esse risco. A trava contra cena inventada entrou depois e não foi testada.
- **Thumbnail ilegível.** A taxa de motivos citando texto ilegível, cortado ou sobreposto foi 0% sem skill, 8% em v1, 25% em v2, 33% em v3 e 28% em v4. O pacote de v4 caiu para último 7 vezes, quase sempre por esse defeito. As thumbnails eram SVG desenhado pelo gerador, sem medir largura de texto: parte do defeito é de ofício de SVG. Por isso existe `scripts/checar_thumbnail.py`.
- **Intervalo sem pagamento.** No auditor, a mediana do maior intervalo sem pagamento foi 4,45 min sem skill e 5,5 a 6 min nos braços da skill, junto do limite de 6 min que a própria base usa para dividir um bloco.
- **Hook e pacote andam juntos.** Dentro do tema, rho 0,48 entre as colocações dos dois; o mesmo braço foi 1º nos dois quesitos em 14 de 20 grupos. Pode ser efeito de halo do juiz.
- **`ideia.md` não foi testado.** A ficha de fatos já vinha pronta.

## 6. Heurísticas que o teste sugere

Fonte: relatório de análise do projeto, `out/revisao/05_dados_do_teste.md`, fora da pasta da skill (análise descritiva sobre 68 entregas-rodada em 20 grupos tema por rodada). Escala de força: **moderada** (consistente em 3 ou mais olhares, incluindo controle por braço ou por tamanho), **fraca** (direção consistente em parte dos olhares, ou só nas justificativas), **exploratória** (um olhar só). Todas são `[TESTE-IA]`.

| # | Heurística | Números | Força |
|---|---|---|---|
| H1 | Preencher o tempo do hook: piso perto de 185 palavras (cerca de 75 a 90 s de fala) | 185 ou mais: 1º em 63% dos votos e último em 6% (n = 28); abaixo: 6% e 46% (n = 40). Dentro do tema, rho 0,67. Nos pares de tamanho parecido, 16 a 14 (nulo); acima de 185, rho 0,07 | Moderada para o piso. Nula para "mais longo é melhor" |
| H2 | Levar o caso até a virada, sem dar a explicação | Fatos da ficha cobertos: 6,25 nos 1ºs e 4,50 nos últimos; controlando o tamanho, rho 0,27 (p ≈ 0,06) | Fraca a moderada |
| H3 | Não fechar o hook em afirmação seca; fechar com pergunta que nomeia a contradição | Afirmação seca: 85% dos últimos e 5% dos 1ºs. Controlando o tamanho, rho −0,28 (p = 0,058). Pergunta no fim: 40% dos 1ºs e 0% dos últimos | Moderada para "não terminar seco". Fraca para "terminar em pergunta" |
| H4 | Uma pergunta central, sem agenda numerada nem método no começo ou no meio | Perguntas abertas segundo o auditor: 2,0 nos 1ºs e 2,8 nos últimos; controlando o tamanho, rho −0,31 (p = 0,031); vencedor com menos perguntas em 16 de 20 pares de tamanho parecido. Frase sobre o vídeo em si não prediz (75% dos 1ºs têm uma) | Moderada para o número de perguntas. Fraca para "agenda" |
| H5 | Abrir pelo que se vê antes de data e ficha técnica | Abre com data: 60% dos 1ºs e 80% dos últimos; pares de tamanho parecido, 2 a 11 | Fraca (vem das justificativas) |
| H6 | Voz direta pontual ("imagine", "repare") | 30% dos 1ºs e 5% dos últimos; controlando o tamanho, rho 0,16 | Fraca |
| H7 | Thumbnail com frase em linguagem comum que afirma ou nega o dado estranho, mais um objeto que a ilustra | 9 dos 12 vencedores da 2ª rodada têm uma frase assim; 10 dos 12 últimos são v3, com rótulo de nome, ano e número | Moderada pelos motivos e pela leitura visual. Fraca nas medidas automáticas |
| H8 | Porta de legibilidade: nenhuma thumbnail com texto cortado, sobreposto ou ilegível a 320×180 | Defeito de texto: 40% dos pacotes em último e 0 dos 60 primeiros | A mais clara nos motivos. Higiene, risco baixo |
| H9 | Título que completa a thumbnail em vez do formato "Caso (ano): descrição" | Dois-pontos: 95% dos pacotes em último e 75% dos 1ºs; pares 2 a 12 (1 de 25 testes) | Fraca |

O que os dados não sustentam: fato mais estranho nas primeiras 40 palavras (15% dos 1ºs e 20% dos últimos), pergunta cedo, número total de perguntas (rho 0,03), números em dígitos, superlativos e apelos "fique até o fim" (quase não foram punidos), título com número, pergunta ou nome do caso, repetir ou não as palavras do título na thumbnail, "menos palavras na thumbnail" (os vencedores não têm menos texto) e o auditor como proxy de preferência.

## 7. Limites

- **12 temas.** A unidade independente é o tema. Dentro de um tema, os 3 juízes quase sempre votam igual: no hook, 10 de 12 temas terminam com o mesmo 1º dos três. Os 36 votos de uma rodada valem bem menos que 36 observações. Cada célula teve um único sorteio de geração, então o ruído é grande.
- **Juízes são IA.** Concordam muito entre si (tau de Kendall 0,78 a 0,89), o que dá consistência e não afasta viés compartilhado. Modelos tendem a preferir texto mais longo e mais detalhado, que é o principal achado de hook. Trate esse achado com desconfiança até testar com público.
- **Correlação não é causa.** O braço confunde quase tudo: cada versão mudou tamanho do hook, forma do fecho, regras de thumbnail e formato do título ao mesmo tempo. Foram testadas 28 medidas de hook e 26 de pacote; a 5% esperam-se 1 a 2 falsos positivos por família. As codificações de motivo são por palavra-chave, depois da decisão do juiz, e valem como ordem de grandeza.
- **O roteiro nunca foi julgado.** O teste cobre título, thumbnail, hook e mapa de blocos. Nenhum roteiro nem texto narrado de um vídeo inteiro foi gerado ou ordenado. O mapa de blocos só passou pelo auditor, que checa critérios observáveis. A primeira tela foi gerada e não foi ordenada. O título nunca foi julgado sozinho.
- **Sem ficha para o juiz.** Os juízes viram só o hook ou só thumbnail e título. Fidelidade aos fatos ficou fora da conta.
- **Sem audiência.** Nenhum número daqui é CTR, retenção ou tempo assistido.

## 8. Como usar na prática

Trate as heurísticas moderadas (piso de tamanho do hook, fecho que não seja afirmação seca, uma pergunta central, thumbnail legível com frase que afirma ou nega o fato) como padrão de estilo do projeto, com a etiqueta. Trate as fracas como opção a escolher e a registrar. Quando o canal tiver curva e volume, teste uma por vez (`10` §3).

Próxima rodada sugerida pelo relatório: ablação a partir de v4, uma heurística por vez; 12 temas novos com 3 sorteios por célula; a ficha de fatos à vista do juiz, com marca separada para "contém algo fora da ficha"; mais de um modelo juiz e uma amostra de leitores humanos; título julgado separado da thumbnail. Para detectar preferência de 70% contra 30% com 80% de poder, são necessários cerca de 47 pares independentes.
