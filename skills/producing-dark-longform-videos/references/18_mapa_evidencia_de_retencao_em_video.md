# Retenção e engajamento em vídeo: a evidência do YouTube

> Mapa temático da biblioteca de livros e artigos (27 obras lidas por agentes). Livro de autor é `[PRATICANTE]`; estudo que o livro cita é `[ESTUDO citado pelo autor]`, não verificado pelo projeto; artigo lido na íntegra é `[ESTUDO]`.

# Mapa temático: Retenção e engajamento em vídeo, a evidência do YouTube

**Recorte.** O que os estudos com dados do YouTube mostram sobre duração, proporção assistida, retenção relativa e engajamento; o que a documentação oficial define; e o que isso autoriza ou não sobre um vídeo de 30 minutos.

**Fontes desta leitura (todas com dados ou com definição oficial):**
- [ESTUDO] Park, Naaman & Berger (2016), *A Data-driven Study of View Duration on YouTube* (ICWSM'16). Observacional e correlacional. Amostra Random: 1.125 vídeos. Amostra Individual: 189 participantes com extensão de navegador (número divergente nas notas; em outra seção aparece 158), 1.814 sessões após filtros. Data de coleta não consta; pelas referências citadas, deve ser 2015–2016 [INFERÊNCIA].
- [ESTUDO] Wu, Rizoiu & Xie (2017/2018), *Beyond Views* (arXiv:1709.02541). Observacional. 5.331.204 vídeos publicados em jul–ago de 2016, coletados por menções em tweets. Não é amostra aleatória do YouTube. Mediana de duração 5 min, média 12 min.
- [ESTUDO] Bassolas et al. (2025), preprint arXiv:2511.16497. Dois componentes: observacional (2.108 vídeos em espanhol, sobre transição energética) e experimental (dois canais espelho, *Euro al Joule* e *eur2j*, com 15 vídeos completos promovidos por canal, de 1 a 2 min). **As curvas não foram vistas nesta leitura; só o texto.** Trate qualquer número de retenção daqui como relato do autor.
- [OFICIAL] YouTube Help, *Measure key moments for audience retention* (support.google.com/youtube/answer/9314415). Sem data. Não traz dados. Define métricas e descreve a interface.

**Fora do recorte:** Berger & Milkman (2012), sobre compartilhamento de artigos do NYT; van Laer et al. (2014, 2019) e Green & Appel (2024), sobre transporte e persuasão; Kane, Eyal e Berger, em livro, que são [PRATICANTE] quando tratam de métricas de plataforma.

**Limite geral.** Nenhuma das quatro fontes publica a curva por minuto de um vídeo longo. Nenhuma mede um vídeo de 30 minutos. Park inclui vídeos de até cerca de 4 horas, mas só como variável contínua. Bassolas mede retenção só em vídeos de 1 a 2 min.

---

## 1. O que as obras dizem em comum

**P1. A proporção média assistida cai com a duração, entre vídeos.**
- Park et al. (2016): coeficiente padronizado de −0,146 (Random) e −0,123 (Individual), ambos com p < 0,001. A duração é, segundo os autores, o controle mais forte. [ESTUDO]
- Wu et al. (2017/2018): a duração sozinha explica mais de 58% da variância de µ̄30 (proporção média assistida em 30 dias). [ESTUDO]
- Apoio: duas amostras diferentes, duas métricas parecidas (Park: AVD dividido pela duração; Wu: tempo médio dividido pela duração), mesma direção.
- Limite: a queda é entre vídeos, não dentro de um vídeo. Nenhuma das duas fontes diz qual duração é boa. A faixa de 30 a 60 min não é reportada separadamente. [INFERÊNCIA] A queda pode refletir um limite de atenção em minutos absolutos; os estudos não separam essa hipótese de outras.

**P2. Compare dentro da faixa de duração, não pela proporção bruta.**
- Wu et al.: η̄ é o percentil do vídeo dentro da sua faixa de duração (escala log, 1.000 faixas; faixas com menos de 50 vídeos são fundidas às vizinhas). [ESTUDO]
- Bassolas et al.: "relative retention performance", que compara a retenção do vídeo com a de vídeos de duração semelhante (0,5 = metade dos vídeos de duração semelhante retém melhor). O autor afirma que a métrica "lava" o efeito da duração. A definição vem de documentação do Google não verificada aqui. [ESTUDO, definição não verificada]
- YouTube Help: "typical retention" compara com os 10 vídeos mais recentes de "similar length"; "SEE MORE" compara com todos os vídeos de duração semelhante. [OFICIAL] A faixa de "similar length" não é definida.
- Apoio: três fontes, uma oficial, com método convergente. Nenhuma mostra que o método melhora alguma decisão. É um procedimento de comparação, não um efeito.

**P3. Volume de views não mede proporção assistida.**
- Wu et al.: correlação de Spearman entre o ranking por views e o ranking por tempo assistido: ρ = 0,48 com n = 50, e ρ = 0,08 com n = 500. Por categoria: música ρ = 0,80 e notícias ρ = −0,34 (n = 100 cada). [ESTUDO]
- Park et al.: log de views com coeficiente +0,026 (Random) e +0,045 (Individual). Efeito pequeno. [ESTUDO]
- YouTube Help: a soma das views por segmento pode superar o total de views, porque o mesmo espectador reassiste trechos. [OFICIAL]
- Limite: nenhum dos três mede qualidade narrativa. Views são volume de exposição.

**P4. Nenhuma fonte pública tem curva intravídeo de vídeo longo.**
- Park: média por vídeo. Wu: séries diárias, por dia de vida do vídeo, não por minuto. Bassolas: fração do vídeo (time ratio), mas só em vídeos de 1 a 2 min e sem curvas vistas aqui. YouTube Help: descreve o gráfico, sem dados. [ESTUDO; OFICIAL]
- Consequência: qualquer leitura de "onde o público sai" em um vídeo de 30 min vem da curva do próprio canal. [INFERÊNCIA]

**P5. Nenhum dos estudos estabelece causa.**
- Park et al. dizem, literalmente, que o efeito da qualidade real do vídeo "não é evidente nos dados" (tradução minha). [ESTUDO]
- Wu et al. tratam a relação como correlação. A qualidade é medida por proxy (rankings da indústria, lista de canais de notícias). [ESTUDO]
- Bassolas et al. declaram que o narrador é confundidor: o canal conversacional tinha um narrador com "well-developed interpretative and communication abilities". [ESTUDO]

---

## 2. Onde os autores divergem, e o que fazer enquanto isso não se resolve

**D1. Qual janela de abertura conta.**
- YouTube Help: a Intro é a porcentagem de público que ainda assiste após 30 s. É a única janela de tempo definida na documentação. [OFICIAL]
- Bassolas et al.: a diferença de retenção aparece entre 1 e 4 s, em vídeo de cerca de 1 min. [ESTUDO]
- Kane (2019?, livro): regra dos três segundos, vinda de métrica de feed social. [PRATICANTE]
- Leitura: não é divergência de evidência, e sim de escopo. Para vídeo longo, a referência oficial é a Intro de 30 s. As janelas de 1 a 4 s e de 3 s não transportam. Para 60 e 90 s, não há fonte: é processo do projeto (base 01 §1, item 3).

**D2. Categoria muda a relação entre views e tempo assistido?**
- Wu et al. encontram sinal oposto entre música (ρ = 0,80) e notícias (ρ = −0,34). Categoria é autodeclarada.
- Park et al. tratam categoria só como efeito aleatório. Os coeficientes por categoria não aparecem no trecho lido. Há apenas a direção: no Individual, Comedy, Entertainment, People & Blogs, Film & Animation e Gaming aparecem com tempo maior que Auto & Vehicle, sem valores.
- O que fazer: não comparar proporção assistida entre séries de temas diferentes sem separar por tema. No canal, analisar séries separadas. Não concluir que um tema "retém mais" sem número de vídeos por tema.

**D3. Proporção bruta cai com a duração, mas a métrica relativa "lava" a duração?**
- Park et al. e Wu et al. mostram que a proporção bruta cai com a duração.
- Bassolas et al. afirmam que a retenção relativa à faixa remove o efeito da duração.
- Não é contradição. São duas métricas. A bruta depende da duração por construção. A relativa é comparada dentro de faixas de duração parecida, então não tem tendência de duração por construção.
- O que fazer: nomear a métrica em cada leitura. Comparar vídeos de faixa parecida com a métrica relativa. Usar a proporção bruta só quando a faixa for a mesma. Nunca comparar a bruta entre faixas diferentes.

**D4. Peso da duração.** Park et al. chamam a duração de "controle mais forte" (coeficiente padronizado) e Wu et al. de "principal preditor" (variância explicada). A direção é a mesma, mas as unidades não são comparáveis: o desvio-padrão do log da duração não consta nas notas. Não somar nem comparar as magnitudes.

**D5. Tom e sentimento.** Park et al. encontram associação pequena entre sentimento negativo nos comentários e proporção assistida maior (+0,019 e +0,022). Bassolas et al. encontram correlação de −0,11 entre formalidade da narração e comentários. As variáveis são diferentes: uma mede comentários, a outra mede a narração. Nenhuma sustenta mudar o tom de um vídeo. Tratar como hipótese (ver §7).

---

## 3. Técnicas por etapa do pipeline

Formato: o que é; fonte; como aplicar em vídeo de 30 min de canal dark; rótulo de transferência; contraindicação.

**Ideia.** Nenhuma técnica de escolha de tema sai destas fontes. Não há dado sobre tema e retenção em vídeo longo, exceto a ressalva de D2.

**Pacote (título e miniatura) e Hook.**

**T1. Ler a Intro como única métrica oficial de abertura.**
- O que é: porcentagem do público que ainda assiste após 30 s. [OFICIAL, YouTube Help]
- Como aplicar: registrar a Intro de cada vídeo do canal, separada por origem de tráfego, antes de qualquer conclusão sobre abertura. Confirmar no Studio se o denominador é views ou audiência (a documentação não diz).
- Se a Intro estiver abaixo do esperado, então revise título e miniatura para que reflitam o conteúdo, e/ou revise os primeiros 30 s. [OFICIAL, recomendação da própria fonte]
- Se a Intro estiver alta, então isso "could mean" (pode significar) que a promessa foi cumprida. A fonte diz "could mean". Não é prova. [OFICIAL, limite do próprio texto]
- Rótulo: definição [OFICIAL]; uso como métrica primária de hook [ADAPTAÇÃO].
- Contraindicação: não há limiar oficial. Não fixe meta numérica. Não use 60 ou 90 s como janela oficial. Tráfego pago pode distorcer a Intro, porque o documento lista anúncios pulháveis como origem [INFERÊNCIA]: compare só dentro da mesma origem.

**T2. Auditoria de promessa pela Intro.** Combina T1 com o registro de promessas (base 09 §3.5). A leitura é: promessa sem pagamento nos primeiros 30 s tende a ser sinal de descolamento entre pacote e conteúdo. Rótulo: [ADAPTAÇÃO] com a recomendação oficial de T1. Contraindicação: a Intro baixa tem várias causas possíveis; o documento não as separa.

**Roteiro.**

**T3. Trecho de pico de reassistência (spike): ler o texto do minuto.**
- O que é: trecho em que mais espectadores assistem, reassistem ou compartilham. [OFICIAL]
- Como aplicar: quando houver spike, ler o texto do roteiro naquele minuto. Decidir entre duas leituras possíveis: interesse, ou trecho que o público precisou rever. A própria documentação admite a segunda: "seu conteúdo não está claro e o público precisou reassistir uma seção" (tradução minha). Um critério de decisão, aplicado ao texto: o trecho tem nomes, datas ou números introduzidos sem contexto?
- Se houver spike sem explicação, então trate como candidato a trecho pouco claro, até provar o contrário. [ADAPTAÇÃO]
- Rótulo: duas leituras [OFICIAL]; procedimento de decisão [ADAPTAÇÃO].
- Contraindicação: não há critério oficial para escolher entre as leituras. Não trate spike como elogio automático.

**T4. Dip: cruzar com o texto, sem supor a causa.** O relatório junta "pulado" e "abandonado" no mesmo rótulo. Se houver dip, então cruze com o texto do minuto, mas registre que o relatório não separa pulo de saída. [OFICIAL + ADAPTAÇÃO]

**T5. Queda gradual como linha de base.** A documentação diz que vídeos "generally taper off" (tendem a cair ao longo da reprodução) e que tamanhos de audiência "typically decrease" ao longo do vídeo. Se a curva só cai gradualmente, então trate como linha de base esperada e procure os dips localizados. [OFICIAL, descrição sem medida]. Contraindicação: a fonte não diz quanto de queda é normal. Não converta "gradual" em número.

**T6. Mover o trecho mais forte para antes.** A documentação recomenda trazer o conteúdo mais forte para antes se ele estiver no fim do vídeo. [OFICIAL, recomendação sem medida]. O playbook trata a posição do clímax como aposta (base 01 §1, item 7). Contraindicação: o motivo dado é que audiências tendem a cair ao longo do vídeo, o que é um padrão observado e não causal. Mover um trecho pode quebrar a cronologia ou a causalidade do caso. Só testar com uma variável por vez (ver H6).

**Comparação de tratamento.**

**T7. Desenho de duas versões do mesmo trecho, não de dois vídeos.** Se a pergunta é sobre tom ou voz, então use o mesmo roteiro e o mesmo tema com duas versões da abertura, e não dois vídeos diferentes. Bassolas et al. usaram dois canais com temas e datas espelhados, mas o narrador variou, e o próprio estudo não isolou essa diferença. [ESTUDO, com limite declarado] Rótulo: desenho [ESTUDO]; aplicação a 30 min [INFERÊNCIA]. Contraindicação: 15 vídeos por canal, sem correção de comparações múltiplas e sem tamanho de efeito. Não basta para decidir nada.

**T8. Normalização por faixa de duração.** Se o canal tem vídeos de tamanhos diferentes, então agrupe por faixa de duração e compare só dentro da faixa, usando o percentil de Wu et al. (η̄). Se a faixa tiver menos de 50 vídeos, não calcule percentil; use a média da faixa como referência descritiva. O limite de 50 é do estudo de Wu, feito com milhões de vídeos; não está validado para canal pequeno. [ESTUDO para o método; ADAPTAÇÃO para o limite] Contraindicação: a faixa de duração não é o único fator; Wu et al. mostram que tópico e reputação do canal também pesam.

**Pós-publicação e diagnóstico.**

**T9. Proporção assistida = AVD ÷ duração, como referência interna.** Park et al. usam essa definição. O YouTube dá AVD em minutos, sem definir "engaged views", e não dá APV. [OFICIAL para AVD; ESTUDO para a razão] Como aplicar: calcular para cada vídeo do canal e comparar só dentro da faixa. Contraindicação: os interceptos de Park (49% e 66%) são de outra amostra e não servem de benchmark.

**T10. Sinais de comentário como monitoramento, não como alavanca.** Park et al. associam likes por view e sentimento dos comentários à proporção assistida, sem causalidade. Se o canal usar esses sinais, então registre-os como monitoramento e não os otimize diretamente. Otimizar pode produzir o efeito sem sustentação. [ESTUDO + INFERÊNCIA]

---

## 4. O que é evidência e o que é ofício

| Categoria | Fontes | Limite principal |
|---|---|---|
| Medição com dados do YouTube | Park et al. (2016); Wu et al. (2017/2018); Bassolas et al. (2025) | Amostras não aleatórias ou pequenas; anos antigos (2016); só Bassolas é recente, com n = 15 por canal |
| Definição e orientação oficial | YouTube Help 9314415 | Sem dados. As recomendações são [OFICIAL] como orientação, não como efeito medido |
| Inferência do sistema | Conversão de janelas em segundos (Bassolas); r² calculados; leitura do spike | Construções sobre as fontes, não achados delas |
| Praticante | Kane (regra de 3 s; 7–8 min e 15+ min de watch time; CTR de 10–30%); Eyal | Sem dados verificáveis; o próprio projeto já marca como não validado (base 03 §8.2) |
| Citado e não lido | van Kessel, Toor & Smith (2019), sobre YouTube; Schmälzle et al. (2022), sobre picos de engajamento; Appel & Mengelkamp (2022) | [ESTUDO citado pelo autor]. Só título. Schmälzle pode ser relevante para T3 (spikes); não usar antes de ler |

Por que Park, Wu e Bassolas são [ESTUDO] e não [DADO]: são artigos com método, e não dados publicados por um criador. Não há no corpus nenhum [DADO] de analytics de canal publicado com curva.

---

## 5. O que não transportar para vídeo longo

- **Bassolas et al.:** os vídeos são de 1 a 2 min, com versões de cerca de 20 s. A promoção paga (Google Ads) domina o alcance, mas isso é um vídeo de 1 a 2 min com público pago. A conversão para 28 a 84 s em um vídeo de 30 min é construção minha, não dado. Os 75% (versões breves assistidas até o fim) e 15% (completos) não são referência de retenção de vídeo longo. Também não usar "três ordens de magnitude", porque o próprio texto se contradiz: a Discussão diz três, e as tabelas dão cerca de uma.
- **Wu et al.:** amostra de tweets, portanto não aleatória. Mediana de 5 min. Categorias de música e notícias não representam canal dark. Os R² de previsão (0,04, 0,19 e 0,42) são de 2016 e não se transferem. O caso Smyth Radio (dois vídeos com título conspiratório, n = 2) é hipótese dos autores, não teste.
- **Park et al.:** os interceptos (49% e 66%) não são benchmark. "Dwell time" do Individual não é tempo de visualização, é aproximação. Amostra restrita a vídeos com ao menos 5 comentários em inglês. Participantes recrutados por TaskRabbit não são espectadores aleatórios.
- **YouTube Help:** "similar length" não tem faixa definida. Não há limiar para Top moment, Spike, Dip ou Intro alta/baixa. "Typical retention" mistura tema, época e formato. A recomendação de mover o trecho mais forte para antes não é efeito medido.
- **Kane:** regra de 3 s (métrica de feed social), watch time de 7–8 min e 15+ min, CTR de 10–30% atribuído a MrBeast via Muller. Não usar; a base já marca faixas de CTR como números que circulam (base 03 §8.2).
- **Berger & Milkman (2012):** mede entrada em lista de artigos do NYT, não permanência. Não é retenção.
- **Shorts:** nenhuma das fontes diz que vale para Shorts. A documentação não restringe formato, e a leitura para vídeo longo é [ADAPTAÇÃO]. Bassolas tem versão vertical, mas não há dado sobre ela aqui.

---

## 6. Relação com a base

**Limite desta comparação.** Recebi o índice dos documentos 01 a 10, o Master Playbook §1 e a skill. Não li o texto das seções, exceto as do Playbook e da skill. Os pontos abaixo, exceto os que citam o Playbook e a skill, precisam ser conferidos na seção indicada.

**Confirma:**
- **01 §1, item 3:** a Intro de 30 s é a única métrica oficial de abertura, sem limiar. Confirmado por YouTube Help 9314415 [OFICIAL].
- **01 §1, item 6 e 08 §7.3:** as quebras de contagem devem ser anotadas. A documentação confirma que os números por segmento podem superar o total de views. A ordem de leitura é do projeto; a plataforma não a descreve.
- **01 §1, item 7:** não há receita de duração. Park e Wu descrevem médias e associações, não uma duração-alvo.
- **04 §1 e 04 §2.1:** a documentação descreve flat, queda gradual, spike e dip, e não dá critério para spike ambíguo. A conferir: se 04 §1.2 já trata a ambiguidade do spike, a fonte apenas a confirma.
- **08 §5 (CTR alto nem sempre é melhor):** Wu et al. mostram divergência entre views e tempo assistido (Fig. 1, três canais de 128 vídeos em 30 dias). É ilustração do estudo, não prova geral.
- **08 §2 e 03 §8 (origem de tráfego):** a documentação segmenta por origem; Bassolas mostra que promoção paga domina o alcance. Confirma origem como condição de leitura.
- **10 §1.5 (tema versus tratamento):** o typical retention e o desenho espelhado de Bassolas confundem esses dois fatores. Confirma.
- **10 §4.5 (poder):** n = 15 por canal em Bassolas e a falta de cálculo de potência. Confirma.
- **06 §8 (diferenças por idioma e nicho):** Bassolas é em espanhol e Park exige comentários em inglês. A conferir na seção.

**Acrescenta:**
- A definição de proporção assistida (AVD ÷ duração), com a ressalva de que a associação é entre vídeos, não dentro deles.
- O limite de 50 vídeos por faixa, como parâmetro de Wu, a validar no canal.
- O procedimento para spikes (T3), a partir das duas leituras que a documentação admite.
- O cuidado de tratar AVD como métrica que depende de "engaged views" não definido (a conferir em 08 §4).

**Tensiona:**
- A recomendação oficial de mover o trecho mais forte para antes (T6) é de autoridade, mas sem medida. Não muda o status de aposta (base 01 §1, item 7; 06 §4.3). Autoridade de plataforma não é efeito medido.

**Contradição direta:** não identifiquei nas seções que tenho acesso. Pendências para conferir: 07 §5.6 (Bassolas é fonte lida em parte, com figuras não vistas) e 07 §3.3 (transporte e retenção), se a biblioteca citar algum dos quatro estudos por fonte secundária.

---

## 7. Hipóteses a testar com a curva do canal

Cada hipótese traz o que a fonte sugere, a métrica primária, a condição e o limite. Definir o critério de decisão antes da publicação (base 10 §1.2 e §1.3).

**H1. A Intro de vídeos com promessa cumprida é maior que a de vídeos com promessa descolada?**
- Fonte: YouTube Help (Intro alta "could mean" promessa cumprida).
- Métrica primária: Intro (30 s), na mesma origem de tráfego. Classificação prévia por auditoria de promessa (base 09 §3.5).
- Limite: a fonte não sustenta causalidade. Precisa de dezenas de vídeos para qualquer leitura.

**H2. Spikes de reassistência coincidem com trechos de maior densidade de informação nova (nomes, datas, números)?**
- Fonte: YouTube Help (segunda leitura de spike); Schmälzle et al. (2022), a ler.
- Métrica primária: proporção de spikes em trechos acima da média de densidade do roteiro.
- Limite: exige ao menos dez spikes identificáveis. A densidade é codificação do roteiro, com um avaliador só; precisa de dois.

**H3. A ordem dos vídeos por proporção bruta coincide com a ordem por proporção relativa à faixa?**
- Fonte: Wu et al. (concordância cai com o aumento de n); Bassolas et al. (métrica relativa).
- Métrica primária: correlação de ordem (Spearman) entre as duas leituras, no histórico do próprio canal.
- Limite: se a concordância for alta dentro de uma faixa, a diferença só aparece entre faixas. Use isso para decidir qual métrica usar em comparações.

**H4. A relação entre views e proporção assistida muda entre séries do mesmo canal?**
- Fonte: Wu et al. (sinal oposto por categoria).
- Métrica primária: Spearman entre views e proporção dentro de cada série.
- Limite: a série é uma categoria própria do canal, não uma categoria oficial. Com poucos vídeos por série, não conclua.

**H5. Registro coloquial na abertura retém mais nos primeiros 30 s do que registro formal, com o mesmo roteiro e a mesma voz?**
- Fonte: Bassolas et al. (desenho espelhado, com narrador confundidor).
- Desenho: duas gravações da mesma abertura, com a mesma voz, ritmo e edição, e não dois canais.
- Métrica primária: Intro (30 s). Secundária: curva de 30 a 90 s.
- Limite: a janela do estudo é de 1 a 4 s, em vídeo de 1 min. Qualquer efeito nos 30 s é resultado novo, não confirmação.

**H6. Mover o trecho mais forte para antes melhora a proporção assistida?**
- Fonte: YouTube Help (recomendação sem medida); base 01 §1, item 7 (aposta).
- Desenho: uma única variável (ordem dos blocos), no mesmo tema e na mesma estrutura de série. Duas versões do mesmo vídeo não bastam por causa da cronologia do caso.
- Métrica primária: proporção assistida (AVD ÷ duração). Secundária: Intro.
- Limite: com um vídeo por variante, tema e tratamento se confundem (base 10 §1.5). Pode ser inviável para canal pequeno.

**H7. A queda da proporção com a duração se reproduz dentro da faixa de 20 a 40 min do próprio canal?**
- Fonte: Park et al. e Wu et al. (queda entre vídeos, não dentro da faixa longa).
- Métrica primária: inclinação da proporção assistida em função da duração, dentro da faixa.
- Limite: exige muitos vídeos de faixa estreita. Pode não ser possível em canal novo.

**H8. A estabilidade de η̄ entre o dia 7 e o dia 30 vale para vídeo longo?**
- Fonte: Wu et al. (92,7% dentro de ±0,1 na população, majoritariamente curta).
- Métrica primária: diferença absoluta entre η̄ aos 7 e aos 30 dias, em vídeos de 20 a 60 min.
- Limite: a população do estudo é majoritariamente curta. Para vídeo longo, o resultado é novo. A documentação diz que o processamento leva 1 a 2 dias, o que limita leituras muito cedo.
