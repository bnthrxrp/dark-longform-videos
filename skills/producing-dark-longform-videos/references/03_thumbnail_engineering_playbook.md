# Thumbnail Engineering Playbook

# Thumbnail Engineering Playbook: canais dark, vídeos longos (10 a 60+ min)

**Data de referência:** 20/11/2026.

**Etiquetas:** [OFICIAL] documentação do YouTube/Google · [ESTUDO] artigo ou experimento, com autor e ano quando conhecidos · [DADO] número publicado ou medido, com fonte · [PRATICANTE] heurística de criador ou consultor, hipótese · [INFERÊNCIA] dedução minha a partir do material.

**Limite do corpus de vídeos:** todos os vídeos analisados estão acima da mediana do próprio canal, e não há curvas de retenção nem CTR por variante. Logo, o corpus não compara miniaturas fortes com fracas. Os casos abaixo ilustram mecanismos e tipos de relação. Não mostram que uma escolha causou o desempenho. As razões de outlier vêm do input e não foram verificadas.

**Chaves de fonte oficial** (todas lidas no material; prefixo https://www.)

| Chave | Documento |
|---|---|
| AJ-IMP | Regras de contagem de impressões: support.google.com/youtube/answer/9314486 |
| AJ-CTR | FAQ de impressões e CTR: support.google.com/youtube/answer/7628154 |
| AJ-ORIG | Performance de conteúdo e origens de tráfego: support.google.com/youtube/answer/12220281 |
| AJ-TESTE | Teste A/B de títulos e miniaturas: support.google.com/youtube/answer/16391400 |
| AJ-DICA | Dicas de títulos e miniaturas: support.google.com/youtube/answer/12340300 |
| AJ-POL | Política de miniaturas: support.google.com/youtube/answer/9229980 |
| BLOG-2019 | Post sobre recomendações e clickbait, 25/01/2019: blog.youtube/news-and-events/continuing-our-work-to-improve/ |

---

## 1. Modelo do clique

A miniatura (thumbnail) influencia o clique só depois de passar por três filtros. Cada um tem fonte e grau de evidência próprios.

### 1.1 Três filtros em sequência

**Filtro 1: exposição.** A miniatura só conta se for impressa: aparece por mais de 1 segundo e com pelo menos metade da área visível [OFICIAL, AJ-IMP]. Contam as superfícies de busca, início (inclusive autoplay), feeds (inscrições, Em alta, histórico, Assistir mais tarde), "Up Next" e playlists. Não contam embeds externos, cards e end screens dentro do player, e-mails, notificações e aba em segundo plano [OFICIAL, AJ-IMP].
[INFERÊNCIA] Um vídeo cujas impressões vêm sobretudo do início é lido por outro público, em outro contexto, do que um vídeo cujas impressões vêm de sugeridos. Qualquer leitura de miniatura começa separando as impressões por superfície.

**Filtro 2: leitura competitiva.** A miniatura concorre com outros vídeos na mesma superfície. A Central diz que a miniatura compete com outros vídeos em início, Up Next, busca e feeds de inscrições, e que o CTR varia conforme o local de exibição [OFICIAL, AJ-CTR].
Sobre a velocidade da leitura, o dado primário mais próximo é de laboratório. Crouzet, Kirchner e Thorpe (2010, *Journal of Vision* 10(4)), em tarefa de escolha sacádica entre dois alvos, registraram latência mínima de cerca de 110 ms para rostos, 120 ms para animais e 140 ms para veículos [ESTUDO]. Limite: imagens de 14°, dois alvos, medida de olhar; sem clique, sem feed, sem miniaturas reais.
Em anúncios impressos, Pieters e Wedel (2004, *Journal of Marketing* 68(2)), com eye tracking em 1.363 anúncios e mais de 3.600 consumidores, encontraram que o elemento pictórico capta atenção independentemente do tamanho, e o texto, em proporção ao seu tamanho [ESTUDO]. Transferir isso para miniatura de vídeo é [INFERÊNCIA].
Não encontrei tempo de decisão medido para miniatura de vídeo. O número de 1,8 segundo que circula é divergente (ver 1.4).

**Filtro 3: promessa crível e pagável.** Título e miniatura prometem algo. Duas regras oficiais limitam a promessa. Miniatura que faz o espectador esperar algo que não está no vídeo é proibida, com exceção caso a caso para contexto educativo, documental, científico ou artístico [OFICIAL, AJ-POL]. O sinal de clickbait é CTR alto com AVD baixo e impressões abaixo do esperado, e esses vídeos tendem a ser menos recomendados [OFICIAL, AJ-CTR].

### 1.2 O que decide o clique em cada contexto

**Superfícies**

| Contexto | Intenção do espectador | O que o material sustenta | Hipótese de decisão (não medida) | Lacuna |
|---|---|---|---|---|
| Início (Browse) | Sem intenção explícita. Mistura assinantes e público frio [INFERÊNCIA a partir de AJ-ORIG] | Início é superfície competitiva [OFICIAL, AJ-CTR]. CTR tende a ser menor onde há muitas impressões no início [OFICIAL, AJ-CTR] | Reconhecimento rápido do assunto e do formato do canal | Sem faixa oficial por origem |
| Sugeridos (Suggested / Up Next) | Já está num assunto e compara com vídeos do mesmo tema | Concorrência por superfície [OFICIAL, AJ-CTR]. Suggested inclui sugestões ao lado ou ao fim do vídeo e links da descrição [OFICIAL, AJ-ORIG] | A miniatura precisa mostrar em que este vídeo é diferente do que o espectador está assistindo [INFERÊNCIA] | Nenhuma fonte primária mede quais elementos ganham aqui |
| Pesquisa | Intenção explícita. Compara títulos e miniaturas da lista | Busca é superfície de impressão [OFICIAL, AJ-IMP] | Correspondência entre o termo buscado e o nome ou objeto visível; clareza do assunto [INFERÊNCIA] | Não encontrei estudo sobre o peso de título versus miniatura na busca |
| Inscrições (feed) | Já conhece o canal | Destacar elementos familiares para inscritos [OFICIAL, AJ-DICA] | Identidade visual constante e continuidade de formato [INFERÊNCIA] | Sem medição |

**Dispositivos**

| Dispositivo | O que o material sustenta | Hipótese (não medida) | Lacuna |
|---|---|---|---|
| Celular | A miniatura aparece em tamanhos diferentes conforme o dispositivo; use a versão maior possível. A fonte deve ser fácil de ler [OFICIAL, AJ-DICA] | Texto secundário e detalhe fino se perdem; o elemento dominante decide [INFERÊNCIA] | Sem estudo revisado sobre legibilidade em tamanho de feed |
| TV | Nenhum documento lido trata de exibição em TV como medição de CTR. Co-views estimadas em TV entram nas contagens públicas a partir de 16/11/2026 (Data API, OFICIAL; a Ajuda diz novembro de 2026). Declarações da Creator Insider, citadas por terceiros, dizem que elas não afetam CTR, impressões de thumbnail nem duração média. O numerador exato do CTR não está publicado. Lacuna declarada: não se sabe se co-views entram em qualquer numerador de CTR além da declaração citada | Nenhuma | Lacuna total. Não extrapolar do celular |

### 1.3 O que conta como sucesso

- **Critério oficial do teste:** a variante com maior tempo assistido (watch time) vence, não a de maior CTR. A justificativa é que título e miniatura devem fazer o espectador entender o assunto, para ele não gastar tempo com um vídeo errado [OFICIAL, AJ-TESTE].
- **Definição de CTR:** no Studio, o numerador são só as visualizações que nasceram de uma impressão contada, e o denominador são as impressões contadas. Dividir o total de visualizações pelas impressões não reproduz o número exibido [OFICIAL, AJ-CTR; leitura registrada no dossiê de testes].
- **Divergência do nome da métrica:** a Central fala em "watch time share" [AJ-TESTE]. O post oficial da comunidade descreve o vencedor pelo tempo assistido por impressão (support.google.com/youtube/thread/393332200, autor não identificado, lido em trecho) [PRATICANTE]. Se as variantes tiverem impressões diferentes, as duas métricas podem ordenar de forma diferente [INFERÊNCIA]. Não resolvido no material (seção 7).
- **Mudança na contagem:** a partir de 24/08/2026 a visualização passa a contar quando o vídeo começa a tocar, inclusive em vídeos longos [OFICIAL, citado por terceiros: a data aparece na variante Android en-UG da Ajuda 12220281, em trecho, e no comunicado da comunidade de 17/08/2026, thread 433409976, lido só por citações; a versão de desktop lida não traz a data]. Como o CTR usa visualizações no numerador, comparações antes e depois dessa data podem não ser diretas [INFERÊNCIA]. O tamanho do efeito não foi medido.

### 1.4 Números que circulam e não servem de base

- **Faixa de CTR:** metade dos canais e vídeos fica entre 2% e 10% [OFICIAL, AJ-CTR]. É a descrição de uma distribuição, não média nem meta. A FAQ não traz faixa por origem.
- **Faixas por origem** (Search, Suggested, Browse) aparecem em blogs, com valores divergentes e sem método. Suggested aparece como 5–10% em uma fonte e 9,5% em outra [PRATICANTE]. Não usar como baseline.
- **"1,8 segundo" na Netflix:** um artigo atribui a Lee (2020) a média de 1,8 s por arte; outra fonte descreve o número como tempo médio de avaliação de uma miniatura. Não verifiquei a fonte primária da Netflix. Não usar como tempo de decisão no YouTube.
- **Personalização:** o único experimento de arte personalizada que li é da Netflix (arXiv 2608.18322: +0,36% de playthrough, p<0,05). Depende de personalização por membro, que um canal não tem [ESTUDO industrial]. Não transfere.
- **Não usar, por falta de fonte primária:** "+20% a 30% de CTR com rosto emocional" (atribuído ao VidIQ, sem método); "6,8% com rosto contra 4,1% sem rosto"; "30% mais CTR com cores contrastantes" (Vidooly, 2023, não localizado); "38% mais cliques com rosto", cuja origem é um estudo de curtidas no Instagram de 2014, segundo o Mark Studios; "90% dos vídeos de melhor desempenho têm miniatura personalizada" (fun fact da Central, sem definição; o Mark Studios diz que vem de 2015).

### 1.5 Ordem de diagnóstico

[INFERÊNCIA] Quando o CTR de um vídeo sobe ou cai, a miniatura é a última causa a verificar:
1. Impressões contadas e distribuição por superfície [AJ-IMP, AJ-ORIG].
2. CTR dentro de cada superfície. Não comparar CTR de superfícies diferentes.
3. Watch time e AVD, contra o histórico do próprio canal.
4. Só o que sobrar pode ser atribuído à miniatura ou ao título.

Condição: canal com histórico e acesso ao Studio. Limite: o material não confirma se o Studio mostra CTR separado por origem (seção 8).

### 1.6 O que o corpus permite dizer sobre o clique

- **Mesmo título, desempenhos diferentes.** "3 People Who Disappeared Then REAPPEARED Years Later..." (Cold Case Detective, 18:06) aparece com 791 mil e 2 milhões de views, segundo o input. O título não explica o resultado sozinho.
- **O tema domina.** "Doku: Wie war Sex im Mittelalter?" (Timeline Deutschland, 33:36; 1,8 milhão de views; razão 43,9, do input) tem um tema que atrai por si. Não há como separar o efeito do rótulo "Doku:" do efeito do tema.
- **Sem grupo de comparação.** Nenhum vídeo do corpus está abaixo da mediana do canal. Qualquer "motivo do clique" extraído do corpus é hipótese.

**Lacuna:** não há CTR por variante, impressões nem curva de retenção para nenhum vídeo do corpus.

---

## 2. Princípios de design

Não encontrei experimento que meça o efeito de design de miniatura sobre CTR em vídeo longo. Os princípios abaixo se apoiam em estudos de outros contextos, em diretrizes oficiais qualitativas e em dados de fornecedores. A força da evidência é indicada em cada um.

| Princípio | Evidência mais forte | Limite principal |
|---|---|---|
| Hierarquia: um foco dominante | Pieters e Wedel (2004), anúncio impresso; diretriz oficial de simplicidade | Não é vídeo; "pictórico" não separa rosto de objeto |
| Composição | Diretriz oficial (regra dos terços); atenção aos olhos em tarefa social | Nenhum estudo de CTR |
| Contraste e cor | Prática sobre interface escura; dado de fornecedor | Sem CTR medido |
| Legibilidade em tela pequena | Diretriz oficial de fonte legível; tamanho variável; piso de 720p | Sem estudo em tamanho de feed |
| Quantidade de informação | Diretriz oficial contra excesso; concretude em manchetes | Manchetes, não miniaturas |
| Personagens e expressões | Estudos de atenção a rostos (laboratório); dado de fornecedor | Nenhum teste rosto contra objeto em clique |
| Objetos e símbolos | Latência de objetos (laboratório); exemplos do corpus | Depende de reconhecimento pelo público |
| Limite de promessa e de choque | Política oficial | Aplicação caso a caso |

### 2.1 Hierarquia visual: um foco dominante

- **Evidência:** Pieters e Wedel (2004): o elemento pictórico capta atenção independentemente do tamanho; o texto, em proporção ao tamanho [ESTUDO, anúncio impresso]. A Central recomenda evitar design complexo demais, porque cor e composição dinâmicas chamam atenção, mas em excesso sobrecarregam [OFICIAL, AJ-DICA].
- **Limite:** anúncio impresso, não vídeo. O estudo não separa rosto de objeto. A transferência é [INFERÊNCIA].
- **Regra:** uma miniatura, um foco. Escolha o elemento que a promessa exige e reduza o resto a fundo.
- **Teste de um segundo** [PRATICANTE]: mostre a miniatura reduzida por um segundo a alguém de fora do projeto e peça uma frase sobre o assunto e a tensão. Se a frase depender de texto secundário ou do título, a hierarquia falhou.

### 2.2 Composição

- **Evidência:** a Central cita a regra dos terços e a sobreposição de texto e marca como recomendações [OFICIAL, AJ-DICA], sem efeito medido. Em julgamentos de atratividade e dominância, olhos, nariz e boca concentram a atenção (Evolutionary Human Sciences, 2025, DOI 10.1017/ehs.2025.2; 93 mulheres e 33 homens avaliaram 80 fotos de rosto com rastreamento ocular) [ESTUDO]. É tarefa social, não miniatura.
- **Limite:** nenhum estudo de composição sobre CTR.
- **Regra** [INFERÊNCIA]: se houver rosto, os olhos precisam estar legíveis no tamanho reduzido. Se houver texto, ele não cobre a região que o olho procura primeiro.
- **Corpus:** em "Die Hexen von Villach" (Real Crime Deutschland, 31:36), a miniatura cobre os olhos da mulher com uma tarja preta. O estudo acima aponta os olhos como foco de atenção em tarefas de julgamento. O efeito dessa escolha na miniatura não foi medido.

### 2.3 Contraste e cor

- **Evidência:** em uma amostra de 500 miniaturas de vídeos que "estouraram", o vidIQ encontrou alto contraste em mais da metade [DADO, fornecedor, sem denominador] (vidiq.com/blog/post/youtube-thumbnail-design-tips/). Koh e Cui (2022), citados em arXiv 2505.21912, associaram a view-through de conteúdo de marca a cores e brilho [ESTUDO, citação secundária]. Mede views, não CTR, e não é long-form.
- **Prática** [PRATICANTE]: vermelho, branco e preto como cor dominante se confundem com a interface do YouTube, que usa fundos claros e escuros.
- **Limite:** não encontrei medição primária de contraste sobre CTR.
- **Regra para canal dark** [INFERÊNCIA]: fundo escuro é o padrão do nicho e pode se confundir com a interface em modo escuro. Antes de publicar, veja a miniatura reduzida nos modos claro e escuro e confirme que o elemento principal e o texto têm contorno próprio. Isso é critério de visibilidade, não prova de clique.
- **Corpus:** "fundo quase preto" em J.P. Morgan (Business Casual, 40:24) e "fundo vermelho-escuro" em "The Secret Chinese Company That Owns Everything" (MagnatesMedia, 78:48). O corpus não permite comparar contraste.

### 2.4 Legibilidade em tela pequena

- **Evidência:**
  - [OFICIAL] A fonte deve ser fácil de ler, e a miniatura aparece em tamanhos diferentes conforme o dispositivo [AJ-DICA].
  - [OFICIAL] Miniatura abaixo de 720p reduz todas as variantes do teste para 480p [AJ-TESTE].
  - [PRATICANTE] Fontes pesadas funcionam melhor; fontes finas somem quando a imagem diminui. Três a cinco palavras de impacto.
  - [DADO, fornecedor] O vidIQ encontrou mediana de cinco palavras no texto das miniaturas de breakouts, sem denominador.
- **Lacuna:** não encontrei estudo revisado sobre legibilidade de texto em tamanho de feed.
- **Regra:** texto principal de até cinco palavras; altura de letra suficiente para leitura no tamanho reduzido; resolução de pelo menos 720p (1280×720) [OFICIAL, AJ-TESTE; número de palavras, PRATICANTE e DADO].
- **Corpus:** "DER INSTAGRAM-MORD" (2 palavras; Doppelgänger, 57:00), "CHINA IS SURROUNDED" (3 palavras; RealLifeLore, 58:24) e "O PAÍS QUE HITLER NÃO TOCOU" (6 palavras; PORTUGAL PARA TODOS, 17:24). A última ultrapassa o limite de cinco palavras.

### 2.5 Quantidade de informação

- **Evidência:**
  - [OFICIAL] Design complexo demais deve ser evitado [AJ-DICA].
  - [ESTUDO, fraco] Estudo de miniaturas de notícias no YouTube (ResearchGate; ano não confirmado no trecho; 221 respostas válidas): miniaturas enganosas geraram mais cliques, e o autor propõe carga cognitiva como mecanismo para a queda em miniaturas com grupos. O mecanismo não foi testado no trecho lido. Usar só como hipótese.
  - Para manchetes, concretude pode reduzir o clique (ver 3.3).
- **Limite:** não há estudo de quantidade de informação em miniatura de vídeo longo.
- **Regra** [INFERÊNCIA]: a miniatura contém o que permite identificar o caso (quem, onde ou o quê) e nada que responda à pergunta do vídeo. Cada elemento acrescentado é uma afirmação que o vídeo precisa sustentar (ver 2.8 e 3.4).

### 2.6 Personagens e expressões em canal sem rosto

- **Evidência:**
  - [ESTUDO] Crouzet et al. (2010): rostos foram localizados mais rápido que animais e veículos em escolha entre dois alvos (ver 1.1).
  - [ESTUDO] Desenvolvimento (PMC3899069; autoria não confirmada no trecho): em cenas naturais, rostos salientes atraem atenção de orientação, de forma confiável só depois da infância.
  - [ESTUDO observacional, via fonte secundária] Estudo coreano de 2022, citado pelo Mark Studios (original não aberto): 3.743 vídeos de canais de 38 marcas; 35% das miniaturas com pessoa; celebridades associadas a mais views; nenhuma miniatura atribuída aleatoriamente.
  - [DADO, fornecedor] vidIQ: rosto em 69% das miniaturas de breakouts e em 80% dos maiores overperformers. Sem denominador: não se sabe quantas miniaturas sem rosto também estouraram.
  - [DADO, terceiro] 1of10, via Search Engine Journal (análise de cerca de 300 mil vídeos virais): desempenho parecido com ou sem rosto, com diferenças por nicho. A métrica é views, não CTR. Relatório original não aberto.
  - [DADO, terceiro] Kapwing (set/2024): emoção classificada automaticamente (Amazon Rekognition) no rosto mais proeminente; emoções positivas associadas a mais views; sem controle por canal ou tema.
  - [PRATICANTE] Expressão de grito forçado lê como clickbait e pode reduzir a confiança do público.
- **Síntese:** a pesquisa mede atenção a rostos; os dados de plataforma mostram associação com desempenho; ninguém mediu rosto contra objeto em clique de vídeo. A direção do efeito no CTR é desconhecida.
- **Limite do canal sem rosto** [INFERÊNCIA]: os estudos de atenção medem olhos, nariz e boca. Silhueta, figura de costas ou ilustração sem olhos não oferece esse sinal. A evidência sobre atenção a rostos não se transfere automaticamente para personagens sem rosto.
- **Regras:**
  1. Rosto de pessoa real identificável só com origem registrada e direito de uso. Se a pessoa for vítima, acusada ou testemunha, a checagem inclui o status jurídico (2.8) [INFERÊNCIA, processo].
  2. Se a miniatura mostra um rosto, o vídeo precisa explicar quem é a pessoa e por que aparece. Caso contrário, há descompasso de promessa [PRATICANTE].
  3. Figura histórica ilustrada deve ser marcada como ilustração. Em "DOM AFONSO HENRIQUES" (Cavaleiro do Tempo, 20:36), o homem de cota de malha na miniatura não tem origem registrada no material. Não afirmar que é retrato do personagem.
  4. Antes de escolher entre rosto, personagem sem rosto e objeto, teste as três versões com o mesmo título (seção 7).
- **Corpus:** em "Enrique Blanco: El fantasma del Cibao/RD" (31:54), a miniatura mostra uma mulher de óculos falando ao microfone de estúdio, ao lado de uma foto de época. O dossiê registra que esse formato contraria a premissa faceless do canal e que a presença da pessoa no vídeo não foi confirmada. Razão 123,0 (input), não atribuível ao rosto.

### 2.7 Objetos e símbolos

- **Evidência:**
  - [ESTUDO] Objetos são localizados rápido em escolha entre dois alvos (animais a ~120 ms, veículos a ~140 ms), mas mais devagar que rostos no mesmo paradigma (Crouzet et al., 2010).
  - [ESTUDO] Elemento pictórico capta atenção (Pieters e Wedel, 2004).
  - [OFICIAL] Elementos familiares para inscritos (AJ-DICA).
- **Símbolo depende de reconhecimento** [INFERÊNCIA]: em "The Secret Chinese Company That Owns Everything" (MagnatesMedia, 78:48), a miniatura mostra um pinguim de desenho, com olhos verdes e faixa vermelha e amarela, sem texto. Quem reconhece o pinguim recebe uma pista. Quem não reconhece vê só o enigma. Para público geral, o símbolo precisa de um nome curto ou de um elemento que o identifique.
- **Detalhe depende de resolução:** em "Die Dienstgrade der Waffen SS" (History Check, 16:48), a miniatura amplia insígnias de colarinho. O dossiê não conseguiu confirmar a contagem de estrelas porque a imagem tem baixa resolução. Detalhe que não se lê não cumpre a função.
- **Forma como tese visual:** em "What's Hidden Under the Ice of Antarctica?" (RealLifeLore, 37:54), a miniatura mostra o terreno sem gelo, sem feições, com o texto "UNDER THE ICE IN ANTARCTICA". A forma responde "o que está lá" sem responder "o que é". O render exige nota de método (ver 3.3).
- **Lacuna:** nenhum estudo compara objeto e rosto em clique de vídeo. O dossiê de design propõe um teste direto (E3).

### 2.8 Limite de promessa e de choque

- **Evidência:** a política proíbe miniatura que leve a esperar conteúdo ausente, com exceção caso a caso para contexto educativo, documental, científico ou artístico. Lista imagens de gore feitas para chocar. Título e descrição que indicam intenção de chocar entram na restrição de idade ou na remoção. Primeira violação gera aviso; violação repetida em 90 dias pode gerar strike [OFICIAL, AJ-POL].
- **Limite:** a lista não é completa e a exceção não é garantida. Não validei como a exceção se aplica a mistério.
- **Sinais no corpus:**
  - "CRIME SCENE DO NOT CROSS" (fita de cena de crime), junto com "EL NIÑO / JAMES BULGER", em "EL ASESINATO DE JAMES BULGER" (Canal Prohibido, 13:42). A vítima é criança. O dossiê registra uma recusa pública da mãe a um filme sobre o caso (fonte secundária).
  - "Puppen aus MENSCHEN" (bonecas feitas de pessoas), em "Das Horrorhaus des Anatoly Moskvin" (abnorm - True Crime, 26:36), é uma afirmação factual na capa. O dossiê registra divergência de números entre fontes e ausência de registro judicial verificado.
  - Em "Doppelgänger-Mord in Ingolstadt" (Insolito, 57:00), duas fotos de mulheres lado a lado, com seta e "DER INSTAGRAM-MORD". A seta afirma uma relação entre as duas pessoas. Uma delas é acusada, e o caso tem recurso.
- **Regra** [INFERÊNCIA]: todo texto de miniatura que afirma fato (quem, quantos, o quê) passa pela mesma checagem do roteiro: fonte primária, data e status jurídico. Acusado sem sentença definitiva é "acusado" na miniatura e na narração.

---

## 3. Título + miniatura como sistema

### 3.1 Por que tratar como par

- [OFICIAL] Título e miniatura devem fazer o espectador entender o assunto, para ele não clicar no vídeo errado [AJ-TESTE]. O par serve ao alinhamento, não só ao clique.
- [OFICIAL] Se título ou miniatura for alterado durante um teste A/B, o teste para e precisa ser reiniciado [AJ-TESTE]. Trate o par como versão única e registre as duas peças juntas.
- [PRATICANTE] Divisão de papéis: o título carrega a promessa em nível de frase; a miniatura carrega a prova visual ou a tensão. A atribuição dessa regra ao Creator Academy não foi verificada.

### 3.2 Tipos de relação

| Tipo | Teste de reconhecimento | Exemplo do corpus | Risco |
|---|---|---|---|
| **Complementar** | Cada peça traz um elemento que a outra não tem, e nenhuma contradiz a outra. | Título: "Doppelgänger-Mord in Ingolstadt" (conceito: sósia). Miniatura: "DER INSTAGRAM-MORD" e seta entre duas fotos (mecanismo). O dossiê classifica como complemento, não repetição. | Duas fotos de mulheres reais com seta sugerem identidade entre elas. Uma é acusada, sem sentença final. |
| **Complementar com troca de verbo** | O verbo muda a pergunta. | Título: "...Then REAPPEARED Years Later..." (reaparecer: a pessoa volta). Miniatura: "MISSING 1981 / FOUND IN 2006" (encontrar: alguém a localizou). | A miniatura mostra um caso; o título promete três. |
| **Redundante** | Mesmo sujeito e mesmo fato nas duas peças, sem informação nova. | Título: "Der Dreißigjährige Krieg | Die Komplette Geschichte...". Miniatura: "Der Dreißigjährige / Krieg". O escopo ("completa") fica só no título. | O espaço da miniatura repete o tema, em vez de mostrar tensão ou prova. |
| **Dependente** (classe acrescentada por mim) | Uma peça não tem sujeito sem a outra: pronome sem antecedente, "antes/agora" sem objeto. | Título: "Warum ließ Hitler 350.000 Soldaten in Norwegen, während Berlin fiel?". Miniatura: "SIE WARTETEN." (Eles esperaram). O antecedente de "Sie" está só no título. | Peça isolada perde sentido [INFERÊNCIA]. |
| **Contraditória: escopo** | As peças prometem escopos diferentes. | Título: "Por Que Hitler Nunca Invadiu Portugal?". Miniatura: "O PAÍS QUE HITLER NÃO TOCOU". "Tocar" é mais amplo que "invadir". | A miniatura promete mais que o título. A narração precisa definir "tocar". |
| **Contraditória: sujeito** | Os sujeitos não coincidem. | Título: "How the US & China Are Preparing to Fight Total War". Miniatura: "CHINA IS SURROUNDED", com um só país cercado. | Enquadramento unilateral; sem o outro lado no início, a promessa do título não é cumprida. |
| **Descasada: objeto ausente** | A pergunta do título não tem objeto visível na miniatura. | Título: "Sleepy History of London | What lies beneath Trafalgar Square?". Miniatura: skyline e "LONDON". O dossiê: a capa mostra a cidade, não o objeto da pergunta. | Pergunta sem âncora visual. |

**Caso excluído:** "Designers Que Usaram 100% Do Cérebro" (Fala Sério, 38:42) tem miniatura com "GUARDA-CHUVA MÁGICO" e um guarda-chuva, sem relação com o título ou a descrição. O dossiê não consegue confirmar que a imagem pertence ao vídeo. Não entra na análise. Regra decorrente: confirmar a miniatura pelo ID do vídeo antes de qualquer análise.

**Decisão por teste de reconhecimento** [INFERÊNCIA]:
1. Remova o título e leia a miniatura: ela diz o assunto? Remova a miniatura e leia o título: ele diz o assunto?
2. Se as duas dizem o mesmo sem nada novo: redundante.
3. Se uma não tem sujeito sem a outra: dependente.
4. Se cada uma traz elementos distintos sem contradição: complementar.
5. Se escopo, sujeito ou fato não batem: contraditória. Corrigir antes de qualquer teste.

**Evidência por tipo:** nenhuma fonte mede efeito por tipo de relação. A regra de alinhamento tem base oficial (3.1). A redundância como desperdício é [PRATICANTE]; um blog cita "I FIXED IT" na miniatura e "I Fixed My Broken Camera" no título como exemplo de repetição, sem dado.

### 3.3 Lacuna de curiosidade: evidência e construção

**Evidência disponível**
- [ESTUDO] Loewenstein (1994, *Psychological Bulletin* 116(1), 75–98): curiosidade surge quando se percebe uma lacuna de conhecimento. Uma pequena dose de informação aumenta a curiosidade, até a saciedade. Segundo uma descrição secundária (arXiv 2604.25648), a motivação cai quando a lacuna é grande demais ou pequena demais. Li resumos e citações, não o texto integral; o estudo não testa miniaturas.
- [ESTUDO] APA, "Curiosity and Reward" (autoria não confirmada no trecho): o aprendizado depende da diferença entre a recompensa esperada e a recebida. Aplicado ao par: a promessa cria a expectativa, e o pagamento define o tamanho do erro [INFERÊNCIA].
- [ESTUDO] Scacco e Muddiman (*New Media & Society*; publicado online em 2019 e no volume 22(3) em 2020, conforme a fonte): em notícias, manchetes em forma de pergunta geraram atitudes mais negativas; no campo, manchetes de curiosidade associaram-se a menos page views. Limite: notícia, métrica de página, não AVD.
- [ESTUDO] ACM, DOI 10.1145/3411764.3445753 (autoria e ano não confirmados): manchetes não-clickbait geraram mais curiosidade que todas as manchetes clickbait testadas. Limite: notícia.
- [ESTUDO] PMC11704130 (trecho de busca; página bloqueada; autores não identificados no trecho): concretude pode reduzir o clique. Em testes A/B de manchetes do Upworthy, o modelo prevê que 8,7% das manchetes ganhariam com mais concretude, enquanto para 50,9% ela reduziria o CTR de forma significativa. O sentido do efeito depende do conjunto testado.
- [ESTUDO, revisão] "Emotion Sells" (ResearchGate): alguns estudos encontram mais engajamento com clickbait; outros não. Os autores sugerem que subtipos não separados explicam a diferença. É hipótese, não resultado.

**Conclusão:** a lacuna tem base teórica, mas a evidência sobre quais lacunas funcionam vem de notícia e é contraditória. Para miniatura de vídeo longo, não há estudo. A construção abaixo é processo, não achado.

**Fórmula de construção** [INFERÊNCIA]:

**Lacuna = objeto verificável + pergunta única + ponto de pagamento + limite de revelação**

- **Objeto verificável:** algo que existe no vídeo e aparece na miniatura: documento, lugar, objeto, número com fonte. Exemplo: "MISSING 1981 / FOUND IN 2006" são dois documentos com data.
- **Pergunta única:** uma pergunta com resposta factual (quem, o quê, quando, por quê, como acabou). Evitar pergunta de julgamento sem critério. "O MELHOR REI?" (Dom Dinis, Cavaleiro do Tempo, 17:12) só tem resposta se o vídeo declarar critérios; o dossiê propõe comércio, agricultura, guerra e cultura, com fontes secundárias.
- **Ponto de pagamento:** minuto ou capítulo em que a pergunta é respondida (3.4).
- **Limite de revelação:** a miniatura mostra o objeto, não a resposta. Exceção: se a miniatura entrega um fato, o título passa a perguntar a causa (caso Portugal, abaixo).

**Calibração** [PRATICANTE, a calibrar com o canal]: conte as perguntas abertas no par. Uma pergunta principal, com no máximo uma secundária, é o alvo. Nenhuma é resumo. Três ou mais é ruído. O limite é heurística minha, sem número nas fontes; Loewenstein (1994) trata do tamanho da lacuna de conhecimento e não sustenta essa contagem.

**Tipos de lacuna e construção no corpus**

| Tipo de lacuna | Como o par constrói | Exemplo do corpus | Ponto de atenção |
|---|---|---|---|
| Quem (identidade do sujeito) | Sujeito oculto na miniatura; nome revelado depois | "The Secret Chinese Company": pinguim na miniatura. O título do capítulo 1, "QQ & The Mysterious Founder of Tencent", começa aos 10:21 (13% de 78:48). Capítulos vêm de cópias de terceiros, não confirmadas na versão atual | Pagar o nome no minuto anunciado |
| O quê, passa a ser quem ou como | Miniatura mostra o núcleo do fato; a pergunta muda para autoria ou mecanismo | Moskvin (26:36): "Puppen aus MENSCHEN" na miniatura; o título fala de lugar, nome e gênero | Pré-revelação: abrir pergunta nova cedo (3.4) |
| Por quê (causa de um fato) | Miniatura dá o fato; título pergunta a causa | Portugal (17:24): "NÃO TOCOU" (fato) e "Por Que... Nunca Invadiu" (causa) | Definir "tocar" antes da causa |
| Como acabou (desfecho) | Desfecho no título; a pergunta vira "o que o registro mostra" | Archivo Criminal (20:48): "Todo quedó grabado" anuncia o assassinato; a miniatura tem um recorte de câmera de segurança | Abertura precisa abrir outra pergunta; registro verificado |
| Escala (quanto, quantos) | Número com data; dois pontos que criam distância | Cold Case: "MISSING 1981 / FOUND IN 2006". A distância de 25 anos é aritmética minha | Blocos iguais ao número prometido no título |
| Julgamento (é o melhor?) | Pergunta de valor | Dom Dinis: "O MELHOR REI?" com título "O Rei que fez tudo o que quis" | Critérios declarados antes do veredito |
| Forma sem feição | Miniatura mostra a forma e esconde o conteúdo | Antarctica (37:54): render sem gelo, "UNDER THE ICE IN ANTARCTICA" | Mapa ou modelo exige nota de método |
| Descasada | Pergunta sem âncora visual | Sleepy History (180:12): "What lies beneath Trafalgar Square?" com skyline | Mostrar o objeto da pergunta |

### 3.4 Como manter a promessa pagável

**Evidência**
- [OFICIAL] Clickbait é CTR alto com AVD baixo [AJ-CTR]. Miniatura que sugere conteúdo ausente é proibida [AJ-POL].
- [OFICIAL] Não há curva de retenção pública nem número oficial sobre o efeito de promessa não cumprida sobre a satisfação. O post de 2019 fala em satisfação sem pesos [BLOG-2019].
- [PRATICANTE] O vidIQ diz que clickbait "bem feito" é promessa atendida, e usa 7 milhões de views como prova. Views não medem qualidade narrativa, então o argumento não sustenta a tese.
- [INFERÊNCIA] O critério oficial separa os dois casos. Se a promessa é paga cedo, o sinal de clickbait da FAQ tem menos chance de aparecer. Isso é coerente, não comprovado.

**Registro de promessas** (processo; condição: vídeo com transcrição ou roteiro com minutagem):
1. Liste cada promessa do par: objeto, número, verbo ("lutou", "reapareceu"), superlativo ("mais perigosa"), pergunta.
2. Para cada uma, anote o bloco e o minuto em que é paga. Se não há pagamento, marque "não paga".
3. Para cada "não paga", faça uma de três coisas: retire a promessa do par, crie o bloco, ou reformule como limite honesto (por exemplo, "o caso segue sem explicação pública", sugestão do dossiê de título).
4. Para cada número ou fato da miniatura, anote a fonte primária ou a fonte secundária com os conflitos.
5. Confronte cada palavra-promessa com os fatos levantados.

Limite: o material não traz limiar de tempo para pagar a primeira promessa. O número de 90 segundos aparece como hipótese.

**Exemplos do corpus**
- **Miyako** (A TRAGÉDIA DE MIYAKO, Um Documentário, 67:54): a descrição promete cinco coisas: a causa da ruptura, o motivo do apagamento em 1896, as defesas que falharam, a história dos avisos em pedra e o momento em que a onda atinge 40,5 m. O dossiê não encontrou fonte para 40,5 m; uma fonte encontrada dá 38,9 m para a subida em Aneyoshi [DADO, fonte secundária]. A descrição também diz "Todas que ignoraram, e construíram abaixo dela, morreram", afirmação que as fontes consultadas não sustentam. Corrigir ou sustentar antes de publicar.
- **Clodimar Pedrosa Lô** (Marcos Campos, 47:06): a descrição promete reconstruir "o desaparecimento e as circunstâncias do caso". As reportagens tratam de morte. A única ocorrência de "desaparecimento" nas fontes se refere ao sumiço dos autores do crime. A palavra-promessa não tem bloco correspondente [DADO, dossiê].
- **Homo habilis** (Um Documentário, 50:18): o título diz "lutou e sobreviveu". Pelo critério do dossiê, "lutou" exige um bloco de confronto ou defesa. A miniatura mostra ameaça e grupo, sem luta. A checagem depende da transcrição, que não foi obtida.

**Pré-revelação** [PRATICANTE]: quando a miniatura entrega o "o quê", o roteiro deve abrir uma pergunta nova cedo. O dossiê propõe reprovar o roteiro se a primeira pergunta nova só for paga depois de 90 segundos. O limiar não tem fonte. Calibre com a retenção dos primeiros 30, 60 e 90 segundos do próprio canal, no Studio. O corpus cita o relatório "Key moments for audience retention" (support.google.com/youtube/answer/9314415), que não li nesta parte.

### 3.5 Checklist do par antes de publicar

1. Classifique o par (complementar, redundante, dependente ou contraditória) pelo teste de 3.2.
2. Se for contraditória, corrija escopo, sujeito ou fato antes de qualquer teste.
3. Registre a versão do par (título, miniatura, data). Se uma peça mudar, trate como nova versão.
4. Faça o registro de promessas e marque o minuto de pagamento de cada uma (3.4).
5. Confira cada número e fato escrito na miniatura contra fonte primária, ou marque o conflito.
6. Confira direito de imagem e status jurídico das pessoas que aparecem (2.6 e 2.8).
7. Confirme que a miniatura pertence ao vídeo pelo ID.
8. Veja a miniatura reduzida, em modo claro e escuro (2.3 e 2.4).

Condição: qualquer vídeo longo. Limite: é checagem de coerência e de risco. Não garante desempenho.

---

## 4. Mecanismos que sustentam miniaturas simples (sem teste primário em vídeo longo)

### 4.1 Definição e limite da afirmação

"Simples" aqui tem três critérios observáveis: um foco dominante; texto principal de até cinco palavras [PRATICANTE, com dado de fornecedor]; nenhum elemento sem função na promessa. Simples não é vazia: a miniatura ainda diz o objeto e o tema.

Não encontrei teste primário que compare miniatura simples e complexa em CTR de vídeo longo. Há mecanismos plausíveis, casos observacionais e um contraexemplo em notícias. O que segue descreve mecanismos, não efeito.

### 4.2 Mecanismos

| Mecanismo | Base | O que sustenta | Limite |
|---|---|---|---|
| **M1. Leitura de um foco** | [ESTUDO] Crouzet et al. (2010); [ESTUDO] Pieters e Wedel (2004) | Objeto ou rosto é localizado em ~110–140 ms em escolha entre dois alvos; elemento pictórico capta atenção independentemente do tamanho | Laboratório e anúncio impresso; nenhuma medida de clique |
| **M2. Texto só conta se for grande** | [ESTUDO] Pieters e Wedel (2004) | O texto ganha atenção em proporção ao tamanho. Para ser lido, o texto precisa de espaço. [INFERÊNCIA] Poucas palavras grandes ocupam menos espaço do que muitas pequenas | Ganho líquido de atenção só ocorre com aumento real do texto |
| **M3. Sobrevivência ao menor tamanho** | [OFICIAL] tamanho variável, fonte legível, design complexo demais (AJ-DICA); [PRATICANTE] fontes finas somem | O elemento que se lê no menor tamanho é o que compete de fato | A Central não publica tamanho mínimo; nenhum estudo |
| **M4. Lacuna aberta** | [ESTUDO] Loewenstein (1994); [ESTUDO] PMC11704130 (concretude) | Miniatura que mostra o objeto e não a resposta mantém a pergunta. Mais detalhe pode fechar a lacuna | Concretude estudada em manchetes; o sentido depende do conjunto |
| **M5. Menos afirmações, menos descompasso** | [OFICIAL] AJ-POL e AJ-TESTE (não clicar no errado) | [INFERÊNCIA] Cada elemento da miniatura é uma afirmação que o vídeo pode não sustentar. Menos elementos reduzem os pontos de descompasso | Não medido |
| **M6. Carga cognitiva** | [ESTUDO fraco] estudo de notícias no YouTube (221 respostas; ano não confirmado) | Mecanismo proposto para a queda com miniaturas de grupo | Mecanismo não testado no trecho lido. Só hipótese |

**Contraevidência:** [ESTUDO] arXiv 2101.06141 (recomendação de artigos de opinião, duas semanas de experimento): a presença de imagem na miniatura não teve efeito significativo sobre o CTR. [INFERÊNCIA] Ter imagem não basta; o que importa é o conteúdo da imagem, o que nenhum estudo aqui mediu.

### 4.3 Casos do material

Razões de outlier são do input e não verificadas. Nenhuma delas é atribuível à miniatura.

| Vídeo (canal, duração) | Miniatura | Texto | Razão | Leitura do dossiê |
|---|---|---|---|---|
| "The Secret Chinese Company That Owns Everything" (MagnatesMedia, 78:48) | Pinguim de desenho, olhos verdes, fundo vermelho com chamas | Nenhum | 10,0 | Símbolo como pista; quem não reconhece fica com o enigma [INFERÊNCIA] |
| "The Vanishing of Flight 370" (LEMMiNO, 24:54) | Avião em voo, fundo azul em degradê | Nenhum | 7,5 | O objeto identifica o tema; o desfecho fica no título |
| "The Most Dangerous Ocean Crossing on Earth" (Scary Interesting, 26:48) | Globo com rota e trecho vermelho | Nenhum | 4,7 | A rota traduz "crossing"; "dangerous" aparece em vermelho |
| "Os primeiros Humanos: ... Homo habilis" (Um Documentário, 50:18) | Savana, quatro figuras, dois predadores | Nenhum | 5,4 | Responde "onde" e "com quem", não "como" |
| "DOM AFONSO HENRIQUES..." (Cavaleiro do Tempo, 20:36) | Um homem de cota de malha | Nenhum | 5,9 | Confirma gênero e época; "anos de ouro" não tem representação |
| "Sleepy History of London..." (Sleepy History, 180:12) | Skyline e "LONDON" | Uma palavra | 115,6 | Sem âncora para a pergunta; nicho de sono confunde |
| "Joachim Kroll..." (Verbrechen im Rückblick, 61:48) | Retrato P&B, nome e apelido, fundo industrial | Dois níveis | 4,6 | Nome em destaque, apelido menor |
| "Die Hexen von Villach" (Real Crime Deutschland, 31:36) | Incêndio, mulher com tarja nos olhos | Título de 4 palavras e logo | 15,6 | Elemento criminal e figura anônima |
| "Doppelgänger-Mord in Ingolstadt" (Insolito, 57:00) | Duas fotos, seta e "DER INSTAGRAM-MORD" | 2 palavras | 3,8 | Mecanismo na miniatura; risco de identidade |
| "La Masacre de EL Señorial" (Delitos de Sangre, 56:36) | Prédio comercial, título e mulher | Título | 141,6 | Lugar e rótulo; pessoa não identificada |
| "Los TSUNAMI más GRANDES..." (Pero eso es otra Historia, 16:12) | Onda, barco, "TSUNAMIS Y OLAS MONSTRUO" e "EL TERROR DE LOS MARES" | Dois blocos | 22,6 | Onda cresta quebrando, que não é o mecanismo do tsunami [dossiê] |
| "Micronações ao redor do mundo" (Canal das Curiosidades, 11:24) | Três painéis com rótulos | Três rótulos | 6,6 | Amostra de três de dez itens prometidos |

**Interpretação** [INFERÊNCIA]: miniaturas com pouco texto e com um objeto aparecem em casos de razão alta, e miniaturas densas também. No corpus, a simplicidade não é condição necessária para desempenho alto. Os casos mais simples de razão alta têm explicações concorrentes: "Sleepy History" tem nicho de sono; o pinguim depende de reconhecimento. Além disso, o dossiê registra descompasso na capa de Sleepy History, o que mostra que simplicidade sem âncora não basta.

### 4.4 Quando a simplicidade não funciona

- **Símbolo não reconhecível:** o pinguim funciona para quem conhece a referência (2.7).
- **Lacuna de identidade:** quando a pergunta é "quem é", a miniatura simples pode esconder a pessoa. "Doppelgänger-Mord" usa duas fotos e uma seta para sustentar a identificação. Isso não é simples, e tem risco jurídico (2.8).
- **Pergunta de julgamento sem critério no texto:** "O MELHOR REI?" tem cinco palavras, mas o critério não cabe na miniatura. O critério precisa estar no vídeo, no primeiro bloco de contexto.
- **Detalhe que depende de resolução:** a miniatura de insígnias de "Dienstgrade der Waffen SS" é de baixa resolução. O detalhe não se lê, e a função da miniatura se perde.
- **Simples com descompasso:** "SIE WARTETEN." só se entende com o título (dependente). "Sleepy History" tem skyline sem o objeto da pergunta. Ambas são simples, e ambas têm problema de alinhamento.
- **Fundo escuro que some:** a simplicidade com fundo escuro pode desaparecer na interface escura (2.3).

### 4.5 Como testar simplicidade sem confundir com o tema

- **Desenho** [INFERÊNCIA a partir de E3 do dossiê de design]: mesmo vídeo, mesmo título, três versões de miniatura. (A) um objeto, sem texto. (B) o objeto e até cinco palavras. (C) o objeto e duas camadas de texto.
- **Critério de decisão:** o watch time do teste nativo, que é o critério oficial (AJ-TESTE). CTR de impressão serve como diagnóstico, e AVD vem depois (1.5). Se o resultado for "Performed Same" ou "Inconclusive", não escolha pelo CTR.
- **Condição:** canal com impressões suficientes. A Central não publica o mínimo.
- **Limite:** um vídeo não separa o efeito da miniatura do efeito do tema. Para comparar temas, use vídeos paralelos, e não o mesmo vídeo em dois momentos.

**Lacunas desta seção:** não há teste primário de simplicidade em vídeo longo, nem dado de canal dark com miniaturas simples e complexas comparadas no mesmo período. A seção 9 consolida as lacunas de todo o playbook.

## 5. Framework de criação

Processo para montar a miniatura de um vídeo longo, do caso escolhido ao arquivo que entra no teste. Cada etapa traz decisão, critério e saída. Dois limites valem para tudo o que segue. Primeiro, os exemplos vêm de vídeos acima da mediana do próprio canal, sem CTR publicado e sem denominador: mostram o que apareceu junto com sucesso, não o que funciona. Segundo, nenhum elemento visual abaixo foi medido em CTR de vídeo longo. Cada escolha entra como hipótese para a seção 7 e é pontuada com a rubrica da seção 6.

### 5.1 Pré-requisitos

| Pré-requisito | Usado em | Se faltar |
|---|---|---|
| Formato declarado do canal (faceless, personagem ilustrado ou apresentador) | Passo 1; critério 8 da rubrica | Não há como checar se a miniatura promete um formato que o canal não tem |
| Roteiro ou transcrição com minutagem | Passo 2; portão G4; critério 4 | A promessa pagável fica como risco aberto, não verificado |
| Fonte e data de cada fato, número e nome | Passo 11; portão G4 | Não entra número, nome ou data na miniatura |
| Acesso ao Studio (teste nativo, impressões, retenção) | Passo 12; seções 7 e 8 | Há só hipótese, sem calibração |
| Histórico de vídeos do próprio canal | Seção 6.5 | Canal novo roda a rubrica sem calibração |

Lacuna: não encontrei experimento que relacione rosto, cor, texto ou objeto a CTR de vídeo longo. Os achados usados aqui vêm de laboratório, de notícias, de anúncios impressos e de dados correlacionais de fornecedores (dossiê de psicologia do clique, lacunas).

### 5.2 Passo a passo: da ideia ao arquivo

**Passo 1. Triagem de formato.**
- Decisão: a miniatura terá pessoa? Ela pode sugerir apresentador?
- Critério: canal sem apresentador não usa imagem de pessoa falando ao microfone nem retrato que pareça âncora de estúdio.
- Exemplo do corpus: Delitos de Sangre, "ENRIQUE BLANCO: EL FANTASMA DEL CIBAO/RD" (youtube.com/watch?v=rCAQRus_CX4). A miniatura junta uma fotografia antiga de um homem de chapéu, sobre a bandeira dominicana, e uma mulher de óculos diante de um microfone de estúdio [DADO, miniatura observada]. A seleção já marcava "faceless não confirmado". Que a imagem sugere narração com apresentadora é [INFERÊNCIA], a checar no vídeo.
- Saída: formato declarado e lista do que pode aparecer na miniatura.

**Passo 2. Promessa pagável.**
- Decisão: escrever em uma frase a pergunta central, a resposta que o vídeo dá (ou "sem resposta pública") e a fonte que sustenta a resposta.
- Critério: sem resposta documentada, a embalagem promete o que se sabe e o que segue sem explicação, não a explicação [INFERÊNCIA].
- Base: Loewenstein (1994, *Psychological Bulletin*, 116(1), 75–98) descreve a curiosidade como privação que surge quando se percebe uma lacuna de conhecimento; a motivação cai quando a lacuna é grande demais ou pequena demais [ESTUDO; li resumos e descrições secundárias, não o texto integral].
- Limite: teoria, sem medição em miniatura de vídeo. Em manchetes de notícia, perguntas geraram atitudes mais negativas (Scacco e Muddiman, *New Media & Society*; o ano varia entre 2019 e 2020 conforme a versão) [ESTUDO, notícia]. Pergunta no título não é padrão sem teste.

**Passo 3. Âncora visual.**
- Decisão: escolher uma âncora principal entre objeto, lugar, documento, mapa, pessoa, cena reconstruída, ilustração ou detalhe ampliado.
- Para cada candidato, anotar: (a) em qual minuto aparece no vídeo; (b) origem e direito de uso; (c) se é legível em tela pequena; (d) se é registro, reconstrução ou ilustração.
- Critério: nenhuma âncora que o vídeo não mostra ou não explica. Reconstrução ou ilustração é declarada no vídeo, cedo.
- Exemplo do corpus: Canal del Misterio, "El Misterio De La Dama De Elche" (youtube.com/watch?v=2zBOLPYurHQ). A miniatura põe o rosto de uma figura com adorno metálico diante de uma cidade futurista, que o título não menciona [DADO]. O dossiê não leu a narração nem a descrição completa. Se o roteiro não declarar que é reconstrução, a âncora sai.
- Saída: quadro de âncoras com status de cada uma.

**Passo 4. Divisão de papéis entre título e miniatura.**
- Decisão: distribuir a promessa. O título carrega palavras de busca, categoria, nome e escopo. A miniatura carrega uma âncora e um rótulo curto.
- Tipos de relação: complementar (cada peça traz algo que a outra não traz), redundante (as duas repetem o mesmo) ou contraditória (uma promete o que a outra restringe ou nega). A recomendação de complementaridade é de praticante, sem fonte oficial verificada [PRATICANTE].
- Exemplos:
  - Complementar: Business Casual, "J.P. Morgan Documentary: How One Man Financed America" (youtube.com/watch?v=5jjdErDkDZE). Miniatura: "THE GREAT / FINANCIER / BC DOCUMENTARY" (O grande financista). O título traz nome e mecanismo; a miniatura traz categoria e superlativo [DADO; INFERÊNCIA de leitura].
  - Divergência de escopo: "Por Que Hitler Nunca Invadiu Portugal?" (youtube.com/watch?v=oNkKg04ZBAE). O título pergunta sobre invasão. A miniatura diz "O PAÍS QUE HITLER NÃO TOCOU" (O país que Hitler não tocou), com "NÃO" em destaque [DADO]. "Tocar" é mais amplo que "invadir", e as fontes secundárias reunidas pelo dossiê descrevem Portugal como rota de fuga durante a ocupação [DADO, fontes secundárias]. O "não tocou" sem qualificação fica exposto.
  - Divergência de escopo: RealLifeLore, "How the US & China Are Preparing to Fight Total War" (youtube.com/watch?v=xBY5veWGBd8). O título trata dois países; a miniatura diz "CHINA IS SURROUNDED" (A China está cercada) sobre um mapa em que só a China aparece cercada [DADO]. Se o vídeo trata os dois lados, a miniatura precisa mostrar o outro; se trata um lado só, o título é que deve mudar.
- Lacuna: não há dado mostrando qual relação performa melhor.

**Passo 5. Arquétipo.**
- Decisão: que pergunta o vídeo responde? "Quem foi" ou "por que aconteceu" aponta para documentário (arquétipo A). Um caso com vítima e desfecho aponta para história real (C). "O que não se sabe" aponta para mistério (B). "O que é", "quantos" ou "qual o ranking" aponta para curiosidade (D).
- Critério: arquétipo errado cria promessa errada. Exemplo: tratar como mistério um caso já sentenciado.
- Saída: arquétipo e variante.

**Passo 6. Hierarquia e composição.**
- Decisão: quantos elementos disputam o olhar?
- Critério: um ponto focal; no máximo uma unidade de texto; o resto é fundo ou contexto.
- Evidência: [OFICIAL] as diretrizes do YouTube recomendam regra dos terços, texto legível e design não complexo demais. É orientação qualitativa, sem tamanho de efeito. [ESTUDO] Pieters e Wedel (2004, *Journal of Marketing*, 68(2)): em 1.363 anúncios impressos, com eye tracking em mais de 3.600 consumidores, o elemento pictórico captou atenção independentemente do tamanho, e o texto captou atenção em proporção ao tamanho.
- Transferência: [INFERÊNCIA] a imagem é o que se nota primeiro; o texto precisa de tamanho para ser lido. Limite: o estudo é de anúncio impresso e não separa rosto de objeto.

**Passo 7. Pessoa, objeto ou símbolo.**

| Situação | Caminho | Limite |
|---|---|---|
| Canal faceless, sem retrato com direito de uso | Objeto, símbolo, mapa ou ilustração declarada como ilustração | Sem dado de CTR comparando objeto e rosto; teste obrigatório |
| Figura histórica com retrato de época e origem registrada | Retrato com fonte e data anotadas | Origem não verificada reprova no portão G1 |
| Pessoa envolvida em caso real (acusado, vítima adulta, familiar) | Rosto só com direito e análise ética; tarja ou silhueta não resolvem sozinhas | Não é orientação jurídica |
| Criança vítima | Sem imagem da criança; checar a posição pública da família | Critério de julgamento, não medido |

- [DADO, terceiro] vidIQ: rosto em 69% de 500 miniaturas de vídeos que estouraram, e em 80% dos maiores overperformers. Amostra só de sucessos, sem denominador: não permite calcular efeito (correlação, não causa).
- [DADO, terceiro] 1of10, via Search Engine Journal: em mais de 300 mil vídeos virais, rosto teve desempenho parecido com ou sem rosto, com diferença maior por nicho. Mede views, não CTR.
- [ESTUDO] Crouzet, Kirchner e Thorpe (2010, *Journal of Vision*): em tarefa de laboratório, a latência mínima foi de cerca de 110 ms para rostos, 120 ms para animais e 140 ms para veículos. Não há clique nem feed.
- Conclusão: a escolha é empírica. [INFERÊNCIA] Um rosto pode atrair o olhar antes do elemento principal; é hipótese a testar.

**Passo 8. Expressão (só se houver rosto).**
- Critério: a expressão corresponde ao primeiro bloco do vídeo. Expressão sem fato que a sustente é risco de clickbait.
- Evidência: [DADO, terceiro] Kapwing (setembro de 2024) classificou a emoção do rosto mais proeminente com reconhecimento facial automático e associou emoções positivas a mais views. O desfecho é views, não CTR (dossiê de psicologia do clique, A15). [DADO, terceiro] vidIQ: expressão extrema em cerca de 1 em cada 20 miniaturas de sucesso. [OFICIAL, qualitativo] o guia recomenda emoções universais, como um rosto chocado, para público casual. [PRACTITIONER] grito forçado é lido como clickbait.
- Limite: não há dado de CTR por expressão.

**Passo 9. Cor e contraste.**
- Critério: o ponto focal se separa do fundo quando a miniatura é convertida para tons de cinza. Esse teste é checagem própria, não validada [INFERÊNCIA].
- Evitar vermelho, branco e preto como cor dominante, porque se confundem com a interface do YouTube [PRACTITIONER; sem medição primária].
- Observação do corpus: fundo escuro e vermelho aparecem em vários vídeos (Kroll, a empresa chinesa, Hitler em Portugal). [DADO, observação] Não há evidência de que isso ajude ou atrapalhe.

**Passo 10. Texto.**
- Critério: uma unidade de texto, de três a cinco palavras [PRACTITIONER]. Nos breakouts do vidIQ, a mediana era de cinco palavras [DADO, correlacional].
- Não repetir o título palavra por palavra, salvo decisão deliberada. Algumas miniaturas do corpus repetem o título quase inteiro (Dama de Elche); outras repetem só o rótulo do caso (Die Hexen von Villach).
- Revisão por falante nativo antes do teste. Exemplo: a miniatura de Schlachtbericht (youtube.com/watch?v=590Pbg4zXAI) traz "SS-Panzer im Prochorowka" (Blindados SS em Prokhorovka). O uso alemão corrente é "bei Prochorowka" [DADO, texto de referência citado no dossiê].
- Pronome sem antecedente: "SIE WARTETEN." (Eles esperaram.), em "Warum ließ Hitler 350.000 Soldaten in Norwegen, während Berlin fiel?" (youtube.com/watch?v=fQtCsnD8ork). O antecedente existe só no título. Trocar por sujeito explícito ou testar as duas versões [INFERÊNCIA].

**Passo 11. Portões antes de publicar.**
- Aplicar os cinco portões da seção 6.1: direito de uso, prova ligada à fonte, arquivo que confere, fatos e status com fonte e data, ética e política.
- Exemplo que reprova no portão G2: Archivo Criminal, "La encontró en la cama con otro hombre y la asesinó | Todo quedó grabado | RESUELTO" (youtube.com/watch?v=5dBKrFQyHkg). A miniatura traz um recorte em tons de cinza no estilo de câmera de segurança, com seta vermelha [DADO]. A pesquisa não encontrou reportagem sobre o caso do título, e o registro não foi ligado a nenhuma fonte. Regra: prova visual só entra com a fonte do registro.
- Exemplo que reprova no portão G3: Designers Que Usaram 100% Do Cérebro (youtube.com/watch?v=ha_mqcCBcQo). A imagem recebida traz o texto "GUARDA-CHUVA MÁGICO" (guarda-chuva mágico), sem relação com o título nem com a descrição [DADO]. Regra: conferir o arquivo pelo ID do vídeo antes de qualquer análise ou teste.
- Política: [OFICIAL] a política de miniaturas proíbe miniatura que leve o espectador a esperar algo que não está no vídeo; gore feito para chocar está na lista; contexto documental ou educativo pode ser aceito caso a caso (dossiê de título e miniatura, item 6).

**Passo 12. Variantes e registro.**
- Decisão: 2 ou 3 variantes, com diferença grande entre elas e uma variável principal por vez. Exemplo construído (não é do corpus): para um vídeo sobre um cerco histórico, variante A é um mapa sem rótulos com o texto "O CERCO"; variante B é o retrato do comandante com o mesmo texto. Variável única: a âncora. Título idêntico.
- Critério de arquivo: resolução de pelo menos 720p. [OFICIAL] Se alguma miniatura ficar abaixo disso, o teste reduz todas as variantes para 480p (lido na Central de Ajuda).
- Critério de diferença: [OFICIAL] a página do teste recomenda variantes bem diferentes entre si. Variantes parecidas tendem a dar Performed Same ou Inconclusive (seção 7).
- Registro por publicação: arquivo exato, data, título, relação título–miniatura, arquétipo, nota da rubrica e, depois, impressões, CTR por origem, watch time share, AVD, APV e retenção aos 30 s. Anotar se a data é anterior ou posterior a 24/08/2026 (ver 6.4).
- Não trocar título ou miniatura durante o teste: [OFICIAL] a troca interrompe o experimento.

### 5.3 Arquétipos

Convenções: [DADO] significa miniatura ou metadado observado no corpus. A razão de outlier vem da seleção e não foi verificada. Seis vídeos com razão entre 4,7 e 12,8 têm miniatura sem texto legível (empresa chinesa, Flight 370, Drake Passage, Miyako, Afonso Henriques e Os primeiros humanos). Eles coexistem com sucesso e não permitem concluir que texto ausente ajuda. Nenhum arquétipo tem curva de retenção ou CTR no corpus.

#### A. Documentário: figura, período ou tese

- **Quando usar:** o vídeo explica uma figura, um período ou uma decisão com tese ou arco (biografia, análise de decisão, guerra por fases).
- **Promessa:** quem era a figura, em qual escala ou por que algo aconteceu.
- **Padrão:** retrato ou ilustração de época, com direito declarado, e um segundo plano de contexto (mapa, cidade, objeto de época). Um rótulo de nome, categoria ou pergunta curta.
- **Exemplos:**
  - Ampulheta, "QUEM FOI HITLER: a história completa" (youtube.com/watch?v=lGbl3BFD17k). Miniatura: "HITLER" no topo e a ilustração de um homem com o rosto dividido em duas metades de sombreado diferente [DADO]. Trecho da descrição: "Quem foi Hitler antes do poder e longe dos discursos" [DADO]. A miniatura não mostra "antes do poder". Ler o lado claro como fase anterior é [INFERÊNCIA]. Razão 4,4 (674 mil contra 153 mil; seleção).
  - Geschichte der Welt, "Der Dreißigjährige Krieg | Die Komplette Geschichte..." (A Guerra dos Trinta Anos | A história completa; youtube.com/watch?v=rtmNK_QpwSw). Miniatura: retrato de época com armadura e um mapa com manchas vermelhas, e o texto "Der Dreißigjährige Krieg" [DADO]. O mapa mostra dano territorial sem número; "completa" fica só no título. Razão 12,8 (seleção).
  - Variante causal: "Warum ließ Hitler 350.000 Soldaten in Norwegen, während Berlin fiel?" (Por que Hitler manteve 350 mil soldados na Noruega enquanto Berlim caía?; youtube.com/watch?v=fQtCsnD8ork). Miniatura: "SIE WARTETEN." com fiorde, artilharia e um soldado de costas [DADO]. A imagem mostra espera, não a causa. Razão 12,3 (seleção).
  - Variante de curiosidade histórica: "Doku: Wie war Sex im Mittelalter?" (Documentário: como era o sexo na Idade Média?; youtube.com/watch?v=y1KRwUvJw0w). Miniatura: "SEX IM MITTELALTER?" (Sexo na Idade Média?) sobre duas figuras de época [DADO]. Razão 43,9 (1,8 milhão contra 41 mil; seleção). Não atribuir o desempenho à miniatura: título e tema também contam.
- **Contraindicações:** retrato sem origem registrada; superlativo sem critério. Exemplo: "DOM DINIS | O Rei que fez tudo o que quis" (youtube.com/watch?v=n6qfrtVi_Us). A miniatura pergunta "O MELHOR REI?", o título afirma "fez tudo o que quis" e a descrição fala em "o rei português mais importante" [DADO]. São três formulações para uma figura. O vídeo precisa sustentar uma delas com critérios explícitos.
- **Teste:** três vídeos com nome na miniatura e três com pergunta causal, mesmo tema e duração parecida. Comparar CTR por origem e AVD (seção 8). A amostra mínima precisa ser definida antes, com a regra da seção 6.5.

#### B. Mistério: pergunta aberta sem resposta consensual

- **Quando usar:** há dúvida real e documentada (identidade, função, causa, mecanismo, desaparecimento) sem resposta pública consensual.
- **Promessa:** o que existe ou o que aconteceu, e o que segue sem explicação.
- **Padrão:** objeto, lugar ou representação do objeto, sem rosto e sem a resposta visível; ilustração ou modelo sem rótulos. A pergunta fica no título.
- **Exemplos:**
  - LEMMiNO, "The Vanishing of Flight 370" (O desaparecimento do voo 370; youtube.com/watch?v=kd2KEHvK-q8). Miniatura: ilustração de avião comercial em diagonal, sem texto, sem destroço e sem mar [DADO]. O título nomeia o evento; a imagem mostra o objeto intacto, sem indício de sumiço. Razão 7,5 (30 milhões contra 4 milhões; seleção).
  - RealLifeLore, "What's Hidden Under the Ice of Antarctica?" (youtube.com/watch?v=KOnB47PyZJw). Miniatura: "UNDER THE ICE IN ANTARCTICA" (Sob o gelo da Antártida) sobre um render do continente sem o gelo, sem feições rotuladas [DADO]. A fórmula "O que está escondido sob..." aparece em pelo menos três títulos nos resultados de busca, então está saturada [DADO, busca]. Razão 5,4.
  - Canal del Misterio, "El Misterio De La Dama De Elche" (youtube.com/watch?v=2zBOLPYurHQ). Miniatura repete o título em três linhas e acrescenta um rosto ilustrado e uma cidade futurista [DADO]. É um caso (n = 1, 6.200 views). O cenário precisa ser explicado ou declarado como reconstrução.
  - Contraexemplo: Sleepy History, "What lies beneath Trafalgar Square?" (youtube.com/watch?v=v_9omSEaMr0). Capa: "LONDON" sobre um skyline; a praça e o "embaixo" não aparecem na capa [DADO]. A pergunta tem objeto no título e nenhum objeto visual. A razão de 115,6 não serve como evidência, porque a mediana é de 8.650 e a base não foi verificada.
- **Contraindicações:** mistério sem fonte. O dossiê encontrou páginas de conspiração sobre o mesmo tema e as descartou. Também não se usa "sem resposta" quando já há sentença. E não se promete registro sem registro verificado (Archivo Criminal, passo 11).
- **Teste:** duas miniaturas com o mesmo título, uma com objeto isolado e outra com objeto em contexto (mapa, rota). Métrica: CTR por origem e watch time share (seção 7).

#### C. História real: caso criminal ou evento com vítimas

- **Quando usar:** há fatos datados, vítimas e desfecho documentados por fonte primária ou jornalismo de época.
- **Promessa:** o caso, o mecanismo e o resultado.
- **Padrão:** no máximo três elementos: (1) rótulo do caso (nome da vítima já público, apelido documentado, local ou mecanismo); (2) um elemento de mecanismo (fogo, aplicativo, objeto, câmera); (3) tratamento da identidade (sem rosto, silhueta, tarja ou foto com direito). Superlativo só com o critério mostrado no vídeo.
- **Exemplos:**
  - História de Kroll: "Serienmörder aus Duisburg - Der Ruhrkannibale" (Assassino em série de Duisburg – O canibal do Ruhr; youtube.com/watch?v=4Km6CKepj7M, canal Verbrechen im Rückblick). Miniatura: "Joachim Kroll" em destaque e "Der Ruhrkannibale" menor, sobre retrato em preto e branco e céu industrial escuro [DADO]. O título traz a categoria; a miniatura não. Razão 4,6 (169 mil contra 37 mil). A origem da fotografia não foi verificada, e reutilizá-la exige checagem de direitos.
  - Die Hexen von Villach (youtube.com/watch?v=TU3xntt-M8s, canal Real Crime Deutschland). Miniatura: "Die Hexen von Villach" (As bruxas de Villach) em amarelo; cena noturna de prédio com fumaça e bombeiros; rosto de mulher com tarja preta sobre os olhos [DADO]. O título traz "Österreichs schlimmste Sektenführerin" (a pior líder de seita da Áustria); a miniatura omite o superlativo. O roteiro precisa mostrar o critério. Razão 15,6 (seleção). O dossiê relata que a sentença de primeira instância foi parcialmente anulada e que a pena de uma das acusadas foi elevada depois. Verificar o status atual antes de publicar.
  - Doppelgänger (Ingolstadt, youtube.com/watch?v=am_Jp5hV-vg, canal Insolito). Miniatura: duas fotografias lado a lado, seta vermelha e o texto "DER INSTAGRAM-MORD" (O assassinato do Instagram) [DADO]. O mecanismo está na miniatura; o conceito, no título. Razão 3,8 (seleção). Há um documentário sobre o mesmo caso na Prime Video, lançado em 16/10/2025, disputando a mesma busca [DADO].
  - Cold Case Detective, "3 People Who Disappeared Then REAPPEARED Years Later..." (youtube.com/watch?v=C9tlBZjS6JY). Miniatura: "MISSING 1981" (desaparecido em 1981) e "FOUND IN 2006" (encontrado em 2006), com seta sobre o cabelo de uma das figuras [DADO]. A miniatura mostra um caso; o título promete três. O verbo diverge ("reappeared" contra "found"). Razão 42,1 (2 milhões contra 47.500).
  - Canal Prohibido, "EL ASESINATO DE JAMES BULGER" (youtube.com/watch?v=Uo10088FXx4). Miniatura: "EL NIÑO / JAMES BULGER" (O menino / James Bulger) com efeito de falha e fita de cena de crime, sem rosto [DADO]. A vítima é uma criança. Razão 32,9, sobre uma mediana de 10 vídeos. O risco principal é o enquadramento de horror sobre uma criança real (portão G5).
  - Delitos de Sangre, "La Masacre de EL Señorial" (youtube.com/watch?v=Dg7-risWecc). Miniatura: "LA MASACRE DEL SEÑORIAL" (O massacre do Señorial) sobre uma fachada em preto e branco com a placa "FARMACIA SEÑORIAL" e uma mulher em cor [DADO]. Não confirmei que o prédio é o local do crime. Regra: foto de local só com identidade confirmada por fonte. Razão 141,6, sobre mediana de 805.
- **Pré-revelação:** se a miniatura mostra o fato central, o primeiro bloco precisa abrir uma pergunta nova. Exemplo: Moskvin, "Das Horrorhaus des Anatoly Moskvin" (youtube.com/watch?v=kbhVAqWbg8I). A miniatura traz "Puppen aus MENSCHEN" (Bonecas feitas de SERES HUMANOS). O roteiro deve abrir cedo outra pergunta, como quantas, quem ou como foi descoberto [INFERÊNCIA; regra do dossiê, não testada].
- **Contraindicações:** vítima criança sem avaliação ética; foto de pessoa ou local sem identidade confirmada; acusado apresentado como culpado antes de sentença final, quando o correto é "acusado" ou "acusada" com o status declarado; sangue e corpos em destaque (política de gore).
- **Teste:** miniatura com mecanismo contra miniatura só com rótulo do caso. Métrica: CTR por origem e AVD. Tema e canal confundem o resultado.

#### D. Curiosidade, lista ou fenômeno explicado

- **Quando usar:** o vídeo é um ranking, uma lista, uma explicação de "o que é" ou um contraste antes e depois com explicação.
- **Promessa:** o número e o critério no título; o item na miniatura.
- **Padrão:** (a) uma unidade ampliada (objeto, detalhe, insígnia); (b) três itens rotulados como amostra, quando o título diz "10"; (c) contraste antes e agora, com o termo medido explicado no vídeo.
- **Exemplos:**
  - Canal das Curiosidades, "10 MICRONAÇÕES AO REDOR DO MUNDO" (youtube.com/watch?v=5ZIPz_Yehno). Três painéis com rótulos "REINO GAY", "KUGELMUGEL" e "SEALAND" [DADO]. A miniatura mostra três dos dez; o número está só no título. Razão 6,6 (548 mil contra 83.500). O status de Sealand diverge entre fontes, então o critério de inclusão precisa ser definido antes do roteiro. A origem de "REINO GAY" não foi encontrada.
  - History Check, "Die Dienstgrade der Waffen SS | Eine Übersicht" (Os graus da Waffen-SS | Uma visão geral; youtube.com/watch?v=UsmWUSLl6kw). Miniatura: ilustração de soldado e duas abas pretas com runas SS e pips prateados; texto "Dienstgrade der Waffen-SS" [DADO]. A contagem dos pips não se lê na miniatura de baixa resolução. O hífen da miniatura diverge do título. Razão 25,7 (seleção).
  - Pero eso es otra Historia, "Los TSUNAMI más GRANDES de la Historia | TOP 10" (youtube.com/watch?v=cRrxyfOEq9A). Miniatura: "TSUNAMIS Y OLAS MONSTRUO / EL TERROR DE LOS MARES" (Tsunamis e ondas monstro / o terror dos mares) sobre uma onda de crista quebrando e um barco pequeno [DADO]. Um material didático de oceanografia citado no dossiê diz que o tsunami não se parece com onda que se enrola e quebra na costa [fonte secundária, material didático não revisado por pares]. A imagem mostra o que o próprio material corrige. Razão 22,6 (6,2 milhões contra 274,5 mil). Se a ilustração é usada, deve ser marcada como ilustração.
  - Economía Ilustrada, "VIVIENDA en ESPAÑA - ¿Por qué NO se puede arreglar?" (youtube.com/watch?v=d6E3jM68LJg). Miniatura: "ANTES vs AHORA" (Antes vs agora) e "1.200€" sobre ilustração cartoon [DADO]. O preço não diz o que mede; o vídeo precisa dizer. Razão 2,5 (418 mil contra 170,5 mil).
  - Curiosidad Sin Fin, "¿Por qué casi el 60% de los peruanos vive en la costa?" (youtube.com/watch?v=1xROfxQ5Ydw). Miniatura: "EL IMÁN LLAMADO LIMA" (O ímã chamado Lima), com setas de dois lados [DADO]. O título fala da costa; a miniatura troca a região pela cidade. Dado público citado no dossiê: 59% da população na costa em 2022, e cerca de 10 milhões em Lima (Forbes Perú, citando o INEI). A razão de 21,2 não é evidência: são 773 views contra mediana de 36 em 24 vídeos.
- **Contraindicações:** lista sem critério de ordenação; mito apresentado como fato na miniatura. Exemplo: "Designers Que Usaram 100% Do Cérebro" (youtube.com/watch?v=ha_mqcCBcQo). A premissa é tratada como não comprovada por fontes secundárias do dossiê (Gazeta do Povo, 2025; Wikipédia em inglês), e a miniatura não confere com o vídeo (passo 11). Também evitar ilustração de fenômeno apresentada como registro, e unidade trocada entre título e miniatura.
- **Teste:** unidade ampliada contra três itens rotulados, mesmo tema. Métrica: CTR por origem e AVD.

**Lacunas desta subseção**
- Nenhum arquétipo tem CTR ou curva de retenção no corpus; não há vídeos de baixo desempenho para comparação.
- Origem das fotos de Kroll, Clodimar, Afonso Henriques e Dinis não verificada.
- Política específica para símbolos de regimes históricos em miniatura não verificada. A miniatura de "Segunda Guerra Mundial: do primeiro tiro ao último dia" (youtube.com/watch?v=mTVdsVL8Y0U), com bandeiras e comício, exige revisão de política antes da publicação. Não identifiquei símbolo específico.
- Monetização: a miniatura de Confederates (youtube.com/watch?v=S66Bs8ixvdQ) tem bandeira e respingos vermelhos. O dossiê levanta a possibilidade de revisão de monetização; não verifiquei.

## 6. Framework de avaliação

O processo tem três estágios: portões eliminatórios, rubrica com teste em tamanho reduzido (antes de publicar) e leitura pós-publicação com dados do Studio. Pesos, notas de corte e tamanhos de teste são heurísticas a calibrar com dados do canal (6.5). Nenhuma fonte pública que li valida os pesos.

### 6.1 Portões (eliminatórios)

Se um portão falha, a miniatura não é pontuada nem publicada até ser corrigida.

| Portão | Pergunta | Passa se | Base |
|---|---|---|---|
| G1. Direito de uso | Cada imagem tem origem e licença? | Documento de licença ou origem registrada | Vários exemplos do corpus têm origem não verificada; reutilizar exige checagem [INFERÊNCIA] |
| G2. Prova ligada à fonte | Todo registro, documento ou cena mostrado tem fonte? | Fonte com data, arquivo ou sentença | Archivo Criminal (youtube.com/watch?v=5dBKrFQyHkg) |
| G3. Arquivo confere | ID, texto e imagem pertencem ao vídeo? | Conferência pelo ID do vídeo | Designers (youtube.com/watch?v=ha_mqcCBcQo) |
| G4. Fatos e status | Nomes, números, datas e status jurídico têm fonte e data? A divergência está declarada? | Tabela de fatos completa, com a versão escolhida e o motivo | Divergência de data no caso Clodimar Pedrosa Lô: 23 ou 24 de novembro de 1967, conforme a fonte [DADO]. A transcrição do vídeo indica outubro de 1970, data que não aparece entre as fontes citadas; confrontar com fonte primária e declarar a versão adotada antes de publicar. Status recursal em Villach (passo 3 do arquétipo C) |
| G5. Ética e política | Há criança vítima, gore, sangue ou símbolo que o público lerá como endosso? A miniatura engana sobre o conteúdo? | Itens revisados e justificados | [OFICIAL] política de miniaturas: enganosa é vedada; violência feita para chocar está na lista; exceção documental caso a caso. Caso Bulger: ver arquétipo C |

### 6.2 Rubrica pré-publicação

Dez critérios, pontuados de 0 a 2. O peso é heurística.

| Critério | Peso (heurística) | O que observar | 0 | 1 | 2 |
|---|---|---|---|---|---|
| 1. Tema em uma olhada | 2 | Pessoa de fora diz o tema após o teste de 6.3 | Não acerta | Acerta a categoria (guerra, crime, lista) | Acerta o caso, o objeto ou a figura |
| 2. Legibilidade reduzida | 2 | Texto e ponto focal na versão reduzida | Ilegível | Legível com esforço | Legível de imediato |
| 3. Ponto focal | 1 | Quantos elementos disputam o olhar | Dois ou mais com peso igual, ou nenhum | Um dominante com competidor forte | Um dominante; o resto é fundo |
| 4. Promessa pagável | 2 | Cada elemento da miniatura aparece no vídeo, com minuto registrado | Algum elemento não aparece | Aparece só depois do primeiro bloco, ou só em parte | Todos aparecem nos primeiros 90 s, ou a lacuna é declarada |
| 5. Relação título–miniatura | 1 | Os papéis são distintos? | Contraditória sem justificativa editorial | Redundante | Complementar |
| 6. Lacuna dimensionada | 1 | A miniatura abre pergunta sem entregar a resposta central? | Entrega a resposta central ou sugere resposta falsa | Revela o fato central sem pergunta nova | Abre pergunta e não entrega a resposta |
| 7. Diferenciação na busca | 1 | Comparada com os 4 primeiros resultados do mesmo caso | Quase igual a outra | Parecida em um eixo | Distinta em composição, cor ou texto |
| 8. Coerência de formato | 1 | Há pessoa? O vídeo a mostra ou explica? | Contradiz o formato declarado | Pessoa sem papel claro no vídeo | Sem pessoa, ou pessoa que o vídeo mostra |
| 9. Contraste | 1 | Ponto focal em escala de cinza | Some | Separa só na cor | Separa em cinza |
| 10. Linguagem | 1 | Revisão por falante nativo | Erro de idioma ou de sentido | Correta, mas ambígua (pronome sem antecedente) | Correta e sem ambiguidade |

- Pontuação máxima: 26 (soma dos pesos × 2).
- Notas de corte, heurística [INFERÊNCIA], sem validação:
  - Total de 20 ou mais e nenhum zero em critério de peso 2: segue para o teste de 6.3.
  - Total entre 14 e 19: revisar primeiro o critério de menor nota.
  - Total abaixo de 14, ou zero em critério de peso 2: refazer a âncora ou a promessa.
- Lacuna no critério 6: a literatura lida mostra que o efeito da concretude depende do conjunto. Em manchetes de notícia, um modelo sobre testes A/B do Upworthy previu que mais concretude reduziria o CTR para a maioria dos casos testados, mas não para todos (PMC11704130, lido só em trecho) [ESTUDO, modelo, notícia]. Não maximizar a pontuação do critério 6 sem teste.
- Lacuna: a rubrica não mede CTR. Uma miniatura pode pontuar bem e ter CTR baixo.

**Exemplo construído (não é do corpus):** documentário sobre um comandante, com retrato tirado de um site sem licença registrada. O portão G1 reprova. A rubrica não é aplicada até que o retrato seja substituído ou tenha origem e licença documentadas.

### 6.3 Teste em tamanho reduzido

1. **Montar a lista simulada.** Coloque a miniatura candidata entre três ou quatro miniaturas reais do mesmo caso, capturadas no mesmo dia na busca ou nas sugestões. [OFICIAL] Uma impressão conta só se a miniatura ficar visível por mais de 1 segundo com pelo menos metade da área na tela, e as miniaturas concorrem com outros vídeos em cada superfície (Central de Ajuda, lida no dossiê de testes). [OFICIAL] As miniaturas aparecem em tamanhos diferentes conforme o dispositivo. [INFERÊNCIA] Testar pelo menos um tamanho de celular e um de tela maior.
2. **Reduzir.** Reduza a imagem até o tamanho de lista de celular. Se a âncora desaparece antes do texto, a âncora está pequena demais [heurística, não validada].
3. **Teste de desconhecido.** Mostre a versão reduzida, sem contexto, por poucos segundos a cinco pessoas fora do canal. A janela de exibição (3 a 5 segundos) e o número de pessoas são escolhas minhas, sem validação. Pergunte: sobre o que é o vídeo? O que você espera ver? Que pergunta você acha que ele responde? Registre o acerto do tema (critério 1) e a expectativa.
4. **Teste de cinza.** Converta para tons de cinza. O ponto focal ainda se destaca? (critério 9).
5. **Teste de desfoque leve.** O elemento principal ainda se reconhece? (critérios 2 e 3). [INFERÊNCIA]
6. **Teste de promessa.** Depois de pontuar, abra o roteiro e marque o minuto da primeira aparição de cada elemento da miniatura (critério 4).

Limites: cinco pessoas não têm poder estatístico. Pessoas de fora podem não ser o público-alvo. O teste mede legibilidade e entendimento, não CTR. Quando houver teste nativo com impressões suficientes, o resultado do Studio vale mais (seção 7).

### 6.4 Leitura pós-publicação

Ler sempre por origem de tráfego e na mesma janela de tempo. Os sinais abaixo são leitura diagnóstica, não veredito.

| Sinal no Studio | Leitura | Ação |
|---|---|---|
| CTR sobe; AVD e APV sobem | Pacote coerente com o vídeo | Manter; registrar arquétipo e nota |
| CTR sobe; AVD cai; impressões abaixo do esperado | Os três sinais que a FAQ oficial descreve como assinatura de clickbait | Revisar critérios 4 e 5; checar minutos de pagamento |
| CTR sobe; AVD cai; impressões não caem | Não é a assinatura completa da FAQ; promessa a checar | Checar pagamento da promessa no primeiro bloco |
| CTR cai; AVD sobe | Possível filtragem de audiência | Não decidir pelo CTR sozinho; interpretar na seção 8 |
| CTR cai; AVD cai | Pacote pior nos dois eixos | Revisar critérios 1, 4 e 5 |

Notas:
- [OFICIAL] A FAQ de impressões e CTR descreve o sinal de clickbait como CTR alto, AVD baixo e impressões abaixo do esperado, juntos. Nenhum desses sinais isolado prova clickbait.
- [OFICIAL] O resultado Inconclusive não é fracasso: a primeira versão enviada fica como padrão (seção 7).
- [OFICIAL] Troca sequencial de miniatura confunde origem e audiência; a FAQ alerta contra isso. Usar o teste nativo para comparar variantes.
- [OFICIAL] Em 24/08/2026, a contagem de visualizações passou a ocorrer quando o vídeo começa a tocar, inclusive em vídeos longos. Como o CTR usa visualizações no numerador, registros antes e depois dessa data não são diretamente comparáveis. Não consegui medir o tamanho do efeito.
- Quando ler o CTR: [OFICIAL] a FAQ desaconselha olhar o CTR logo após a publicação e pede volume substancial de impressões antes de decidir. Divergência: um texto de terceiro atribui ao YouTube a leitura nas primeiras 24 horas em vídeos com impressões acima da média. Não confirmei essa recomendação, e ela contradiz a leitura da FAQ. Até verificar, usar a regra da FAQ.
- Retenção: o relatório de retenção do Studio é a única curva disponível, e só para vídeos do próprio canal. Citado no corpus como documentação oficial, mas a página não foi lida nesta coleta. Nunca comparar com curva de vídeo de terceiro, que não é pública.

### 6.5 Calibração com dados do canal

1. **Registrar cada publicação:** nota por critério, arquétipo, relação título–miniatura, se houve teste e o resultado, CTR por origem, AVD, APV e retenção aos 30 s.
2. **Definir o tamanho antes de decidir.** A nota técnica de Evan Miller (2010, não revisada por pares) dá n ≈ 16σ²/δ² por grupo, com σ² = p(1 − p) e δ o menor efeito que interessa. [INFERÊNCIA, cálculo meu] Com p = 5% e δ = 2 pontos percentuais, são cerca de 1.900 impressões por variante. Abaixo disso, a leitura é descritiva. A fórmula assume impressões independentes; a mesma pessoa vendo a miniatura várias vezes infla a amostra efetiva.
3. **Comparar só o comparável:** mesmo tema, duração próxima e mesma origem. Views não medem qualidade narrativa, então não servem como medida da rubrica.
4. **Ajustar um critério por vez,** e só se a diferença se repetir em mais de um vídeo do mesmo arquétipo.
5. **Tratar a rubrica como registro de decisões,** não como previsão, enquanto o histórico for curto.

Limites: o teste nativo do Studio tem parâmetros não publicados, e a fórmula não se aplica diretamente a ele (dossiê de testes, C3). O corpus de exemplos não serve para calibrar: não tem CTR nem denominador.

### Lacunas desta seção

- Pesos, notas de corte e tamanhos de teste: sem fonte pública. São propostas.
- Teste de desconhecido com cinco pessoas e janela de 3 a 5 segundos: sem validação e sem poder estatístico.
- Legibilidade em tamanho de feed: não encontrei estudo revisado por pares.
- Efeito de rosto, expressão, cor e texto sobre CTR de vídeo longo: não encontrei experimento primário.
- Lacuna de curiosidade em miniatura de vídeo longo: a literatura lida é de manchete de notícia.
- Status jurídico dos casos com recurso: deve ser verificado na data da publicação; não verifiquei.
- Política específica para símbolos de regimes históricos: não verificada.
- Se o Studio mostra CTR separado por variante no teste nativo: não confirmado (seção 7).
- Divergência sobre CTR nas primeiras 24 horas: não resolvida (6.4).

## 7. Testes A/B

**Legenda de fontes (vale para as seções 7 a 9)**
- [AB-HELP] https://support.google.com/youtube/answer/16391400?hl=en: Help oficial do teste A/B de títulos e miniaturas (lida).
- [FAQ-CTR] https://support.google.com/youtube/answer/7628154?hl=en: FAQ oficial de impressões e CTR (lida).
- [IMP-HELP] https://support.google.com/youtube/answer/9314486?hl=en: Help oficial de impressões (lida).
- [PERF-HELP] https://support.google.com/youtube/answer/12220281?hl=en-ie: Help oficial de performance de conteúdo (lida).
- [POL-MIN] https://support.google.com/youtube/answer/9229980?hl=en-WS: política oficial de miniaturas (lida).
- [MILLER] https://www.evanmiller.org/how-not-to-run-an-ab-test.html: nota técnica de Evan Miller (2010), não revisada por pares (lida).
- [COMUNIDADE] https://support.google.com/youtube/thread/393332200: post oficial da comunidade de ajuda (só trecho).
- [PPC] https://ppc.land/youtube-expands-a-b-testing-to-include-titles-alongside-thumbnails/: cobertura de imprensa especializada (só trecho).
- [VIDIQ-TESTE] https://vidiq.com/blog/post/youtube-launches-new-thumbnail-testing-tool/: blog de fornecedor (só trecho).

**Resumo operacional**
- O teste nativo escolhe a variante pelo tempo assistido, não pelo CTR [AB-HELP]. Ele diz qual pacote acumula mais tempo de visualização na sua fatia de impressões. Não diz qual pacote recebe mais cliques.
- O rótulo Winner exige significância estatística. Método, nível de significância, poder e tamanho de amostra não são publicados [AB-HELP]. A decisão não é reproduzível fora do Studio.
- Canal pequeno, ou vídeo com poucas impressões, deve esperar Inconclusive [INFERÊNCIA, a partir das causas listadas em AB-HELP].
- Trocar a miniatura à mão e comparar CTR de períodos diferentes não é teste. A própria FAQ alerta que a diferença pode vir do tráfego, não da arte [FAQ-CTR].

### 7.1 Elegibilidade e funcionamento

| Item | O que a fonte diz | Implicação para vídeo longo |
|---|---|---|
| Interface | Só no Studio de desktop, com recursos avançados habilitados [AB-HELP] | Canal sem o recurso não tem teste nativo (ver 7.8) |
| Formato | Vídeo longo publicado entra. Shorts, lives agendadas e Premieres ainda não convertidas ficam de fora [AB-HELP] | Premiere só entra depois de virar vídeo |
| Público | Vídeos feitos para crianças ficam de fora. Conteúdo +18 precisa estar marcado como tal; a marcação errada pode custar o acesso ao recurso [AB-HELP, conforme dossiê de testes] | Conferir a classificação antes de criar variantes |
| Privacidade | Vídeos privados não entram [AB-HELP] | Não aplicável |
| Variantes | Até três. Podem ser só título, só miniatura ou combinações [AB-HELP] | Para testar miniatura, mantenha o título fixo |
| Exibição | As variantes rodam ao mesmo tempo. Uma pequena fatia do tráfego vê só a versão padrão e fica fora do cálculo. A porcentagem não é publicada [AB-HELP] | Grupo de controle não é ajustável |
| Duração | De alguns dias a duas semanas, conforme impressões e data de publicação [AB-HELP] | Vídeo com poucas impressões pode esgotar a janela sem rótulo |
| Interrupção | Trocar título ou miniatura durante o teste o interrompe, e ele precisa ser reiniciado. É possível parar em "Manage test" [AB-HELP] | Congelar o pacote antes de iniciar |
| Escolha do vídeo | A Help recomenda começar por vídeos antigos, para limitar o impacto no alcance do canal [AB-HELP] | Escolher vídeo antigo com histórico de impressões |
| Resolução | Se alguma miniatura estiver abaixo de 720p, todas as variantes são reduzidas para 480p [AB-HELP, conforme dossiê de miniaturas] | Subir todas em pelo menos 720p |
| Diferença entre variantes | A página recomenda variantes bem diferentes entre si [AB-HELP, conforme dossiê de miniaturas] | Ver 7.4, linha 6 |

### 7.2 O que o teste otimiza

- A Help declara: "we optimize tests for overall watch time over other metrics, like click-through-rate" (tradução: "otimizamos os testes pelo tempo assistido total, em vez de outras métricas, como a taxa de cliques") [OFICIAL, AB-HELP].
- A justificativa é que título e miniatura precisam fazer o espectador entender o vídeo, para que ele não gaste tempo com o vídeo errado [OFICIAL, AB-HELP].
- Consequência 1: uma variante que ganha clique e perde tempo assistido perde no critério oficial [INFERÊNCIA].
- Consequência 2: como a métrica é tempo assistido do vídeo, e não só do clique, uma promessa que o vídeo não cumpre é punida depois do clique [INFERÊNCIA].
- O teste não usa CTR como critério. A leitura de CTR fica na seção 8.

**Divergência não resolvida: o nome e a base da métrica**

| Fonte | Como descreve a métrica |
|---|---|
| [AB-HELP] | "watch time share" (fatia do tempo assistido do experimento) |
| [COMUNIDADE] | rótulo Winner pelo tempo assistido por impressão; diz que as variantes rodam de forma uniforme entre espectadores por até duas semanas |
| [PPC] | tempo assistido por impressão, com variantes exibidas em partes iguais |
| [VIDIQ-TESTE] | watch time share é a fatia creditada a quem viu cada variante; não é AVD, nem tempo total do vídeo, nem CTR |

A Help também cita diferenças de impressões entre variantes como causa de variação. [INFERÊNCIA] Se as impressões forem desiguais, fatia e tempo por impressão podem ordenar as variantes de forma diferente. Com impressões iguais, os dois coincidem (ver 8.4). Ação: quando o relatório mostrar impressões por variante, registre-as. Se forem muito desiguais, trate o rótulo como sinal fraco.

### 7.3 Como ler o resultado

| Rótulo | O que a fonte diz | Ação | Limite |
|---|---|---|---|
| Winner | Uma variante se destacou; a Help diz que o resultado é estatisticamente significativo. A vencedora é mostrada a todo o público [AB-HELP] | Adotar. Registrar métrica, impressões, datas e origem | Limiar não publicado; a diferença em pontos não decide sozinha |
| Performed Same | Desempenho parecido. O criador escolhe a que preferir [AB-HELP] | Não declarar vitória. Escolher pelo critério de promessa e coerência (8.5) | Não há decisão estatística |
| Inconclusive | Sem diferença estatística forte. A primeira título/miniatura enviada vira o padrão. O criador pode trocar manualmente [AB-HELP] | Manter o padrão. Só repetir com variantes mais diferentes ou com mais impressões | [INFERÊNCIA] Envie primeiro a variante que você aceitaria como padrão |

A Help também diz que o teste não declara vencedor quando a diferença entre as opções é pequena ou quando faltam impressões [AB-HELP].

**Regra de leitura (processo)**
1. Leia o rótulo. Só Winner autoriza troca. "Ganhou por X pontos" não é leitura válida se o rótulo não for Winner.
2. Confira qual métrica o relatório mostra: fatia ou tempo por impressão.
3. Confira as impressões por variante, se o relatório mostrar. Impressões muito desiguais enfraquecem o rótulo.
4. Confira se houve alteração de título ou miniatura durante o teste. Se houve, o resultado não é leitura limpa [INFERÊNCIA].
5. Anote data, duração e origem de tráfego.
6. Só depois, confira AVD, APV e CTR (seção 8).

**Exemplo com cautela.** Em julho de 2026, o vidIQ testou duas miniaturas no vídeo "Your Videos Don't Have to Look Amateur Anymore (Claude + Remotion)". O relatório deu 54,4% de watch time share contra 45,6%, com rótulo Winner após dois dias [DADO, VIDIQ-TESTE, só trecho]. O formato e a duração do vídeo não foram confirmados. O mesmo blog diz que uma divisão de 60/40 não basta para declarar vencedora a primeira miniatura. [INFERÊNCIA] Um caso só mostra que o rótulo depende também do cálculo e do volume de impressões, e não só do tamanho da diferença. Não serve como limiar.

### 7.4 Erros estatísticos e de processo mais comuns

| Erro | Por que engana | Como evitar | Base |
|---|---|---|---|
| 1. Parar no primeiro resultado favorável (peeking) | Checar repetidamente e parar no primeiro sinal significativo aumenta falsos positivos. Segundo a nota de Miller, para manter 5% real, o nível exigido cai a cada checagem: 2,9% com uma checagem, 2,2% com duas, 1,8% com três, 1,4% com cinco e 1,0% com dez (valores do dossiê; conferir a contagem na nota original antes de citar) | Fixar data final ou amostra antes do teste. Não encerrar por resultado parcial | [MILLER, ESTUDO, nota técnica] |
| 2. Trocar a miniatura à mão e comparar CTR de períodos | Público e origem de tráfego mudam entre períodos. A diferença pode vir do tráfego | Usar o teste nativo. Sem ele, tratar como hipótese | [FAQ-CTR] |
| 3. Decidir pelo CTR do teste nativo | O critério oficial é tempo assistido | Ler o rótulo do teste. CTR entra depois (seção 8) | [AB-HELP] |
| 4. Tratar Performed Same ou Inconclusive como vitória | Inconclusive mantém a primeira enviada; Performed Same deixa a escolha ao criador. Nenhum dos dois é vitória estatística | Registrar o rótulo sem reinterpretar | [AB-HELP] |
| 5. Mudar título ou miniatura no meio do teste | O teste para e precisa ser reiniciado. Uma troca manual vira teste sequencial sem controle | Congelar o pacote até o fim | [AB-HELP] |
| 6. Variantes quase iguais | Diferença mínima pode impedir vencedor. Mudanças pequenas exigem muito mais impressões | Testar uma variável com mudança grande (conceito, sujeito, texto principal) | [AB-HELP]; [INFERÊNCIA] |
| 7. Ignorar a mudança de audiência | Impressões iniciais vêm de quem já conhece o canal; as posteriores incluem quem nunca viu o canal | Anotar origem e datas. Não tratar a janela inicial e a final como a mesma audiência | [AB-HELP] |
| 8. Testar em vídeo sem histórico de impressões | Sem impressões suficientes, o teste não declara vencedor | Escolher vídeo antigo com histórico | [AB-HELP] |
| 9. Usar antes e depois como prova | Nos casos de terceiros, miniatura e tráfego mudaram juntos, sem controle | Usar antes e depois só como hipótese para o teste nativo | [FAQ-CTR]; casos em 8.7 |
| 10. Comparar CTR de antes e depois de 24/08/2026 | A partir dessa data a visualização conta quando o vídeo começa a tocar, inclusive em vídeo longo. O CTR usa visualizações no numerador | Marcar a data. Não comparar a série sem ajuste | [PERF-HELP] |
| 11. Dividir visualizações totais por impressões | O Studio usa só as visualizações originadas de impressões contadas | Usar o CTR do relatório | [FAQ-CTR] |
| 12. Usar regras numéricas de fornecedores | "Diferença de 20% no CTR" como atalho de vencedor; "1.000 a 5.000 impressões por variante"; "70% dos testes acham vencedor" | Não usar. Calcular com a regra da seção 7.5 | [PRATICANTE, sem fonte] |
| 13. Rodar várias vezes até aparecer vencedor | Cada rodada é nova comparação. A plataforma não publica correção para isso | Uma hipótese por teste. Registrar todas as rodadas, inclusive as sem vencedor | [INFERÊNCIA] |

### 7.5 Tamanho de amostra: regra de bolso (fora do teste nativo)

A nota de Miller dá, para comparar duas proporções, n ≈ 16·p(1−p)/δ² por grupo, em que p é o CTR de base e δ o menor efeito que se quer detectar [ESTUDO, MILLER; regra reproduzida pelo dossiê, conferir na nota]. Os valores abaixo são cálculos meus com essa regra [INFERÊNCIA]:

| CTR de base (p) | Menor efeito (δ) | n por variante (aprox.) |
|---|---|---|
| 5% | 1 ponto percentual | 7.600 |
| 5% | 2 pontos percentuais | 1.900 |
| 2% | 1 ponto percentual | 3.136 |
| 2% | 0,5 ponto percentual | 12.544 |

Com 2.000 impressões por variante e p = 5%, o menor efeito detectável fica perto de 2 pontos percentuais.

**Limites:** a regra não foi calibrada para CTR do YouTube. Supõe impressões independentes, e a mesma pessoa vendo a miniatura várias vezes infla a amostra efetiva. Não considera mudança de audiência nem mistura de origens. Não se aplica ao teste nativo, cujos parâmetros não são publicados.

**Processo:** antes de começar, escreva p, δ e o n necessário. Se as impressões previstas não chegam ao n, o resultado é exploratório e não decide.

### 7.6 Desenhos sugeridos pelo corpus (hipóteses; nenhum foi executado)

As análises do corpus propuseram os testes abaixo. Nenhum foi executado, e o corpus não tem CTR nem rótulo de teste. Métrica de decisão em todos os casos: fatia de watch time do teste nativo, com variável única.

| Vídeo (canal) | Variável única | Variante A | Variante B | Restrição da análise de origem |
|---|---|---|---|---|
| "3 People Who Disappeared Then REAPPEARED Years Later..." (Cold Case Detective, https://www.youtube.com/watch?v=C9tlBZjS6JY) | Seta vermelha sobre o painel "FOUND IN 2006" | Atual, com seta | Mesmo texto e fotos, sem seta | Direito de uso das fotos e sensibilidade com familiares não avaliados |
| "EL ASESINATO DE JAMES BULGER" (Canal Prohibido, https://www.youtube.com/watch?v=Uo10088FXx4) | Sujeito da chamada principal | "EL NIÑO" (vítima como sujeito) | "EL ASESINATO" (ato como sujeito) | Variante com a criança como sujeito retirada do teste. O caso só entra em teste com critério ético definido antes (posição pública da família, sem criança como sujeito) e só com variantes sobre o ato ou o contexto |
| "What lies beneath Trafalgar Square?" (Sleepy History, https://www.youtube.com/watch?v=v_9omSEaMr0) | Conteúdo da capa | Silhueta da cidade (atual) | Corte do solo com camadas (sugestão do corpus) | A variante B só é coerente se a narração tratar o subsolo. A palheta noturna pode atrair público de sono [INFERÊNCIA] |
| "10 MICRONAÇÕES AO REDOR DO MUNDO" (Canal das Curiosidades, https://www.youtube.com/watch?v=5ZIPz_Yehno) | Número de itens na capa | Três itens (atual) | Um item em destaque | O "10" aparece só no título. Uma capa com um item pode prometer menos |
| Verbrechen im Rückblick, "Joachim Kroll" (https://www.youtube.com/watch?v=4Km6CKepj7M) | Apelido no título | Título atual, com "Der Ruhrkannibale" | Mesmo título sem o apelido | Origem da foto de capa não verificada; checar direitos antes de usar como modelo |

**Notas de desenho**
- [INFERÊNCIA] Mudança pequena, como uma seta ou uma cor, tende a dar Inconclusive. Mudança de conceito (sujeito, cena, texto principal) tem mais chance de Winner, mas mistura causas. Para concluir sobre uma variável, teste uma por vez.
- [INFERÊNCIA] O teste nativo de título, no mesmo vídeo, é mais limpo que a comparação entre vídeos de tema parecido que o corpus propôs.
- Toda variante precisa cumprir a política de miniaturas (ver 7.7, passo 4).

### 7.7 Checklist de execução (processo)

1. Pré-requisitos: Studio de desktop com o recurso; vídeo longo já publicado; sem marcação de conteúdo infantil; classificação +18 correta, se for o caso [AB-HELP].
2. Escolha de vídeo: antigo, com histórico de impressões. Não use o vídeo principal do canal para uma hipótese arriscada [AB-HELP; INFERÊNCIA].
3. Hipótese e variável: uma variável por teste (título, miniatura ou combinação declarada). Registre a métrica de decisão e a janela prevista.
4. Variantes: bem diferentes dentro da variável. Cada uma precisa cumprir a política. A política proíbe miniatura que leve o espectador a esperar algo que não está no vídeo; conteúdo gráfico ou feito para chocar é restrito; contextos documentais, científicos ou educativos podem ter exceção caso a caso [POL-MIN]. Uma variante que promete o que o vídeo não entrega não deve ser testada.
5. Resolução: todas as miniaturas em pelo menos 720p [AB-HELP].
6. Padrão: escolha como primeira enviada a variante que você aceitaria como padrão, porque ela vence em caso de Inconclusive [AB-HELP].
7. Congelar título e miniatura até o fim do teste.
8. Registrar: datas de início e fim previstas, impressões por variante (se o relatório mostrar), origem de tráfego e se a data cruza 24/08/2026 [PERF-HELP].
9. Não encerrar por resultado parcial. Encerrar antes só para retirar variante que viole política ou cause problema [INFERÊNCIA, a partir de MILLER e AB-HELP].
10. Ler o rótulo conforme 7.3.
11. Depois do rótulo, conferir AVD, APV e CTR por origem (seção 8.5). Winner com CTR subindo e AVD caindo é sinal de alerta [FAQ-CTR].
12. Registrar o resultado com canal, vídeo, período e variável. Não generalizar para outros vídeos com um único teste [INFERÊNCIA].

### 7.8 Limites do teste nativo

- Método estatístico, nível de significância, poder e porcentagem do grupo de controle não são publicados [AB-HELP].
- O critério é tempo assistido. O teste não mede o CTR de cada variante de forma oficial (divergência em 9.2).
- Não se sabe se o relatório mostra impressões por variante. Se não mostrar, o rótulo não pode ser avaliado quanto à desigualdade de exposição.
- Canal pequeno ou vídeo com poucas impressões tende a Inconclusive. [INFERÊNCIA, a partir das causas listadas em AB-HELP]
- Shorts, lives agendadas e Premieres não convertidas estão fora do escopo e fora do teste.
- Para contas sem o recurso, não há desenho validado pelas fontes lidas. Qualquer comparação manual é hipótese.

---

## 8. CTR por origem e contexto

### 8.1 O que entra no CTR

- CTR de impressões = visualizações originadas de impressões contadas ÷ impressões contadas [OFICIAL, FAQ-CTR; IMP-HELP].
- Visualizações vindas de fora do YouTube, de cards e de end screens não entram no numerador [FAQ-CTR, conforme dossiê de testes].
- Uma impressão conta quando a miniatura aparece por mais de 1 segundo, com pelo menos 50% da área visível [OFICIAL, IMP-HELP].

| Superfície | Conta como impressão? | Fonte |
|---|---|---|
| Busca | Sim | [IMP-HELP] |
| Página inicial (inclui autoplay) | Sim | [IMP-HELP] |
| Feeds: inscrições, em alta, histórico, Assistir mais tarde | Sim | [IMP-HELP] |
| "Up Next" (próximos vídeos) | Sim | [IMP-HELP] |
| Playlists | Sim | [IMP-HELP] |
| Sites e apps externos, embeds | Não | [IMP-HELP] |
| Cards e end screens dentro do player | Não | [IMP-HELP] |
| E-mails e notificações | Não | [IMP-HELP] |
| Aba em segundo plano | Não | [IMP-HELP] |

Para vídeo longo, "Up Next" e página inicial são superfícies relevantes. A proporção entre elas não é publicada [INFERÊNCIA].

### 8.2 Faixas de referência: o que é oficial e o que circula

**Oficial**
- Metade dos canais e vídeos do YouTube fica entre 2% e 10% de CTR de impressões. É a descrição de uma distribuição, não uma meta nem uma média [OFICIAL, FAQ-CTR].
- Vídeos com menos de uma semana, ou com menos de 100 visualizações, têm faixa mais ampla [OFICIAL, FAQ-CTR].
- Direção por audiência: vídeos com poucas impressões e visualizações costumam ter CTR maior, porque o público é mais restrito e fiel. Vídeos com muitas impressões na página inicial tendem a ter CTR menor. Vídeos em que a maior parte das impressões vem da página do canal podem ter CTR maior [OFICIAL, FAQ-CTR]. A direção é oficial. A magnitude não é.
- A FAQ não publica faixa de CTR por origem (Browse, Suggested, Search) [OFICIAL, FAQ-CTR].

**De terceiros (sem método publicado; não usar como baseline)**

| Origem | Focus Digital | ytgrowth | berryviral | ytshark | teleprompter |
|---|---|---|---|---|---|
| Search | 12,5% | 8–15% | 8–15% | ~12,5% | não informado |
| Suggested | 9,5% | 5–10% | 5–10% | ~9,5% | 6–10%, atribuído ao Focus |
| Browse | 3,5% | 2–6% | 3–7% | 2–6% | não informado |

[PRATICANTE, sem método]. Fontes: https://focus-digital.co/average-youtube-ctr-organic-paid-benchmarks-2026/; https://ytgrowth.io/blog/youtube-ctr; https://berryviral.com/blog/what-is-a-good-ctr-on-youtube-and-when-to-stop-worrying/; https://ytshark.com/what-is-a-good-ctr-on-youtube/; https://www.teleprompter.com/blog/whats-a-good-click-through-rate-on-youtube.

- [INFERÊNCIA] Os valores 12,5% e 9,5% aparecem iguais em mais de um site. Podem não ser confirmações independentes. O teleprompter atribui a faixa de Suggested ao Focus, mas o Focus dá 9,5%, não 6–10%.
- Ordem entre Browse e Suggested: a maioria dos sites põe Browse abaixo. Um relato de criadores, em r/NewTubers e citado pelo ytgrowth, diz que num canal específico Suggested fica perto de 0,6% e Browse entre 10% e 12%. O relato não traz vídeo, data nem métrica completa [PRATICANTE, não verificado]. Serve para mostrar que a ordem pode inverter por canal.
- Um blog afirma que a média oficial do YouTube seria de "4% a 6%". Essa média não aparece na FAQ [PRATICANTE]. Não use.

**Ação:** compare o CTR do vídeo com o histórico do próprio canal, na mesma origem e na mesma janela de tempo.

### 8.3 Por que o CTR varia com a origem

- [OFICIAL] A miniatura concorre com outros vídeos em cada superfície: página inicial, "Up Next", resultados de busca e feeds de inscrições [FAQ-CTR].
- [INFERÊNCIA] Cada superfície tem concorrência diferente e um público com outro grau de familiaridade com o canal. A FAQ explica a variação, mas não quantifica.
- [INFERÊNCIA] Uma média geral de CTR mistura origens. Se a proporção de Browse subir, o CTR geral pode cair sem que nenhuma miniatura tenha piorado.

| Origem | Quem costuma clicar [INFERÊNCIA] | Concorrência na tela [OFICIAL, FAQ-CTR] | O que a miniatura precisa fazer [INFERÊNCIA] | Lacuna |
|---|---|---|---|---|
| Search | Quem digitou uma intenção; já tem expectativa do tema | Lista de resultados da busca | Confirmar o tema buscado e se diferenciar dos resultados parecidos | Faixa própria não publicada |
| Suggested | Quem está vendo outro vídeo; já está no assunto, mas não necessariamente no canal | Vídeos ao lado e ao fim de outro | Parecer diferente dos vizinhos do mesmo tema | Efeito da similaridade de tema não medido |
| Browse | Mistura assinantes, que já conhecem o canal, e público frio da página inicial [INFERÊNCIA a partir de B6 do dossiê de testes] | Página inicial, feeds, Em alta, Assistir mais tarde | Ser reconhecível para assinantes e dar motivo a quem não conhece o canal | Proporção entre assinantes e público frio não publicada. Uma média de Browse esconde dois públicos |

### 8.4 O número que decide: tempo assistido por impressão

- Tempo assistido por impressão = CTR × tempo médio assistido por visualização originada de impressão [INFERÊNCIA, identidade algébrica].
- Com impressões iguais entre variantes, a fatia do teste nativo e o tempo por impressão dão o mesmo ranking [INFERÊNCIA].

**Exemplo construído (não é dado medido)**

| | Variante A | Variante B |
|---|---|---|
| Impressões | 1.000 | 1.000 |
| CTR | 5% | 4% |
| Visualizações originadas | 50 | 40 |
| Tempo médio por visualização | 2 min | 3 min |
| Tempo total | 100 min | 120 min |
| Tempo por impressão | 0,10 min | 0,12 min |

B vence no critério oficial com CTR menor. [INFERÊNCIA] Essa é a forma de um filtro: a miniatura B deixa de atrair quem sairia cedo. A relação real entre CTR e tempo médio não é conhecida para nenhum canal dark. Não há dado público que a meça.

### 8.5 Quando um CTR menor é bom sinal

Não há fonte que dê um CTR ideal por origem. A decisão combina CTR, AVD/APV, impressões e tempo por impressão, sempre dentro da mesma origem e da mesma janela. [INFERÊNCIA]

Um CTR menor é bom sinal quando três condições valem juntas: a origem muda para uma de alto volume ou público frio; o tempo assistido por impressão sobe ou se mantém; e o AVD não cai. Nesse caso, o CTR menor é o custo de um filtro.

| Cenário (mesma origem, mesma janela) | Leitura | Base |
|---|---|---|
| CTR cai; tempo assistido por impressão sobe ou se mantém | Bom sinal: a miniatura deixou de atrair clique sem intenção | [INFERÊNCIA] a partir de 8.4; [AB-HELP] critério de tempo assistido |
| CTR cai; impressões sobem na página inicial ou Browse; AVD e APV se mantêm | Bom sinal provável: alcance com público mais frio, onde CTR menor é esperado | [FAQ-CTR] (volume alto tende a CTR menor). Efeito sobre AVD: [INFERÊNCIA] |
| CTR sobe; AVD cai | Mau sinal se os três sinais coincidirem (CTR alto, AVD baixo e impressões abaixo do esperado): assinatura de clickbait descrita pela FAQ. Sem a condição de impressões, a combinação é promessa a checar, não assinatura | [FAQ-CTR] |
| CTR sobe; AVD e tempo por impressão sobem | Bom sinal, mas confirme a origem: pode ser mudança de distribuição, não da miniatura | [FAQ-CTR] (composição da audiência); [INFERÊNCIA] |
| CTR cai; AVD cai | Ambíguo. Não atribua à miniatura sem separar origem e tema | [INFERÊNCIA] |
| CTR alto em vídeo com poucas impressões | Não comparar com vídeos de alto volume | [FAQ-CTR] |
| Comparação que atravessa 24/08/2026 | A série pode não ser comparável até que se verifique o efeito da mudança | [PERF-HELP] |

### 8.6 Procedimento de leitura no Studio

1. Defina antes o volume mínimo de impressões para ler o CTR, com a regra da seção 7.5 (p do histórico do canal, δ mínimo que justifica agir). Não leia CTR antes disso [FAQ-CTR, que não aconselha decidir com poucos dados; limiar [INFERÊNCIA]].
2. Janela de leitura: há divergência sobre a janela inicial (ver 9.2). Use as primeiras 24 horas só para diagnóstico de origem. Não decida por elas.
3. Abra o relatório de impressões e anote a parcela de impressões vinda de recomendação do YouTube [IMP-HELP]. O relatório "Impressions and how they led to watch time" também permite ler o tempo assistido das impressões [PERF-HELP, conforme dossiê de testes].
4. Não confirmado se o Studio mostra CTR de impressões separado por Browse, Suggested e Search. A Ajuda lida descreve CTR no nível do vídeo ou do canal; o Advanced Mode permite quebra por origem sem listar as métricas compatíveis; guias de terceiros divergem no caminho e não mostram captura. Até confirmação, o diagnóstico por origem é hipótese (ver protocolo 9.6) A Help lida não confirma que o CTR aparece separado por origem [PERF-HELP; divergência em 9.2]. Se não aparecer, registre o CTR global e não compare origens.
5. Anote a data em relação a 24/08/2026 [PERF-HELP].
6. Registre CTR, impressões, AVD, APV, tempo assistido por impressão e origem.
7. Decida pela tabela de 8.5. Nunca só pelo CTR.

### 8.7 Casos de terceiros: o que o número não permite afirmar

- **Miniatura para a aba Browse** (fornecedor de miniaturas): CTR de 3,4% para 6,1%; impressões de 80 mil para 145 mil; views de Browse de 2.700 para 8.800. Antes: 1 a 28 de julho de 2026. Depois: 29 de julho a 25 de agosto de 2026 [PRATICANTE; https://www.thumbnailcreator.com/blog/thumbnails-browse-feature-views-case-study; só trecho]. Limites: não há grupo de controle; o autor vende miniaturas; o autor diz que não houve grande mudança de título ou tema, mas não há como verificar. A janela "depois" inclui 24 e 25 de agosto de 2026, dias em que a contagem de visualizações mudou [PERF-HELP]. O efeito desses dois dias não é separável.
- **Vídeo evergreen**: CTR de 3,1% para 4,4% (+42% relativo). As impressões dobraram e o tempo assistido aproximadamente dobrou em 30 dias [PRATICANTE; https://www.clickminded.com/youtube-case-study/; só trecho]. Limite: antes e depois sem controle. A FAQ alerta que esse desenho confunde mudança de tráfego com efeito da miniatura [FAQ-CTR].

**O que dá para dizer:** nos dois casos, o CTR subiu junto com a mudança de impressões. Não é prova de efeito da miniatura. É hipótese a testar com o teste nativo (seção 7).

---

## 9. Lacunas e limites

### 9.1 Efeitos de design sem evidência primária em vídeo longo

| Pergunta | O que existe | Consequência para o playbook |
|---|---|---|
| Rosto ou personagem aumenta o CTR de vídeo longo? | Nenhum estudo primário encontrado. Laboratório: rostos são localizados em cerca de 110 ms, em tarefa de escolha sacádica, sem clique [ESTUDO, Crouzet, Kirchner e Thorpe, 2010, Journal of Vision 10(4)]. Dados de terceiros: no vidIQ, rosto aparece em 69% das miniaturas de 500 "breakouts" e em 80% dos maiores overperformers, sem denominador [PRATICANTE]. Um conjunto de mais de 300 mil vídeos (1of10, via SEJ) sugere desempenho parecido com ou sem rosto, com diferenças por nicho; mede views, não CTR [PRATICANTE] | Tratar como variável a testar, não como regra. Para canal sem rosto, objeto ou símbolo é hipótese |
| Expressão emocional | Kapwing (2024) classificou emoção com reconhecimento facial automático e relacionou a views. Sem controle de canal ou tema [DADO de terceiro] | Descreve padrão. Não prova efeito |
| Cor e contraste | Só heurísticas de praticantes. Um número de "30% mais CTR" atribuído a um estudo de 2023 não foi encontrado [PRATICANTE] | Não usar o número. Testar contraste como variável única |
| Legibilidade do texto em tamanho de feed | Nenhum estudo revisado. A Help pede fonte fácil de ler [OFICIAL]. Práticos sugerem de três a cinco palavras e fontes grossas [PRATICANTE] | Medir legibilidade no celular, em tamanho reduzido, com a rubrica da seção 6 |
| Imagem versus texto, e tamanho do texto | Pieters e Wedel (2004), Journal of Marketing 68(2): 1.363 anúncios impressos, eye tracking em mais de 3.600 consumidores. O elemento pictórico capta atenção independentemente do tamanho; o texto, em proporção ao tamanho [ESTUDO; anúncio impresso, só resumo lido]. A transferência para miniatura é [INFERÊNCIA] | Tensão aberta com a simplicidade pedida pelo YouTube. Testar tamanho do texto contra a imagem |
| Curiosity gap na miniatura | A base é de manchetes de notícia: Scacco e Muddiman (ano divergente, 2019 ou 2020) acharam menos page views para manchetes de curiosidade; ACM (DOI 10.1145/3411764.3445753) acharam mais curiosidade com manchetes não clickbait; PMC11704130 modela que, para parte das manchetes, mais concretude reduz o CTR [ESTUDO, todos de notícia] | Hipótese com mecanismo (Loewenstein, 1994, teoria lida só em resumo). Não há magnitude para miniatura de vídeo longo |
| Clickbait "bem feito" | Um blog de fornecedor defende que, quando a promessa é atendida, o clickbait é marketing; usa 7 milhões de views como prova [PRATICANTE, VIDIQ-CLICKBAIT] | Views não medem qualidade. Não usar como evidência |
| Miniatura com grupo versus pessoa | Estudo de notícias sem ano confirmado e com 221 respostas. Citação de queda de 18,6% em curtidas, fragmentada [ESTUDO fraco] | Não usar |
| Presença de imagem no CTR | Experimento de recomendação de artigos de opinião (arXiv 2101.06141): imagem de miniatura e título editorial não tiveram efeito significativo no CTR [ESTUDO, notícia em texto] | Sugere efeito pequeno em outro formato. Não transfere |
| Tempo de atenção de miniatura (1,8 s) | Número atribuído à Netflix diverge entre fontes e não foi verificado na fonte primária [PRATICANTE] | Não usar |

### 9.2 O que o YouTube não publica, ou publica de forma divergente

| Item | Situação | Fontes |
|---|---|---|
| Método, nível de significância, poder e tamanho mínimo de amostra do teste | Não publicados | [AB-HELP] |
| Porcentagem do grupo de controle | Não publicada | [AB-HELP] |
| Métrica do rótulo: fatia de watch time ou tempo assistido por impressão | Divergente. Não resolvido | [AB-HELP] versus [COMUNIDADE] e [PPC] |
| CTR por variante no teste nativo | Divergente. A Help não diz. Terceiros dizem que sim | [AB-HELP]; https://thumbnailbench.com/resources/youtube-ctr-explained; https://www.thumbmagic.co/blog/youtube-thumbnail-ctr-benchmarks |
| CTR por origem no Studio | Divergente. Confirmar no próprio Studio | [PERF-HELP]; terceiros acima |
| Faixa de CTR por origem | Não oficial | [FAQ-CTR] |
| Janela de leitura do CTR | Divergente. Um dossiê atribui à FAQ a recomendação de olhar Início e Sugeridos nas primeiras 24 horas, em vídeos com impressões acima da média. Outro lê na mesma FAQ que não se deve checar o CTR logo após o upload. Não resolvido | [FAQ-CTR] |
| CTR por idade do vídeo | Sem fonte primária. Um blog diz que a plataforma reconhece a queda; essa afirmação não aparece no texto oficial lido | Não usar como "confirmação oficial" |
| Contagem de visualizações a partir de 24/08/2026 | Mudou para contagem ao começar a tocar, inclusive em vídeo longo. A regra anterior para vídeo longo não foi encontrada. Efeito não medido | [PERF-HELP] |
| Peso da satisfação no algoritmo | Post oficial de 2019 fala em satisfação, sem números. Pesos percentuais de fontes de marketing não foram verificados e foram descartados | [OFICIAL, https://blog.youtube/news-and-events/continuing-our-work-to-improve/] |
| Magnitude da penalidade de clickbait | Não publicada. A FAQ descreve a assinatura, não o tamanho do efeito | [FAQ-CTR] |
| Critério de exceção documental em miniaturas | Caso a caso; a lista de proibições não é completa | [POL-MIN] |
| Política de "misleading metadata" | Aparece só em espelhos e blogs; a página primária não foi lida | Não verificado |
| Regras para miniaturas geradas por IA | Citadas por blogs de 2026; não verificadas na política oficial | Não verificado |

### 9.3 Limites do corpus de vídeos

- O corpus é de alto desempenho, selecionado por razão de outlier. Qualquer padrão dele é hipótese, não prova.
- Quase todos os vídeos estão sem transcrição com tempos. A exceção parcial é o J.P. Morgan, com legenda de terceiro sem marcações de tempo. Nenhum minuto de miniatura foi relacionado a retenção.
- Nenhum vídeo do corpus tem CTR, origem de tráfego, teste A/B, curva de retenção ou gráfico "most replayed" observados. Todo CTR de vídeo longo citado neste documento vem de fontes externas.
- As razões de outlier vêm do pipeline, com medianas de bases pequenas (9 a 120 vídeos). Várias não foram reverificadas.
- Views não medem qualidade narrativa. Por exemplo, a razão de 129 do vídeo "Por Que Hitler Nunca Invadiu Portugal?" não pode ser atribuída a título ou miniatura. O próprio dossiê não atribui.
- A miniatura de "Designers Que Usaram 100% Do Cérebro" (Fala Sério, https://www.youtube.com/watch?v=ha_mqcCBcQo) mostra "GUARDA-CHUVA MÁGICO" e um guarda-chuva, sem relação com o vídeo. Foi descartada. [INFERÊNCIA] Alerta de integridade: confira o arquivo pelo ID antes de usar qualquer miniatura do corpus como exemplo.
- Várias miniaturas usam fotos de origem não verificada (Kroll, Clodimar Pedrosa Lô, Dom Afonso Henriques). Checar direitos antes de copiar o modelo.

### 9.4 Limites de transferência

- **Formato:** a maior parte da evidência não é de vídeo longo. É de laboratório (Crouzet), anúncio impresso (Pieters e Wedel), manchete de notícia e blog de fornecedor. Shorts e Reels estão fora do escopo e sem validação.
- **Canal dark e faceless:** não encontrei caso verificável de canal dark de vídeo longo com miniatura, minuto e métrica pública (E4 do dossiê de miniaturas).
- **Porte do canal:** o teste exige impressões. Canais do corpus com poucos inscritos (89 em Curiosidade Sin Fin; 2.390 em Geschichte Ohne Mythos) tendem a Inconclusive. [INFERÊNCIA]
- **Idioma:** as fontes de legibilidade e de CTR são em inglês. O texto das miniaturas do corpus é em português, alemão e espanhol. A legibilidade nessas línguas não foi testada. [INFERÊNCIA]
- **Fornecedores:** os benchmarks e casos de CTR vêm de empresas que vendem ferramentas ou miniaturas (vidIQ, Focus Digital, ytgrowth, berryviral, thumbnailcreator, clickminded, vireovideo). Todos têm interesse comercial. Os números sem método são [PRATICANTE].
- **Política:** miniatura que engana é proibida. Miniaturas de true crime com corpos ou sangue têm o maior risco. A exceção documental é caso a caso e não foi validada para canais de mistério [POL-MIN]. Variantes de teste que violem a política podem gerar aviso e, em reincidência em 90 dias, strike.
- **Ética:** casos com vítima criança exigem cuidado adicional. O corpus recomendou verificar a posição pública da família antes de produzir (caso Bulger). O critério não foi medido.

### 9.5 Afirmações que o playbook não pode fazer

| Afirmação proibida | Por que não | O que pode dizer |
|---|---|---|
| "Rosto aumenta o CTR" | Sem estudo primário. Os dados de breakouts não têm denominador | "Rostos aparecem em miniaturas de vídeos que estouraram. O efeito é variável a testar" |
| "Miniatura simples ganha watch time" | Nenhum estudo de vídeo longo. Simplicidade não foi testada no critério oficial | "Simplicidade é hipótese. Testar com o teste nativo" |
| "Seu CTR de X% é normal" | Faixas de terceiros divergem; a faixa oficial é de distribuição geral | "Compare com o histórico do próprio canal, na mesma origem" |
| "Clickbait funciona" | A FAQ aponta AVD baixo como assinatura; o argumento de sucesso usa views | "CTR alto com AVD baixo é sinal de alerta" |
| "A miniatura causou o outlier" | Razão de views entre vídeos, sem controle de tema, tráfego ou idade | "Tema, distribuição ou miniatura. Não separável com o corpus" |
| "1.000 a 5.000 impressões por variante bastam" | Regra sem fonte | "Calcule com a regra da seção 7.5, com o p e o δ do próprio canal" |
| "Winner significa mais CTR" | O teste mede tempo assistido | "Winner significa mais tempo assistido na fatia de impressões do teste" |
| "Expressão de grito reduz confiança" | Heurística de praticante | "Pode ser lida como clickbait. Testar" |
| "Curiosity gap aumenta o CTR de vídeo longo" | Literatura de notícia com resultados divergentes | "Hipótese com mecanismo (Loewenstein, 1994). Sem magnitude para miniatura" |
| "Views provam que o formato funciona" | Views não medem qualidade narrativa | "Views são contexto. A decisão usa o teste ou o CTR por origem" |

### 9.6 Dados a coletar para fechar lacunas

Para cada vídeo testado ou publicado com miniatura nova, registre no próprio canal:

- Hipótese, variável única e métrica de decisão.
- Arquivos de cada variante, com nome e data.
- Datas de publicação, início e fim do teste, e se a janela cruza 24/08/2026.
- Rótulo do teste (Winner, Performed Same ou Inconclusive) e a métrica exibida.
- Impressões por variante, quando o relatório mostrar.
- CTR, impressões, AVD, APV, tempo assistido por impressão e origem de tráfego, por origem, na mesma janela.
- Parcela de impressões vinda de recomendação do YouTube [IMP-HELP].
- Curva de retenção do vídeo, para ver em que minuto ocorrem as quedas. A análise do corpus cita o relatório "Key moments for audience retention" do Studio como [OFICIAL, https://support.google.com/youtube/answer/9314415], mas essa página não foi lida nesta rodada.
- Resultado da checagem de política da miniatura (ver 7.7, passo 4).
- Origem da imagem e status de direitos, quando houver foto de pessoa real ou de arquivo.

Com dez ou mais vídeos desse registro, por origem e por janela, o canal consegue calibrar as faixas de referência que hoje só existem em fontes de terceiros.

---
## Adendo da revisão
## Reinvestigações incorporadas

- [OFICIAL] Advanced Mode (Ajuda 9717005) permite quebra por origem de tráfego, mas não lista compatibilidade de CTR nem volume mínimo. A Ajuda diz que a página Analytics virou Insights. Não confirmado que o CTR de impressões aparece por origem.
- [OFICIAL] Ajuda 12220281: o cartão de métricas da aba Videos traz impressões e CTR, sem quebra por origem no texto.
- [OFICIAL] Ajuda 9314486, versão Android: o relatório de impressões mostra a fração de impressões vinda de recomendações do YouTube. Isso não é CTR por origem.
- [PRATICANTE] Benchmarks de CTR por origem (Miraflow, thumbnailinsight e outros) não têm fonte oficial e se contradizem. Não usar como baseline.
- [OFICIAL] Data API, revision history: co-views a partir de 16/11/2026 em long-form, Live e Shorts, só em TV. A Ajuda diz novembro de 2026.
- [OFICIAL, citado por terceiros] Co-views não afetam impressões de thumbnail, CTR nem duração média (Creator Insider, post no X). Não li o post diretamente.
- [OFICIAL] Co-view rate (Ajuda, comunidade 472646918): taxa para dividir o total e remover co-views; exemplo oficial de 1,10. Métricas que excluem co-views: engaged views e unique viewers.
- [INFERÊNCIA] Engaged views não mudam de definição em 24/08 nem em 16/11, segundo a tabela da Data API. O limiar de segundos não é publicado, então a série não é reconstruível a partir de dados públicos.
- [OFICIAL, citado por terceiros] Antes de 24/08/2026, o limite mínimo para contar view não está documentado oficialmente; fontes falam em cerca de 30 segundos sem base oficial.
- [PRATICANTE] Caso de terceiros de miniatura para Browse (thumbnailcreator) e de evergreen (clickminded): antes e depois sem controle. Não usar como prova.

## Registro de revisão
Foram aplicadas dez alterações. Acatados: data de 24/08/2026 reatribuída à Ajuda 12220281 (variante Android) e ao comunicado citado por terceiros; lacuna de co-views e de 16/11/2026 incluída em TV; CTR por origem declarado como não confirmado; critério de clickbait alinhado à condição tripla; atribuição a Loewenstein removida; rotulagem de post de comunidade e de material didático corrigida; variante com criança como sujeito retirada; título da seção 4 reformulado; data do caso Clodimar sinalizada como pendência. Não alterado: divergências de duração de vídeos (18:06, 33:36 e outros), porque a tabela de amostra de referência não estava no pacote de revisão e eu não consegui conferir os valores; a checagem deve ser feita no próprio vídeo. Em aberto: abertura da Ajuda 2991785 não conseguida; métrica do rótulo Winner (fatia ou tempo por impressão) e exibição de impressões por variante ainda sem resposta oficial; janela de leitura do CTR nas primeiras 24 horas divergente; a transcrição de Clodimar citada pela auditoria não foi verificada por mim. Discordância: nenhuma; o registro cobre apenas a correção de proveniência e não reabre os pesos da rubrica.

Correções aplicadas ao texto: 10.
