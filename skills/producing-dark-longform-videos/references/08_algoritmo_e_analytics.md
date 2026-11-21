# YouTube Algorithm & Analytics

# Algoritmo de recomendação e Analytics para vídeos longos

**Data de referência:** 20/11/2026 · **Escopo:** vídeos longos (10 a 60+ min), canal dark/faceless. Shorts, Reels e TikTok ficam fora.

**Etiquetas:** [OFICIAL] documentação, blog ou declaração do YouTube · [ESTUDO] artigo, com autores e ano · [DADO] dado público medido · [PRATICANTE] heurística de terceiro, só hipótese · [INFERÊNCIA] raciocínio meu a partir do material · [LACUNA] não encontrado. **(via terceiros)** indica declaração que chegou por cobertura de imprensa ou blog, sem verificação na fonte primária. **(trecho)** indica que a fonte foi vista só em resultado de busca. Códigos como "Ajuda 9314486" remetem à lista de fontes no fim.

---

## Resumo operacional

- Não há, em fonte oficial, pesos de sinais, fórmula de ranqueamento nem duração recomendada para vídeo longo. Peso que aparece em blog é hipótese e não entra como premissa.
- O que o YouTube documenta e você pode usar no diagnóstico: CTR de impressões (só dentro da mesma origem de tráfego e com volume), retenção nos primeiros 30 segundos, curva de retenção comparada com vídeos de duração semelhante, e AVD em minutos.
- Antes de qualquer comparação histórica, marque duas quebras na contagem de visualizações: primeiro frame em long-form (24/08/2026; [OFICIAL] blog do YouTube de 19/08/2026 e histórico de revisões da Analytics API de 27/08/2026, lidos em trecho ou aberto; a Ajuda 2991785 lida não traz a data) e co-views estimadas em TV (início em novembro de 2026 pela Ajuda; o dia 16/11/2026 vem só de imprensa e de post do Creator Insider não aberto).
- CTR alto não indica vídeo melhor. A própria Ajuda descreve CTR alto com AVD baixa como assinatura de clickbait, ou seja, promessa maior que o conteúdo.
- Satisfação não é observável diretamente. Você lê retenção, intro e reações públicas, e deve tratá-las como proxies.

---

## 1. Como a recomendação funciona

### 1.1 O que as fontes oficiais declaram

- **Objetivos.** Ajudar cada espectador a encontrar o que quer assistir e maximizar a satisfação de longo prazo. [OFICIAL] Ajuda 16533387, sem data visível. Um agregador diz 2024; não confirmei.
- **Personalização.** O sistema analisa o perfil de cada espectador em tempo real: dispositivo, horário e hábitos. [OFICIAL] Ajuda 16533387.
- **Sinais.** Quanto do vídeo foi assistido, escolhas, ignorados, "não tenho interesse", pesquisas de satisfação, likes, compartilhamentos, comentários, inscrições, idiomas e "interest affinity" (afinidade com audiências parecidas). [OFICIAL] Ajuda 16533387. A página não dá pesos, não dá limiares e não trata de duração. Em outra página oficial, o YouTube fala em "mais de 80 bilhões de sinais" sem dizer quantos entram em cada superfície. [OFICIAL] How YouTube Works (trecho).
- **Histórico.** Em 2011 o YouTube aprendeu que clicar não garante que o vídeo foi assistido. O watch time entrou em 2012 e, segundo o próprio texto, causou queda imediata de 20% nas visualizações. [OFICIAL] Cristos Goodrow, blog oficial, 15/09/2021.
- **Pesos.** Não há fórmula fixa; a importância de cada sinal depende do espectador. [OFICIAL] Goodrow, 2021.
- **Dados recentes.** O sistema usa o desempenho recente de cada vídeo, não só o passado. A Ajuda não informa janela de tempo. [OFICIAL] Ajuda 16533387.
- **Informação e categorias sensíveis.** Avaliadores humanos classificam canais e vídeos de informação; vídeos "borderline" são rebaixados nas recomendações. O blog diz que categorias como notícias podem seguir lógica diferente. Critérios não publicados. [OFICIAL] Goodrow, 2021. [INFERÊNCIA] Canais de divulgação científica e história podem cair nessa lógica. Não sei qual categoria o YouTube aplica.

### 1.2 Artigos técnicos, ano e o que mudou

| Fonte | Ano | Superfície | O que descreve | Status para 2026 |
|---|---|---|---|---|
| Covington, Adams e Sargin, *Deep Neural Networks for YouTube Recommendations* (Redes neurais profundas para recomendações do YouTube), RecSys '16 | 2016 [ESTUDO] | Não confirmei a superfície | Dois estágios: geração de candidatos e ranqueamento. Objetivo: tempo esperado por impressão, por regressão logística ponderada pelo tempo assistido. Em 2016, os autores dizem que a satisfação real quase nunca é conhecida e usam sinais implícitos (pp. 191–192). | Superado como objetivo. Não usar como objetivo vigente. |
| Zhao et al., *Recommending What Video to Watch Next: A Multitask Ranking System* (Recomendando qual vídeo assistir em seguida: um sistema de ranqueamento multitarefa), RecSys '19 | 2019 [ESTUDO] | Watch-next (painel Up Next, equivalente a Suggested) | Candidatos por tópico e por coexibição. Ranqueamento multiobjetivo: engajamento e satisfação, com pesos ajustados manualmente. Em teste ao vivo, o MMoE com 8 experts reportou ganhos relativos de +0,45% em engajamento e +3,07% em satisfação, sem referência informada no texto. Sistema de 2019; não usar como efeito esperado em 2026. CTR cai da posição 1 à 9 (Figura 6). | 2019. Não sei se o desenho atual é o mesmo. Não separa por duração. |
| Chen et al., *Top-K Off-Policy Correction for a REINFORCE Recommender System* (Correção off-policy top-K para um sistema de recomendação REINFORCE), WSDM 2019 | 2019 [ESTUDO] | Geração de candidatos | Recomendador top-K em produção, com exploração. Li só o resumo e trechos. | Etapa de candidatos, não ranqueamento final. Long-form não testado. |
| Goodrow, "On YouTube's recommendation system" | 15/09/2021 [OFICIAL] | Geral (Home e Up Next, segundo o blog) | Valued watchtime; pesquisas de 1 a 5 estrelas (ver seção 3); borderline; Home mistura recomendações, inscrições e notícias. | Descrição oficial mais recente que li. Pode ter mudado. |
| "Continuing our work to improve recommendations on YouTube" | Data não confirmada [OFICIAL] | Geral | Foco em satisfação, e não em views; mede likes, dislikes, pesquisas e "time well spent" (tempo bem gasto); recomenda clickbait com menos frequência. (trecho) | Data não confirmada. |
| Creator Insider, 01/09/2026 | 2026 [OFICIAL, via terceiros] | Geral | Ranking feito por espectador, a cada abertura do app; novos vídeos casados por tópico; aprendizado separado para inscritos, não inscritos e novos; ponderação "não é a mesma para todos". | Não verificado. Vídeo não aberto. Hipótese até transcrição. |

**Evolução [INFERÊNCIA].** A sequência é: objetivo de tempo por impressão (2016), multiobjetivo com satisfação (2019), valued watchtime (2021), ponderação por espectador (2026, via terceiros). Cada etapa substitui a anterior. Não use a descrição de 2016 como estado atual.

### 1.3 O que isso significa para vídeo longo

- Nenhuma fonte primária que li mede o efeito da duração no ranqueamento. [LACUNA]
- A única declaração de funcionário sobre duração é de Todd Beaupré, no VidCon 2022: "Make the video as long as it needs to be" (faça o vídeo tão longo quanto precisar ser). [OFICIAL] (via TechCrunch, 24/06/2022). É um princípio, não evidência de efeito.
- Se o objetivo de 2016 (tempo esperado por impressão) ainda valesse, vídeos longos teriam vantagem em minutos absolutos. Não há prova de que valha. [INFERÊNCIA] Não use como premissa.
- Chen et al. (2019) descrevem exploração na geração de candidatos. [INFERÊNCIA] Um vídeo novo pode ser testado com audiências diferentes nas primeiras semanas, então leituras muito cedo são instáveis. Hipótese não medida.
- O arXiv 2206.06003 (2022), sobre viés de duração na predição de watch time, não foi lido integralmente e não trata do YouTube. Não sei se o sistema corrige esse viés.

---

## 2. Browse, Suggested e Search

Definições do Studio: [OFICIAL] Ajuda 9314355 (lida).

| Superfície | Definição oficial (Studio) | O que a fonte diz que alimenta a superfície | Evidência específica para long-form | Onde isolar no Studio |
|---|---|---|---|---|
| **Browse** (Página inicial, Inscrições, Assistir mais tarde, Em alta/Explorar e outros) | Tráfego desses recursos de navegação | Perfil e histórico do espectador; mistura de recomendações, inscrições e notícias (Goodrow, 2021) | Nenhuma | Fonte "Browse features" |
| **Suggested** (sugestões ao lado ou depois de outro vídeo, e links em descrições) | Tráfego dessas sugestões e links | Modelo de watch-next (Zhao et al., 2019): candidatos por tópico e por coexibição | Nenhuma. O estudo de 2019 não separa por duração | Fonte "Suggested videos" (inclui links de descrição) |
| **Search** (resultados de busca) | Tráfego dos resultados de busca | Relevância à consulta e engajamento por consulta (Ajuda 16559651, trecho) | Nenhuma | Fonte "YouTube search" (com termos, se a sua interface mostrar) |

Exemplo real de superfície: Zhao et al. (2019), Figura 4 (p. 48 do PDF), mostra o painel Up Next ao lado do vídeo "Large-Scale Deep Learning with TensorFlow" (Jeff Dean). A figura ilustra a superfície. Não mostra desempenho.

**O que muda para vídeo longo:**

1. **Suggested não é só recomendação algorítmica.** Links de descrição, inclusive para outros vídeos do próprio canal, entram nessa categoria. [OFICIAL] Ajuda 9314355. [INFERÊNCIA] Antes de atribuir uma variação de Suggested ao algoritmo, verifique se você mudou links de descrição no período. Registre essas mudanças.
2. **Suggested depende de vizinhança de tema e de coexibição.** O modelo de 2019 gera candidatos a partir de vídeos de tema parecido e de vídeos frequentemente assistidos juntos. [ESTUDO] [INFERÊNCIA] Para vídeo longo, séries e playlists que ligam vídeos do mesmo tema criam essa coexibição. A Ajuda 16533387 recomenda séries, playlists e telas finais para ampliar o consumo. [OFICIAL] Contraindicação: o modelo é de 2019 e os ganhos são relativos.
3. **Browse é personalizado por espectador.** Você não vê essa visão por espectador, só agregados do canal. [INFERÊNCIA a partir da Ajuda 16533387] Ao comparar Browse entre dois períodos, compare na mesma origem e com o mesmo público possível. Mudança no público não é mudança no algoritmo.
4. **Search é a única superfície em que a intenção é explícita.** A fonte oficial diz que a busca considera relevância e engajamento por consulta, sem pesos. [OFICIAL] Ajuda 16559651 (trecho). [INFERÊNCIA] Título, descrição e promessa alinhados à consulta são o que você controla nessa fonte.
5. **Mistura de origens distorce o CTR.** Impressões na Página inicial tendem a reduzir o CTR; impressões concentradas na página do canal tendem a elevá-lo. [OFICIAL] Ajuda 7628154.
6. **O Studio mostra parte das impressões vindas de recomendações** no relatório de impressões por origem. [OFICIAL] Ajuda 12220281.

**Lacunas nesta seção.** Não há lista oficial de sinais por superfície. Listas de blogs de terceiros (tinymedialab, weaveaura) são hipóteses. A Ajuda diz só que superfícies diferentes usam sinais de forma diferente, sem listar.

---

## 3. Satisfação do espectador

### 3.1 Como o YouTube descreve

- **Três grupos de sinais:** apelo (escolheu assistir ou ignorou e marcou "não tenho interesse"), engajamento (continua assistindo?) e satisfação (gostou?). Os sinais específicos variam por formato, e a Ajuda não diz quais. [OFICIAL] Ajuda 16559650.
- **Pesquisas.** O espectador avalia vídeos que assistiu. A Ajuda diz que isso ajuda a entender satisfação, não só tempo assistido. [OFICIAL] Ajuda 16089387. Frequência, escala, amostragem e peso não são informados.
- **Valued watchtime.** Segundo o blog de 2021, as pesquisas são de 1 a 5 estrelas, e só respostas de 4 e 5 contam como tempo valorizado. Para quem não respondeu, um modelo prevê a resposta, e algumas respostas reais ficam reservadas para testar a precisão. [OFICIAL] Goodrow, 2021, lido na unidade de pesquisa 1.
- **Atenção à escala.** A unidade que leu as Ajudas 16559650 e 16089387 não encontrou a escala de 1 a 5 estrelas nelas, e a atribuiu a um blog de terceiro. Releia o texto do blog de 2021 antes de citar a escala.
- **[INFERÊNCIA]** Se a descrição de 2021 ainda vale, 25 minutos assistidos com nota 3 não geram crédito de valued watchtime. Essa leitura depende de a descrição estar atual.
- **Divergência de 2026.** Blogs de terceiros (milx, dataslayer) dizem que a satisfação passou a pesar mais que o watch time. Outros (outlierkit, onetube) dizem que não há peso publicado nem mudança oficial verificada. A Ajuda diz que a satisfação entra além do tempo assistido, o que indica complemento, não substituição. Use a versão oficial.

### 3.2 Como inferir satisfação

- **Promessa cumprida no início.** A Ajuda diz que os primeiros segundos são o momento em que o espectador decide ficar ou sair, sobretudo em long-form, e que a introdução deve cumprir o que título e miniatura prometeram. [OFICIAL] Ajuda 16559650. Exemplo oficial, sem resultado medido: um título de análise do mercado de café foi reescrito como pergunta do cotidiano, para atrair quem não é especialista. [OFICIAL] Ajuda 16559650.
- **Mecanismo com estudo qualitativo.** Grupo focal com 21 jovens espectadores; autores e ano não identificados no material. O mecanismo é a confirmação de expectativa: quando o conteúdo confirma o que título e miniatura criaram, o espectador costuma ficar satisfeito e dar like ou comentário positivo. [ESTUDO qualitativo] (trecho, researchgate 395261047). Limite: n=21, sem métricas de retenção.
- **Retenção por minuto.** Mostra onde o espectador sai, não por quê. [INFERÊNCIA]
- **Reações públicas** (likes, comentários). São sinais que o sistema usa. Contagens públicas não equivalem à medida de satisfação do sistema. [INFERÊNCIA]

### 3.3 O que você observa e o que não observa

| Item | Observável pelo criador? | Fonte e nota |
|---|---|---|
| Retenção por minuto, picos, quedas, top moments | Sim, com 1 a 2 dias de processamento | Ajuda 9314415 |
| Retenção nos 30 s (intro) | Sim | Ajuda 9314415 |
| AVD (minutos), tempo de exibição | Sim | Ajuda 9313698 (trecho), 9314415 |
| APV | Só se você calcular (AVD ÷ duração) | Ver glossário |
| Likes e comentários | Sim, como contagens públicas | Reação, não medida do sistema |
| Respostas às pesquisas de satisfação | Não, pelo que li | Sem agregado oficial confirmado |
| Score de satisfação por vídeo | Não encontrei | [LACUNA] [INFERÊNCIA] Não existe na Ajuda lida |
| Peso de cada sinal | Não | Ajuda 16533387; Goodrow 2021 |
| Ranking por espectador e pool de candidatos | Não | Só hipóteses de 2026 e modelos de 2019 |

---

## 4. Glossário operacional

**Impressões**
- *Oficial:* uma miniatura conta como impressão quando fica visível por mais de 1 segundo, com ao menos metade da área na tela. Contam: busca, Página inicial (com reprodução automática), feeds (inscrições, em alta, histórico, Assistir mais tarde), Up Next com reprodução automática e playlists. Não contam: sites e apps externos, site móvel, YouTube Kids, YouTube Music, cards e telas finais, e-mails e notificações, vídeo em aba de segundo plano e anúncios TrueView de descoberta. [OFICIAL] Ajuda 9314486 (lida). A lista não separa por duração nem por formato.
- *Como ler:* contagem de exposições da miniatura, por origem. [INFERÊNCIA] Não é contagem de pessoas. O cartão do Studio aparece poucas horas após a publicação e atualiza com mais frequência que o relatório "Impressões e como levaram ao tempo de exibição". Os dois podem divergir. [OFICIAL] Ajuda 9314486.
- *Erro mais comum:* somar impressões de origens diferentes, ou tratar impressão como alcance de pessoas.

**CTR de impressões (taxa de cliques)**
- *Oficial:* visualizações vindas de impressões contadas ÷ impressões contadas. Visualizações de fontes externas entram no total de visualizações, mas não no CTR. [OFICIAL] Ajuda 7628154 (lida, versão en e en-GB). Metade dos canais e vídeos fica entre 2% e 10%. Isso é descrição de distribuição, não meta. A faixa varia por tipo de conteúdo, público e local da impressão. Vídeos com menos de uma semana ou menos de 100 visualizações podem ter faixa mais ampla. [OFICIAL] Ajuda 7628154.
- *Como ler:* só depois de acumular impressões "substanciais" (a Ajuda não define o número). Compare dentro da mesma origem. Variação pequena não pede ação. A Ajuda não define teste estatístico nem tamanho de amostra. [OFICIAL] Ajuda 7628154.
- *Erro mais comum:* dividir visualizações totais por impressões e esperar o CTR exibido. O numerador é outro, então o resultado difere. Também: tomar 2% a 10% como meta, e testar miniaturas trocando à mão.

**Visualizações**
- *Oficial:* contadas no momento em que o vídeo começa a tocar, em todos os formatos, incluindo long-form e lives. [OFICIAL] Ajuda 12220281 (lida até a tabela de métricas, que ficou truncada) e Ajuda 2991785 (trecho). Para long-form, a data do primeiro frame é 24/08/2026: [OFICIAL] blog do YouTube de 19/08/2026 (engaged-views-youtube-explained) e histórico de revisões da Analytics API de 27/08/2026 (trecho). A Ajuda 2991785 que li integralmente não traz a data; a versão en-GB em cache (trecho) e o Creator Insider (via ppc.land) também a citam. Relatos de terceiros mencionam um piso não oficial de cerca de 30 segundos antes disso. Não encontrei esse piso na Ajuda que li.
- *Co-views (coespectadores):* a partir de novembro de 2026, a contagem pública inclui estimativas de pessoas que assistem juntas numa TV. A métrica "Views (Co-viewed)" fica disponível no modo avançado até maio de 2027 ([OFICIAL] Ajuda 12220281, lida até a tabela de métricas; a Ajuda 2991785 é só trecho). O dia de início (16/11/2026) é [OFICIAL, via terceiros]: relatado pela imprensa e por post do Creator Insider não aberto. Retroatividade: a Ajuda não diz; relato do Creator Insider afirma que não é retroativa, mas novas views na TV de vídeos antigos passam a incluir co-views. A data exata não é consistente: a Ajuda diz "novembro"; a cobertura cita 16/11/2026 (via terceiros); outra cobertura de 17/11/2026 diz que a funcionalidade está sendo lançada. O método do estimador não é descrito. Contexto de tamanho: o YouTube afirma ver mais de 1 bilhão de horas de watch time em TV por dia (via TechCrunch, 10/08/2026). A Nielsen mede 15,8% de share de TV para o YouTube nos EUA em agosto de 2026 (trecho). Não são dados do seu canal.
- *Como ler:* a série de visualizações públicas tem duas quebras. Não compare períodos antes e depois sem anotá-las. [INFERÊNCIA]
- *Erro mais comum:* ler o crescimento de views após novembro de 2026 como crescimento real de audiência.

**Engaged views (visualizações engajadas)**
- *Oficial:* a Ajuda usa engaged views para avaliar visualizações sem co-views, e como base da AVD e dos espectadores únicos. [OFICIAL] Ajuda 2375431 e 9313698 (trechos). A receita do YPP é baseada em engaged views e engaged watch hours. [OFICIAL] Ajuda 12220281. A definição geral de engaged view vale para todos os formatos ([OFICIAL] blog do YouTube de 19/08/2026, aberto; inclui vídeo longo em autoplay). O limiar em segundos não é publicado, e a Ajuda do Studio App (snippet) não o define. Termos como loops não estão definidos para vídeo longo. [LACUNA]
- *Como ler:* [INFERÊNCIA] é a série candidata a comparar períodos, porque não inclui co-views. O limiar em segundos da engaged view não é publicado; comparar períodos exige testar a série no próprio canal antes de usá-la.
- *Erro mais comum:* confundir engaged views (base de monetização e de AVD) com "as visualizações que o YouTube distribuiu".

**Tempo de exibição (watch time)**
- *Oficial:* total de tempo que os espectadores passaram assistindo, incluindo o tempo de co-views. [OFICIAL] Ajuda 9313698 (trecho).
- *Como ler:* volume em minutos ou horas. Cresce com visualizações e com a duração do vídeo. Não separa atenção de passividade.
- *Erro mais comum:* lê-lo como satisfação. Valued watchtime (2021) é outra medida, se a descrição do blog ainda valer.

**AVD (duração média de visualização)**
- *Oficial:* média de minutos assistidos entre quem ficou para assistir ("among those who stayed to watch", entre quem ficou para assistir). É calculada a partir de engaged views e do tempo de exibição correspondente. [OFICIAL] Ajuda 9313698 (trecho) e 9314415 (lida).
- *Como ler:* valor em minutos. Compare só com vídeos de duração semelhante do canal. [OFICIAL] Ajuda 9313698 (aberta) diz que a AVD é calculada a partir de engaged views e do watch time correspondente, e não de todas as visualizações.
- *Exemplo construído:* vídeo de 30 min com AVD de 10 min equivale a APV calculado de 33%.
- *Erro mais comum:* calcular AVD como tempo total ÷ todas as visualizações. Essa é a fórmula de terceiros (vidiq, gyre), e os dois números divergem quando há muitas visualizações sem engajamento. Também: comparar AVD em minutos entre vídeos de durações muito diferentes.

**APV (porcentagem média visualizada)**
- *Status:* não confirmado como definição oficial. Um terceiro (prepublish.ai) atribui à Ajuda a expressão "entre quem ficou para assistir". Não consegui confirmar, porque a leitura da Ajuda 12220281 foi truncada antes da tabela de métricas. [PRATICANTE] Fórmula de terceiros: AVD ÷ duração × 100 (air.io; vidiq).
- *Como ler:* se usar, rotule como "APV calculado (AVD ÷ duração)". Serve para comparar durações diferentes, que a AVD em minutos não compara.
- *Erro mais comum:* tratar benchmarks de terceiros como alvo. Circulam valores de 30%, de 40% a 60% e 23,7% (média de um relatório de 2025 citado por gyre). Nenhum é oficial.

**Retenção: curva por minuto e comparação com outros vídeos**
- *Oficial:* o relatório de retenção existe só no nível do vídeo. Mostra o trecho assistido, quedas, picos e top moments. Leva de 1 a 2 dias para processar. [OFICIAL] Ajuda 9314415 (lida). Ao clicar em "ver mais", o Studio compara com todos os vídeos do YouTube de duração semelhante. A "retenção típica" usa os 10 vídeos mais recentes do próprio canal com duração semelhante. [OFICIAL] Ajuda 9314415.
- *Retenção absoluta e relativa:* não há definição oficial que eu possa citar. Terceiros (prepublish.ai) afirmam que o Studio mostra duas curvas, uma absoluta e uma relativa. Nas páginas oficiais que li, a comparação existe, mas os rótulos não aparecem. [PRATICANTE]
- *Como ler:* use a curva do próprio vídeo para localizar minutos. Procedimento proposto [INFERÊNCIA]: comparar a curva com a « retenção típica » (10 vídeos recentes de duração semelhante) e com a referência da plataforma por duração, sem rotular nenhuma delas como absoluta ou relativa, já que essa definição não foi encontrada. Use a "retenção típica" (10 vídeos recentes do canal) como linha de base interna. A comparação com todos os vídeos de duração semelhante é referência de plataforma. [INFERÊNCIA] Não compare com curvas de terceiros, que não são públicas.
- *Erro mais comum:* tratar "absoluta" e "relativa" como termos oficiais. Também: ler os números absolutos por segmento como pessoas. Eles podem superar o total de visualizações, porque a mesma pessoa pode rever trechos. [OFICIAL] Ajuda 9314415.

**Retenção nos primeiros 30 segundos (intro)**
- *Oficial:* percentual da audiência que continua assistindo após 30 segundos. Intro alta pode indicar que o início correspondeu ao que título e miniatura prometeram. A Ajuda sugere alinhar título e miniatura ao conteúdo e testar outro estilo nos primeiros 30 segundos. [OFICIAL] Ajuda 9314415.
- *Limiar oficial:* não há. A regra de "50%" vem de um blog de terceiro e não aparece na página oficial que li.
- *Como ler:* compare com a referência interna do canal (os 10 vídeos recentes de duração semelhante, a mesma convenção do Studio).
- *Erro mais comum:* tratar 50% como aprovação.

**Picos, quedas e top moments**
- *Oficial:* picos são trechos assistidos, reassistidos ou compartilhados por mais gente. A Ajuda dá duas leituras: trecho valorizado, ou conteúdo pouco claro que exigiu reassistir. Quedas são trechos pulados ou em que o espectador parou; a Ajuda recomenda revisar. Top moments são trechos em que quase ninguém saiu. Os destaques só aparecem em vídeos com pelo menos 60 segundos e 100 visualizações. [OFICIAL] Ajuda 9314415.
- *Erro mais comum:* ler todo pico como "trecho bom" sem ouvir o trecho.

**Audiência: novos, casuais, regulares, audiência mensal**
- *Oficial:* novo é quem assistiu ao canal pela primeira vez no período (inclui navegação privada, histórico apagado e quem não assistia há mais de um ano). Casual: assistiu pelo menos uma vez por mês, em 1 a 5 meses do último ano. Regular: pelo menos uma vez por mês, por mais de 6 meses no último ano. Audiência mensal: espectadores únicos nos últimos 28 dias, recalculada todo dia. [OFICIAL] Ajuda 9314416 (lida).
- *Lacunas:* a faixa exata de "regular" entre 5 e 6 meses não está definida. Outra versão da mesma página fala em "recorrentes" como métrica (ver seção 9.2).

---

## 5. Por que CTR alto nem sempre é melhor

### 5.1 Mecanismos

1. **CTR mede uma miniatura dentro de um contexto.** Impressões na Página inicial tendem a reduzir o CTR; na página do canal, tendem a elevá-lo. [OFICIAL] Ajuda 7628154. No estudo de watch-next, o CTR cai de forma clara da posição 1 à 9 do painel. [ESTUDO] Zhao et al. (2019), Figura 6. *Consequência:* CTR em posição 1 não prova que a miniatura é melhor. *Condição:* vale para comparações dentro da mesma origem e da mesma posição.
2. **Volume pequeno pode inflar o CTR.** A Ajuda diz que vídeos com poucas impressões costumam ter CTR e AVD mais altos, porque o público é menor e mais fiel. O YouTube não quantifica isso. [OFICIAL] Ajuda 7628154. *Consequência:* CTR alto em volume pequeno não prova nada.
3. **Clicar não é assistir.** Em 2011 o YouTube aprendeu que clicar não garante que o vídeo foi visto. [OFICIAL] Goodrow, 2021. Covington et al. (2016) descrevem o uso de sinais implícitos de engajamento. A afirmação de que ordenar por CTR promove vídeos que o usuário não completa não foi localizada na passagem lida; fica como [INFERÊNCIA] não verificada, sem atribuição ao estudo. Lido em cópia pública. *Limite:* sistema de 2016.
4. **Promessa maior que o conteúdo derruba a AVD.** A Ajuda descreve a assinatura de clickbait: CTR alto, AVD baixa e impressões abaixo do esperado. Clickbait tende a ter menos chance de ser recomendado. [OFICIAL] Ajuda 7628154. *Limite:* é heurística com base em taxas agregadas, e a própria Ajuda diz que não garante resultado num caso específico. *Mecanismo de apoio:* confirmação de expectativa (seção 3.2). [ESTUDO qualitativo]
5. **O concorrente do vídeo é o universo do espectador.** Cada vídeo é comparado com todos os que o espectador poderia assistir, não só com os do próprio canal. [OFICIAL] Ajuda 7628154. *Consequência:* comparar CTR só com os vídeos do canal é leitura parcial. Mesmo assim, comparar dentro do canal continua útil para medir o efeito de uma mudança. [INFERÊNCIA]
6. **Trocas manuais confundem a leitura.** Testar várias miniaturas ou títulos à mão, no mesmo vídeo, impede garantir que a mesma audiência veja cada versão. A diferença pode vir da origem. [OFICIAL] Ajuda 7628154.
7. **Possível efeito de contagem.** Não sei se as co-views entram no numerador do CTR. [LACUNA] [INFERÊNCIA] Se entrarem, um vídeo com audiência de TV pode ter CTR subindo sem mudança de comportamento. Não verificado.

### 5.2 Exemplo construído

Os números abaixo são **construídos por mim** para ilustrar a divergência. Não são dados do YouTube nem de nenhum canal. Premissas: mesma origem de tráfego, mesmo número de impressões e engaged views como base de AVD (a definição de engaged view em long-form não foi encontrada).

| | Vídeo A (construído) | Vídeo B (construído) |
|---|---|---|
| Duração | 12 min | 12 min |
| Impressões (mesma origem) | 20.000 | 20.000 |
| Visualizações vindas de impressões (cliques) | 1.800 | 800 |
| **CTR** | **9,0%** | **4,0%** |
| Engaged views (premissa) | 1.000 | 700 |
| Tempo de exibição | 1.500 min | 4.700 min |
| **AVD** (tempo ÷ engaged views) | **1,5 min** | **6,7 min** |
| APV calculado (AVD ÷ 12 min) | 12,5% | 56% |
| Por 1.000 impressões: cliques | 90 | 40 |
| Por 1.000 impressões: minutos assistidos | 75 | 235 |

**Como ler:**
- O Vídeo A ganha em CTR (2,25 vezes). O Vídeo B ganha em minutos assistidos por impressão (3,1 vezes), em AVD e em APV calculado.
- A regra de clickbait da Ajuda exige impressões abaixo do esperado. Aqui as impressões são iguais, então a regra não se aciona. O descasamento entre clique e permanência continua aparecendo.
- O exemplo não mostra qual vídeo o YouTube recomenda mais. "Minutos por 1.000 impressões" é uma conta minha para ilustrar. Não é métrica oficial.

**Quando CTR alto ajuda.** [INFERÊNCIA] Para comparar duas embalagens do mesmo vídeo, com a mesma origem e volume, o CTR é o diagnóstico certo. Para decidir se o vídeo é bom, ele não basta. Leia junto com intro, AVD e curva.

---

## 6. Três classes de métrica

**Diagnóstico:** aponta onde o vídeo ganha ou perde atenção. Pode ser alterado por embalagem ou roteiro.
**Resultado:** mede o que o vídeo entregou no total. Sofre com mudanças de definição e de distribuição.
**Não observável:** influencia a recomendação e não pode ser lida diretamente. Só se estima por proxies.

| Métrica (onde ver) | Classe | Pergunta que responde | Decisão que orienta | Limite |
|---|---|---|---|---|
| Impressões (Alcance) | Diagnóstico | Quanta oportunidade de clique o vídeo teve, e de qual origem? | Ler CTR só com volume; decidir por origem | Não é pessoa; cartão atrasa e pode divergir do relatório |
| CTR de impressões (Alcance) | Diagnóstico | Quem viu a miniatura clicou, dentro da origem? | Trocar título ou miniatura só por teste nativo, após volume | Depende de origem, posição e concorrência; faixa de 2% a 10% é descritiva |
| Retenção nos 30 s (intro) | Diagnóstico | A abertura confirmou o que título e miniatura prometeram? | Revisar a abertura se ficar abaixo da referência interna | Sem limiar oficial |
| Curva de retenção, quedas e picos | Diagnóstico | Em que minuto o público sai, e que trecho segura? | Revisar o trecho da queda; ouvir o pico | Não mostra o motivo; processa em 1 a 2 dias; destaques só com 60 s e 100 views |
| AVD (minutos) | Diagnóstico | Entre quem ficou, quanto assistiram em média? | Comparar só com vídeos de duração semelhante do canal | Em minutos não compara durações; base de engaged views confirmada pela Ajuda 9313698 (aberta) |
| APV calculado (AVD ÷ duração) | Diagnóstico | Que fração do vídeo, em média, foi assistida? | Comparar durações diferentes dentro do canal | Não confirmado como oficial; não usar benchmark de terceiro como alvo |
| Visualizações públicas | Resultado | Quanto alcance o vídeo gerou? | Acompanhar tendência, anotando quebras | Mudou em 24/08/2026 (long-form) e em novembro/2026 (co-views) |
| Engaged views | Resultado | Quanto da contagem tem engajamento e não inclui co-views? | Série para comparar períodos | Definição para long-form não encontrada |
| Tempo de exibição | Resultado | Quantos minutos o vídeo entregou? | Medir volume; ler depois dos diagnósticos | Não separa atenção de passividade; inclui co-views |
| Novos, casuais, regulares | Resultado | O vídeo traz gente nova ou devolve a base? | Distinguir descoberta de fidelização | Faixa de "regular" não exata |
| Likes e comentários | Não observável (proxy) | Qual é a reação explícita do público? | Usar como reação, nunca como prova de satisfação | Não equivalem à medida do sistema |
| Respostas às pesquisas de satisfação | Não observável | O espectador gostou? | Nenhuma decisão direta | Sem escala, frequência, amostra ou agregado confirmados |
| Pesos, objetivos e pool de candidatos | Não observável | Por que o vídeo foi mostrado a quem? | Nenhuma. Só testar hipóteses com mudanças controladas | Não publicados; 2016 e 2019 descrevem arquitetura, não pesos atuais |

---

## 7. Roteiro de leitura do Analytics para vídeo longo

### 7.1 Antes de abrir o Analytics

Registre na planilha:
- Data de publicação, duração e data da leitura.
- Quebras de contagem: 24/08/2026 (primeiro frame em long-form) e novembro/2026 (co-views; dia a confirmar).
- Mudanças feitas: título, miniatura, links de descrição, séries, playlists, telas finais.
- Campos de leitura: impressões e CTR por origem; intro de 30 s; AVD em minutos; APV calculado (rotulado como tal); visualizações públicas; engaged views, quando visíveis; tempo de exibição; novos e regulares.

### 7.2 Janelas de tempo

| Janela | O que ler | O que não concluir | Base |
|---|---|---|---|
| 0 a 48 h | Checagem: publicação, cartão de impressões | Nenhuma decisão. Retenção leva 1 a 2 dias; cartão e relatório podem divergir | [OFICIAL] Ajuda 9314415, 9314486 |
| 3 a 14 dias | Diagnóstico: curva, intro, CTR (se houver volume), origem | Conclusão sobre embalagem sem volume | Faixa de 7 a 14 dias de impressões é [PRATICANTE] (vidiq). Sem limiar oficial |
| 28 dias | Comparação com os outros vídeos do canal, na mesma janela | Comparar com vídeos lidos em outro período sem ajuste | [INFERÊNCIA] Mesma janela da audiência mensal do Studio |
| 90 dias | Resultado: tempo de exibição, novos espectadores | Estimar cauda de longo prazo | [LACUNA] A Ajuda diz que o sistema usa dados recentes, mas não por quanto tempo |

[INFERÊNCIA] Nas primeiras semanas, um vídeo pode estar sendo testado em audiências diferentes. Por isso a primeira leitura de CTR tende a ser instável.

### 7.3 Ordem de leitura

1. **Origem e volume.** Se as impressões forem insuficientes, pare. Não leia CTR.
2. **CTR por origem**, comparado com a referência interna: os 10 vídeos recentes de duração semelhante, na mesma origem. [INFERÊNCIA] Adoto a convenção do Studio para comparar.
3. **Intro (30 s)**, com a mesma referência.
4. **Curva.** Encontre os dois ou três minutos de maior queda e os picos e top moments.
5. **AVD em minutos e APV calculado**, comparados a vídeos de duração semelhante.
6. **Resultado.** Visualizações (com as quebras anotadas), tempo de exibição, novos versus regulares.
7. **Reações públicas** (likes, comentários), como proxies e nunca como prova.

Os limiares de "alvo" e "abaixo" são definidos por você, a partir da própria série. Nenhuma fonte oficial os fornece. [LACUNA]

### 7.4 Combinações de sinais

| Combinação (relativa à referência interna) | Leitura sugerida | Ação | Condição e contraindicação |
|---|---|---|---|
| CTR, intro e AVD no alvo | Embalagem e promessa alinhadas | Manter; não mexer no que funciona | Não prova qualidade. Confirme volume e origem [INFERÊNCIA] |
| CTR acima, intro abaixo, AVD abaixo | Assinatura de clickbait da Ajuda: promessa maior que o conteúdo | Reduzir a promessa de título e miniatura, ou cumpri-la nos primeiros 30 s. Não trocar só a miniatura | Ajuda 7628154 (heurística). Não há limiar oficial de "abaixo" |
| CTR abaixo, intro no alvo ou acima, AVD no alvo ou acima | Conteúdo retém quem chega. O gargalo é embalagem ou origem | Verificar a origem. Testar miniatura com teste nativo | Contraindicação: se a maior parte das impressões vier da Página inicial, CTR baixo pode ser esperado (Ajuda 7628154) |
| CTR abaixo, intro abaixo | Abertura e embalagem não funcionam juntas, ou a origem é desfavorável | Revisar a abertura primeiro; depois a embalagem | Confirmar origem antes de concluir |
| Intro no alvo; queda concentrada em um minuto | Problema localizado no trecho | Ouvir o trecho antes da queda; revisar o que muda ali: tema, ritmo, transição | A Ajuda recomenda revisar, sem dizer o motivo. [INFERÊNCIA] A queda pode ter causa externa ao vídeo |
| Pico isolado em um trecho | Trecho valorizado, ou trecho confuso que foi reassistido | Ouvir o trecho: se houve confusão, reescrever; se houve valorização, repetir o formato | A Ajuda dá as duas leituras; a escolha depende de você |
| Visualizações sobem; AVD cai | Mais exposição sem permanência | Checar a origem: Página inicial, Up Next ou busca? | [INFERÊNCIA] Se houve quebra de contagem na janela, a subida pode ser de contagem |
| Tempo de exibição sobe; AVD estável | Crescimento de distribuição com retenção estável | Manter e monitorar | Confirmar que não há quebra de contagem na janela |
| Tempo de exibição alto; novos baixos; regulares altos | Audiência fiel, pouca descoberta | Séries e playlists que levem a vídeos novos (Ajuda 16533387) | [INFERÊNCIA] Faixa de "regular" não definida: use com cautela |

### 7.5 Se for testar embalagem

- Use o teste nativo do Studio, não trocas manuais. [OFICIAL] Ajuda 7628154.
- Segundo terceiros (via terceiros, trecho), o teste escolhe a versão vencedora pelo tempo assistido por impressão, não pelo CTR. Não confirmei o desenho do teste na Ajuda. [OFICIAL, via terceiros]
- Restrições relatadas por terceiros (via terceiros): o teste não está disponível para vídeos feitos para crianças (Made for Kids), conteúdo para público adulto e vídeos privados. Se o seu canal se encaixa nessas categorias, o teste não serve.
- Condição: volume suficiente. A Ajuda não define significância nem tamanho de amostra. Defina o limiar com testes próprios. [INFERÊNCIA]
- Contraindicação: variação pequena não pede ação. Registre, repita e só troque se a diferença se sustentar. [OFICIAL] Ajuda 7628154.

---

## 8. Mitos que as fontes oficiais desmentem

| Mito | O que a fonte oficial diz | Fonte e etiqueta | Uso prático |
|---|---|---|---|
| "CTR alto indica vídeo bom." | CTR depende de origem, público e posição. CTR alto com AVD baixa é assinatura de clickbait, recomendado com menos frequência. | Ajuda 7628154 [OFICIAL] | Leia CTR junto com intro e AVD |
| "O YouTube recomenda pelo clique." | Clicar não garante que o vídeo foi assistido. O watch time entrou em 2012. | Goodrow, 2021 [OFICIAL] | Meça retenção, não só clique |
| "Existe uma fórmula com pesos que dá para aplicar." | Não há fórmula fixa. A importância de cada sinal depende do espectador. Pesos não são publicados. | Goodrow, 2021 [OFICIAL]; Ajuda 16533387 | Não planeje com pesos de blog |
| "AVD é tempo total dividido pelas visualizações." | A Ajuda diz "entre quem ficou para assistir", calculada a partir de engaged views. | Ajuda 9313698 (trecho), 9314415 [OFICIAL]. O denominador é inferência | Use a base oficial. Não use a fórmula de terceiro |
| "Dá para testar miniatura trocando à mão." | Trocas manuais confundem a leitura, e a diferença pode vir da origem. | Ajuda 7628154 [OFICIAL] | Use o teste nativo, com as condições da seção 7.5 |
| "Views de antes e depois são comparáveis." | A contagem mudou: primeiro frame em long-form (24/08/2026) e co-views (novembro de 2026). | Ajuda 12220281 (lida, truncada); 2991785 (trecho) [OFICIAL] | Anote as quebras e não compare sem ajuste |
| "O YouTube recomenda uma duração ideal." | Não há declaração oficial recente sobre duração no ranqueamento. O princípio declarado é "tão longo quanto precisar". | Beaupré, VidCon 2022 (via TechCrunch) [OFICIAL] | Decida a duração pela retenção do próprio vídeo |
| "Hora de publicação é fator de desempenho de longo prazo." | Não verificado: a redação da Ajuda 16533387 não foi confirmada na leitura, e por isso o item não é desmentido. | Ajuda 16533387 [LACUNA] | Não planeje em torno de horário com base em blog |

---

## 9. Lacunas e limites

### 9.1 O que não foi possível verificar

- **Pesos, objetivos e fórmula atuais** de qualquer sinal, para qualquer formato. Não publicados.
- **Duração no ranqueamento.** Nenhuma fonte primária que li trata disso.
- **Sinais por superfície** no sistema atual. Não há fonte oficial.
- **Pesquisas de satisfação:** escala, frequência, taxa de resposta, amostragem e se existe agregado visível ao criador.
- **APV:** definição oficial. A leitura da Ajuda 12220281 foi truncada antes da tabela de métricas. O campo de co-view rate também está nessa parte. Confirme antes de usar.
- **Rótulos "absoluta" e "relativa"** da curva de retenção, como o Studio os apresenta.
- **Engaged view em long-form.** A definição não foi encontrada.
- **Co-views** no CTR, na AVD e na retenção. Não sei se entram. Também não sei o método do estimador.
- **Retroatividade** da mudança de contagem (ver 9.2).
- **Significância estatística** e tamanho de amostra para julgar mudança de CTR. A Ajuda não define.
- **Benchmarks oficiais** de CTR (além da descrição de distribuição), de retenção e de AVD. Não existem nas fontes que li.
- **Cauda de longo prazo.** Quanto tempo um vídeo longo continua recebendo impressões.
- **Casos reais.** Não encontrei, no material, nenhum vídeo, canal ou minuto com curva real. Os exemplos com números são construídos. O único exemplo oficial, do café, não traz resultado. O exemplo de watch-next (Figura 4 de Zhao et al.) ilustra a superfície.
- **Texto integral** de Covington et al. (2016, lido em cópia pública), Chen et al. (2019, só resumo e trechos), arXiv 2206.06003 (não lido) e Zhao et al. (2019, cópia pública).
- **Creator Insider de 01/09/2026:** não aberto. Todas as afirmações de 2026 sobre ranqueamento por espectador dependem dele.
- **Estudo de clickbait e satisfação** (n=21): autores e ano não identificados no material.
- **Dados brasileiros.** Não encontrei. A Nielsen é dos EUA.

### 9.2 Divergências em aberto e o que fazer

| Tema | Uma versão | Outra versão | O que fazer enquanto não se resolve |
|---|---|---|---|
| Satisfação versus watch time em 2026 | Blogs de terceiros (milx, dataslayer): satisfação superou o watch time | Outros terceiros (outlierkit, onetube): nenhuma mudança oficial verificada. Ajuda: satisfação "além" do tempo | Usar a Ajuda: complemento. Não planejar em torno de troca de peso |
| Escala das pesquisas de satisfação | Blog de 2021 (lido pela unidade 1): 1 a 5 estrelas, 4 e 5 contam | Ajudas 16559650 e 16089387 (unidade 3): escala não informada | Reler o blog de 2021 antes de citar. Não atribuir a escala à Ajuda |
| Reformulação do Browse em fevereiro de 2026 | Terceiros (dataslayer, milx, weaveaura, socialpilot) falam em "clusters de histórico". Um deles diz que o YouTube confirmou | Terceiro (gleam.fit) afirma que o log oficial de atualizações até 29/08/2026 não tem entrada de Browse | Não usar como premissa |
| Dimensões que alteram os pesos | outlierkit: espectador e dispositivo | ppc.land: pessoas, superfícies e momentos. Air.io: espectador e momento | Não usar. A Ajuda diz só que depende do espectador |
| Sinais por superfície | Listas de terceiros (tinymedialab, weaveaura) | Ajuda: sinais diferentes, sem lista | Prevalece a Ajuda |
| Separação de Shorts e long-form | dataslayer: separação formal | postigniter: desacoplamento no fim de 2025. Sem fonte primária | Fora do escopo, mas pode afetar o Browse de long-form. Não usar |
| Data do primeiro frame | Ajuda 2991785, versão en-GB em cache (trecho), e Creator Insider via ppc.land: 24/08/2026 | Versão da Ajuda que li: sem data | Usar 24/08/2026 como data de trabalho, marcada como não confirmada |
| Data dos co-views | Ajuda: "novembro de 2026". Cobertura: 16/11/2026 | Cobertura de 17/11/2026: "rolling out now" | Registrar "novembro de 2026 (dia não confirmado)" |
| Retroatividade dos co-views | mediaweek: só novas visualizações em TV | sprizzy: não diz se reprocessamentos foram recontados | Não assumir. Guardar snapshots |
| Piso de 30 s antes de 24/08/2026 | Terceiros (chewbr; relatos citados pela unidade 2) | Ajuda que li: não menciona piso | Não usar como fato |
| Segmento "recorrentes" | Ajuda 9314415 fala em novos versus recorrentes | Ajuda 9314416 lista novos, casuais, regulares e também recorrentes | Usar novos, casuais e regulares. Não comparar com séries antigas de "recorrentes" |
| Nome da área no Studio | Ajuda 9314486: "Analytics" | Ajuda 12220281: "Insights". Terceiro diz que foi renomeada em 13/11/2026 | Usar o nome que aparece na sua conta |
| Benchmarks de retenção e APV | 30% (guia); 40% a 60% (guias); 23,7% (relatório citado por gyre) | Nenhum oficial | Não usar como alvo. Comparar com o próprio canal |
| CTR de inscritos "perto de 10%" | Terceiros (outlierkit; ppc.land) | Mesma entrevista; não confirmado | Não usar |

### 9.3 Limites de generalização

- Quase todas as fontes técnicas são de 2016 a 2019 e não separam por duração. O ganho de 2019 é relativo, em um sistema de 2019, e não se aplica automaticamente a 2026.
- As afirmações sobre 2026 vêm de cobertura de terceiros, não de primárias. Qualquer uso precisa de verificação.
- A regra de clickbait da Ajuda é heurística agregada. Não se aplica a um vídeo isolado como diagnóstico definitivo.
- Os exemplos com números são construídos e servem para ilustrar mecanismos, não para estimar efeitos.

### 9.4 Próximos passos de verificação, em ordem

1. Transcrever o Creator Insider de 01/09/2026 (https://www.youtube.com/watch?v=rHLjxrbXmmY) antes de usar qualquer afirmação de 2026 sobre ranqueamento.
2. Reler a Ajuda 12220281 na tabela de métricas e confirmar a fórmula do co-view rate e a definição de APV, se houver.
3. Reler o blog de 2021 e confirmar a escala de 1 a 5 estrelas.
4. Confirmar, na Ajuda atual, a data do primeiro frame e a data de início dos co-views.
5. Guardar snapshots datados de três a cinco vídeos de referência durante duas semanas, para medir se as quebras de contagem afetaram os números. [INFERÊNCIA]
6. Fora de escopo para decisão de roteiro: as regras de monetização (8.000 horas qualificadas em 365 dias, a partir de 01/02/2027, segundo TechCrunch, 10/08/2026) não são sinal de recomendação.

---

## Fontes

| Código | Fonte | URL | Como foi usada |
|---|---|---|---|
| Ajuda 16533387 | YouTube's Recommendation System (Sistema de recomendação do YouTube) | https://support.google.com/youtube/answer/16533387?hl=en | Lida. Sem data visível |
| Ajuda 16559650 | Understand your content performance for YouTube's recommendation system | https://support.google.com/youtube/answer/16559650?hl=en | Lida (unidade 3) |
| Ajuda 16089387 | How YouTube recommendations work | https://support.google.com/youtube/answer/16089387?hl=en | Lida (unidade 3) |
| Ajuda 16559651 | Good to know about recommendations | https://support.google.com/youtube/answer/16559651?hl=en | Trecho |
| Ajuda 9314355 | Understand your YouTube video reach | https://support.google.com/youtube/answer/9314355?hl=en | Lida |
| Ajuda 9314486 | Impressões e watch time (Analytics) | https://support.google.com/youtube/answer/9314486?hl=en | Lida |
| Ajuda 7628154 | Impressions and click-through rate FAQ | https://support.google.com/youtube/answer/7628154?hl=en e https://support.google.com/youtubecreatorstudio/answer/7628154?hl=en-GB | Lida (en e en-GB) |
| Ajuda 9314415 | Measure key moments for audience retention | https://support.google.com/youtube/answer/9314415?hl=en | Lida |
| Ajuda 9314416 | Understand your YouTube audience | https://support.google.com/youtube/answer/9314416?hl=en | Lida |
| Ajuda 12220281 | Understand your YouTube content performance | https://support.google.com/youtube/answer/12220281?hl=en | Lida até a tabela de métricas (truncada) |
| Ajuda 2991785 | How engagement metrics are counted | https://support.google.com/youtube/answer/2991785?hl=en-cu | Trecho. Versão en-GB em cache cita 24/08/2026 |
| Ajuda 9313698 | Understand your YouTube engagement | https://support.google.com/youtube/answer/9313698?hl=en | Trecho (AVD e tempo de exibição) |
| Ajuda 2375431 | About YouTube ads and view metrics | https://support.google.com/youtube/answer/2375431?hl=en | Trecho (engaged views e co-view rate) |
| Goodrow, 2021 | On YouTube's recommendation system | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | Lido (15/09/2021) |
| Blog "Continuing our work…" | Continuing our work to improve recommendations on YouTube | https://blog.youtube/news-and-events/continuing-our-work-to-improve/ | Trecho. Data não confirmada |
| Zhao et al., 2019 | Recommending What Video to Watch Next: A Multitask Ranking System. DOI 10.1145/3298689.3346997 | Cópia pública: https://daiwk.github.io/assets/youtube-multitask.pdf | Lido (cópia) |
| Covington et al., 2016 | Deep Neural Networks for YouTube Recommendations. DOI 10.1145/2959100.2959190 | Cópia pública: https://cseweb.ucsd.edu/classes/fa17/cse291-b/reading/p191-covington.pdf | Lido (unidade 3) |
| Chen et al., 2019 | Top-K Off-Policy Correction for a REINFORCE Recommender System | https://arxiv.org/html/1812.02353.pdf | Trecho |
| arXiv 2206.06003 (2022) | Deconfounding Duration Bias in Watch-time Prediction for Video Recommendation | https://arxiv.org/pdf/2206.06003 | Trecho. Não lido integralmente |
| Beaupré, VidCon 2022 | Cobertura do TechCrunch, 24/06/2022 | https://techcrunch.com/2022/06/24/mrbeast-explain-algorithm-youtube-vidcon/ | Via terceiros |
| Creator Insider, 01/09/2026 | YouTube Algorithm 2026 - What Creators Need to Know | https://www.youtube.com/watch?v=rHLjxrbXmmY | Não aberto |
| Cobertura de co-views | ppc.land, Creator Insider e co-views | https://ppc.land/youtube-adds-estimated-tv-co-viewers-to-public-view-counts/ | Via terceiros |
| Monetização, 10/08/2026 | TechCrunch | https://techcrunch.com/2026/08/10/youtube-now-requires-creators-to-have-twice-as-many-watch-hours-to-start-earning-money/ | Via imprensa. Fora do escopo de decisão |
| Nielsen, agosto de 2026 | Release de TV viewing | https://www.nielsen.com/news-center/2026/tv-viewing-cools-off-in-nielsens-august-gauge-reports-as-sports-take-a-breather-and-school-resumes/ | Trecho. Dados dos EUA |
| Estudo de clickbait | Viewer Responses to Clickbait on YouTube: A Marketing Perspective | https://www.researchgate.net/publication/395261047_Viewer_Responses_to_Clickbait_on_YouTube_A_Marketing_Perspective | Trecho. Autores não identificados |
| Terceiros (só divergência ou hipótese) | vidiq, gyre, air.io, prepublish.ai, tinymedialab, weaveaura, outlierkit, gleam.fit, dataslayer, milx, onetube, postigniter, sprizzy, mediaweek, chewbr, PhoneArena | Ver seção 9.2 | Não são prova |

---
## Adendo da revisão
**Achados novos das reinvestigações (com etiqueta).** **Data do primeiro frame:** [OFICIAL] blog do YouTube de 19/08/2026 (lido) e histórico de revisões da Analytics API de 27/08/2026 (trecho) dizem que a view conta desde o primeiro frame a partir de 24/08/2026, e que a definição antiga virou engaged view. **Separação por origem:** [OFICIAL] a Reporting API tem channel_reach_combined_a1, com CTR de miniatura e impressões por tipo de origem, e channel_reports, com AVD e engaged views por tipo de origem (snippets; relatórios em massa, não tela). [OFICIAL] a Ajuda 12220281 não descreve CTR ou AVD por origem na tela. [PRATICANTE] terceiros dizem que a divisão existe no Reach e em Advanced Mode, sem captura; não validado. A tabela de origem da Analytics API conflita quanto a AVD (A6), não resolvido. **CTR e engaged views:** [OFICIAL] o blog de 19/08/2026 diz que CTR, AVD e retenção seguem ancorados em engaged views; a Ajuda define CTR por quem assistiu após ver a miniatura. Conflito não resolvido; testar. **Co-views:** conflito sobre o efeito em CTR, AVD e watch time. [PRATICANTE] NetInfluencer, citando Creator Insider, diz que CTR e AVD não mudam e que o watch time inclui co-views; peggyktc diz que o watch time é afetado; a versão Android da Ajuda diz que o watch time inclui co-views. [INFERÊNCIA] a AVD pode mudar mecanicamente em vídeos vistos na TV; testar separando TV antes e depois do corte. **Exemplo construído (não é dado real):** vídeo de 30 min, 1.000 views públicas, 600 engaged views e 5.400 min de watch time dão AVD de 9,0 min pela definição oficial, contra 5,4 min pela conta de views totais. **Latência:** [OFICIAL, snippet da Ajuda do Google Ads em zh-Hant] dados de origem chegam com atraso de 48 a 72 horas; regra provisória, fora do contexto de vídeo orgânico. **Ainda em aberto:** tela do Studio por origem; reconciliação entre API e Studio; limiar em segundos da engaged view; sentido de loops em vídeo longo; efeito dos co-views no CTR e na AVD; benchmarks de origem (excluídos por serem de terceiros).

## Registro de revisão
Foram feitas 12 alterações. Procedem os apontamentos 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12 da auditoria. Em 7 e 6, a f2 confirmou que a AVD usa engaged views na Ajuda 9313698 aberta; por isso a alteração corrige a seção 6 (contradição interna) e não remove o termo. A alteração 4 e a 5 trocam a lacuna sobre engaged views por uma definição geral oficial, mantendo como lacuna o limiar em segundos. A data de 24/08/2026 foi mantida, mas com a fonte oficial descrita (blog de 19/08 e API de 27/08), pois a f2 a encontrou em fonte primária. Não se mudou o apontamento sobre o formato do ganho de Zhao et al., que foi só contextualizado. Em aberto: captura do Studio por origem, retroatividade dos co-views, limiar em segundos, sentido de loops, e o dia 16/11/2026 (sem Ajuda aberta). O apontamento sobre CTR e co-views não foi alterado no texto por falta de fonte consistente; a inserção fica no adendo.

Correções aplicadas ao texto: 11.

### Correções propostas e não aplicadas automaticamente
O trecho original não foi localizado de forma única no documento; a correção vale, mas precisa ser aplicada à mão.

- Onde se lê: "[INFERÊNCIA] Se a descrição de 2021 ainda vale, 25 minutos assistidos com nota 3 não geram crédito de valued watchtime."
  Leia-se: "[INFERÊNCIA] Se a descrição de 2021 ainda vale, respostas abaixo de 4 não entram como tempo valorizado. A escala de 1 a 5 estrelas ainda precisa ser confirmada na fonte primária antes de citar."
  Motivo: O exemplo numérico depende de uma escala que não foi confirmada na Ajuda. A conclusão fica condicionada.
