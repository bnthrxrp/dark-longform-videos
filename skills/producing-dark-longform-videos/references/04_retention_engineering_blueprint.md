# Retention Engineering Blueprint

# Retention Engineering Blueprint: seções 1 a 11

**Limite do corpus:** nenhum vídeo do corpus tem curva de retenção visível. O corpus traz transcrições, metadados e análises estruturais. Por isso, toda leitura de "onde a curva cai" neste documento é [INFERÊNCIA] a partir da estrutura do roteiro, não observação de curva. Os exemplos reais são citados com minuto e trecho literal.

**Legenda:** [OFICIAL], [ESTUDO], [DADO], [PRATICANTE], [INFERÊNCIA]. Quando um estudo foi lido só em trecho, isso está indicado.

---

## 1. Leitura de curvas

### 1.1 O que o relatório mostra

- [OFICIAL] O relatório de retenção existe só no nível do vídeo, dentro de Analytics do vídeo. Os dados levam 1 a 2 dias para processar. Os "momentos-chave" só aparecem em vídeos com pelo menos 60 s e 100 views (https://support.google.com/youtube/answer/9314415?hl=en).
- [OFICIAL] Intro é a fração do público que ainda assiste após 30 s. Num vídeo de 40 min, esses 30 s são 1,25% da duração; num de 60 min, 0,83% [INFERÊNCIA, aritmética]. Intro mede sobretudo a promessa da abertura. A própria Central recomenda conferir se título e thumbnail correspondem ao conteúdo e testar outra abertura.
- [OFICIAL] Trecho plano: o público assiste do início ao fim daquele trecho. Queda gradual: perda de interesse ao longo do tempo. A Central diz que vídeos tendem a afinar durante a reprodução. Pico: trecho mais assistido, reassistido ou compartilhado. Vale: abandono ou pulo naquele ponto.
- [OFICIAL] Um pico pode indicar trecho interessante ou conteúdo pouco claro que obrigou o público a reassistir. Pico não é automaticamente bom.
- [OFICIAL] "Top moments" são trechos com quase nenhum abandono. Se aparecem tarde, a Central recomenda trazer o conteúdo forte para antes.
- [OFICIAL] A faixa "typical retention" compara com os 10 vídeos mais recentes do próprio canal de duração semelhante. A Central não define "duração semelhante".
- [OFICIAL] AVD é a média de minutos entre quem ficou (engaged views). APV, derivado, é AVD dividido pela duração [INFERÊNCIA, aritmética sobre a definição oficial de AVD].

**Divergência a registrar.** Terceiros usam "absoluta" e "relativa" para nomear a curva, e a Central usa "absolute number of views" para contagem bruta por segmento. A Central não define a base do percentual. Antes de planilhar, separe contagem por segmento de porcentagem.

**Gráfico "Most replayed" (público).** [OFICIAL] Mostra trechos reassistidos ao arrastar o marcador. Não é curva de retenção: não mostra quem saiu nem onde saiu. Não compare alturas entre vídeos.

### 1.2 Formatos, o que indicam e diagnóstico diferencial

| Formato | O que a documentação diz | Causa provável (status) | O que checar no roteiro | O que checar na edição |
|---|---|---|---|---|
| **Queda abrupta no início** (Intro baixo) | Vale na abertura; Central manda rever thumbnail/título e a abertura | Promessa que não bate com o título/thumbnail [OFICIAL]; abertura sem pergunta ou com contexto longo antes do primeiro fato [INFERÊNCIA] | A promessa dos primeiros 30 s coincide com título e thumbnail? Há pergunta explícita antes de 90 s? | Cortar saudações e agradecimentos; levar a cena ou o dado mais forte para o primeiro minuto |
| **Vale pontual** (queda em um instante) | Abandono ou pulo naquele ponto [OFICIAL] | Troca de tema sem ponte; inserção publicitária; trecho repetitivo que leva a pulo [INFERÊNCIA] | O que foi dito e mostrado nos 10 s antes do vale? Há mudança de tema sem frase de transição? | Verificar se a curva recupera a inclinação depois. Se recupera, provável pulo de trecho pouco útil. Se continua mais baixa, provável abandono |
| **Queda gradual** | Perda de interesse ao longo do tempo [OFICIAL] | Ausência de recompensa parcial por longo período; ritmo sem mudança de cena; bloco de contexto longo [INFERÊNCIA] | Quantos minutos seguidos sem pergunta respondida ou dado novo? Há bloco de inventário? | Comparar com a faixa "typical retention". Declínio contínuo é esperado; a pergunta é se o declínio é mais íngreme que o normal do canal |
| **Platô** | Trecho assistido do início ao fim [OFICIAL] | Público que precisa daquele conteúdo ou ritmo que o mantém [INFERÊNCIA] | O trecho plano tem recompensa ou é só exposição? | Se o platô segue um clímax ou revelação, ótimo. Se segue um bloco de contexto, o platô pode ser de quem não está mais engajado e ainda não saiu. Não trate como sucesso sem ler o conteúdo |
| **Pico** | Trecho interessante, reassistido ou compartilhado, ou confuso [OFICIAL] | Revelação, clímax ou explicação difícil [INFERÊNCIA] | O pico cai em revelação ou em explicação densa? | Se o pico é seguido de vale logo depois, releia o trecho: pode ser confusão. Se é seguido de platô, provável interesse |
| **Replay** (gráfico público) | Reassistido com frequência [OFICIAL] | Não é retenção; indica o que o público quis rever | Qual é o trecho reassistido: explicação, revelação ou cena? | Não use como prova de retenção. Use como pista de conteúdo difícil ou memorável |

**Leitura com evidência de outro formato.** Kim et al. (2014, [ESTUDO, trecho]), em 80 vídeos de tutorial de MOOC, relatam que 61% dos picos coincidem com transições visuais. É associação em aula online, não prova para narrativa de YouTube. [INFERÊNCIA] Se o pico coincide com troca de cena, é plausível que a transição seja a causa do pico, mas isso não foi testado em long-form narrativo.

**Pergunta que separa pulo de abandono.** [INFERÊNCIA] O relatório não separa pulo de saída. Um vale pode ser os dois. Sem essa separação, não atribua o vale a um trecho específico do roteiro sem ler o que o público viu antes e depois.

### 1.3 Limites de leitura

- A Central não dá limiar numérico para plano, pico ou vale. A leitura é qualitativa.
- Benchmarks de terceiros para retenção de 20+ min divergem (relatos de 30% a 55%, sem metodologia; ver §11). [PRATICANTE] Não use como alvo. A faixa "typical retention" do próprio canal é a referência oficial mais próxima.
- Em canal pequeno, a faixa "typical" é ruidosa [INFERÊNCIA, pois depende de 10 vídeos].
- Mudança de contagem de views a partir de 24/08/2026: a Central diz que a view passa a contar no início da reprodução. Terceiros afirmam que retenção e AVD não mudam, mas isso não está na página oficial que li. Ao comparar antes e depois dessa data, confirme a base.
- **Lacuna:** não encontrei curva de vídeo long-form de criador dark, com duração declarada e gráfico acessível. Não há como validar nenhum formato contra curva real neste material.

---

## 2. Pontos de abandono típicos

### 2.1 O que é documentado (e com que limite)

| Fonte | O que mostra | Limite |
|---|---|---|
| [OFICIAL] Central, Intro | Fração que fica após 30 s; recomenda rever promessa da abertura | Sem limiar numérico |
| [OFICIAL] Central, dips | Vales marcam abandono ou pulo em trechos específicos | Não separa pulo de saída |
| [DADO] Wu, Rizoiu & Xie (2018, ICWSM; PDF lido) | Duração sozinha explica mais de 58% da variância da porcentagem média assistida nos primeiros 30 dias, em 5,3 milhões de vídeos públicos | Dados agregados, sem curva; correlação; amostra de vídeos citados no Twitter com pelo menos 100 views |
| [ESTUDO, trecho] Kim et al. (2014, L@S) | Em MOOC, abandonos mais frequentes em vídeos mais longos e em sessões de primeira exibição. Slides (trecho truncado): 55% das sessões foram abandonos, e parte relevante dos abandonos ocorreu nos primeiros segundos (o percentual de 36% não foi verificado no texto integral) | MOOC; trecho truncado |
| [ESTUDO, trecho] Guo, Kim & Rubin (2014, L@S) | Um trecho atribui ao estudo que a mediana de engajamento é de no máximo 6 min, independentemente da duração total | MOOC; leitura do PDF falhou. **Divergência:** o dossiê de fadiga não confirmou esse limiar. Não use 6 min como regra |
| [ESTUDO, trecho] Risko et al. (2012) e Risko & Kingstone (2013) | Em aula gravada de 60 min, divagação aumenta com o tempo e a memória diminui; em aula de 40 min, atenção e retenção caem com o tempo | Laboratório, aula gravada; causa confundida com o conteúdo |
| [DADO, trecho sem autor confirmado] Estudo com registros do Panopto | Abandono de aula gravada concentrado no início do primeiro terço do vídeo | Aula, não YouTube; autores não confirmados. Não usar como fato |

**Conclusão do bloco:** a duração está associada a menor porcentagem assistida, mas a fonte não mostra onde o abandono acontece dentro do vídeo. O que se sabe sobre a posição do abandono vem de MOOC e de aula gravada, não de narrativa de entretenimento.

### 2.2 Pontos de abandono: causa provável e status

**A. Primeiros 30 s (Intro).**
- **Documentado:** Intro é medido e a Central manda conferir a promessa do título e da thumbnail [OFICIAL].
- **Inferência:** abertura de contexto antes de qualquer fato ou pergunta. No corpus, a maioria das aberturas tem fato ou cena em menos de 60 s; o contraste está em casos como Scary Interesting, em que o primeiro evento só aparece em 01:12 ("Caso 1: Marlborough"), depois de 72 s de geografia [DADO, transcrição].
- **Como verificar:** confira em quantos segundos aparece a primeira pergunta ou o primeiro fato verificável. Compare com a promessa do título.
- **Contraindicação:** em vídeos de ambiência, como Sleepy History (London, 180 min), a abertura calma é o formato. Esse caso não serve de modelo para o resto.

**B. Após o gancho: bloco de contexto longo antes do primeiro caso.**
- **Inferência, sem curva:** o risco de abandono está na distância entre a promessa e a primeira recompensa. Exemplo real: em "Joachim Kroll - Der Serienmörder aus Duisburg" (61:48), o bloco "Biografie" vai de 01:36 a 18:20; a primeira pergunta de "quem era esse homem" só é respondida em 18:20. O roteiro usa microgancho em 18:35 ("Was sie nicht wissen konnte, an diesem Tag begegnete sie einem Mann...", "O que ela não podia saber: naquele dia encontrou um homem..."). Não sei se a curva cai nesse bloco.
- **Como verificar:** no roteiro, conte os minutos entre a promessa e a primeira recompensa. Se passam de cerca de 10 min sem nova pergunta, o bloco precisa de uma pergunta de passagem ou de um dado novo.

**C. Inserção publicitária.**
- **Documentado:** nada na Central sobre patrocínio. Não há evidência de efeito de patrocínio sobre retenção no material.
- **Inferência, com exemplos:** em "How the US & China Are Preparing to Fight Total War", o narrador sai do argumento em 04:18–05:23 com inserção publicitária. Na transcrição de "Schlachtbericht..." (63:34) não encontrei inserção publicitária. Em "The Secret Chinese Company That Owns Everything", a narração de dominância segue depois. Em "The Armchair Historian: What Happened to Confederates...", a inserção aparece entre 04:18 e 05:23, e o roteiro retoma a imagem anterior ao voltar: "broad black streak of Ruin and desolation" (uma ampla faixa negra de ruína e desolação), vista em 04:02 e retomada depois do patrocínio. Isso é um padrão de reconexão, não prova de que a inserção não cause queda.
- **Como verificar:** anote o minuto de cada inserção e compare com o vale mais próximo na curva. Se o vale cai na inserção, a curva está dizendo isso; se não cai, a reconexão funcionou ou a inserção não custou.

**D. Blocos de catálogo ou inventário.**
- **Inferência:** blocos com a mesma estrutura repetida (ficha, dado, fechamento) podem gerar queda gradual, porque o espectador já sabe o que vem. Exemplos no corpus: "Die Dienstgrade der Waffen SS" (16:47) tem sete blocos de posto com os mesmos campos; "10 MICRONAÇÕES AO REDOR DO MUNDO" (11:26) repete o mesmo gabarito em 10 casos; "The Most Dangerous Ocean Crossing" segue casos de naufrágio com estrutura parecida.
- **Contraindicação:** catálogos curtos podem funcionar bem se cada item tem um desfecho diferente. O corpus mostra a diferença: as micronações fecham cada caso com o destino do território ou do fundador, o que dá um fim a cada item [DADO, transcrição].

**E. Depois do clímax (queda de pergunta).**
- **Inferência:** quando o clímax acontece e o roteiro continua por muito tempo sem nova pergunta, o espectador pode sair. O caso mais claro no corpus é "A TRAGÉDIA DE MIYAKO" (67:53): o clímax está em 39:14–40:42 ("A onda passa sobre o muro"), e o vídeo segue por cerca de 27 min com memória, consequência e fechamento, com encerramento em 66:39. Não sei se a curva cai ali; a estrutura torna essa queda plausível.
- **Como verificar:** meça o tempo entre o clímax e o último ponto de pergunta aberta. Se passa de cerca de um terço do vídeo, o bloco pós-clímax precisa de uma pergunta nova (consequência, responsabilidade, desfecho).

**F. Encerramento.**
- **Documentado:** a Central diz que trechos finais costumam perder audiência, e recomenda trazer o forte para antes [OFICIAL].
- **Praticante, não validado:** anunciar o fim com muito tempo de sobra incentiva a saída (dossiê de ritmo, item 15, [PRATICANTE]).
- **Corpus:** em "Warum ließ Hitler 350.000 Soldaten in Norwegen..." (30:42), a recapitulação dos vereditos é de 27:59 a 28:33. Em "Por Que Hitler Nunca Invadiu Portugal?" (17:21), a recapitulação começa em 16:19. [INFERÊNCIA] Recapitulação longa no fim é um risco se o espectador já conhece o argumento.

**G. Ponto de virada sem ponte.**
- **Documentado:** a Central fala em vales em trechos específicos, mas não diz por que [OFICIAL].
- **Inferência, com exemplo:** em "Schlachtbericht" (63:34), a passagem de 45:13 a 63:29 é um setor inteiro. Não há mudança de conflito ou de tema que o marque como novo, exceto o título de setor. Uma ponte explícita, como "Wir wenden uns nun..." (agora nos voltamos para...), é a forma de sinalizar a mudança. Não há dado sobre o efeito dela.

### 2.3 O que o material não permite diagnosticar

- Qual dos pontos A a G causa vale em algum vídeo do corpus. Não há curva.
- Efeito da duração de bloco sobre abandono em entretenimento. Os estudos de duração são de MOOC e de aula.
- Efeito de patrocínio em retenção.
- Efeito do humor, da relevância pessoal ou da mudança de escala sobre a curva. Nenhuma fonte mediu isso em long-form.

---

## 3. Mecanismos de sustentação que não são suspense

**Escopo.** Suspense, curiosidade e loops abertos ficam na seção de economia de loops (seção 6). Aqui entram os mecanismos que mantêm o espectador sem depender de uma pergunta pendente. A base empírica é fraca. Para cada mecanismo, marco o que é estudo, o que é corpus e o que é inferência.

**Teste de qualquer mecanismo: a aplicação só vale se o espectador recebe algo novo dentro do bloco, não só uma repetição com outra roupa.**

### 3.1 Visão geral

| Mecanismo | Base de evidência | Força | Dose de referência (status) | Principal contraindicação |
|---|---|---|---|---|
| Progressão de compreensão (uma explicação por bloco) | Rey et al. (2019), meta-análise de segmentação [ESTUDO]; corpus | Média para aprendizagem; baixa para retenção de visualização | Um mecanismo explicado por bloco [INFERÊNCIA] | Em entretenimento, pode virar palestra |
| Recompensa parcial | Hahn et al. (2023) [ESTUDO, nota de imprensa]; corpus | Baixa a média | Uma por bloco [INFERÊNCIA] | Recompensa sem consequência vira ruído |
| Novidade e mudança de cena | Zacks et al. (cinema) [ESTUDO]; Kim et al. (2014) [ESTUDO, trecho] | Média para segmentação de evento; sem evidência de retenção | Sem dose numérica; checar se o bloco parece parado [INFERÊNCIA; o dado de cinema não define intervalo de mudança] | Mudança sem sentido é só ruído visual |
| Mudança de escala | Corpus; sem estudo | Sem evidência | Uma mudança de escala por bloco [INFERÊNCIA] | Escala sem âncora na escala anterior confunde |
| Mudança de perspectiva | Corpus; sem estudo | Sem evidência | Uma por fronteira de bloco [INFERÊNCIA] | Quebra o fio se o narrador troca de lado sem aviso |
| Humor | Sem estudo no material | Sem evidência | Não definido | Humor fora de tom quebra a credibilidade |
| Relevância pessoal | Busselle & Bilandzic (2009) [ESTUDO, escala de autorrelato]; corpus | Sem evidência de retenção | Uma frase por bloco que liga ao espectador [INFERÊNCIA] | Endereçamento excessivo soa como vendas |
| Alternância informação/emoção | Ariga & Lleras (2011) [ESTUDO, laboratório]; corpus | Baixa para vídeo | Alternar tipo de bloco a cada bloco [INFERÊNCIA] | Alternância sem ponte parece corte brusco |

### 3.2 Mecanismos

**3.2.1 Progressão de compreensão.**
- **Como aplicar:** cada bloco entrega uma peça nova de explicação e termina sabendo mais do que começou. Em documentário, isso é um mecanismo ("como"), não só uma lista de fatos.
- **Evidência:** Rey et al. (2019) reúnem 56 investigações e 88 comparações sobre segmentação de material educativo. Na retenção (de aprendizagem, não de visualização), o efeito é d = 0,32 no geral; com segmentação imposta pelo sistema, d = 0,42; com controle do aprendiz, d = 0,19 e não significativo. Os autores não separam os mecanismos [ESTUDO, leitura integral]. Lacuna: esse dado mede aprendizagem em laboratório, não permanência em vídeo.
- **Corpus:** em "Warum Hitler nicht Portugal invadierte" (o título em português é "Por Que Hitler Nunca Invadiu Portugal?", 17:21), a pergunta do título é respondida em 14:59 com "quatro causas em sequência" [DADO, transcrição]. Em "Por Que Hitler...", a progressão parece seguir blocos temáticos ("Planos militares", "Lisboa como porta de saída", "Recurso econômico"), mas esses títulos não têm fonte verificada e a leitura de progressão depende da transcrição. Em "The Secret Chinese Company", o vídeo tem capítulos cronológicos nomeados (títulos não verificados na versão atual; a progressão precisa ser confirmada na transcrição) (ex.: "Virada mobile: WeChat", 33:51–39:35).
- **Dose:** um mecanismo principal por bloco de 5 a 10 min [INFERÊNCIA]. Se o bloco tem dois mecanismos, a explicação fica densa demais.
- **Contraindicação:** em formato de catálogo, a progressão vira inventário e perde força. Também pode gerar fadiga se o bloco é só explicação, sem pessoa ou consequência (ver seção 8).

**3.2.2 Recompensa parcial.**
- **Como aplicar:** dentro de um bloco, pague uma parte da promessa antes de abrir a próxima. Não é a resposta final: é um fato que muda o que o espectador pensa.
- **Evidência:** Hahn et al. (2023, [ESTUDO, nota de imprensa do UB; artigo não lido]) relatam em texto narrativo que suspense sem resolução deixa o público num estado negativo, e mediu, em texto curto, que um final de cliffhanger aumentou o desejo declarado de ler a próxima parte, sem diferença de suspense ou de enjoyment (Schibler, Hahn & Green, 2023, resumo; texto integral não lido). Esse é o único dado que li sobre resolução parcial e permanência. Condição: texto, não vídeo.
- **Corpus:** "Por Que Hitler..." paga em 02:30 o "primeiro segredo" da aliança com a Inglaterra. "J.P. Morgan Documentary: How One Man Financed America" paga em 09:33 o esquema das carabinas, com valores que o espectador acompanha ("compra a 3,5..."). "QUEM FOI HITLER: a história completa" paga em 06:48 o motivo da reprovação ("desenho de prova insuficiente", com a explicação dos desenhos de prédios).
- **Dose:** pelo menos uma recompensa parcial por bloco [INFERÊNCIA, heurística a testar]. Não há evidência para um intervalo específico em minutos.
- **Contraindicação:** recompensa que não muda nada na história vira "ruído de resolução". Verifique se a recompensa altera a pergunta seguinte.

**3.2.3 Novidade e mudança de cena.**
- **Como aplicar:** trocar o tipo de imagem, o lugar ou a ação com frequência suficiente para que o espectador não se acomode, e com sentido narrativo.
- **Evidência:** Zacks et al. (2010, cinema narrativo, [ESTUDO, trecho]) relatam duração média de 59,4 s (DP 28,1 s) para eventos grossos no cinema. Magliano & Zacks (2011, [ESTUDO, trecho]) mostram que a descontinuidade de ação prevê fronteira de evento. Kim et al. (2014, [ESTUDO, trecho]) associam picos a transições visuais em tutoriais de MOOC. Nenhum desses estudos mede retenção de vídeo longo.
- **Corpus:** "SEGUNDA GUERRA MUNDIAL: do primeiro tiro ao último dia" (49:02) abre com seis cenas em cerca de 50 s, cada uma com um lugar e um fato. "Sleepy History of London" (180:09) usa um achado físico ("cave lions, wild ox, hippopotami, and rhinoceroses", em 02:38) como troca de cena.
- **Dose:** [INFERÊNCIA] sem dose numérica: o dado de cinema (eventos de cerca de 59 s) descreve duração de evento perceptivo e não define intervalo de mudança em vídeo longo. Não é meta: é um ponto de partida para checar se o bloco parece parado.
- **Contraindicação:** em documentário com entrevistas longas, mudança de plano sem mudança de conteúdo não sustenta. Vale mais a mudança de *informação* do que de *imagem*.

**3.2.4 Mudança de escala.**
- **Como aplicar:** alternar a escala do que está sendo mostrado: do indivíduo ao sistema, do local ao continente, do microscópico ao cósmico. A escala muda, e a comparação com algo conhecido ancora a nova escala.
- **Evidência:** nenhuma fonte mediu isso. É prática observada no corpus [DADO, transcrição].
- **Corpus:** "What's Hidden Under the Ice of Antarctica?" (37:54) compara a Antártida com os 48 estados dos EUA em 00:31, e o cânion com o Mar Morto e com o Everest em 09:40. "Top 5 legendäre Schlachten..." trata escala de explosão (17:24, "60 Tonnen Sprengstoff", 60 toneladas). "A TRAGÉDIA DE MIYAKO": a escala muda de uma cidade para uma costa inteira na parte de geografia. O tsunami de Lituya Bay é declarado o maior em 13:19 e separado do efeito geral em 13:51 ("ponto de medição" versus efeito geral) [DADO, transcrição].
- **Dose:** uma mudança de escala por bloco [INFERÊNCIA].
- **Contraindicação:** escala sem âncora confunde. A mudança precisa de uma comparação que o espectador já tenha. Superlativo sem correção (ex.: "o maior da história") é arriscado: o próprio corpus mostra a correção em 13:51.

**3.2.5 Mudança de perspectiva.**
- **Como aplicar:** mudar quem fala, de que lado a história é vista, ou que pergunta está sendo feita. Ex.: pedir ao espectador que pense como o adversário.
- **Evidência:** sem estudo no material. Corpus e prática.
- **Corpus:** "How the US & China Are Preparing to Fight Total War" (58:25) pede ao espectador que pense como o adversário em 37:11–38:00 (resumo do dossiê; minuto e trecho não verificados no transcrito). "Warum ließ Hitler 350.000 Soldaten..." reenquadra a questão moral em 28:17: "Die Frage, ob die Soldaten gekämpft haben, verdeckt die Frage, was sie getan haben." (A pergunta se os soldados lutaram encobre a pergunta sobre o que eles fizeram.)
- **Dose:** uma mudança de perspectiva por fronteira de bloco [INFERÊNCIA].
- **Contraindicação:** trocar de lado sem aviso confunde. Em documentário com tese, a mudança precisa vir antes da conclusão, não depois.

**3.2.6 Humor.**
- **Evidência:** nenhuma fonte do material mede humor e retenção em long-form. Lacuna.
- **Corpus:** "J.P. Morgan" usa humor com dado concreto em 03:30: "ما يعادل Photoshop في القرن التاسع عشر." (O equivalente ao Photoshop no século XIX.) A comparação é com um dado concreto, não com piada solta.
- **Dose:** [INFERÊNCIA] humor que nasce de dado ou de comparação, em pequenas doses, sem tomar a cena dramática.
- **Contraindicação:** humor fora de tom em true crime ou em história de guerra reduz a credibilidade. Não use humor sobre vítimas.

**3.2.7 Relevância pessoal.**
- **Evidência:** Busselle & Bilandzic (2009, [ESTUDO, escala de autorrelato]) separam quatro dimensões do engajamento narrativo, incluindo engajamento emocional e presença narrativa. A escala não mede retenção.
- **Corpus:** "Micronações" (11:26) usa endereçamento direto em 03:31: "bem se você pensou em declarar a sua casa como seu reino" (quem já pensou em declarar a casa como seu reino). "Designers Que Usaram 100% Do Cérebro" (38:40) convida a discordar em 03:45: "Você pode até achar que o design lembra mais um repolho, mas fazendo um certo esforço, eu vou discordar."
- **Dose:** uma frase de endereçamento por bloco [INFERÊNCIA].
- **Contraindicação:** endereçamento excessivo soa como vendedor e pode aumentar o vale de quem não se reconhece no exemplo.

**3.2.8 Alternância informação/emoção.**
- **Evidência:** Ariga & Lleras (2011, [ESTUDO, laboratório, tarefa visual]) mostram que tarefas ativas intercaladas preservam desempenho em vigilância, o que é análogo, mas não equivalente, a alternar tipo de bloco em vídeo. Sem estudo de vídeo longo.
- **Corpus:** "What Happened to Confederates After the Civil War?" (16:00) alterna bloco político (02:10–03:13), bloco de "Virada e devastação humana" (03:13–04:18), e "Ruína econômica" (05:23–06:28). "Por Que Hitler..." tem um "Respiro narrativo" em 09:17–10:21 (Casino Estoril, Popov e Fleming) entre blocos logísticos. O respiro é explicitamente anunciado como tal.
- **Dose:** alternar entre bloco analítico e bloco de pessoa ou de consequência, sem regra de minutos [INFERÊNCIA].
- **Contraindicação:** alternância sem ponte causa corte brusco. Também não substitui a progressão: um respiro que não avança a história só desacelera.

### 3.3 Como combinar

- [INFERÊNCIA] Em cada bloco, um mecanismo dominante (progressão ou novidade) e um secundário (recompensa, endereçamento ou mudança de perspectiva). Mais de três mecanismos no mesmo bloco não tem base no material.
- Os mecanismos de 3.2 não substituem o cronograma de perguntas. Se o bloco não tem pergunta nem recompensa, a novidade sozinha não sustenta (ver seção 6).
- Nenhum deles foi medido em retenção de vídeo long-form de YouTube. Os usos acima são hipóteses a verificar com a curva do próprio canal, usando a faixa "typical retention" como referência oficial.

**Lacunas desta seção:** nenhum estudo mediu humor, relevância pessoal, mudança de escala ou de perspectiva com retenção. A evidência de novidade vem de cinema e de MOOC. A evidência de recompensa parcial vem de texto narrativo. Não há curva de vídeo do corpus para confirmar nenhum dos padrões de 2.2 ou 3.2.

## 4. Blocos narrativos de 2, 5 e 10 minutos

**Legenda dos vídeos citados** (transcrições automáticas; os minutos vêm das fichas de engenharia reversa, não de medição própria): *Norwegen* = "Warum ließ Hitler 350.000 Soldaten in Norwegen..." (30:42); *Antarktis* = "What's Hidden Under the Ice of Antarctica?" (37:54); *Mittelalter* = "Doku: Wie war Sex im Mittelalter?" (33:39); *Dreißigjährige* = "Der Dreißigjährige Krieg" (46:32); *Villach* = "Die Hexen von Villach" (31:34); *Kroll* = "Joachim Kroll" (61:48); *Cold Case* = "3 People Who Disappeared..." (18:08); *Portugal* = "Por Que Hitler Nunca Invadiu Portugal?" (17:21); *Prochorowka* = "Schlachtbericht..." (63:34); *Tencent* = "The Secret Chinese Company..." (78:46).

**Status da evidência.** [INFERÊNCIA] Não encontrei estudo que compare blocos de 2, 5 ou 10 minutos em vídeo longo com retenção, AVD ou divagação. Os tamanhos abaixo são desenho de processo, não achado. O que existe é mais distante:
- Guo, Kim & Rubin (2014), MOOC [ESTUDO, trecho; PDF não lido]: sessão mediana de até 6 min, "regardless of total video length". É limite de sessão de aula, não de retenção de entretenimento.
- Rey et al. (2019), meta-análise de segmentação [ESTUDO, PDF lido]: retenção d = 0,32 no geral; d = 0,42 quando o sistema impõe as pausas; d = 0,19, não significativo, quando o aprendiz controla o ritmo. A unidade é "significado coerente", não minutagem. Condição: lições de laboratório.
- Zacks et al., segmentação de cinema [ESTUDO, trecho]: eventos grossos com média de 59,4 s. [INFERÊNCIA] A unidade de cena fica na casa de segundos a um minuto. Um bloco de 10 min contém dezenas de cenas. O tamanho do bloco de capítulo não se deduz daí.

**Blocos observados no corpus** [DADO: minutagem das fichas; o cálculo de duração é meu]:

| Vídeo | Blocos internos (duração em min) | Leitura [INFERÊNCIA] |
|---|---|---|
| Norwegen | 1,2 · 2,4 · 2,0 · 2,3 · 2,3 · 2,2 · **7,7** | Explicação em blocos de ~2 min; um bloco de teste longo |
| Antarktis | 2,9 · 1,9 · 1,9 · 2,2 · 1,6 · 1,8 · 2,2 · 1,6 · 2,9 | Blocos de 1,6 a 2,2 min no miolo |
| Mittelalter | 1,9 · 2,9 · 1,4 · 1,9 · 1,7 · 2,8 · 1,4 · 2,7 | 1,4 a 2,9 min, alternando âncora de lugar e tema |
| Dreißigjährige | 3,1 · 1,3 · 5,0 · 1,7 · 4,5 · 5,7 · 3,0 · 7,2 | Blocos de época e de batalha: 3 a 7 min |
| Villach | 2,1 · 3,3 · 3,25 · 3,6 · 2,4 · 2,6 | Cada caso ocupa ~2,5 a 3,5 min |
| Cold Case | 3,6 · 5,3 · 8,0 | Um caso por bloco; o terceiro caso é o mais longo |
| Kroll | 1:36–18:20 (biografia); 18:20–49:18 (série de crimes) | Macroblocos de 17 a 31 min, com subfichas por caso |

Leitura agregada: as subdivisões internas mais comuns ficam entre 1,5 e 3 min (explicação, contexto, tese). Casos de true crime ficam entre 3 e 5 min. Macroblocos acima de 7 min aparecem em contextos longos (Dreißigjährige, Kroll) ou em um teste extenso (Norwegen, 15:13–22:54). Nenhum dos vídeos usa 10 min como bloco regular. Isso é descritivo, não é meta.

**Função de cada tamanho (processo proposto).**

| Tamanho | Função | Usar quando | Contraindicação |
|---|---|---|---|
| **2 min** | Unidade de explicação: um mecanismo, um dado ou uma hipótese, com resposta parcial | Contexto, mecanismo, verificação de fonte (Norwegen, Antarktis) | Não sustenta uma cena sozinho. Sem ponte, vira passagem sem recompensa. |
| **5 min** | Unidade de caso ou de virada: pergunta, complicação, resposta parcial e nova pergunta | Casos em série (Villach, Cold Case) e uma hipótese com teste | Caso sem resposta parcial até o fim do bloco acumula loops (ver seção 6) |
| **10 min** | Ato ou capítulo, formado por dois blocos de 5 min com marcador de transição | Vídeos de 30 min ou mais, onde o capítulo é o ato | Sem marcador interno, um bloco de 7 a 8 min já vira "trecho longo" (Norwegen 15:13–22:54). A regra de 10 min não tem fonte primária (ver seção 8). |

**Estrutura interna (modelo preenchível).** Quatro slots em todo bloco:
1. **Abertura (até ~15 s):** âncora (data, lugar, nome) + pergunta do bloco. Exemplos reais: "Der 12. Juli 1943. Es ist der achte Tag des Unternehmens Zitadelle" (Prochorowka, 00:00); "Das nächste Opfer." (Villach, 13:18), que abre o bloco seguinte.
2. **Desenvolvimento:** um mecanismo ou um caso. Num bloco de 5 min, no máximo uma complicação (um dado que contradiz a hipótese anterior).
3. **Recompensa:** uma resposta parcial com número ou nome. Exemplos: Norwegen 06:30, "o minério explica a ida à Noruega", com ressalva; Villach 05:19, "explicação completa do método em duas fases".
4. **Ponte (últimos ~15 s):** a frase final aponta a próxima pergunta. Exemplo: "Um den Verlauf am Nordflügel zu verstehen, müssen wir zum Morgen des 12. Juli zurückkehren." (Para entender o curso na ala norte, precisamos voltar à manhã de 12 de julho; Prochorowka, 34:01).

Modelos:
- **Bloco de 2 min:** 0:00–0:15 âncora + pergunta · 0:15–1:30 mecanismo ou dado · 1:30–1:50 resposta parcial · 1:50–2:00 ponte.
- **Bloco de 5 min:** 0:00–0:20 abertura · 0:20–2:30 caso ou hipótese 1 · 2:30–3:30 complicação · 3:30–4:40 resposta parcial · 4:40–5:00 ponte para o próximo caso ou loop.
- **Bloco de 10 min:** dois blocos de 5 min com marcador explícito entre eles. Marcador observado: "Musik" seguido de nova cena (WWI, "Top 5 legendäre Schlachten", reabertura de bloco; Prochorowka, [musik] em 62:40).

**Exemplo construído (não é dado):** um vídeo de 30 min com 1 abertura de 2 min, 4 blocos de 5 min e 1 capítulo final de 10 min com dois marcadores. A soma dá 32 min; no roteiro, reduza o capítulo final para 8 min.

**Condições e limites.** Vale para narrativa de não-ficção com casos ou mecanismos. Não validado para vídeo de entretenimento com cena contínua. O corpus é de alto desempenho e pequeno (o número de vídeos varia entre seções e está pendente de fixação; ver §11); não mostra que esses tamanhos produzem retenção melhor.

## 5. Microganchos e pontes

**Catálogo.** Cada entrada traz a função, a frase do corpus (original, com tradução entre parênteses) e a posição observada. A minutagem vem das fichas.

| Tipo | Função | Exemplo do corpus | Posição |
|---|---|---|---|
| Ironia dramática | O espectador sabe mais que o personagem | Kroll, 18:35: "Was sie nicht wissen konnte, an diesem Tag begegnete sie einem Mann..." (O que ela não podia saber: naquele dia encontrou um homem...) | Antes de um ataque ou de um erro |
| Revelação atrasada de identidade | Pagar um nome que já foi prometido | Kroll, 00:19 (personagem sem nome) → 00:36: "Sein Name ist Joachim Kroll." (Seu nome é Joachim Kroll.) | Dentro do cold open |
| Reenquadramento de título ou de rótulo | Corrige a expectativa criada pela promessa | Prochorowka, 14:18: "Es handelt sich jedoch um ein örtlich begrenztes Gefecht, nicht um hunderte Tiger..." (Trata-se de um combate localizado, não de centenas de Tigers...) | Após o clímax prometido pelo título |
| Reenquadramento de pessoa | Desfaz o rótulo do vilão | Clodimar, 02:08: "O tal homem do chapéu... eu já posso adiantar que não era nenhum bandido não" | Primeiro minuto e meio |
| Marcação de dado para retorno | Um detalhe fica guardado para ser usado depois | Norwegen, 07:54: "Merk dir diese Delle." (Guarde essa queda.) | No meio do bloco, com retorno explícito |
| Checagem de fonte | Diz de onde vem a afirmação | Norwegen, 05:32: "Eine hübsche Geschichte. Sie stammt aber nur von ihm selbst." (Uma história bonita. Mas vem só dele mesmo.) | Antes de usar um testemunho |
| Objeção antecipada | Responde à dúvida que o espectador ainda não formulou | Norwegen, 10:41: "Nun könnte man sagen: Hitler hatte eben Angst, ohne Grund. Aber das stimmt nicht ganz." (Poderia-se dizer que Hitler tinha medo sem razão. Mas isso não é bem assim.) | Antes de uma tese |
| Ressalva de credibilidade | Admite a falta de evidência sem perder a linha | El Señorial, 13:13: "pero quiero aclarar que en aquel momento no había evidencia que confirmara esas versiones." (mas quero deixar claro que, naquele momento, não havia evidência que confirmasse essas versões) | Antes de uma versão não comprovada |
| Anúncio de caso | Fecha um caso e abre o próximo | Villach, 13:18: "Das nächste Opfer." (A próxima vítima.) | Última frase do bloco |
| Prolepse de custo | Anuncia um preço que será pago depois | Bulger, 02:45: "que James Bulger pagaría muy caro aquel día" (que James Bulger pagaria muito caro naquele dia) | Antes da cena central |
| Contagem em loop | Abre com um número e fecha com a contagem completa | Segunda Guerra (PT), 00:38: "E são repelidos. Quatro vezes." → 39:22, quinta tentativa | Teaser, com pagamento longe |
| Pergunta de transição de capítulo | Passa ao próximo eixo como pergunta | Segunda Guerra (PT), 05:33: "Faltava ver até onde o resto do mundo ia deixar que eles fossem." (Faltava ver até onde o resto do mundo ia deixar que eles fossem.) | Ponte entre capítulos |
| Reversão de mito | Nega a versão popular antes de expor a fonte | Homo habilis, 06:58 → 07:16: "...uma versão beta da humanidade" → "Errado." | Após a apresentação do mito |
| Lacuna declarada | Admite o que não se sabe | Sleepy History, 11:15: "we don't know exactly what was going on in Londinium" (não sabemos exatamente o que acontecia em Londinium) | Ponto de incerteza do bloco |
| Desinflação | Reduz uma suspeita antes de ela crescer | Cicada 3301, 02:17: "Of course, it was nothing but a rumor." (Claro, era só um boato.) | Depois de uma pista sedutora |

**Posicionamento (regras de processo, [INFERÊNCIA] a partir das posições observadas):**
- Ponte no último trecho do bloco, em frase curta. Os exemplos reais (Villach 13:18; Prochorowka 34:01) são frases curtas no fim.
- Ironia dramática antes do evento, nunca depois. Depois do fato, ela vira informação.
- Microgancho de reenquadramento (título ou pessoa) só depois de a promessa ter sido feita. Antes, não há expectativa a corrigir.
- Pedido explícito de permanência ("acompanhe até o fim para saber mais", JP Morgan, 01:30, em árabe) não tem evidência de efeito no corpus. Use só com um pagamento marcado.
- Cadência em segundos: praticantes propõem intervalos divergentes (30–60 s, 60–90 s, 90–180 s) sem fonte primária (ritmo, item 13). Não use como regra. Use a fronteira de bloco como unidade.

**Limites.** Os microganchos são observados em transcrição automática (erros como "Trafalga Square" e "Hábiles" aparecem no original). A eficácia de cada tipo não foi medida. A classificação é minha, a partir das fichas.

## 6. Economia de loops

**Definição de loop.** Pergunta, promessa ou lacuna aberta, com prazo declarado ou implícito. Um loop é "pago" quando recebe resposta, mesmo parcial.

**Evidência disponível.**
- Loewenstein (1994) [ESTUDO, página secundária]: a curiosidade surge de uma lacuna de conhecimento. Uma revisão de 2026 relata que a motivação cai quando a lacuna é grande demais ou pequena demais. [INFERÊNCIA] "Algo misterioso" tende a ser lacuna grande demais. Pergunta específica funciona melhor.
- Ely, Frankel & Kamenica (2015) [ESTUDO, modelo teórico; resumo]: o suspense cresce com a variância das crenças seguintes. Num romance de mistério, a chance de reviravolta cai a cada capítulo, mas a reviravolta fica mais dramática. [INFERÊNCIA] Hipótese: poucos loops grandes e tardios, em vez de muitos pequenos.
- Hahn, Schibler & Green (2023) [ESTUDO, nota de imprensa; texto narrativo, não vídeo]: um final de cliffhanger deixa o público num estado negativo, e o desejo declarado de ler a próxima parte aumentou, sem diferença de suspense ou de enjoyment (Schibler, Hahn & Green, 2023; resumo, texto integral não lido). [INFERÊNCIA] Trate o pagamento parcial de loop como hipótese de teste, não como regra.
- Wirz et al. (2022) [ESTUDO, trecho; leitura falhou]: o resultado, segundo o trecho, contraria a crença de que cliffhangers prendem o espectador. **Divergência não resolvida** com Hahn et al. Não escolha lado sem o texto integral de Wirz.

**Intervalos de pagamento observados no corpus** [DADO, minutagem das fichas; INFERÊNCIA no agregado]:

| Loop | Abertura | Pagamento | Intervalo aprox. |
|---|---|---|---|
| Segunda Guerra (PT): "Paris cai" | 00:07 | 15:28 | ~15 min |
| Segunda Guerra (PT): navios afundando no litoral brasileiro | 00:22 | 25:17 | ~25 min |
| Portugal: pergunta-título | 01:22 | 14:59 | ~13,5 min |
| Kroll: "Wer also war dieser Mann..." | 01:09 | 18:20 | ~17 min |
| Doppelgänger: "Wer tot scheint, ist lebendig." | 01:03 | 10:12 (identidade) / 11:12 | ~9–10 min |
| Sleepy History: "we'll get to that later" | 24:48 | 36:16 | ~11,5 min |
| Tencent: "Only later would it become clear why" | 31:03 | 44:24 | ~13 min |
| Villach: "Was sich wirklich dahinter verbirgt..." | 00:10 | 01:59 (resposta parcial) / 05:19 (método completo) | ~2 a ~5 min |

Leitura [INFERÊNCIA]: nos vídeos mais longos, pagamentos parciais chegam em 2 a 10 min e pagamentos completos em 10 a 25 min. Não há relação causal demonstrada.

**Quantos loops manter.** O corpus não dá número ótimo. Observado: Portugal tem 2 perguntas-mestras (título e preço, 01:22). Ampulheta (Hitler, PT) abre com cinco perguntas no primeiro minuto (00:07–01:22). Cold Case reformula uma pergunta única a cada bloco. [INFERÊNCIA] Processo sem número validado: liste no roteiro todos os loops abertos, e a partir de 2 loops simultâneos sem pagamento parcial, pare e pague antes de abrir o terceiro. A cifra "2" é minha, sem fonte. Teste no próprio canal antes de adotá-la.

**Processo de auditoria de loops (roteiro):**
1. Atribua a cada loop um ID (P1, P2…), o minuto de abertura e o tipo: resposta, lacuna declarada, reenquadramento ou prolepse.
2. Marque o pagamento parcial e o final, com minuto.
3. Verifique se há loop aberto no último terço sem prazo. Se houver, ou o pagamento entra no último terço, ou o loop é encerrado com lacuna declarada.
4. Verifique se algum loop nasceu de um objeto e se o objeto volta (ex.: a "pedra negra" de Portugal, 01:22, volta como volfrâmio, 10:22, segundo o dossiê de ritmo).

**Frustração e esvaziamento.**
- *Frustração:* loop sem prazo, sem pista nova e com a mesma pergunta repetida. Sinal no roteiro: duas ou mais ocorrências seguidas da pergunta sem fato novo entre elas. Não há limiar medido.
- *Esvaziamento:* todos os loops pagos cedo e nenhum novo aberto no último terço. Nesse caso, o vídeo perde a razão de ficar.
- *Ponto de equilíbrio observado:* Flight 370 encerra com incerteza declarada ("For now, it seems, the vanishing of Flight 370 will remain a mystery", Flight 370, 24:24). Cicada 3301 encerra com hipótese marcada como tal, em 17:04. Sleepy History declara lacuna (11:15). A incerteza é aceitável quando é declarada; sem declaração, vira frustração.

**Condições e contraindicações.**
- Loops de identidade e de mistério funcionam em true crime e em história. Em documentário de processo, a pergunta deve ter resposta verificável.
- Loop de incerteza declarada precisa de um fecho honesto, como o de Cicada 3301 (17:04: "I personally think... the most plausible explanation").
- Não use loops como substitutos de conteúdo. Hipótese sem respaldo: um loop sem resposta planejada tende a parecer enrolação.
- Todos os intervalos vêm de transcrições automáticas e de anotações das fichas. A leitura de "pagamento parcial" é interpretação, não medida.

## 7. Ritmo e densidade

### 7.1 O que a medida captura e o que não captura

- **Definição usada:** palavras da transcrição divididas pelos minutos do bloco. O corpus traz esse valor por bloco de 5 min e por vídeo. [DADO: transcrições do corpus de engenharia reversa]
- **Limite 1, transcrição automática.** A base é legenda automática, com erros em nomes próprios e em palavras estrangeiras. Trechos como "[musik]" aparecem sem conteúdo. [DADO]
- **Limite 2, mede só fala.** Pausas, música, efeitos sonoros, silêncio e texto na tela não entram. Um bloco de 103 palavras/min pode ter 30% de silêncio ou nenhum. A densidade percebida depende disso, e o corpus não permite separar os dois casos. [INFERÊNCIA]
- **Limite 3, blocos finais são parciais.** Blocos de menos de 5 min no fim do vídeo distorcem a leitura. Exemplos: Sleepy History, 55 min com 4 palavras; Villach, 30 min com 28; Norway, 30 min com 11; Moskvin, 25 min com 51; Cape Horn, 25 min com 69. Não usei esses blocos nas comparações.
- **Limite 4, idioma.** A contagem de palavras depende da língua. O alemão aglutina termos compostos, e as demais línguas têm outra tokenização. Compare só dentro do mesmo idioma e, de preferência, com o mesmo narrador.
- **Limite 5, não é medida de retenção.** Nenhum vídeo do corpus tem curva publicada. A "razão de outlier" mede views contra a mediana do canal, não retenção. Views não medem qualidade narrativa. [regra do corpus; DADO]

### 7.2 Referência descritiva do corpus

Valores do corpus, vídeos com valor disponível (37 de 38; Crop Circles não tem transcrição). Medianas calculadas por mim a partir dos valores do corpus. [INFERÊNCIA sobre DADO]

| Idioma | n | Faixa (palavras/min) | Mediana | Extremos |
|---|---|---|---|---|
| Alemão | 10 | 103–163 | 131,5 | Prochorowka 103; Ingolstadt 163 |
| Inglês | 10 | 30–209 | 157,5 | Sleepy History 30 (artefato de transcrição, a excluir da faixa); Cape Horn 209 |
| Espanhol | 8 | 107–173 | 136 | Bulger 107; OVNIS 173 |
| Português | 9 | 93–177 | 122 | Miyako 93; Designers 177 |

Mediana geral (todos os idiomas misturados, só para ter um número de referência): 138. Não use como alvo: a mistura de idiomas invalida a comparação.

Leituras:
- **Sleepy History (30 palavras/min)** é narração para dormir, instruída explicitamente a relaxar ("just relax and let your mind drift", 00:38–00:56). A densidade baixa não deve ser lida como densidade real: a média de 30 palavras/min mistura blocos completos de 87 a 98 com blocos finais quase vazios, um artefato de transcrição truncada (ver §7.1). Seu volume de views (1.048.659) não é evidência de que a densidade baixa funcione. [DADO; regra 4]
- **Cape Horn (209 palavras/min)** é o extremo alto. O vídeo tem 26:45 e 3,5 milhões de views. A densidade alta conviveu com desempenho alto, mas isso não diz que a densidade causou o desempenho. [DADO; regra 3]
- **Abertura (primeiros 90 s):** o corpus vai de 58 palavras (Flight 370, cuja abertura é uma cena de rotina seguida de ruptura aos 02:29) a 296 (Total War, com contexto geopolítico denso desde o primeiro segundo). [DADO] Um hook denso em palavras não é pré-requisito: o caso de Flight 370 mostra que imagem e normalidade anunciada também seguram a abertura. Isso é descritivo; não há curva para confirmar o efeito. [INFERÊNCIA]

### 7.3 Variação dentro do vídeo

Amplitude entre o bloco mais lento e o mais rápido (blocos de 5 min completos). [DADO] calculado a partir das transcrições; [INFERÊNCIA] nas interpretações.

| Vídeo (idioma, duração) | Mais lento | Mais rápido | Amplitude | Leitura |
|---|---|---|---|---|
| Sleepy History (en, 180:09) | 87 (50 min) | 98 (20 min) | 11 | Variação baixa, estilo constante |
| Prochorowka (de, 63:34) | 97 (45 min) | 112 (55 min) | 15 | Variação baixa |
| Miyako (pt, 67:53) | 86 (35 e 45 min) | 103 (40 min) | 17 | Pico no bloco da onda, ao redor de 39 min |
| Norway (de, 30:42) | 119 (15 min) | 136 (0 min) | 17 | Abertura mais densa |
| Villach (de, 31:34) | 129 (0 min) | 152 (15 min) | 23 | Pico no meio |
| Moskvin (de, 26:35) | 150 (10 min) | 171 (15 min) | 21 | Pico logo antes da revelação |
| Antarctica (en, 37:54) | 172 (20 min) | 191 (0 min) | 19 | Abertura mais rápida |
| Kroll (de, 61:48) | 124 (55 min) | 156 (35 min) | 32 | Queda depois do clímax (49–52 min) |
| Ingolstadt (de, 57:00) | 150 (25 min) | 179 (40 min) | 29 | Pico antes da perseguição |
| Flight 370 (en, 24:54) | 108 (0–5 min) | 154 (10 min) | 46 | Bloco inicial com cena de normalidade |
| WWI Top 5 (de, 221:22) | 79 (40 min) | 129 (50 min) | 50 | Bloco de 40 min não verificado; pode conter silêncio ou transição; transcrição truncada em 192:55 |

Leitura geral:
- Em vídeos de canal com estilo estável (Sleepy History, Prochorowka), a variação fica entre 11 e 15 palavras/min. [DADO]
- Amplitudes acima de 40 (Flight 370, WWI Top 5) aparecem em blocos que misturam cena com silêncio ou trecho de transcrição curta. A transcrição não diz se o bloco baixo é silêncio ou fala lenta. [INFERÊNCIA]
- **Exemplo do corpus, Kroll:** o bloco de 49–52 min (prisão, clímax) está em 126 e 124 palavras/min nos blocos de 50 e 55 min. Depois do clímax, a densidade cai, com as cenas de investigação e a confissão. O corpus não mostra se a retenção acompanhou essa queda. [DADO + INFERÊNCIA]

### 7.4 Como variar a densidade no roteiro

Processo sugerido (hipótese de trabalho, não regra validada):

1. **Classifique cada bloco pela função:** explicar (dado, mecanismo), mostrar (cena, arquivo, documento), revelar (virada, identidade, número), descansar (recapitulação, cena sem informação nova).
2. **Meça no roteiro e na transcrição:** palavras/min por bloco de 5 min, no mesmo idioma e com o mesmo narrador. Marque blocos de explicação acima da faixa do idioma e blocos de revelação sem pausa antes.
3. **Regra de alternância:** depois de um bloco de explicação acima da faixa do idioma, insira um bloco de cena ou de pausa planejada. [INFERÊNCIA]
4. **Pausa antes da revelação:** coloque uma pausa curta antes da frase de revelação. Exemplo construído: 1,5 a 3 s de silêncio ou de som ambiente antes de "Sein Name ist Joachim Kroll" (Kroll, 00:36). Não há medida de efeito dessa pausa em YouTube.

Evidência disponível para pausas e ritmo:
- **Rey et al. (2019), meta-análise de segmentação** [ESTUDO; leitura integral do PDF]: retenção d = 0,32 no geral; d = 0,42 quando o sistema impõe as pausas; d = 0,19 e não significativo quando o aprendiz controla o ritmo. Limites: tarefas de aprendizagem em laboratório, média de 19,7 anos de idade, conteúdo didático. Não mede visualização de entretenimento.
- **Noetel et al. (2022), meta-meta-análise** [ESTUDO; trecho]: retenção g = 0,32; carga cognitiva autorrelatada g = 0,23. Mesmo limite: aprendizagem, não entretenimento.
- **Divergência:** um resumo em arXiv de estudo ligado a Rey relata ausência de diferença entre pausas definidas pelo sistema e pelo aprendiz [secundária]. O aprendiz ser ou não o controlador do ritmo continua não resolvido.
- **Guo, Kim & Rubin (2014)** [ESTUDO; trecho]: nos vídeos de MOOC, instrutores mais rápidos pareciam transmitir mais energia e tinham mais engajamento. É associação observada, em MOOC, sem controle. Não é regra de ritmo para vídeo narrativo.

**Contraindicações:**
- Não fixe palavras/min como alvo. O corpus é descritivo, e o próprio Kroll mostra densidade variada sem curva conhecida.
- Pausas longas em narração com TTS (voz sintetizada) podem soar como falha técnica. [INFERÊNCIA]
- Em true crime, a densidade alta de revelações pode ser a própria tensão. Diminuir o ritmo ali pode esvaziar o gancho. [INFERÊNCIA]
- Mudar o ritmo sem mudar a função do bloco tende a produzir só sensação de arrastado. Não medido.

**Lacunas da seção:** não encontrei estudo que relacione palavras/min, pausas ou densidade de fala com retenção em YouTube long-form. Não há curva de retenção de nenhum vídeo do corpus para cruzar com o tempo de fala. Não há análise de áudio (pausas reais, música, SFX), só transcrição.

---

## 8. Fadiga cognitiva

Neste documento, "fadiga cognitiva" é a queda de atenção ou o aumento da divagação ao longo da visualização. [INFERÊNCIA; o corpus não define o termo] Não é cansaço físico nem prova de que o espectador desistiu por fadiga.

### 8.1 Evidência por fonte

| Estudo | Contexto | Achado | Limite |
|---|---|---|---|
| Wu, Rizoiu & Xie (2018), ICWSM, arXiv 1709.02541 [ESTUDO + DADO; PDF lido] | 5,3 milhões de vídeos públicos do YouTube, 2016 | Duração explica mais de 58% da variância da porcentagem média assistida nos primeiros 30 dias. Os autores interpretam como "limited human attention span", sem teste. | Dados agregados, sem curva por segundo; correlação; percentual, não fadiga |
| Guo, Kim & Rubin (2014), L@S [ESTUDO; trecho] | MOOC edX, 6,9 milhões de sessões | Sessão mediana de até 6 min em qualquer duração; tutoriais, 2 a 3 min. Retrospectivo, não controlado. | Engajamento = tempo de sessão. Não é entretenimento |
| Bunce, Flens & Neiles (2010), J Chem Educ [ESTUDO; resumo] | Aula presencial de química, clickers | Lapsos de 1 min ou menos são mais frequentes que lapsos longos. | Autorrelato; texto integral não lido. Fontes secundárias dizem "10 a 20 min", o que não bate com o resumo |
| Bradbury (2016), J Physiol Adv Educ [trecho; secundária] | Crítica ao "limite de 10 min" | Afirma que pouca evidência primária sustenta 10 a 15 min | Não li o artigo |
| Warm, Parasuraman & Matthews (2008) [ESTUDO; resumo] | Detecção de sinal raro em fluxo monótono | Queda de detecção de 10 a 15% nos primeiros 30 min | Não é narrativa. Outro artigo fala em decremento por volta de 20 min [trecho] |
| Ariga & Lleras (2011), Cognition [ESTUDO; resumo] | Vigilância visual em laboratório | Pausas mentais breves e esporádicas, com troca de tarefa, evitaram queda de desempenho. Mecanismo: "goal habituation" | Pausa era tarefa ativa, não passiva. Sem vídeo |
| Risko et al. (2012), Applied Cognitive Psychology [ESTUDO; trecho] | Aula em vídeo de 60 min | Divagação aumenta com o tempo; memória do material cai | Confundido com conteúdo que muda ao longo da aula |
| Risko & Kingstone (2013), Frontiers [ESTUDO; trecho] | Aula gravada de 40 min, avaliação a cada 5 min | Atenção e retenção caem com o tempo | Laboratório; confundimento com conteúdo |
| Wammes et al. (citados em trecho de outro estudo) [ESTUDO; trecho] | Aula presencial vs. vídeo | Em aula presencial, a divagação fica estável; em vídeo, há mais divagação; um estudo de vídeo não achou mudança de engajamento autorreportado com o tempo | Universidade; achados divergentes |
| Szpunar, Khan & Schacter (2013), PNAS [ESTUDO; registro e trechos] | Excerto de 21 min de aula de estatística | Testes intercalados reduziram a divagação e melhoraram a retenção | Magnitude divergente (ver §8.4); laboratório |
| Zacks et al. (2007), Psychological Bulletin [ESTUDO; trecho] | Percepção de eventos | Fronteiras de evento aparecem quando o modelo do evento é violado | Laboratório |
| Zacks et al. (cinema, ano não confirmado) [ESTUDO; trecho] | Cinema narrativo | Eventos grossos duram em média 59,4 s (DP 28,1 s) | Leitura integral não feita |

### 8.2 Sinais observáveis e diagnóstico diferencial

Definições oficiais usadas (YouTube Help, relatório de retenção) [OFICIAL]: queda gradual indica perda de interesse ao longo do tempo; vale indica abandono ou pulo naquele ponto; pico indica trecho reassistido ou compartilhado, e o próprio YouTube diz que pico pode ser trecho interessante ou conteúdo pouco claro. Kim et al. (2014) reforçam: pico pode indicar confusão, não só interesse. [ESTUDO, trecho]

Sinais de fadiga, no sentido deste documento, não estão validados para curva de YouTube long-form. A tabela é hipótese de diagnóstico:

| Sinal na curva | Hipótese de fadiga/divagação | Hipótese de confusão | Hipótese de falta de recompensa | O que checar no roteiro e na edição |
|---|---|---|---|---|
| Queda gradual dentro de bloco longo, sem vale localizado | Forte, se o bloco tem muitas palavras/min e nenhuma mudança de função | Possível, se o bloco tem muitos termos novos | Possível, se o bloco não tem pergunta ou recompensa | Quantas perguntas abertas há no bloco? Há mudança de cena, local ou função? Qual a palavras/min? |
| Vale localizado logo após um bloco de explicação | Fraca | Forte: o espectador não entendeu e saiu | Fraca | Há definição, dado ou nome novo nos 30 s anteriores? Há recapitulação? |
| Vale localizado após uma revelação ou clímax | Média: pode ser descompressão | Fraca | Forte se a revelação não pagou a pergunta | A promessa foi paga? Houve mudança de ritmo depois? |
| Picos repetidos num trecho de explicação | Fraca | Forte: reassistência para entender (OFICIAL/Kim) | Fraca | Ler a fala e o visual dos 10 s antes do pico |
| Platô longo seguido de queda no fim | Média: o espectador segue, mas perde o fio | Fraca | Média | A última promessa foi paga? O fim anunciou o encerramento? |

Regra de uso: nunca decida a causa só pela curva. Use a tabela para escolher o que checar. Compare sempre com a faixa "typical retention" do próprio canal e segmente por tráfego (OFICIAL: relatório oferece segmentação).

### 8.3 Causas prováveis e a evidência de cada uma

- **Muita informação sem pausa ou sem mudança de função.** Evidência: Rey et al. (2019) mostram efeito de segmentação para retenção em aprendizagem (d = 0,42 quando o sistema impõe as pausas) [ESTUDO]. Não testado em entretenimento. [INFERÊNCIA ao aplicar]
- **Tempo de exibição longo sem variação de tarefa.** Evidência: Risko et al. (2012) e Risko & Kingstone (2013) mostram queda de atenção em aula gravada de 40 a 60 min [ESTUDO]. Confundido com conteúdo.
- **Ausência de tarefa ativa.** Evidência: Ariga & Lleras (2011) mostram que troca de tarefa preserva desempenho em laboratório [ESTUDO]. Não há evidência de que vídeo passivo siga o mesmo padrão.
- **Ausência de pergunta a responder.** Evidência: Kroll e o corpus mostram estrutura com perguntas [DADO], mas não há dado de retenção que mostre o efeito. Sustentação por curiosidade é teoria: Loewenstein (1994) descreve a curiosidade como lacuna percebida de conhecimento [ESTUDO, secundário]. Ver seção 3 para mecanismos de sustentação.

### 8.4 Contramedidas, com nível de evidência e contraindicação

| Contramedida | Evidência | Nível | Contraindicação |
|---|---|---|---|
| Marcar fronteira de bloco com mudança de função (cena, local, tipo de ação) | Rey et al. (2019), Zacks et al. (2007) e Magliano & Zacks (2011) apontam fronteiras de ação e de expectativa | Laboratório; fronteira de evento ≠ fronteira de minuto | Excesso de fronteiras pode fragmentar o argumento. [INFERÊNCIA] |
| Pergunta curta de recuperação no fim do bloco ("o que ficou?") | Szpunar et al. (2013): testes entre segmentos reduziram divagação e melhoraram retenção (21 min, estatística) | Laboratório; adultos; magnitude divergente | Pode quebrar a imersão em narrativa. Não medido em entretenimento |
| Recapitulação de um dado do bloco anterior | Mesma linha de Szpunar; a recapitulação atua como teste implícito | Inferência a partir de laboratório | Recapitulação longa vira enrolação |
| Interrupção ativa leve (pergunta, cena, troca de fonte) | Ariga & Lleras (2011): pausas ativas breves preservaram desempenho em tarefa de vigilância | Laboratório, tarefa visual | Pausa passiva (silêncio ou música) não foi testada |
| Dose de palavras/min alternada com cena | Rey et al. e Guo et al. (associação em MOOC) | Aprendizagem e MOOC | Não validado para curva de entretenimento |
| Limite de 6 minutos ou 10 minutos de bloco | Guo et al. (2014) é limite de sessão, não de retenção; "10 minutos" tem fonte primária contestada | Não validado | Não use como regra. Dossiê 3 item 24 |

**Divergências a manter abertas:**
- **Início do decremento:** 30 min (Warm et al., 2008) ou cerca de 20 min (artigo com título "The Vigilance Decrement Reflects Limitations in Effortful Attention, Not Mindlessness") [trecho]. Não resolvido, e ambos são vigilância, não narrativa.
- **Magnitude dos testes intercalados:** o comunicado de imprensa fala em queda pela metade da divagação; um resumo secundário fala em 19% a menos de episódios. Não resolvido sem o PNAS.
- **Divagação em vídeo vs. aula presencial:** em vídeo, a divagação sobe com o tempo (Risko et al.); em aula presencial, fica estável (Wammes et al., citados). Um estudo de vídeo não achou mudança de engajamento autorreportado. Divergência de formato e de método.
- **Quem define a pausa:** especialistas, aprendiz ou sem diferença. Ver §7.4.

### 8.5 Limites

- Quase toda a evidência é de laboratório, aula presencial, MOOC ou vigilância. Não há estudo de fadiga cognitiva em YouTube long-form com retenção.
- Divagação é medida por autorrelato ou por sondagem, não por retenção. Não sabemos se a queda de atenção gera abandono.
- A curva de retenção de YouTube não diz se o espectador está distraído, confuso ou só pausou. Sem dados do próprio canal, qualquer diagnóstico de fadiga é hipótese.
- Não encontrei dado de fadiga para narração em voz sintetizada, nem para documentário com narrador e imagens fixas em 30 a 60 min.
- A segmentação por "minutos" (2, 5 ou 10) não tem fonte primária que a sustente. O que tem suporte é a fronteira por mudança de função ou de ação. [INFERÊNCIA]

## 9. O framework dos 30 minutos

**Status:** [INFERÊNCIA]. Nenhuma fonte deste material mediu retenção de vídeo de 30 min de entretenimento. O que existe: (a) a Central do YouTube descreve o formato da curva, mas não dá limiares [OFICIAL, support.google.com/youtube/answer/9314415]; (b) Wu et al. (2018) mostram que a duração explica mais de 58% da variância da porcentagem assistida, em dados agregados e sem curva por segundo [DADO, arxiv.org/pdf/1709.02541]; (c) o corpus tem 30 transcrições de alto desempenho, sem curvas. O framework abaixo organiza a estrutura. Os minutos são hipóteses a testar, não metas.

**Premissas:**
- Não depender só de suspense. Cada bloco precisa de pelo menos uma razão para ficar que não seja a pergunta pendente: compreensão nova, recompensa verificável, mudança de escala ou perspectiva, consequência humana ou humor (mecanismos em §3).
- Ritmo de referência: a 130 palavras por minuto, um roteiro de 30 min tem cerca de 3.900 palavras. Os vídeos do corpus de 30 a 37 min ficaram entre 122 e 137 palavras por minuto (Norway, 126; Villach, 137; Ampulheta/Hitler, 122). Use como descrição, não como meta causal.

**Estrutura em nove segmentos de duração variável, sem subtempos.** Os tempos são âncoras. Se um bloco passar de 6 min sem pagamento, divida-o.

| Minuto | Função | Motivo para ficar | Pagamento ou entrega | Risco típico [INFERÊNCIA] | Exemplo do corpus |
|---|---|---|---|---|---|
| 0:00–0:30 | Gancho: cena concreta ou resultado antecipado | Decidir se vale a pena | Uma cena com data, lugar ou número | Saída antes de qualquer informação | Norway 00:01 (desfecho antecipado); Villach 00:10 (cena de morte) |
| 0:30–2:00 | Pergunta-âncora explícita e primeira recompensa parcial | Transformar curiosidade em pergunta específica | Um fato verificável que responde parte da pergunta | Lacuna grande demais ("algo misterioso") | Villach: pergunta em 00:10, "Macht und Geld" em 01:59 |
| 2:00–5:00 | Contexto mínimo: só o que a pergunta exige, e o formato do vídeo | Saber como o vídeo vai responder | Regra de leitura (ex.: formato de veredito, cronologia) | Contexto longo antes de qualquer pagamento | Norway 01:27–02:37 anuncia o tribunal e as três hipóteses |
| 5:00–10:00 | Primeiro caso ou hipótese fechado do início ao fim | Sensação de progresso e fechamento de uma unidade | Mecanismo, prova e veredito parcial | Caso sem fechamento, ou fechamento sem prova | Norway 06:09–08:10: teste da hipótese 1 |
| 10:00–15:00 | Mudança de escala ou de perspectiva (do caso ao padrão, do indivíduo ao sistema) | Novo nível de compreensão, não repetição | Segundo caso ou contrafactual | Repetir o mesmo molde do bloco anterior | Villach 13:36–17:10: segundo caso; Norway 13:01–15:13: hipótese 2 |
| 15:00–20:00 | Escalada de custo humano ou ameaça, com prova documental. Se o bloco passar de 6 min, divida em duas partes de cerca de 2,5 min | Consequência concreta | Número de vítimas ou custo, com fonte | Bloco longo sem virada (o ato 2 vira "uma cena só") | Norway 15:13–22:54 tem 7,7 min na hipótese 3: candidato a dividir |
| 20:00–24:00 | Virada principal: revelação ou contradição, tardia | Pergunta maior paga | Resposta à pergunta central ou reviravolta | Virada antes do minuto 15 (esvazia o restante) | Villach: clímax em 24:11–24:47 (~77% do vídeo) |
| 24:00–27:00 | Reenquadramento: o que a resposta muda | Sentido, não só informação | Tese do narrador, com ressalva | Tese sem prova do bloco anterior | Norway 28:17: "a pergunta se os soldados lutaram encobre o que fizeram" |
| 27:00–30:00 | Síntese: resposta final à pergunta da abertura, o que continua sem resposta, e a ponte | Fechar o que foi aberto | Veredito, lacuna declarada, próxima pergunta | Anúncio de encerramento com minutos restantes (praticante, não testado) | Norway 27:59: recapitulação dos vereditos; Villach 30:36: coda |

**Regras de dose:**
- Cada bloco de 5 min tem pelo menos uma recompensa verificável e um motivo que não seja só a pergunta pendente. Nos blocos de respiro (10:00–15:00 e 24:00–27:00), a coluna de motivo deve citar um mecanismo da seção 3 que não seja pergunta: escala, perspectiva, consequência humana ou humor com dado concreto (§3.2.4–3.2.6). Não há dose validada de humor ou relevância pessoal para este formato.
- Reviravoltas grandes: poucas e tardias. Ely, Frankel & Kamenica (2015) sugerem, em modelo teórico sem teste em narrativa, que viradas menos frequentes e mais fortes podem sustentar o suspense [ESTUDO, modelo; não testado em vídeo]. Aplicação: no máximo uma reviravolta grande antes do minuto 20.
- Posição do clímax: não há padrão consistente no corpus. Villach (~77%) e a virada argumentativa de Norway (~92%) são tardios; Doppelgänger (57 min) revela a identidade em 10:12. [INFERÊNCIA] Trate a posição como variável a testar, não como regra.
- Divisão do vídeo: o corpus mostra blocos temáticos explícitos (Norway: tribunal com três hipóteses; Villach: casos numerados). [INFERÊNCIA] Quando o tema é uma série de casos, os blocos coincidem com os casos. Quando é uma biografia, o bloco de causa pode ser longo: Kroll (61 min) gasta 01:36–18:20 na biografia antes da série de crimes, o que é um risco de dip por inferência, não medido.

**Exemplo construído (não é dado):** um vídeo de 30 min sobre a queda de uma ponte. 0:00 abre com o momento do colapso e a frase "a engenheira tinha aprovado o projeto". 0:30 pergunta: "aprovado por quem, e com que cálculo?" 2:00 paga com a norma vigente na época. 5:00 fecha o caso da inspeção de 1998. 10:00 muda de escala: do caso ao padrão de inspeções do país. 15:00 mostra o custo. 20:00 revela o erro de cálculo. 24:00 mostra por que o erro passou. 27:00 responde à pergunta da abertura e declara o que continua sem prova.

**Como checar o framework:** Central do YouTube, leitura em 1 a 2 dias, comparando cada fronteira de bloco com a faixa "typical retention" dos 10 vídeos mais recentes de duração semelhante [OFICIAL]. Cada fronteira vira hipótese e precisa de três uploads antes de ser considerada validada (heurística de praticante, playpause.io).

## 10. Checklist de auditoria de retenção

**Uso:** A = antes de escrever o roteiro; B = antes de publicar o corte final; C = 1 a 2 dias após a publicação. Marque cada item como "ok", "falha" ou "não se aplica". Uma falha em A ou B não bloqueia a publicação, mas precisa de decisão registrada.

### A. Roteiro

- [ ] **A1.** A abertura (0:00–0:30) contém uma cena concreta com data, lugar, número ou objeto. Se não, reescreva. [INFERÊNCIA a partir de corpus; sem teste]
- [ ] **A2.** A pergunta central cabe em uma frase com "como" ou "por que" e tem resposta verificável. Se for "algo misterioso", reduza a lacuna. (Loewenstein, 1994: curiosidade cai com lacuna grande demais e com lacuna pequena demais [ESTUDO, laboratório].)
- [ ] **A3.** A primeira recompensa parcial está antes do minuto 2:00. [INFERÊNCIA]
- [ ] **A4.** Cada pergunta aberta tem o minuto em que será paga, escrito no roteiro. Intervalo observado no corpus entre promessa e pagamento: de cerca de 2 min (Villach, 00:10 → 01:59) a 15 min (Portugal, 01:22 → 14:59). Escolha um prazo máximo por pergunta e justifique. (Ver §6.)
- [ ] **A5.** Nenhum bloco de 5 min passa de 6 min sem pagamento ou sem mudança de tipo de informação (fato, prova, consequência, perspectiva). [INFERÊNCIA]
- [ ] **A6.** Há no máximo uma reviravolta grande antes do minuto 20. [INFERÊNCIA a partir de Ely et al., 2015, modelo]
- [ ] **A7.** Há mudança de escala ou de perspectiva entre os minutos 10 e 15. [INFERÊNCIA; mecanismo em §3]
- [ ] **A8.** Cada afirmação numérica tem fonte anotada no roteiro, com etiqueta [OFICIAL], [ESTUDO], [DADO] ou [PRATICANTE]. Número sem fonte não entra. (Regra do sistema de pesquisa.)
- [ ] **A9.** O roteiro tem um anúncio de estrutura (mapa ou formato), se o vídeo tem mais de três temas. Exemplo do corpus: Sleepy History (180 min) anuncia padrões; Portugal (17 min) anuncia "por que" e "qual o preço". [DADO, transcrição]
- [ ] **A10.** Nenhum bloco depende de uma informação dada só depois dele (sem ponte para trás). Teste: leia cada bloco isolado e pergunte "o que o espectador precisa saber aqui?".

### B. Corte final

- [ ] **B1.** Marque, no tempo do corte, cada pagamento de pergunta, cada reviravolta e cada fronteira de bloco. Compare com os minutos de A4 e A6. Diferença maior que 1 min: justifique.
- [ ] **B2.** O primeiro segundo de cada fronteira de bloco tem uma marca de transição (fala, título, visual ou música). Se não tem, adicione. (Sinalização de fronteira, §4.)
- [ ] **B3.** Nenhum trecho de imagem parada ou narração sem mudança de visual passa de 60 s sem uma mudança de informação. [INFERÊNCIA; Central: queda gradual pode indicar perda de interesse, sem limiar]
- [ ] **B4.** Conte palavras por minuto de cada bloco com o mesmo método usado em todos os vídeos do canal. Compare com a faixa do corpus (103 a 209 wpm nos 30 vídeos, incluindo os curtos) apenas como referência descritiva. Um bloco que fica muito acima ou abaixo da média do próprio vídeo pede revisão.
- [ ] **B5.** Cada bloco tem ao menos um elemento sensorial ou humano (pessoa, decisão, consequência), não só dados. [INFERÊNCIA; dimensão emocional e de presença, Busselle & Bilandzic, 2009: escala de autorrelato, não testada em YouTube]
- [ ] **B6.** Os últimos 60 s respondem à pergunta da abertura. Se não respondem, declare explicitamente o que não tem resposta.
- [ ] **B7.** O fechamento não anuncia o fim com minutos restantes (praticante, não testado). Se o vídeo tem fim com CTA, o CTA está no último bloco, não antes do conteúdo.
- [ ] **B8.** A miniatura e o título prometem o que o vídeo paga, e o epíteto ou a promessa aparecem antes de 40% do tempo. (Regra de praticante, de Enrique Blanco, Delitos de Sangre; corpus, não validada.)

### C. Após a publicação (1 a 2 dias)

- [ ] **C1.** Espere 1 a 2 dias para ler o relatório (Central). Os momentos-chave exigem vídeo com 60 s ou mais e 100 views [OFICIAL].
- [ ] **C2.** Registre Intro (porcentagem após 30 s), AVD e APV. Lembre que AVD e APV são médias de quem ficou, e não incluem quem saiu cedo. (Central; ver §1.)
- [ ] **C3.** Compare a curva com a faixa "typical retention" dos 10 vídeos mais recentes de duração semelhante [OFICIAL]. Não compare com zero.
- [ ] **C4.** Liste os três maiores vales, com timestamp e o que estava na tela e na fala nos 10 s anteriores. Associe cada vale a uma fronteira de A4–A6 ou a um trecho de B3. Vales não associados a nada do roteiro são investigados primeiro.
- [ ] **C5.** Para cada pico, decida entre interesse e confusão, ouvindo a fala daquele trecho. A Central diz que pico pode indicar trecho interessante ou conteúdo confuso [OFICIAL].
- [ ] **C6.** Antes de editar, separe os segmentos (novos ou recorrentes; tráfego orgânico ou não). Um vale que existe só em tráfego pago pode ser problema de público, não de roteiro.
- [ ] **C7.** Antes de comparar com vídeos anteriores, verifique se a data de publicação é anterior ou posterior a 24/08/2026. Nessa data, a contagem de views passa a começar no início da reprodução, em todos os formatos [OFICIAL, support.google.com/youtube/answer/2991785]. Terceiros afirmam que retenção e AVD não mudaram; não confirmei na página oficial.
- [ ] **C8.** Se o vídeo tiver muitos vales, mude uma variável por upload. Um ajuste só vale depois de repetido em cerca de três uploads [PRATICANTE].
- [ ] **C9.** Registre a decisão tomada e a leitura que a motivou, para que o próximo ciclo de auditoria não repita o mesmo erro.

## 11. Lacunas e limites

**O que este framework não é:** não é um modelo validado de retenção. As fontes disponíveis não medem retenção de vídeo de 30 min de entretenimento narrado em YouTube. Os minutos da seção 9 são hipóteses estruturais, a testar no próprio canal.

**Lacunas de dados:**
- **Curvas de retenção de terceiros:** não encontradas. Nenhuma curva de vídeo do corpus foi vista; toda leitura de curva é regra de documentação oficial ou inferência.
- **Corpus:** 30 transcrições de vídeos com desempenho acima da mediana do próprio canal. Isso é viés de sobrevivência: não há vídeos de baixo desempenho para comparar. Não há AVD, APV, CTR nem curva. Os padrões são hipóteses, não causas.
- **Dark (faceless) em long-form:** nenhum dado de curva ou estudo encontrado para esse formato.
- **Vídeo de entretenimento em 30 min:** nenhum estudo de retenção encontrado. Os estudos sobre atenção e divagação são de aula e laboratório (Risko et al., 2012; Risko & Kingstone, 2013; Szpunar et al., 2013). Os estudos de segmentação são de aprendizagem (Rey et al., 2019). Guo et al. (2014) são MOOC, com sessões que o próprio estudo não generaliza.
- **Fadiga em 30 min:** nenhum estudo de vídeo narrativo de 30 min com medida de atenção. Warm et al. (2008) reportam queda de 10 a 15% nos primeiros 30 min, mas em vigilância, não em narrativa. Bunce et al. (2010) só foram lidos no resumo.
- **Blocos de 5 e 10 minutos e pausas em vídeo longo:** não há fonte com dados.

**Divergências que afetam o framework (não resolvidas):**
- **Cliffhanger:** Wirz et al. (2022), em série com laboratório, contrariam a crença de que cliffhanger prende; Schibler, Hahn & Green (2023), com texto, mediram aumento de desejo declarado pela próxima parte com cliffhanger, sem diferença de suspense; o texto integral não foi lido. Só li a nota de imprensa de Hahn e o trecho de Wirz. A regra de "pagar parcialmente antes de abrir outra pergunta" depende de qual dos dois se confirmar.
- **Início do decremento de atenção:** 30 min (Warm et al., 2008) ou cerca de 20 min (outro artigo, em monitoramento passivo). Os dois números orientam a escolha de quando colocar a virada, e não há resolução.
- **Interrupção ativa:** Ariga & Lleras (2011) mostram que tarefas esporádicas evitam queda, em laboratório visual. Não há prova de pausa passiva com o mesmo efeito em vídeo.
- **Magnitude dos testes intercalados:** Szpunar et al. (2013) têm números divergentes entre imprensa e resumo secundário. Não usar magnitude.
- **Quem define a pausa:** especialista, aprendiz ou sem diferença (Rey et al., 2019; resumo em arXiv). Não resolvido.
- **Duração como variável:** Wu et al. (2018) mostram que duração explica muito; no mesmo estudo, canal e tópico também preveem engajamento. Não existe limiar de duração validado para entretenimento.
- **Benchmarks de retenção:** variam de 30% a 55% para 20+ min, todos [PRATICANTE], sem metodologia. Não use como alvo.
- **Most Replayed:** limiar de views e efeito de capítulos não confirmados. Não use o gráfico público como curva de retenção.

**Lacunas de método:**
- Não há teste de A/B controlado para ordem de payoff, densidade ou posição de clímax. O teste mínimo proposto (§10, C8) é observacional e pequeno.
- Os exemplos construídos (ponte, Miyako, bloco de 6 min) não são dados.
- As citações de vídeos do corpus vêm de transcrições automáticas, com erros de nome próprio e trechos truncados. Minutagens em transcrição truncada (ex.: Schlachtbericht com 63:34 de duração, mas transcrição parcial) não servem para afirmar encerramento.
- A amostra de idiomas (alemão, espanhol, português, inglês) mistura convenções de cada mercado. Nenhum estudo comparou idiomas.

**Próximo passo para fechar a lacuna:** levantar, do próprio canal, as curvas de pelo menos 10 vídeos de 25 a 35 min (Central, 1 a 2 dias após cada publicação), anotar fronteiras de bloco no roteiro e verificar se os vales caem sobre elas. Com 10 vídeos, o resultado é só descritivo. Serve para decidir se o framework merece três uploads de teste.

---
## Adendo da revisão
**Reinvestigação: Schibler, Hahn & Green (2023) [ESTUDO, resumo e trechos; texto integral e OSF não lidos].** Desenho: experimentos entre sujeitos com narrativa escrita em série, N=202 (Estudo 1) e N=273 (Estudo 2), soma 475 [INFERÊNCIA]. Três desfechos: cliffhanger, vitória do protagonista e vitória do antagonista; o antagonista aparece só no Estudo 2, segundo o resumo. Variável principal: desejo declarado de ler a próxima parte (DFFI, dois itens, alfa = 0,89). Não há medida de leitura real nem de comportamento. Resultado: o cliffhanger gerou mais desejo declarado que as vitórias; não houve diferença significativa de suspense nem de enjoyment. Não testa pagamento parcial de loop nem retenção de vídeo. Aplicabilidade a long-form: não validada. [INFERÊNCIA] Hipótese para teste no canal: pagar parcialmente um loop antes de abrir o próximo aumenta a retenção em vídeo longo (não testada). **Lu et al. (2025) [ESTUDO, trecho]:** em crianças, narrativa serial (cliffhanger) gerou mais atividade física ao longo do tempo que a episódica (fechamento temporário); não validado para leitura nem para vídeo. **Divergência:** a release da UB fala em audiências que voltam para mais; o dado é autorrelato. **Em aberto:** texto integral e materiais do OSF; estatísticas de teste; se o Estudo 1 tinha braço de antagonista.

## Registro de revisão
Alterei 19 trechos. Aplicados: cabeçalho e escopo; densidade de Sleepy History (interpretação removida, número marcado como artefato); benchmarks, alinhado à seção 11; percentual de Kim et al. (36%) removido por não verificado; cabeçalho do framework e a tabela de nove segmentos; recompensa e mecanismos de respiro no framework; Ely et al. reescrito como modelo teórico; dose de Zacks retirada; Hahn et al. corrigido com base no dossiê (desejo declarado, não retenção; autoria Schibler, Hahn & Green); Cicada 3301 e Flight 370 separados; títulos de capítulo tratados como não verificados; frase incompleta de Schlachtbericht corrigida; Portugal com início 01:22. Discordâncias e pendências: (1) o total do corpus (38 contra 21 e 30) não foi resolvido, porque não tenho acesso à base do auditor e não consigo confirmar 38; (2) a faixa e a mediana do inglês precisam ser recalculadas sem Sleepy History, o que exige as transcrições; (3) os minutos de inserção publicitária de 04:18 a 05:23 aparecem em dois vídeos, mas não alterei porque não tenho as transcrições para conferir; (4) a leitura do Kim et al. (2014) não foi feita, então a divergência de denominador continua aberta; (5) não reescrevi a regra de 2 loops nem a dose de humor, porque não há evidência nova para isso.

Correções aplicadas ao texto: 20.
