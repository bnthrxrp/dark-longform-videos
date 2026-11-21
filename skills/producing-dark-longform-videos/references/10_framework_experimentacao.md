# Framework de experimentação e otimização contínua

# Framework de experimentação e otimização contínua

**Referências internas.** Os dossiês são citados pelo nome do arquivo: `02_hook_database.md` (Hook Database), `03_thumbnail_engineering_playbook.md` (Thumbnail), `04_retention_engineering_blueprint.md` (Retenção), `05_longform_storytelling_framework.md` (Storytelling), `06_engenharia_reversa_padroes.md` (Engenharia reversa), `07_biblioteca_cientifica.md` (Biblioteca científica), `08_algoritmo_e_analytics.md` (Algoritmo e Analytics).

**Fatos da execução que valem aqui.** Amostra da engenharia reversa: 38 vídeos, todos de alto desempenho (razão de outlier acima da mediana do próprio canal), sem grupo de comparação, sem curva de retenção, sem CTR e sem dado de "most replayed". Os demais dossiês adotam esse número, mas divergem sobre a contagem exata (30, 35, 38 ou 21 vídeos em diferentes partes). Vale o número 38, com a ressalva de que a contagem por seção não foi reconferida.

**Etiquetas.** [OFICIAL] documentação do YouTube; [ESTUDO] artigo, com autor e ano; [DADO] número publicado ou medido; [PRATICANTE] heurística de criador ou consultor; [INFERÊNCIA] dedução minha; [LACUNA] não encontrado. Exemplos construídos aparecem como tal.

---

## 1. Princípios

### 1.1 Uma variável por vez, quando possível

**Por que importa.** Qualquer mudança de embalagem ou de roteiro altera ao mesmo tempo a aparência, a promessa e o conteúdo. Se o vídeo B muda título, miniatura e hook, e performa melhor, não há como atribuir o ganho a qualquer um dos três.

**Regra de processo.** Cada experimento altera um elemento. Se um teste precisar de duas mudanças (por exemplo, miniatura e título que dependem um do outro), registre o pacote como uma única variável e declare-o assim na hipótese. Não se pode atribuir o efeito a um dos componentes.

**Base oficial.** O teste nativo de título e miniatura exige que o título ou a miniatura não mude durante o teste. Se mudar, o teste para e precisa ser reiniciado [OFICIAL] (`03_thumbnail`, 7.1; Ajuda 16391400). Isso reforça a regra: a única variável é a que o próprio teste compara.

**Limite.** Em vídeo longo, nem sempre é possível isolar uma variável. Um roteiro com nova ordem de blocos muda o conteúdo inteiro. Nesses casos, a variável é o pacote, e a hipótese deve dizer que o pacote é a unidade de teste [INFERÊNCIA].

### 1.2 Hipótese escrita antes do resultado

Cada experimento começa com uma frase do tipo: "Se eu fizer X, espero Y na métrica Z, porque o achado W sugere isso. Se Y não ocorrer, a hipótese cai." A frase é gravada no log (seção 5 do briefing) antes da publicação.

**Por quê.** Sem hipótese escrita, qualquer resultado vira justificativa. A escrita antecipada também impede escolher a métrica depois de ver o número (ver 1.3).

**Forma mínima.** Sujeito (qual vídeo ou tipo de vídeo), intervenção (o que muda), métrica primária, direção esperada e magnitude mínima que justificaria agir. A magnitude mínima pode ser vaga no início, mas precisa existir [INFERÊNCIA].

### 1.3 Métrica primária e métricas de proteção, definidas antes

**Métrica primária.** Uma só, escolhida pela pergunta do experimento. Exemplos com base nos dossiês:
- Para embalagem (título e miniatura): watch time share do teste nativo, que é o critério oficial (`03_thumbnail`, 7.2; Ajuda 16391400). CTR de impressões entra como diagnóstico, não como critério.
- Para abertura (hook): retenção nos primeiros 30 s, a única métrica oficial de abertura (Intro) (`04_retention`, 1.1; `08_algoritmo`, glossário).
- Para roteiro e retenção: AVD em minutos, comparado com vídeos de duração semelhante, ou APV calculado (AVD ÷ duração), que não é oficial [OFICIAL; `08_algoritmo`, 4].

**Métricas de proteção.** Medem o que o experimento não pode piorar. Para cada teste, defina duas ou três. Exemplos:
- Para teste de título ou miniatura: AVD e impressões. Clickbait é CTR alto com AVD baixa e impressões abaixo do esperado [OFICIAL; Ajuda 7628154].
- Para teste de hook: impressões e CTR, para que uma abertura "melhor" não reduza a exposição.
- Para teste de roteiro: intro e a sensação de satisfação (likes e comentários, como proxy e nunca como prova).

**Por que escrever antes.** Com várias métricas à disposição, é fácil escolher a que favoreceu a variante. A regra é: a primária decide; as de proteção impedem a decisão de passar quando a primária sobe e uma proteção cai com força.

### 1.4 Amostra pequena em canal com poucos vídeos por mês

**O problema.** Um canal dark faceless publica poucos vídeos longos por mês. Cada vídeo recebe impressões de uma distribuição que muda com o tempo. Um teste de embalagem exige impressões suficientes para separar a diferença real do ruído.

**O que os dossiês dizem.**
- A Ajuda não define significância nem tamanho de amostra para o teste nativo; a Central diz que o teste exige impressões suficientes e pode terminar como Inconclusive [OFICIAL; `03_thumbnail`, 7.3; Ajuda 16391400].
- A nota técnica de Evan Miller (2010, não revisada por pares) dá n ≈ 16·p(1−p)/δ² por variante. Com p = 5% e δ = 2 pontos percentuais, cerca de 1.900 impressões por variante; com p = 2% e δ = 0,5 pp, cerca de 12.500 [INFERÊNCIA, cálculo do dossiê de miniatura; `03_thumbnail`, 6.5 e 7.5]. A fórmula não se aplica diretamente ao teste nativo, cujos parâmetros não são publicados.
- O mesmo dossiê alerta que impressões de uma mesma pessoa inflam a amostra efetiva [INFERÊNCIA].

**Consequências práticas.**
- Em canal pequeno, a maioria dos testes de embalagem deve terminar como Inconclusive. Isso não é fracasso: o padrão é mantido.
- Para decidir sobre um elemento com poucos vídeos, a unidade deve ser maior que um vídeo: um conjunto de vídeos do mesmo arquétipo, com a mesma mudança, comparado contra a linha de base do canal (seção 3 do briefing).
- O número de experimentos por trimestre é limitado pelo volume de impressões. O roteiro dos 90 dias (seção 6 do briefing) precisa ser dimensionado para isso.

**Limite.** Não há dado no material sobre o volume mínimo de impressões de um canal dark específico. O cálculo acima é de CTR de vídeo, com premissas de independência que não valem para exibições repetidas [INFERÊNCIA].

### 1.5 Por que comparar vídeos diferentes confunde tema com tratamento

**O problema.** Se o vídeo A (tema X, com miniatura nova) performa melhor que o vídeo B (tema Y, com miniatura antiga), a diferença pode vir do tema, da duração, do público, da época de publicação, da origem de tráfego ou da miniatura. O dado não separa essas causas.

**Evidências do material que ilustram o problema.**
- O mesmo título pode ter desempenhos muito diferentes: "3 People Who Disappeared Then REAPPEARED Years Later" aparece com 791 mil e 2 milhões de views, conforme o input (`03_thumbnail`, 1.6; `06_engenharia`, 2.1).
- "Doku: Wie war Sex im Mittelalter?" tem razão 43,9. O tema atrai por si, e não há como separar o efeito do rótulo "Doku:" do tema [INFERÊNCIA; `03_thumbnail`, 1.6].
- Views de antes e depois não são comparáveis sem ajuste, porque a contagem mudou em 24/08/2026 (início da reprodução em long-form) e em novembro de 2026 (co-views estimadas em TV) [OFICIAL; `08_algoritmo`, glossário e 9.2].
- Casos de terceiros de miniatura para Browse e de vídeo evergreen mostram CTR subindo junto com impressões, sem grupo de controle. A própria FAQ alerta que esse desenho confunde mudança de tráfego com efeito da miniatura [OFICIAL; `03_thumbnail`, 8.7].

**Regra decorrente.** Comparação entre vídeos só vale quando o tema, a duração (faixa semelhante), a origem de tráfego e a janela de tempo são iguais ou declarados. Quando não são, o resultado é hipótese, não decisão. A linha de base do canal (10 vídeos recentes de duração semelhante, convenção do Studio) é a referência mais limpa disponível [OFICIAL; `04_retention`, 1.1].

---

## 2. Backlog de hipóteses testáveis

**Como ler.** Cada etapa tem pelo menos quatro hipóteses. Cada hipótese traz:
- **Enunciado**: falsificável, com sujeito, intervenção, métrica e direção.
- **Origem**: qual achado a motiva e com que evidência (etiqueta).
- **Intervenção**: o que muda, e o que fica igual.
- **Métrica primária** e **métricas de proteção**.
- **Como medir** no YouTube Analytics ou no teste nativo.
- **Confirma se**: resultado que sustenta a hipótese.
- **Derruba se**: resultado que a refuta.

**Limite geral do backlog.** Nenhuma das hipóteses foi testada no material. Nenhum dossiê mediu CTR, retenção ou AVD de variantes em vídeo longo de canal dark. Os números que aparecem nas hipóteses ("confirma se") são critérios de decisão do próprio experimento, definidos antes do teste; não são resultados de fonte. Quando o critério é numérico e sem base, a hipótese diz isso (ver seção 4 do briefing, que trata de limiares).

**Limite de canal.** A maioria das hipóteses de embalagem exige teste nativo com impressões suficientes. Se o canal não tiver o recurso ou o volume, a hipótese vira comparação observacional, que tem as ameaças da seção 1.5.

---

### 2.1 Ideia

Etapa de escolher o assunto e a promessa, antes de qualquer embalagem. A pergunta é se o tipo de promessa que o vídeo faz influencia o desempenho.

**H-I1. Pergunta explícita versus afirmação de escopo no título.**
- **Enunciado:** em vídeos do mesmo arquétipo, o título em forma de pergunta ("Por que X fez Y?") tem watch time share maior que o título afirmativo com o mesmo tema ("A história completa de X").
- **Origem:** o dossiê de engenharia reversa encontrou perguntas com "por que" e número em #7 e #36, com resposta no fim do vídeo (`06_engenharia`, 2.1). A Biblioteca registra que perguntas de notícia geraram atitudes mais negativas (Scacco e Muddiman, 2019/2020, [ESTUDO], notícia) [`07_biblioteca`, 3.3]. Hipótese, não achado.
- **Intervenção:** só o formato do título. Mesmo tema, mesma duração, mesma miniatura.
- **Métrica primária:** watch time share do teste nativo (título).
- **Proteção:** AVD; impressões.
- **Como medir:** teste nativo de título, em vídeo antigo com histórico de impressões [OFICIAL; Ajuda 16391400].
- **Confirma se:** variante em pergunta vence no teste nativo com rótulo Winner.
- **Derruba se:** Performed Same, Inconclusive ou vitória da variante afirmativa.

**H-I2. Promessa de escopo fechado ("do início ao fim") versus promessa de causa.**
- **Enunciado:** títulos que prometem escopo completo geram menos watch time que títulos que prometem uma causa específica, porque o escopo cria expectativa de volume que o vídeo precisa cobrir.
- **Origem:** a Hook Database lista escopo fechado (H-27) como estrutura de hook, sem medida (`02_hook`, H-27) [INFERÊNCIA a partir de Die Komplette Geschichte, rtmNK_QpwSw]. O dossiê de retenção mostra que vídeos de 60+ min com escopo amplo têm pontos de queda após o clímax [`04_retention`, 2.2]. Ambos são [INFERÊNCIA].
- **Intervenção:** título com escopo fechado contra título com causa específica, mesmo tema.
- **Métrica primária:** AVD em minutos, comparado com a linha de base do canal de mesma duração (teste de série, não de teste nativo).
- **Proteção:** CTR e impressões.
- **Como medir:** série alternada de dois vídeos do mesmo arquétipo (desenho na seção 3 do briefing).
- **Confirma se:** AVD do grupo com escopo fechado fica acima da linha de base em pelo menos o mesmo número de vídeos que o grupo com causa específica.
- **Derruba se:** a diferença de AVD não se repete entre os dois grupos.

**H-I3. Tema com dilema moral documentado versus tema com fato único.**
- **Enunciado:** temas com dois lados documentados (dilema) geram mais AVD que temas de fato único, porque o espectador acompanha a resolução do conflito.
- **Origem:** H-18 (dilema moral sobre o protagonista) e o alerta de risco de manipulação quando não há dois lados documentados (`02_hook`, H-18). [PRATICANTE] para a hipótese de que o dilema sustenta a atenção. Nenhuma medida.
- **Intervenção:** escolha de tema (dilema versus fato único), com duração e arquétipo fixados.
- **Métrica primária:** APV calculado (AVD ÷ duração).
- **Proteção:** satisfação por proxy (reações públicas, rotuladas como proxy); incidência de comentários de correção (sinal de erro factual).
- **Como medir:** comparação entre vídeos de mesma duração, na linha de base do canal.
- **Confirma se:** APV do grupo dilema fica acima da linha de base em mais da metade dos vídeos.
- **Derruba se:** APV não separa os grupos, ou se o grupo dilema tem mais comentários de contestação factual.

**H-I4. Caso de vítima identificada versus caso sem vítima nomeada.**
- **Enunciado:** casos de true crime com vítima nomeada geram CTR maior na embalagem, mas AVD menor, porque a identidade da vítima aumenta a expectativa sem sustentar a narrativa.
- **Origem:** o dossiê de miniatura registra que os títulos com nome ou apelido de pessoa aparecem em 11 de 38 casos, com razões variadas, sem medida (`06_engenharia`, 2.1). O risco ético de nomear vítimas e familiares está em `02_hook` (riscos) e em `03_thumbnail` (2.8). [INFERÊNCIA].
- **Intervenção:** título com nome da vítima contra título com o tipo de crime e o local.
- **Métrica primária:** watch time share (teste nativo).
- **Proteção:** AVD; checagem jurídica e ética antes do teste (portão G4 do playbook de miniatura).
- **Como medir:** teste nativo de título.
- **Confirma se:** variante com nome vence no teste sem queda do AVD.
- **Derruba se:** a variante sem nome vence ou empata. Não se testa com vítima criança (`03_thumbnail`, 2.8 e 7.6).

---

### 2.2 Título

**H-T1. Número na promessa versus promessa sem número.**
- **Enunciado:** títulos com número explícito ("10 micronações", "Top 5 batalhas") geram watch time share maior no teste nativo, porque sinalizam escopo mensurável.
- **Origem:** oito de 38 títulos do corpus trazem número na promessa; o padrão é observado, não medido (`06_engenharia`, 2.1). A ficha de #5 (Dienstgrade) mostra título de catálogo sem número, que não é caso suficiente para decidir [INFERÊNCIA].
- **Intervenção:** número na promessa contra a mesma promessa sem número.
- **Métrica primária:** watch time share do teste nativo.
- **Proteção:** AVD; coerência da contagem (o número prometido precisa ser entregue, ver 2.4 e H-R5).
- **Como medir:** teste nativo de título.
- **Confirma se:** variante com número vence.
- **Derruba se:** a variante sem número vence ou empata; e se o número for entregue de forma incompleta, a hipótese não se sustenta, porque a comparação estaria confundida.

**H-T2. Título com nome de lugar no início versus nome de pessoa no início.**
- **Enunciado:** títulos que abrem com o lugar (geografia) geram mais impressões em busca, e títulos que abrem com nome de pessoa geram mais watch time share, porque o nome da pessoa ancora a narrativa.
- **Origem:** lugar nomeado aparece em 12 de 38 títulos e pessoa em 11 de 38 (`06_engenharia`, 2.1). Nenhuma medida; a hipótese de separação entre busca e narrativa é [INFERÊNCIA] a partir de `08_algoritmo` (busca depende de consulta).
- **Intervenção:** ordem de elementos no título, mantendo as mesmas palavras.
- **Métrica primária:** watch time share (teste nativo).
- **Proteção:** impressões por origem (busca versus Browse).
- **Como medir:** teste nativo; impressões por origem no relatório de impressões [OFICIAL; Ajuda 9314486].
- **Confirma se:** a variante com o elemento vence e o ganho aparece em impressões de busca.
- **Derruba se:** impressões de busca não mudam; ou o watch time share não mostra vitória.

**H-T3. Título com verbo de desfecho ("reapareceu", "sobreviveu") versus verbo de investigação ("procurou", "descobriu").**
- **Enunciado:** verbos de desfecho geram mais clique, mas menos AVD, porque anunciam a resposta antes do vídeo.
- **Origem:** o dossiê de miniatura aponta divergência de verbo entre título e miniatura ("reappeared" versus "found") como risco de promessa que o vídeo não cumpre (`03_thumbnail`, 3.2). Efeito sobre CTR não medido. [INFERÊNCIA].
- **Intervenção:** verbo do título.
- **Métrica primária:** AVD, em comparação com a linha de base.
- **Proteção:** CTR (por origem); impressões.
- **Como medir:** série alternada, ou teste nativo de título.
- **Confirma se:** verbo de investigação mantém AVD sem perder CTR de forma relevante.
- **Derruba se:** verbo de desfecho tem AVD igual ou maior.

**H-T4. Título com pergunta que a miniatura não responde versus título que coincide com a miniatura.**
- **Enunciado:** quando a miniatura mostra um elemento que o título pergunta (âncora visual da pergunta), a watch time share sobe, porque o espectador confirma no clique que o vídeo é o que foi buscado.
- **Origem:** o dossiê de miniatura classifica o par título-miniatura em complementar, redundante, dependente ou contraditório, e aponta o caso descasado (pergunta sem objeto visível) em Sleepy History (`03_thumbnail`, 3.2). Hipótese de alinhamento, sem medida de efeito.
- **Intervenção:** mesma pergunta no título; miniatura com ou sem o objeto da pergunta.
- **Métrica primária:** watch time share (teste nativo, com a miniatura como variável).
- **Proteção:** CTR; AVD.
- **Como medir:** teste nativo de miniatura, com o título fixo.
- **Confirma se:** versão com âncora vence.
- **Derruba se:** a versão sem âncora vence ou empata.

---

### 2.3 Thumbnail

**H-M1. Uma âncora dominante versus várias âncoras.**
- **Enunciado:** miniaturas com um único elemento dominante geram watch time share igual ou maior que miniaturas com dois ou mais elementos de peso parecido.
- **Origem:** Pieters e Wedel (2004, [ESTUDO], anúncio impresso): o elemento pictórico capta atenção independentemente do tamanho [`03_thumbnail`, 2.1]. Transferência para miniatura é [INFERÊNCIA]. A Central recomenda evitar design complexo demais [OFICIAL].
- **Intervenção:** número de elementos de peso alto na miniatura; o restante é fundo.
- **Métrica primária:** watch time share (teste nativo).
- **Proteção:** CTR (diagnóstico); legibilidade reduzida (teste de um segundo, `03_thumbnail` 2.1).
- **Como medir:** teste nativo com duas variantes do mesmo vídeo; o teste precisa de variantes bem diferentes, segundo a Central [OFICIAL; Ajuda 16391400].
- **Confirma se:** versão com uma âncora vence sem queda de CTR.
- **Derruba se:** a versão com mais elementos vence, ou se a diferença é Inconclusive em mais de um teste.

**H-M2. Rosto versus objeto ou símbolo, em canal sem apresentador.**
- **Enunciado:** em canal faceless, uma miniatura com objeto ou símbolo (sem rosto) tem watch time share igual ao de uma miniatura com ilustração de personagem sem olhos ou silhueta.
- **Origem:** rostos são localizados mais rápido que objetos em laboratório (Crouzet et al., 2010, [ESTUDO]; ~110 ms contra ~140 ms para veículos) [`03_thumbnail`, 2.6]. Dados de terceiros (vidIQ, 69% de rosto em breakouts) não têm denominador. Hipótese de transferência para canal sem rosto: [INFERÊNCIA].
- **Intervenção:** tipo de âncora (objeto, símbolo ou personagem ilustrado).
- **Métrica primária:** watch time share (teste nativo, três variantes do mesmo título).
- **Proteção:** CTR; checagem de direito de imagem (G1) e de status jurídico (G5).
- **Como medir:** teste nativo; quando houver mais de duas variantes, o teste aceita até três [OFICIAL; Ajuda 16391400].
- **Confirma se:** a variante com objeto ou símbolo não perde para o rosto ou personagem.
- **Derruba se:** o personagem ilustrado vence por margem que se repete em dois vídeos do mesmo arquétipo.

**H-M3. Texto de até cinco palavras versus texto ausente.**
- **Enunciado:** miniatura com texto principal de até cinco palavras tem watch time share maior que miniatura sem texto, quando o texto nomeia o caso ou o objeto.
- **Origem:** a Central pede fonte legível e a miniatura aparece em tamanhos variáveis [OFICIAL; AJ-DICA]. Contagem de cinco palavras é prática de criador e mediana de breakouts do vidIQ, sem denominador [PRATICANTE]. Sete dos 38 vídeos do corpus não têm texto legível; coexistem com sucesso, então não permitem concluir [`03_thumbnail`, 2.4; `06_engenharia`, 2.2].
- **Intervenção:** presença e tamanho do texto; o objeto e a cena são fixos.
- **Métrica primária:** watch time share (teste nativo).
- **Proteção:** CTR; legibilidade no tamanho de feed.
- **Como medir:** teste nativo com variantes com e sem texto, e com texto de cinco palavras contra texto de duas palavras.
- **Confirma se:** versão com texto curto vence.
- **Derruba se:** a versão sem texto empata ou vence.

**H-M4. Miniatura com elemento de mistério (objeto sem resposta) versus miniatura com a resposta.**
- **Enunciado:** miniatura que mostra o objeto da pergunta sem a resposta gera watch time share maior que miniatura que mostra o desfecho.
- **Origem:** a Biblioteca registra que lacunas grandes demais ou pequenas demais reduzem a motivação, segundo uma revisão de 2026 (preprint, [ESTUDO], não verificado no original) [`07_biblioteca`, 2.1.1]. Loewenstein (1994, [ESTUDO], revisão teórica) [`07_biblioteca`, 2.1.1]. Concretude pode reduzir CTR em manchetes (PMC11704130, [ESTUDO], trecho) [`03_thumbnail`, 3.3]. Hipótese de miniatura: [INFERÊNCIA].
- **Intervenção:** mostrar o objeto (sem resposta) contra mostrar o desfecho.
- **Métrica primária:** watch time share (teste nativo).
- **Proteção:** AVD; checagem de promessa (o desfecho precisa estar no vídeo, `03_thumbnail` 2.8).
- **Como medir:** teste nativo de miniatura.
- **Confirma se:** versão com objeto sem resposta vence sem queda de AVD.
- **Derruba se:** a versão com desfecho vence ou a versão de mistério tem AVD menor.

---

### 2.4 Hook

**H-H1. Cena datada com hora e lugar versus abertura com pergunta explícita.**
- **Enunciado:** nos primeiros 30 s, uma cena com data, hora e lugar (H-06) mantém retenção do Intro acima da linha de base do canal, em comparação com uma abertura que começa por pergunta explícita.
- **Origem:** Intro é a única métrica oficial de abertura, e a Central recomenda conferir se título e miniatura correspondem ao conteúdo [OFICIAL; `04_retention`, 1.1]. Wistia (2020, [DADO], 1 a 10 min) mede perda no nose de 2% [`02_hook`, 1]. O corpus tem cena datada em 12 de 37 aberturas, sem curva (`06_engenharia`, 3.2). Hipótese: [INFERÊNCIA].
- **Intervenção:** tipo de abertura (cena datada contra pergunta explícita), com a mesma promessa.
- **Métrica primária:** retenção nos 30 s (Intro).
- **Proteção:** retenção nos 60 e 90 s (leitura visual da curva, [INFERÊNCIA]); AVD.
- **Como medir:** Intro e curva de retenção, após 1 a 2 dias de processamento [OFICIAL; Ajuda 9314415].
- **Confirma se:** o Intro da versão com cena datada fica acima da linha de base em pelo menos a maioria dos vídeos do par.
- **Derruba se:** a diferença não se repete ou fica dentro da variação habitual do canal.

**H-H2. Pergunta explícita com no máximo duas perguntas abertas em 60 s versus três perguntas.**
- **Enunciado:** abrir com três perguntas em 60 s reduz o Intro em relação a abrir com duas, porque a dívida de resposta aumenta.
- **Origem:** o dossiê de hook registra conflito entre a regra de duas perguntas e os exemplos de três (H-23, Ampulheta) e de quatro cortes com loops (H-52) (`02_hook`, 4). Regra do dossiê, sem teste [INFERÊNCIA; `02_hook`, 1].
- **Intervenção:** número de perguntas abertas no primeiro minuto.
- **Métrica primária:** Intro.
- **Proteção:** retenção nos 60 e 90 s.
- **Como medir:** curva de retenção nos primeiros 90 s; revisão manual do roteiro para contar perguntas.
- **Confirma se:** versão com duas perguntas tem Intro maior.
- **Derruba se:** o Intro não separa as versões. A regra de "duas" é limite de processo, não limiar confirmado.

**H-H3. Contexto geográfico antes do primeiro evento versus primeiro evento antes do contexto.**
- **Enunciado:** entrar no primeiro evento antes de 60 s aumenta o Intro, em comparação com abrir com 60 s ou mais de geografia ou história geral.
- **Origem:** Scary Interesting (The Most Dangerous Ocean Crossing) tem primeiro evento em 01:12, depois de 72 s de geografia; a medição não separa o efeito [`02_hook`, 4.5]. Hipótese de posicionamento, [INFERÊNCIA].
- **Intervenção:** antecipar o primeiro evento; o restante do vídeo fica igual.
- **Métrica primária:** Intro.
- **Proteção:** AVD (para ver se a antecipação não tira contexto necessário).
- **Como medir:** Intro e curva em 60 s.
- **Confirma se:** versão antecipada tem Intro maior.
- **Derruba se:** a diferença não se sustenta em dois vídeos ou o AVD cai.

**H-H4. Uso de promessa de mecanismo ("como") versus promessa de resultado ("o que aconteceu") nos primeiros 30 s.**
- **Enunciado:** promessa de mecanismo nos primeiros 30 s eleva o Intro, porque o espectador sabe que o vídeo responde a uma pergunta de processo.
- **Origem:** H-26 (promessa de mecanismo) tem exemplo oficial no J.P. Morgan (00:40) e é um padrão do criador, sem medida [`02_hook`, H-26]. Teoria de lacuna (Loewenstein, 1994) [`07_biblioteca`]. [INFERÊNCIA].
- **Intervenção:** primeira frase da promessa.
- **Métrica primária:** Intro.
- **Proteção:** CTR (para checar se a promessa de mecanismo não piorou a embalagem).
- **Como medir:** Intro e CTR por origem.
- **Confirma se:** versão de mecanismo tem Intro maior sem queda de CTR.
- **Derruba se:** o Intro é igual ou menor.

**H-H5. Escrever primeiro a frase de promessa do título versus construí-la depois do roteiro.** (Este é um teste de processo, não de público.)
- **Enunciado:** roteiros escritos com a promessa do título e da miniatura já fixadas têm menos descompasso entre a abertura e a embalagem (medido pelo registro de promessas do playbook de miniatura) do que roteiros em que a promessa é ajustada depois.
- **Origem:** o dossiê de miniatura propõe o registro de promessas com minuto de pagamento e alerta que uma palavra-promessa sem bloco correspondente é um desvio (`03_thumbnail`, 3.4). Efeito sobre retenção não medido [INFERÊNCIA].
- **Intervenção:** ordem do processo de escrita.
- **Métrica primária:** número de promessas sem pagamento no primeiro bloco (contagem do registro), e Intro.
- **Proteção:** tempo de produção (o teste não pode aumentar o custo sem ganho).
- **Como medir:** registro de promessas (seção 5 do briefing) e Intro.
- **Confirma se:** o processo reduz promessas sem pagamento sem queda do Intro.
- **Derruba se:** o processo não reduz as promessas sem pagamento ou aumenta o tempo de produção sem efeito.

---

### 2.5 Roteiro

**H-R1. Blocos delimitados por mudança de evento versus blocos de tempo fixo.**
- **Enunciado:** blocos cujo corte coincide com mudança de local, personagem ou fato central produzem menos queda na curva do que blocos de tempo fixo com o mesmo número de minutos.
- **Origem:** Rey et al. (2019, [ESTUDO], meta-análise): segmentação em lições melhora retenção de aprendizagem (d = 0,32), com efeito maior quando o sistema controla a pausa (d = 0,42) [`07_biblioteca`, CC2]. Zacks et al. (2007) e Kurby & Zacks (2008) sobre fronteiras de evento [`07_biblioteca`, PI1]. A extensão para curva de visualização é [INFERÊNCIA]. O corte por cronômetro não foi testado como fronteira.
- **Intervenção:** critério de corte do bloco.
- **Métrica primária:** queda entre minutos (vales) na curva, ou seja, a menor retenção nas transições; a leitura é visual e usa o tempo de cada transição [INFERÊNCIA].
- **Proteção:** AVD.
- **Como medir:** curva de retenção, marcando as transições no roteiro (checklist C4 do blueprint de retenção).
- **Confirma se:** vales coincidem com fronteiras de evento menos do que coincidem com cortes de tempo, em dois vídeos do mesmo arquétipo.
- **Derruba se:** a diferença não aparece, ou os vales caem em todas as transições sem relação com o critério.

**H-R2. Uma explicação por bloco versus duas ou mais explicações por bloco.**
- **Enunciado:** blocos com um mecanismo explicado têm menos queda no trecho seguinte do que blocos com dois mecanismos, porque reduzem a carga de conceitos novos.
- **Origem:** Cowan (2001, [ESTUDO], revisão): cerca de quatro chunks sem agrupamento [`07_biblioteca`, MT1]. Sweller et al. (2019, [ESTUDO], revisão): carga intrínseca, extrínseca e germânica [`07_biblioteca`, CC1]. Limite de span, não de narrativa [INFERÊNCIA].
- **Intervenção:** número de conceitos novos por bloco.
- **Métrica primária:** queda média de retenção no bloco (leitura visual da curva, [INFERÊNCIA]).
- **Proteção:** AVD; satisfação por proxy.
- **Como medir:** contagem de conceitos novos por bloco no roteiro; curva.
- **Confirma se:** blocos de um conceito têm queda menor que blocos de dois conceitos, em pelo menos dois vídeos.
- **Derruba se:** não há diferença, ou o efeito aparece só em conteúdo didático.

**H-R3. Pergunta de passagem entre blocos longos versus bloco longo sem pergunta.**
- **Enunciado:** um bloco de mais de 6 min sem pergunta nova tem queda mais íngreme que o mesmo bloco com uma pergunta de passagem no meio.
- **Origem:** o blueprint de retenção propõe o limite de 6 min sem pagamento, sem fonte primária (`04_retention`, 2.2 e 10 A5). A Biblioteca registra que o limite de 6 min da MOOC (Guo et al., 2014) é de sessão, não de retenção (`07_biblioteca`, EA3). [INFERÊNCIA].
- **Intervenção:** inserir uma pergunta de passagem no meio de um bloco longo.
- **Métrica primária:** queda no trecho do bloco.
- **Proteção:** AVD.
- **Como medir:** curva em blocos longos, comparando o trecho com e sem pergunta.
- **Confirma se:** o trecho com pergunta tem menor queda.
- **Derruba se:** a diferença não aparece.

**H-R4. Recapitulação curta no início de bloco versus sem recapitulação.**
- **Enunciado:** uma frase de recapitulação do bloco anterior no início de cada bloco reduz a queda no primeiro minuto do bloco.
- **Origem:** Szpunar, Khan & Schacter (2013, [ESTUDO], aula de 21 min): testes intercalados reduziram divagação; magnitude divergente (19% em resumo indexado, pela metade em nota de imprensa) [`07_biblioteca`, EA2]. A mesma linha aparece em `04_retention`, 8.4. Efeito em narrativa não testado; pode quebrar a imersão [INFERÊNCIA].
- **Intervenção:** recapitulação de uma frase no início de bloco.
- **Métrica primária:** queda no primeiro minuto do bloco.
- **Proteção:** AVD e satisfação por proxy (para checar se a recapitulação não soou como repetição).
- **Como medir:** curva por bloco.
- **Confirma se:** primeiro minuto com recapitulação tem queda menor.
- **Derruba se:** a diferença não aparece, ou a recapitulação aumenta queda.

**H-R5. Entregar o número prometido no título antes do fim do bloco central versus entregar só no fim.**
- **Enunciado:** quando o título promete N itens ou um número, entregar a contagem em cada bloco (e não só no fim) reduz a queda no último terço, porque o espectador acompanha o progresso.
- **Origem:** o corpus tem vídeos com número no título cujo número é entregue em blocos (Top 5 WWI, Micronações); as fichas não medem a queda [`06_engenharia`, 4.2; `04_retention`, 5]. [INFERÊNCIA].
- **Intervenção:** marcar o número de cada item no próprio vídeo (lista de contagem na tela, ou abertura de bloco com o número).
- **Métrica primária:** queda no último terço.
- **Proteção:** AVD.
- **Como medir:** curva.
- **Confirma se:** queda no último terço é menor.
- **Derruba se:** a diferença não aparece.

---

### 2.6 Retenção

**H-T… (retenção, parte 1)**

**H-RT1. Duração do vídeo: vídeo mais curto da mesma série versus mais longo, com o mesmo conteúdo.**
- **Enunciado:** dentro da mesma série, vídeos de 30 min têm APV maior que vídeos de 45 min do mesmo arquétipo, porque a queda acumulada é maior em duração maior.
- **Origem:** Wu, Rizoiu e Xie (2018, [DADO], 5,3 milhões de vídeos públicos): duração explica mais de 58% da variância da porcentagem média assistida nos primeiros 30 dias. Correlação, sem curva [`04_retention`, 2.1]. Guo et al. (2014) mostram sessões de MOOC que caem com duração [`07_biblioteca`, EA3]. Hipótese de série: [INFERÊNCIA].
- **Intervenção:** duração (mesmo conteúdo, duas durações).
- **Métrica primária:** APV calculado (AVD ÷ duração), para comparar durações diferentes [PRATICANTE; `08_algoritmo`, glossário].
- **Proteção:** AVD em minutos (para ver se o tempo absoluto não cai).
- **Como medir:** comparação de duas versões ou comparação com a linha de base do canal por duração.
- **Confirma se:** APV da versão mais curta é maior sem queda de AVD absoluto.
- **Derruba se:** o APV é igual, ou o AVD absoluto cai. Não se usa benchmark de terceiro como alvo.

**H-RT2. Ponto de virada principal antes de 40% da duração versus depois de 60%.**
- **Enunciado:** em vídeos de 30 min ou mais, a reviravolta principal antes de 40% gera APV menor que a reviravolta depois de 60%, porque a virada tardia mantém o suspense.
- **Origem:** Ely, Frankel e Kamenica (2015, [ESTUDO], modelo teórico): viradas mais raras e mais fortes; sem teste em vídeo [`05_storytelling`, 2.5]. O corpus mostra clímax em faixas diversas, sem padrão consistente [`05_storytelling`, 3; `06_engenharia`, 4.3]. Hipótese [INFERÊNCIA].
- **Intervenção:** posição da reviravolta principal.
- **Métrica primária:** APV.
- **Proteção:** Intro e retenção no meio (para checar se a virada tardia não derrubou o meio).
- **Como medir:** curva; contagem de posição da virada por minuto.
- **Confirma se:** APV é maior na versão de virada tardia.
- **Derruba se:** APV é igual ou menor; ou se a virada tardia causa queda antes de ser paga.

**H-RT3. Tensão de final de bloco com a próxima pergunta explícita versus fechamento de bloco sem pergunta.**
- **Enunciado:** terminar o bloco com pergunta aberta (cliffhanger de bloco) reduz a queda no início do bloco seguinte.
- **Origem:** Schibler, Hahn e Green (2023, [ESTUDO], narrativas escritas, N = 202 e 273): cliffhanger aumentou o desejo declarado de ler a próxima parte, sem diferença em suspense ou prazer. Wirz et al. (2022, [ESTUDO], trecho): cliffhanger elevou excitação fisiológica, sem efeito em apreciação ou intenção de continuar assistindo (`04_retention` e `07_biblioteca`). A ligação com retenção de vídeo não está medida.
- **Intervenção:** fim de bloco com pergunta aberta contra fim de bloco com fechamento.
- **Métrica primária:** queda no início do bloco seguinte.
- **Proteção:** AVD; retorno ao próximo vídeo (métrica de canal, a medir por outras vias).
- **Como medir:** curva.
- **Confirma se:** início do bloco seguinte tem queda menor.
- **Derruba se:** não há diferença, ou o fechamento tem queda menor (o que indicaria que a pergunta aberta faz o espectador sair).

**H-RT4. Retomada de um elemento visual no fim do bloco versus corte sem retorno.**
- **Enunciado:** retornar à imagem inicial do bloco no último minuto reduz a queda no fim do bloco.
- **Origem:** o blueprint de retenção recomenda retornar à imagem inicial no encerramento, como callback (`05_storytelling`, 6; `04_retention`, 2.2 F). Prática de criador, sem medida [PRATICANTE].
- **Intervenção:** retorno a uma imagem do início do bloco.
- **Métrica primária:** queda no último minuto do bloco.
- **Proteção:** AVD.
- **Como medir:** curva.
- **Confirma se:** queda no último minuto é menor com callback.
- **Derruba se:** a diferença não se repete.

---

### 2.7 Payoff

**H-P1. Pagamento parcial de loop antes de 5 min versus pagamento apenas no fim do bloco.**
- **Enunciado:** uma resposta parcial à pergunta de abertura antes de 5 min eleva o Intro e reduz a queda do primeiro bloco, em comparação com pagamento só no fim do bloco.
- **Origem:** Schibler et al. (2023) mostram desejo declarado por continuar com fim de capítulo (não vídeo), e Loewenstein (1994) sustenta que informação parcial alimenta a curiosidade [`07_biblioteca`]. O corpus tem pagamento parcial em Villach (01:59) e Sleepy History (02:38) [`04_retention`, 6.1; `06_engenharia`, 6.1]. Hipótese [INFERÊNCIA].
- **Intervenção:** existência e posição do pagamento parcial.
- **Métrica primária:** queda no primeiro bloco (leitura visual).
- **Proteção:** Intro; AVD.
- **Como medir:** curva; registro de pagamentos com minuto.
- **Confirma se:** versão com pagamento parcial tem queda menor no primeiro bloco.
- **Derruba se:** a diferença não aparece. Não se usa como regra de tempo fixo.

**H-P2. Pagamento de promessa no minuto anunciado versus pagamento depois do minuto anunciado.**
- **Enunciado:** quando o vídeo diz "veremos isso no minuto X", pagar até X ± 30 s mantém a curva; pagar depois reduz o AVD.
- **Origem:** o dossiê de miniatura e o de retenção registram promessas com minuto declarado (Trafalgar 24:48 → 36:16; Tencent 31:03 → 44:24) e pagamentos que variam em torno de 11 a 13 min [`04_retention`, 6.1; `03_thumbnail`, 3.4]. Nenhuma medida de efeito.
- **Intervenção:** cumprir o minuto anunciado ou não cumprir.
- **Métrica primária:** queda após o minuto de pagamento.
- **Proteção:** satisfação por proxy; comentários de correção.
- **Como medir:** curva em torno do minuto anunciado.
- **Confirma se:** queda é menor quando o pagamento cumpre o minuto.
- **Derruba se:** não há diferença.

**H-P3. Revelação em duas camadas (prévia e depois revelação) versus revelação direta.**
- **Enunciado:** uma prévia de 30 s antes da revelação reduz a queda no minuto da revelação, em comparação com revelar sem prévia.
- **Origem:** Moskvin (26:35) tem prévia em 05:24 e revelação em 06:12 (`05_storytelling`, 5.4). Ely et al. (2015, modelo) [`05_storytelling`, 2.5]. [INFERÊNCIA].
- **Intervenção:** prévia de 30 s.
- **Métrica primária:** queda no minuto da revelação.
- **Proteção:** AVD; retorno ao próximo bloco.
- **Como medir:** curva no minuto da revelação.
- **Confirma se:** queda é menor com prévia.
- **Derruba se:** a queda é igual ou maior.

**H-P4. Fato a corrigir no próprio vídeo (correção pública) versus fato sem correção quando há erro.**
- **Enunciado:** quando o vídeo corrige um erro próprio em público, o número de comentários de contestação factual cai e a retenção após a correção não cai.
- **Origem:** Khadija O. (57:00, identidade corrigida em 10:12) e Moskvin (09:08, contagem corrigida) como exemplos [`05_storytelling`, 5.4]. Hipótese de confiança.
- **Intervenção:** correção explícita no vídeo, em comparação com correção feita só em descrição ou comentário.
- **Métrica primária:** retenção após o minuto da correção (curva).
- **Proteção:** comentários de contestação (proxy); AVD.
- **Como medir:** curva; contagem de comentários com o tema.
- **Confirma se:** a retenção não cai após a correção, e a contestação cai.
- **Derruba se:** a correção causa queda.

---

### 2.8 Encerramento (e ponte para o próximo vídeo)

**H-E1. Fecho com a pergunta de abertura respondida versus fecho com recapitulação de tese.**
- **Enunciado:** um fecho que responde explicitamente à pergunta de abertura aumenta a fração de espectadores que chega ao fim (APV), em comparação com um fecho de tese que não retoma a pergunta.
- **Origem:** o blueprint de storytelling propõe retomar a pergunta na conclusão [`05_storytelling`, 6]; a Central diz que trechos finais costumam perder audiência e recomenda trazer o forte para antes [OFICIAL; `04_retention`, 2.2 F]. [INFERÊNCIA].
- **Intervenção:** tipo de fecho.
- **Métrica primária:** APV.
- **Proteção:** AVD; retenção nos últimos 2 min.
- **Como medir:** curva nos últimos 3 min.
- **Confirma se:** a fração de quem chega ao fim é maior com a pergunta retomada.
- **Derruba se:** não há diferença.

**H-E2. Ponte para o próximo vídeo com pergunta específica versus indicação genérica de série.**
- **Enunciado:** a última frase do vídeo que nomeia uma pergunta específica (que o próximo vídeo responde) gera mais cliques no próximo vídeo do canal que uma frase genérica de série.
- **Origem:** o blueprint de storytelling distingue três tipos de ponte (pergunta, série e teaser) [`05_storytelling`, 6]. Não há medida. A Ajuda 16533387 recomenda séries e playlists para ampliar consumo [OFICIAL; `08_algoritmo`, 2].
- **Intervenção:** tipo de ponte na última frase.
- **Métrica primária:** cliques do vídeo para o próximo vídeo do canal (métrica de fluxo, no relatório de Analytics de tráfego de vídeo).
- **Proteção:** AVD (para checar se a ponte não cai no fim).
- **Como medir:** relatório de origem de tráfego "vídeos sugeridos" ou "tela final" no próximo vídeo [INFERÊNCIA; confirmar o nome do campo no Studio].
- **Confirma se:** a ponte com pergunta específica tem mais tráfego do vídeo anterior.
- **Derruba se:** não há diferença.

**H-E3. Pedido de inscrição no fim versus no início do vídeo.**
- **Enunciado:** pedir inscrição no fim não reduz o AVD, em comparação com pedido no início (que reduz o Intro).
- **Origem:** o dossiê de storytelling registra pedido de inscrição em cerca de 6 de 36 encerramentos, sempre no fim, sem medida de efeito [`05_storytelling`, 6; `06_engenharia`, 6.3]. Cavaleiro do Tempo pede apoio em 00:04–00:35, antes de qualquer conteúdo (`02_hook`, 4.1). [INFERÊNCIA].
- **Intervenção:** posição do pedido (início contra fim).
- **Métrica primária:** Intro (para a versão com pedido no início); AVD (para a versão com pedido no fim).
- **Proteção:** inscritos novos (métrica de canal).
- **Como medir:** Intro e curva.
- **Confirma se:** pedido no início reduz o Intro, e pedido no fim não reduz o APV.
- **Derruba se:** o pedido no início não afeta o Intro.

**H-E4. Fecho com fato novo versus fecho sem fato novo.**
- **Enunciado:** introduzir um fato central novo no último bloco reduz a fração de espectadores que chega ao fim, porque o espectador percebe que precisaria voltar para entender.
- **Origem:** o blueprint de storytelling recomenda não introduzir fato central novo no último bloco [`05_storytelling`, 6]. [INFERÊNCIA].
- **Intervenção:** fato novo no último bloco.
- **Métrica primária:** APV.
- **Proteção:** AVD.
- **Como medir:** curva nos últimos 5 min.
- **Confirma se:** a versão com fato novo perde APV.
- **Derruba se:** não há diferença.

---

## Lacunas desta parte

- Nenhuma das 50 hipóteses foi testada no material. Os achados que as motivam são de laboratório, de anúncio impresso, de notícia, de MOOC, de contos ou de dados de terceiros.
- Os números usados como critério ("confirma se") são definidos pelo experimento. Não são resultados de fonte.
- O volume mínimo de impressões para cada teste não é definido pela Central; a regra de Miller (2010) é uma nota técnica não revisada, com premissas que não valem para exibições repetidas.
- As variáveis de retenção (queda em transições, queda no primeiro minuto de bloco, APV após minuto de pagamento) são leituras visuais da curva, que a Central não define em termos numéricos [OFICIAL; `04_retention`, 1.3].
- Nenhuma fonte primária mediu CTR, retenção ou AVD por variante em vídeo longo de canal dark.
- Os exemplos do corpus são de alto desempenho e não têm grupo de comparação. Todo exemplo citado aqui como motivação é padrão observado, não causa.
- Divergências entre dossiês que afetam as hipóteses: a contagem de vídeos da amostra (30, 35, 38 ou 21); a janela de leitura do CTR nas primeiras 24 h (divergente); o nome da métrica do teste nativo (fatia ou tempo por impressão, em aberto). Onde afetam, as hipóteses usam a métrica declarada pela Central, com a ressalva.
- Não há dado sobre a retroatividade dos co-views nem sobre a separação de origem na tela do Studio. As hipóteses que dependem disso (H-T2, H-E2) estão condicionadas a verificação.

## 3. Desenhos de experimento

### 3.0 Convenções desta seção

- **Fontes internas:** 02_hook_database.md (códigos H-xx); 03_thumbnail_engineering_playbook.md (§); 04_retention_engineering_blueprint.md (§); 05_longform_storytelling_framework.md (§); 06_engenharia_reversa_padroes.md (§); 07_biblioteca_cientifica.md (fichas); 08_algoritmo_e_analytics.md (§).
- **Ajudas oficiais** citadas pelos entregáveis: 16391400 (teste A/B), 7628154 (CTR), 9314486 (impressões), 12220281 (performance de conteúdo), 9314415 (retenção), 9229980 (política de miniaturas), 2991785 (contagem de visualizações). Cada citação indica se a leitura foi direta ou via entregável.
- **Base do corpus (fatos da execução):** 38 vídeos, 37 com transcrição, sem curva de retenção, sem CTR por variante e sem grupo de comparação. Os entregáveis citam 30 ou 35 vídeos (04, §Registro; 05, §1). Esses números divergem e não são usados aqui.
- **Estatus dos desenhos:** nenhum foi executado no canal. Todo "resultado" nesta seção é critério a aplicar, não achado.
- **Hipóteses:** os códigos de hipótese da seção 2 (backlog) não estão nesta parte. Aqui os desenhos referenciam o achado de origem por arquivo e §. Na consolidação, vincular cada uma ao código da seção 2.

### 3.1 Catálogo de ameaças à validade

Os cinco desenhos abaixo usam este catálogo. Cada um lista apenas as ameaças que se aplicam a ele.

| Código | Ameaça | Como aparece no YouTube | Fonte |
|---|---|---|---|
| T1 | Quebra de contagem e de métrica | Visualização passou a contar no início da reprodução em long-form a partir de 24/08/2026. Co-views em TV entram nas contagens públicas a partir de novembro/2026; o dia 16/11/2026 vem só de terceiros. Não se sabe se o watch time do teste nativo inclui co-views | [OFICIAL, 12220281 e blog de 19/08/2026 via 08 §4 e adendo]; [OFICIAL via terceiros, 08 §4] |
| T2 | Tema e conteúdo | O tema atrai por si. Comparar vídeos de temas diferentes mistura tema com tratamento | 03 §1.6; 06 §2 |
| T3 | Tendência e sazonalidade | Calendário, eventos e modas do nicho mudam a demanda | [INFERÊNCIA] |
| T4 | Mistura de origem de tráfego | Browse, Suggested e Search têm públicos e CTR diferentes. Mudança de mix altera CTR sem mudar a embalagem | [OFICIAL, 7628154 via 08 §2 e 03 §8] |
| T5 | Seleção e regressão à média | Vídeo escolhido porque foi mal tende a se aproximar da média sem intervenção. A seleção só de casos de alto desempenho também distorce | [INFERÊNCIA, padrão estatístico]; corpus só de outliers (fatos da execução) |
| T6 | Contaminação entre vídeos e versões | Suggested inclui links da descrição (08 §2). O mesmo espectador pode ver A e B. Séries ligam vídeos do canal entre si | [OFICIAL, 9314355 via 08 §2] |
| T7 | Mudança de público | Crescimento altera o mix de novos, casuais e regulares, e com isso a linha de base | 08 §4 |
| T8 | Intervenção durante o teste | Trocar título ou miniatura interrompe o teste. Mudar links, série, playlist ou tela final altera a exposição | [OFICIAL, 16391400 via 03 §7.1]; 03 §7.4 item 5 |
| T9 | Volume e variância | Poucas impressões ou poucos vídeos por faixa. Efeitos pequenos não aparecem | 03 §7.5; seção 4.5 desta parte |
| T10 | Múltiplas comparações e parada antecipada | Muitas métricas, muitos testes, parar ao ver o sinal favorável | 03 §7.4, item 1 (nota de Miller, 2010) |
| T11 | Efeito de ordem e de série | O vídeo anterior muda a audiência do seguinte. Em caso de Inconclusive, a primeira variante enviada vira padrão | [OFICIAL, 16391400 via 03 §7.3] |

### Desenho 1. Teste nativo A/B de título ou miniatura

**Quando usar**
- Vídeo longo já publicado, com histórico de impressões, em que só a embalagem muda: miniatura ou título, nunca os dois ao mesmo tempo.
- Canal elegível: Studio de desktop com o recurso habilitado. A Central restringe vídeos feitos para crianças e exige classificação correta para conteúdo +18 [OFICIAL, 16391400 via 03 §7.1; leitura direta não feita nesta parte].
- Não serve para abertura, roteiro, duração ou ordem de blocos. O teste cobre só título e miniatura.

**Como executar**
1. Escolher vídeo antigo com histórico de impressões, sem escolher por desempenho ruim (T5).
2. Fazer as variantes bem diferentes. A página do teste recomenda isso [OFICIAL, via 03 §5.2]. Variantes parecidas tendem a dar Performed Same ou Inconclusive.
3. Subir todas em pelo menos 720p. Se uma ficar abaixo, o teste reduz todas para 480p [OFICIAL, via 03 §7.1].
4. Enviar primeiro a variante que você aceitaria como padrão, porque ela vence em caso de Inconclusive [OFICIAL, via 03 §7.7, passo 6].
5. Congelar título e miniatura até o rótulo. Qualquer troca reinicia o teste.
6. Ler o rótulo e a métrica exibida. Registrar as impressões por variante, se o relatório mostrar.

**Ameaças**
- **T9.** O método, o nível de significância, o poder e a porcentagem do grupo de controle não são publicados [OFICIAL, via 03 §7.8]. O tamanho de efeito que o teste detecta é desconhecido.
- **T1 e métrica ambígua.** A Central fala em "watch time share". Um post de comunidade e uma cobertura falam em tempo assistido por impressão (03 §7.2). Se as impressões forem desiguais, as duas métricas podem ordenar as variantes de forma diferente. Se o teste cruzar 16/11/2026, o watch time pode incluir co-views (conflito em 08 §4 e adendo).
- **T8.** Qualquer alteração manual durante o teste.
- **T10.** Encerrar antes do fim por ver um resultado favorável.
- **T11.** Efeito de ordem em Inconclusive.

**Como reduzir**
- Pré-registrar a métrica primária (o que o Studio mostra como critério) e a direção esperada.
- Registrar a data de início e a janela, e se ela cruza 24/08/2026 ou 16/11/2026.
- Não usar CTR de teste como critério de decisão. O critério é o do rótulo (03 §7.3).
- Anotar a origem do tráfego, se o Studio mostrar.
- Se o Studio mostrar a fatia de TV ou o dispositivo, registrar. Se não mostrar, registrar que a janela pode conter co-views e não tratar o resultado como puro.

**Lacuna.** Não se confirmou se o Studio mostra CTR ou retenção por variante (03 §9.2; 08 §9.2). Se mostrar, a leitura ganha diagnóstico. Se não mostrar, a leitura fica só no rótulo.

### Desenho 2. Comparação antes/depois com troca de pacote

**Quando usar**
- Quando não há teste nativo: recurso indisponível, vídeo recém-publicado sem histórico de impressões, ou canal fora da elegibilidade.
- Quando a mudança não é de embalagem: abertura regravada, nova ordem de blocos, nova duração de vídeo novo.
- É o desenho mais fraco desta parte. Serve para gerar hipótese, não para decidir padrão.

**Como executar**
1. Definir janelas de mesmo comprimento (28 dias) e mesmo número de publicações, de preferência com o mesmo dia da semana.
2. Comparar cada janela com uma linha de base do mesmo período (vídeos de faixa de duração semelhante, desenho 4), não só com a janela anterior.
3. Mudar um único elemento entre as janelas. Anotar no log todos os eventos: links de descrição, série, playlist, tela final.
4. Comparar CTR apenas dentro da mesma origem de tráfego.

**Ameaças:** T1 (se a janela cruza 24/08/2026 ou 16/11/2026), T3, T4, T7, T2, T5 (se o vídeo foi escolhido por ter ido mal), T8.

**Como reduzir**
- Comparar com linha de base concorrente, não só com o passado.
- Não comparar janelas que cruzam uma quebra de contagem sem anotar a quebra. Se cruzarem, a comparação não é válida para decisão.
- Escrever no log, antes da troca, que o resultado é hipótese, e exigir replicação (seção 7, nível E2) antes de virar padrão.

### Desenho 3. Séries alternadas entre vídeos (pares)

**Quando usar**
- Mudanças que o teste nativo não cobre: abertura, payoff, segmentação, ordem de blocos, duração.
- Canal com cadência regular de publicação. Com menos de um vídeo por semana, a série demora mais; ver seção 6.

**Como executar**
1. Parear vídeos por tipo de história (mesma estrutura de caso), faixa de duração e idioma. Sem pareamento, a leitura mede tema (T2; 03 §1.6).
2. Atribuir a versão A ou B por sorteio registrado no log antes da produção. Não escolher a versão depois de ver o vídeo pronto.
3. Usar o par como unidade de análise. Para decidir, o efeito deve aparecer em mais de um par independente (ver seção 4.3).
4. Publicar A e B com intervalo, não no mesmo dia. Não colocar link de A na descrição de B nem o contrário (T6).
5. Ler sempre com o mesmo protocolo: Intro de 30 s, inclinação de 30 a 90 s (leitura visual, não métrica oficial), e curva após 1 a 2 dias de processamento [OFICIAL, 9314415; inclinação é leitura de 04 §1 e 05, não métrica da plataforma].

**Ameaças:** T2, T3, T6, T7, T9 (poucos pares), T10 (muitas métricas em muitos pares), T11 (o público que viu A pode estar em B).

**Como reduzir**
- Pareamento e sorteio documentados antes da produção.
- Métrica primária escrita antes da publicação. Outras métricas são diagnósticas.
- Intervalo entre publicações fixo, para não misturar efeito de cadência com efeito de versão.
- Leitura separada por par, com registro do que aconteceu com cada um.

### Desenho 4. Linha de base do canal por faixa de duração

**Quando usar:** sempre. É a referência de todos os outros desenhos e a leitura de vídeo único.

**Como executar**
1. Definir faixas de duração do canal antes de qualquer leitura. A Central não define "duração semelhante" [OFICIAL, 9314415 via 04 §1.1]. Faixas como 10–20, 20–35 e 35–60+ min são proposta desta parte, não fonte.
2. A referência oficial no Studio é a retenção típica dos 10 vídeos mais recentes de duração semelhante [OFICIAL, 9314415 via 08 §4].
3. Manter uma linha de base interna por faixa, com IDs de vídeos registrados no log, e calcular mediana e amplitude (não média) de Intro 30 s, APV calculado e CTR por origem, quando o Studio mostrar.
4. Medir a dispersão da linha de base. A dispersão é o que permite dizer se um vídeo está fora do normal.

**Ameaças:** T9 (dez vídeos é linha de base ruidosa), T2, T3, T7, T1 (linha de base que cruza quebras), T5.

**Como reduzir**
- Não mover a linha de base após o início de um teste. Congelar a lista de IDs no log.
- Tratar um vídeo como "fora do normal" só se estiver fora da faixa observada na própria linha de base, e não por diferença de média.
- Não tratar a comparação como causal.

### Desenho 5 (complementar). Teste de compreensão pré-publicação

**Quando usar:** antes de publicar miniatura, título ou primeiros 90 s. Custo baixo, roda em qualquer canal.

**Como executar:** conforme 03 §6.3. Mostrar a versão reduzida, sem contexto, por 3 a 5 segundos, a cinco pessoas fora do projeto. Perguntar sobre o tema e sobre a pergunta que o vídeo deve responder. Fazer também os testes de cinza e de desfoque leve.

**Ameaças:** amostra pequena e não representativa (T9); pessoas que querem agradar; não mede comportamento de clique nem de retenção.

**Como reduzir:** usar para eliminar versões que confundem e para checar se a promessa está clara. Não usar para escolher a vencedora. Trocar as pessoas entre rodadas.

### Não é desenho válido: comparar vídeos de razão alta com vídeos de razão baixa

O corpus tem só casos de alto desempenho, sem grupo de comparação (fatos da execução). Comparar um vídeo de razão alta com um de razão baixa mistura tema, canal, tráfego e seleção. Esse procedimento não entra neste framework como teste. Os padrões do corpus são hipóteses de origem para os desenhos acima.

---

## 4. Leitura de resultado

### 4.1 Pré-condições de leitura

Se uma condição falha, o resultado vira "não decidido" (seção 4.6). Não se lê o rótulo do teste nem a série antes de checar a lista.

1. Hipótese, métrica primária, direção esperada e δ (menor diferença que muda a decisão) registrados antes da publicação.
2. Uma única variável alterada. Conferir as versões com comparação lado a lado.
3. Janela de leitura respeitada: 48 horas só para checagem; retenção só após 1 a 2 dias de processamento [OFICIAL, 9314415].
4. Quebras de contagem anotadas: 24/08/2026 (long-form) e novembro/2026 (co-views; 16/11 só por terceiros). Se a janela cruza uma quebra, a comparação só é válida contra linha de base do mesmo lado da quebra.
5. Mix de origem comparável entre janela e linha de base, quando o Studio mostrar a origem.
6. Impressões suficientes para o desenho. A Central não define "substanciais" [OFICIAL, 7628154 via 08 §4]. O critério é o cálculo de 4.5.
7. Mudanças paralelas registradas: links de descrição, série, playlist, tela final, miniaturas de outros vídeos que apontam para este.
8. Classificação e política conferidas: vídeo feito para crianças, +18, miniatura conforme a política [OFICIAL, 9229980].

### 4.2 Métricas por tipo de experimento

A métrica primária é uma só. As proteções impedem uma vitória que piora outra coisa. As diagnósticas explicam o resultado, mas não decidem.

| Tipo de experimento | Primária | Proteções | Diagnósticas | Observação |
|---|---|---|---|---|
| Embalagem (título ou miniatura, desenho 1) | Rótulo e métrica do teste nativo | Intro 30 s e APV calculado do vídeo no período, contra a linha de base | CTR e impressões por origem, se o Studio mostrar | Assinatura de clickbait da Central: CTR alto, AVD baixa e impressões abaixo do esperado, juntos [OFICIAL, 7628154 via 03 §6.4 e 08 §5] |
| Abertura 0–90 s (desenhos 2 e 3) | Intro 30 s [OFICIAL, 9314415] | CTR (não deveria mudar muito se a embalagem não mudou) e AVD | Curva de 0 a 3 min; inclinação de 30 a 90 s [INFERÊNCIA: leitura visual, não métrica oficial] | Os valores de 60 e 90 s não são métrica oficial (02, §1) |
| Estrutura do roteiro (payoff, blocos, ordem) | APV calculado (AVD ÷ duração) [rótulo do canal; "APV" não é definição oficial confirmada, 08 §4] | Intro, CTR e tempo de exibição total | Quedas e picos localizados; minuto do payoff | Ver 4.2.1 |
| Duração (mesma história, duas durações) | APV calculado | Tempo de exibição total por impressão | Curva por bloco | APV favorece vídeos curtos. O tempo total é a proteção que impede ganho falso |
| Posição de clímax ou virada | Queda ou pico no minuto alvo | Intro e APV | Trecho ouvido antes e depois do minuto | Um pico pode ser trecho bom ou trecho confuso. Ouvir o trecho (08 §4) |

**4.2.1 Por que APV sem tempo total engana.** Um vídeo mais curto tem APV mais alto com o mesmo comportamento. Por isso o tempo de exibição total entra como proteção em qualquer teste de duração ou de corte. [INFERÊNCIA] Se o APV sobe e o tempo total cai, o ganho pode ser só de encolher o vídeo.

### 4.3 Regras de decisão

A regra depende de três parâmetros definidos antes do teste: direção esperada, δ (menor diferença que justifica mudar o padrão) e o número de repetições independentes exigido.

- **δ** é uma decisão do canal, não um número de fonte. Deve refletir a diferença que muda uma produção (por exemplo, se trocar o roteiro compensa). O material não oferece valor de referência.
- **Número de repetições:** o material recomenda cerca de três uploads antes de considerar um ajuste validado. Essa é heurística de praticante (03 §6.4; 04 §C8), não fonte primária. Usar como piso enquanto não houver dado do próprio canal.

| Resultado observado | Leitura | Ação |
|---|---|---|
| Winner no teste nativo, sem queda nas proteções | Efeito detectado pelo critério oficial, num vídeo | Adotar na embalagem do vídeo testado. Registrar como E1. Replicar antes de virar padrão do canal |
| Winner com Intro ou AVD abaixo da linha de base | Possível clickbait: promessa maior que o conteúdo (assinatura de 7628154) | Não adotar. Revisar a promessa ou cumpri-la nos primeiros 30 s |
| Performed Same | Sem diferença de desempenho | Não declarar vitória. Escolher pela coerência entre título, miniatura e conteúdo (03 §3) |
| Inconclusive | Sem diferença detectável com o poder do teste, que não é publicado | Manter a variante enviada primeiro. Registrar "sem efeito detectável". Não reinterpretar o rótulo |
| Série: primária na direção esperada, acima de δ, em pares independentes | Sinal consistente | Registrar como E2 ao atingir o número de repetições pré-registrado |
| Série: primária melhora e proteção piora | Conflito | Não adotar. Resolver o conflito antes de qualquer decisão |
| Série: efeito menor que o mínimo detectável (4.5) | Não detectável com o n do canal | Não decidir. Registrar como descritivo |
| Série: efeito oposto repetido | Evidência contrária | Rejeitar a variante. Registrar a evidência contrária, mesmo com n pequeno |
| Qualquer resultado com quebra de contagem na janela e sem linha de base ajustada | Leitura contaminada | "Não decidido" até o dado ser refeito com linha de base do mesmo lado da quebra |

### 4.4 Janelas de observação

| Janela | O que ler | O que não concluir | Base |
|---|---|---|---|
| 0 a 48 h | Publicação, classificação, cartão de impressões | Nenhuma decisão. Retenção ainda não processou. Cartão e relatório podem divergir | [OFICIAL, 9314486 via 08 §4]; 1 a 2 dias de processamento [OFICIAL, 9314415] |
| 3 a 14 dias | Diagnóstico: curva, Intro, origem. Teste nativo costuma durar de alguns dias a duas semanas [OFICIAL, via 03 §7.1] | Conclusão sobre embalagem sem volume | Divergência: um texto de terceiro manda ler CTR nas primeiras 24 h; a Central pede volume e não decidir cedo (03 §6.4; 08 §4). Seguir a Central |
| 28 dias | Comparação com a linha de base da mesma faixa e mesma janela | Comparar com janelas de outro período sem ajuste | [INFERÊNCIA] Mesma janela mensal que o Studio usa para audiência |
| 90 dias | Tempo de exibição, novos espectadores | Estimar cauda de longo prazo | Lacuna: a Central não diz por quanto tempo o sistema usa dados recentes (08 §7.2) |

### 4.5 Poder, tamanho de amostra e mínimo detectável

**Proporções (CTR).** A nota técnica de Evan Miller (2010, não revisada por pares) dá n ≈ 16·p(1−p)/δ² por grupo para comparar duas proporções [PRATICANTE]. Com p = 5% e δ = 2 pontos percentuais, o cálculo dá cerca de 1.900 impressões por variante (03 §6.5). Limites: a fórmula supõe impressões independentes, e a mesma pessoa pode ver a miniatura várias vezes; e o teste nativo tem método não publicado.

**Vídeos como unidade (séries).** Aqui a unidade é o vídeo, e a variância entre vídeos (tema, duração, humor do algoritmo) costuma dominar. A fórmula padrão para comparar duas médias com n vídeos por braço é:

MDE ≈ (z₁₋α/₂ + z₁₋β) · σ · √(2/n)

com z de 1,96 (α = 0,05 bilateral) e 0,84 (poder de 80%) [INFERÊNCIA; valores padrão de estatística, não extraídos do material]. σ deve ser medido na linha de base do canal, não tomado de fonte.

**Exemplo construído (valores hipotéticos, não são dados do canal).** Suponha σ = 8 pontos percentuais de Intro entre vídeos da faixa.
- n = 5 por braço: MDE ≈ 2,8 × 8 × √0,4 ≈ 14 pontos.
- n = 20 por braço: MDE ≈ 2,8 × 8 × √0,1 ≈ 7 pontos.
- Para detectar 3 pontos com σ = 8: n ≈ 111 vídeos por braço.

**Consequência.** Um canal pequeno só detecta efeito grande em série de vídeos. Por isso: (a) testar contrastes grandes, não ajustes finos; (b) usar o teste nativo sempre que houver volume, porque ele acumula impressões; (c) tratar o restante como hipótese replicada, não como resultado.

**Múltiplas comparações.** Com muitas métricas e muitos testes, algum sinal aparece por acaso. [INFERÊNCIA] Por isso a métrica primária é uma só por experimento, e as outras são diagnósticas e registradas.

### 4.6 Resultado ambíguo: o que fazer

1. Não promover a variante. Ambiguidade é ausência de decisão.
2. Verificar primeiro os pré-requisitos (4.1). Se algum falhou, refazer a leitura, não reinterpretar.
3. Se a primária e a proteção divergem, a regra pré-registrada decide. Se não havia regra, registrar o conflito e não decidir.
4. Replicar com contraste maior (variante mais distinta) ou em mais vídeos, se houver motivo para crer que o efeito existe.
5. Registrar como "sem decisão" com o motivo. Um registro de "sem decisão" é um dado útil para o próximo ciclo.

### 4.7 Regras de parada

- Teste nativo: deixar rodar até o fim automático do Studio. Encerrar antes só se houver violação de política ou problema de direito de uso (03 §7.7, passo 9).
- Série: não encerrar um par pela metade por resultado parcial. O número de pares é fixado antes.
- Qualquer parada antecipada é registrada no log com o motivo.

---

## 5. Ciclo operacional

### 5.1 Cadências

**Semanal (dia fixo, cerca de 30 a 60 minutos)**
- Checagem de publicações dos últimos 0 a 2 dias: publicação, classificação, cartão de impressões. Nenhuma decisão.
- Atualizar o log: datas, quebras, mudanças paralelas (links de descrição, série, tela final).
- Leitura diagnóstica de experimentos com 3 a 14 dias. Nenhum rótulo é lido sem a checagem de 4.1.
- Congelar o que está em teste. Preparar a próxima variante ou vídeo passando pelos portões de arquivo e de fatos (03 §6.1).
- Lista de pendências de verificação atualizada (seção 7.4).

**Mensal (reunião de decisão, cerca de 2 horas)**
- Decidir adoções, rejeições, replicações e encerramentos, com base em 4.3.
- Atualizar a linha de base por faixa de duração, com IDs congelados no log (desenho 4).
- Revisar as quebras de contagem do mês e se alguma linha de base precisa de ajuste.
- Escolher o que entra no mês seguinte. [INFERÊNCIA] Recomenda-se no máximo uma mudança de roteiro estrutural e um teste de embalagem por mês, para não confundir efeitos.
- Atualizar a fila de pendências de verificação.

**Trimestral (cerca de 2 horas)**
- Revisar os documentos da seção 7 com os níveis de evidência atingidos.
- Reavaliar o δ e o número de repetições, se o histórico do canal permitir.

### 5.2 Quem decide o quê

O canal pode ter uma pessoa só. Nesse caso, os papéis são chapéus diferentes, e a decisão deve passar pelo checklist de 4.1 antes de ser tomada.

| Decisão | Quem propõe | Quem valida | Quem decide | Critério |
|---|---|---|---|---|
| Abrir hipótese nova | Responsável de experimentos | Dono do canal | Dono do canal | Hipótese falsificável, origem apontada, métrica e proteção escritas |
| Mudar formato, tema sensível, política ou risco jurídico | Qualquer um | Checador de fatos e ética | Dono do canal | Portões G1 a G5 (03 §6.1) |
| Publicar variante de miniatura ou título | Editor ou designer | Checador de arquivo (G1 e G3) | Responsável de experimentos | Teste de compreensão (desenho 5) e checklist de 03 §3.5 |
| Adotar resultado de teste nativo | Responsável de experimentos | Dono do canal | Dono do canal | Winner sem queda nas proteções; registro como E1 |
| Adotar mudança estrutural (roteiro, abertura, duração) | Roteirista | Responsável de experimentos | Dono do canal | Nível E2 ou superior (seção 7.1) |
| Encerrar teste antes do fim | Responsável de experimentos | Checador | Dono do canal | Só por política, direito de uso ou erro de publicação |
| Fatos, números e nomes em roteiro e miniatura | Roteirista | Checador de fatos | Checador de fatos | Fonte primária e data, conforme 02 e 03 |

### 5.3 Modelo de log de experimento

Uma linha por experimento. Linha publicada não é editada. Se algo muda, abre-se nova linha com referência à anterior.

| Campo | Conteúdo obrigatório | Exemplo construído |
|---|---|---|
| ID | Código sequencial e data de registro | EXP-007 · 2026-12-02 |
| Etapa | Ideia, título, miniatura, hook, roteiro, retenção ou payoff | Miniatura |
| Hipótese | Enunciado falsificável, com direção | Miniatura com o mecanismo do caso vence miniatura só com rótulo em watch time |
| Origem | Arquivo e § ou código de hipótese da seção 2 | 03 §5.3, arquétipo C |
| Desenho | 1 a 5 (seção 3) | 1 (teste nativo) |
| Variável única | O elemento alterado | Conteúdo da imagem da miniatura |
| Versões | Nome dos arquivos A e B, resolução | A_mec.png (1280×720); B_rot.png (1280×720) |
| Vídeo e IDs | ID do vídeo, duração, faixa | Vídeo X, 24 min, faixa 20–35 |
| Datas | Publicação, início, fim previsto, janela de leitura | 2026-11-23; 2026-11-25; 2026-12-09 |
| Quebras | 24/08/2026 e 16/11/2026 cruzadas (sim ou não) | 16/11 cruzada; anotar TV se o Studio mostrar |
| Primária e δ | Métrica primária, δ e MDE se calculado | Rótulo do teste; δ definido pelo dono do canal |
| Proteções | Métricas de proteção e a linha de base de referência | Intro 30 s e APV contra linha de base da faixa 20–35 |
| Baseline | IDs congelados dos vídeos de referência | Vídeos Y1 a Y10 |
| Repetições previstas | Número de pares ou de vídeos antes de decidir | 1 (teste nativo) |
| Resultado | Rótulo ou valor, com a métrica exibida | Inconclusive |
| Anomalias | Mudanças paralelas, eventos, quebras | Links de descrição mudaram no dia 3 |
| Decisão | Adotar, rejeitar, replicar, sem decisão | Sem decisão; manter a variante enviada primeiro |
| Próximo passo | Ação e responsável | Replicar em vídeo de faixa semelhante, contraste maior |
| Status | Planejado, publicado, em leitura, concluído, abandonado | Concluído |

### 5.4 Regras de registro

- Salvar as telas ou exportações do Studio na data da leitura. [INFERÊNCIA] Os números podem mudar com a mudança de contagem, e a retroatividade não é clara (08 §9.2). O snapshot é a única forma de reconstruir a leitura.
- Guardar as versões dos arquivos A e B, com nome e data.
- Não apagar hipóteses sem resultado. Registrar também as que foram abandonadas.

---

## 6. Roteiro dos primeiros 90 dias

### 6.1 Critério de ordem

A sequência segue três critérios, em ordem: (1) custo de produção e de espera; (2) velocidade da leitura; (3) impacto esperado sobre a métrica primária. O impacto é hipótese de origem, não medida. Ideias de tema não têm experimento viável no curto prazo; a intervenção para esta etapa é de processo, e mede-se aderência aos portões G1 a G5, não desempenho.

Testes de embalagem vêm primeiro: custo baixo, leitura nativa, e impacto limitado ao clique e à primeira impressão. Testes de abertura vêm em seguida: impacto plausível sobre o começo, custo médio. Testes de estrutura vêm por último: custo alto e impacto sobre o meio do vídeo, com leitura lenta.

### 6.2 Sequência

| Ordem | Semanas | Experimento | Etapa | Origem (arquivo §) | Desenho | Custo | Leitura | Primária | Proteções |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1–2 | Instrumentação e linha de base: log, quebras, faixas de duração, IDs da linha de base, verificação se o Studio mostra CTR por origem e dispositivo | Todas | 03 §5.1; 08 §7.1; 04 §1 | Pré-requisito (desenho 4) | Baixo | 2 semanas | n/a | n/a |
| 1 | 1–2 | Checagem de elegibilidade do canal para o teste nativo: recurso, classificação de vídeo para crianças e +18, política | Todas | 03 §7.1; 08 §7.5 | Pré-requisito | Baixo | Imediata | n/a | n/a |
| 2 | 2–3 | Teste de compreensão pré-publicação em todas as miniaturas e títulos novos | Miniatura, título | 03 §6.3 | Desenho 5 | Muito baixo | 1 dia | Não aplicável (triagem) | Não aplicável |
| 3 | 2–4 | Teste nativo em vídeo antigo: miniatura com mecanismo do caso contra miniatura só com rótulo | Miniatura | 03 §5.3, arquétipo C (teste proposto) | Desenho 1 | Baixo | 1 a 2 semanas | Rótulo do teste | Intro e APV no período |
| 4 | 3–5 | Teste nativo em vídeo antigo com grande contraste de conteúdo: capa com três itens contra capa com um item em destaque | Miniatura e título | 03 §7.6 (micronações; teste proposto, não executado) | Desenho 1 | Baixo | 1 a 2 semanas | Rótulo do teste | Intro, APV, coerência do título |
| 5 | 4–9 | Abertura em par: cena datada com hora e lugar (H-06) contra resultado invertido nos primeiros 30 s (H-19) | Hook | 02 H-06, H-19 e §1 | Desenho 3 | Médio | 3 semanas por par | Intro 30 s | CTR por origem; AVD; APV calculado |
| 6 | 5–10 | Número de perguntas abertas em 0 a 60 s: uma contra três (H-23) | Hook | 02 §4 (conflito com a regra das duas perguntas) | Desenho 3 | Médio | 3 semanas por par | Intro 30 s | Inclinação 30 a 90 s (leitura); AVD |
| 7 | 6–10 | Payoff parcial antes de 2 min contra payoff só depois do bloco 3 | Payoff, roteiro | 05 §3 (Villach 01:59; Portugal 14:59); 05 §5.3 | Desenho 3 | Alto (reescrita do começo do bloco) | 4 semanas por par | APV calculado | Tempo total de exibição; Intro |
| 8 | 8–12 | Marcador de mudança de situação (intertítulo com novo lugar ou tempo) contra vídeo sem marcador | Retenção, roteiro | 07 CC2; PI1 e PI2 (lições e filme curto); 04 §4 | Desenho 3 | Médio (edição) | 4 semanas por par | Queda nas transições da curva | APV; tempo total |
| 9 | 10–13 | Replicação do melhor resultado E1 em tema diferente, com par novo | Todas | Resultado da fase anterior | Desenho 3 ou 4 | Médio | 3 a 4 semanas | Mesma primária | Mesmas proteções |
| 10 | Após 90 dias | Duração: mesma história em duas durações | Duração | 04 §9; 05 §3 | Desenho 3 | Alto | 6 semanas ou mais | APV calculado | Tempo total por impressão |

### 6.3 Condições de avanço e de parada

- **Após a fase de embalagem (linhas 2 a 4):** adotar a variante vencedora só como E1 e replicar. Se nenhum teste gerar Winner, seguir para a fase seguinte sem trocar a embalagem.
- **Após a fase de abertura (linhas 5 e 6):** só avançar para a próxima se houver um par com Intro acima da linha de base da faixa e a direção repetida no segundo par. Se não houver sinal acima do mínimo detectável, não decidir. Seguir para a próxima linha e registrar.
- **Antes de iniciar a fase de estrutura (linha 7 em diante):** exige que a fase de abertura tenha produzido pelo menos um resultado E1. Sem isso, a fase de estrutura é trocar um experimento caro por outro sem base.
- **Parada imediata:** problema de direito de uso (G1), violação de política (G5), quebra de contagem não anotada, ou erro de publicação.
- **Condição de cadência:** se o canal publica menos de um vídeo por semana, a série de pares da linha 5 não cabe em 90 dias com três pares. Nesse caso, reduzir para um par e marcar o resultado como exploratório. [INFERÊNCIA]
- **Sensibilidade:** o conteúdo de crime real envolve vítimas e familiares. Cada variante e cada abertura passa pelos portões G1 a G5 antes de entrar no teste (03 §6.1; 02 §1, riscos éticos).

### 6.4 O que fica fora dos primeiros 90 dias e por quê

- **Duração (linha 10):** custo mais alto, leitura mais lenta, e a faixa de duração ainda não tem linha de base interna. Só entra depois de duas faixas com linha de base estável.
- **Ideia de tema:** sem desenho viável. Entra como medição de aderência aos portões.
- **Efeito de spoiler ou teaser de desfecho:** a evidência é divergente em direção (07 §2.7.7). Não há teste de baixo custo no canal. Fica fora.
- **Cliffhanger por memória:** a evidência de vantagem de memória não se sustenta (07 M8). Só entra como teste de retomada, depois de a fase de payoff ter produzido resultado.

---

## 7. Como o aprendizado volta

### 7.1 Níveis de evidência do canal

Um resultado do próprio canal não muda automaticamente o status de uma estrutura na biblioteca. Ele registra um nível de evidência, com regra de promoção.

| Nível | Definição | Quem pode usar a evidência |
|---|---|---|
| E0 | Hipótese de biblioteca. Mecanismo descrito em fonte, sem medida no canal | Só como hipótese de teste |
| E1 | Um experimento com direção e primária acima do mínimo detectável, sem repetição | Pode orientar o próximo teste. Não entra em playbook como regra |
| E2 | Mesma direção em pelo menos o número de repetições pré-registrado (ao menos três, heurística de praticante, 03 §6.4 e 04 §C8) | Pode atualizar o documento de origem com nota de evidência do canal |
| E3 | Replicado em outro tema e outra faixa de duração, ao longo de pelo menos dois ciclos mensais | Pode alterar a recomendação do documento, com nota de limite |

**Regra geral:** nada passa de E1 para regra sem um segundo tema. Resultado contrário repetido rebaixa a hipótese, mesmo que o efeito original tenha sido positivo.

### 7.2 Destino de cada resultado

| Tipo de resultado | Documento | O que atualizar | Limite |
|---|---|---|---|
| Hipótese de abertura confirmada ou derrubada (E2 ou E3) | 02_hook_database.md | Adicionar coluna "evidência do canal" a cada H-xx testado. Não alterar o símbolo de "exemplo verificado" da matriz, que se refere a exemplo, não a efeito | O símbolo ● indica exemplo, não efeito (02 §2). Não confundir |
| Conflito de regra de perguntas (02 §4: duas perguntas contra H-23 e H-52) | 02_hook_database.md (seção 4) | Substituir o uso condicionado pelo resultado do teste, se E2 | Só vale para o gênero e a duração testados |
| Erro de abertura confirmado no canal (por exemplo, pedido de apoio antes da promessa) | 02_hook_database.md (seção 4 de erros) | Acrescentar o caso com dado do canal | Não generalizar para outros gêneros |
| Resultado de teste nativo de miniatura | 03_thumbnail_engineering_playbook.md | Arquétipos A a D (§5.3) com desempenho do canal; calibrar os critérios da rubrica (§6.2) um por vez | Pesos da rubrica só mudam após repetição (03 §6.5, regra 4) |
| Caso de miniatura que violou política ou direito | 03 §6.1 e §5.3 | Acrescentar o caso como exemplo de portão | Não é efeito sobre CTR |
| Resultado de payoff, segmentação ou clímax | 04_retention_engineering_blueprint.md (§9 e §10) | Linhas de bloco do framework de 30 min; checklist A e B (itens A3, A4, A5, B1 a B3) | Os minutos do framework são hipóteses; só o canal pode validá-los |
| Resultado de duração | 05_longform_storytelling_framework.md (§3) | Posição de clímax por faixa, com dado do canal | Amostra de 2 a 4 vídeos por faixa no documento de origem |
| Resultado de reviravolta ou revelação | 05 §5 | Registro de estados de conhecimento, se o teste mostrar que a revelação com pista plantada muda a retenção | Revelação honesta é exigência de método, não de efeito |
| Resultado de linha de base | 08_algoritmo_e_analytics.md (§4 e §7) | Faixas de duração e referências internas | Não substitui a referência da Central |
| Pergunta sobre Analytics que o canal conseguiu responder (por exemplo, efeito dos co-views) | 08 §9.2 e §9.4 | Mover de pendência para resposta, com o método | Só vale para o período e a fatia de TV observados |
| Resultado que contraria a biblioteca científica | 07_biblioteca_cientifica.md | Nota de "contraevidência do canal" na ficha. Não reescrever a ficha | Dado de canal não equivale a estudo controlado |
| Mudança no sistema de avaliação pré-publicação | 03 §3.5, 03 §6.2, 04 §10, 05 §6 | Item novo ou item removido do checklist, quando um item previu o resultado (ou não previu) | Itens de checklist são instrumentos de processo, não efeito |

### 7.3 Regras de atualização

1. Uma alteração por documento por mês, no máximo. Mudanças simultâneas em vários documentos a partir do mesmo resultado tornam impossível saber qual evidência sustentou cada uma.
2. Toda alteração cita o ID do experimento no log (seção 5.3).
3. Resultados E0 e E1 vão para a fila de pendências, não para os documentos de origem.
4. Antes de alterar um item de checklist, verificar se o item é preditivo: um item de checklist que nunca mudou o resultado de nenhum teste pode ser retirado. [INFERÊNCIA]
5. Quando o canal contradiz uma fonte da biblioteca, a contradição fica registrada, não resolvida por escolha de fonte. A resolução é um teste.

### 7.4 Pendências que os experimentos devem fechar

Estas pendências estão abertas nos entregáveis. Cada uma tem um teste proposto nesta parte.

| Pendência | Onde está | Teste proposto | Desenho |
|---|---|---|---|
| Métrica do rótulo Winner: fatia de watch time ou tempo por impressão | 03 §7.2 e §9.2; 08 §9.2 | Registrar impressões por variante quando o relatório mostrar; comparar o rótulo com as duas contas | Desenho 1 |
| CTR por variante no teste nativo e CTR por origem no Studio | 03 §9.2; 08 §9.2 | Checar na tela do Studio e registrar se aparece | Pré-requisito (linha 0) |
| Efeito dos co-views no watch time, no CTR e no AVD | 08 adendo | Separar, se o Studio mostrar fatia de TV, a leitura antes e depois de 16/11/2026; senão, usar snapshots | Desenho 2 com linha de base |
| Dia em que os co-views começaram | 08 §4 (16/11 por terceiros; "novembro" pela Central) | Confirmar na Central e registrar o dia no log | Pré-requisito |
| Janela de leitura do CTR nas primeiras 24 h | 03 §6.4 e §9.2 (divergente) | Não testar; seguir a Central, que pede volume antes de decidir | Não aplicável |
| Regra das duas perguntas em 0 a 60 s | 02 §4 (conflito com H-23 e H-52) | Linha 6 da seção 6 | Desenho 3 |
| Pagamento parcial de loop antes de abrir outro | 04 §6; 05 §5.3 | Linha 7 da seção 6 | Desenho 3 |
| Marcadores de fronteira e capítulos | 07 CC2, PI1, PI2; 04 §4 | Linha 8 da seção 6 | Desenho 3 |
| Inclinação de 30 a 90 s: leitura estável ou não | 04 §1; 02 §1 | Medir a variabilidade da inclinação na linha de base. Se for alta, não usar como critério | Desenho 4 |
| Faixas de duração do canal | 04 §1.1; 08 §4 | Definir pelas próprias publicações e congelar | Desenho 4 |
| APV como métrica oficial | 08 §4 e §9.1 | Não usar como métrica oficial. Rotular sempre "APV calculado" | Todos |
| Limiar em segundos da engaged view | 08 §4 e §9.1 | Não é possível testar. Anotar como lacuna | Não aplicável |
| Cliffhanger e continuidade de visualização | 07 M8; 05 §5.5; 04 §6 | Comparar a curva nas transições com pendência e sem pendência | Desenho 3, depois da linha 7 |
| Efeito de spoiler e de teaser de desfecho | 07 §2.7.7 | Fora dos 90 dias | Não aplicável |

### 7.5 Lacunas e limites desta parte

- **Nenhum desenho foi executado.** Os desenhos são propostas com base nos entregáveis e na documentação, e não há resultado de canal para ler.
- **Nenhum limiar estatístico é de fonte do material.** O MDE usa fórmula padrão e σ do canal. O δ e o número de repetições são decisões do canal. A regra de três repetições é heurística de praticante.
- **A nota de Miller não é revisada por pares** e supõe impressões independentes, o que não se verifica em vídeo.
- **O teste nativo tem método não publicado.** Não é possível calcular o poder dele. O rótulo Inconclusive não diz quanto efeito ficou sem detecção.
- **Não há curva de retenção de nenhum vídeo do corpus.** A linha de base do canal será a primeira medida de curva disponível. Toda leitura de curva antes disso é hipótese.
- **A amostra de vídeos é de alto desempenho**, sem grupo de comparação. Os padrões do corpus servem como origem de hipótese, não como efeito.
- **Canais em português.** A amostra tem 9 vídeos em português com transcrição, mas que os canais são faceless veio de busca na web e não foi conferido vídeo a vídeo (nota do orquestrador). As leituras de língua e de público são hipóteses.
- **A cadência de publicação do canal não está informada.** O roteiro de 90 dias depende dela; a condição está explícita na seção 6.3.
- **Divergências de entregáveis:** a contagem de vídeos (30, 35 ou 38) foi resolvida pelos fatos da execução (38, com 37 transcritos). Os números de retenção de terceiros (30% a 55%) não são usados em nenhum desenho, por não terem método (04 §11).
