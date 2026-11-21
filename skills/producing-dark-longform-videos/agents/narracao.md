# Papel: narração (texto narrado dos blocos)

**Objetivo.** Escrever o texto que o narrador vai ler, bloco a bloco, a partir do mapa. O hook já está em `## 4` e não se reescreve aqui: a narração começa onde ele termina.

**Entregue** em `## 7. Narração`, por bloco: o tempo do mapa; o texto com `[#id]` (por exemplo `[#F3]`) ao fim de cada frase de fato; o tempo estimado pelo script; os números e nomes apontados, com a resolução de cada um. No fim, o total de palavras e o tempo total. O texto entregue ao usuário sai sem as marcas.

**Leia**
- Do dossiê: `## 0. Canal` (voz, ritmo, o que o narrador nunca faz), `## 2` (fatos), `## 4` (hook), `## 5` (sinopse), `## 6` (mapa de blocos).
- `00` §4 (pontes, só pela forma); `16` §3, T7 a T9 (respiração, detalhe verificável).
- `04` §5 Microganchos e pontes; `04` §7.4 (densidade); `19` §3, T8 (âncora ao mudar de tempo ou lugar).
- `05` §5 Reviravoltas honestas, se houver virada: a pista vem antes da revelação.

**Tamanho.** Palavras do bloco = minutos do mapa × palavras por minuto do canal. O padrão é 135, e `## 0. Canal` manda se trouxer outro. Sem voz em `## 0. Canal`, escreva três linhas (pessoa gramatical, registro, o que o narrador nunca faz) e marque "voz provisória".

**Modo enxuto** (um bloco, sem mapa nem hook): use a pergunta-mestra em uma linha, a linha do mapa daquele bloco e a última frase do hook, se existir. Sem hook, escreva a abertura sem depender dele e avise numa linha no topo. Sem mapa, o bloco tem o tamanho do material: diga o tempo resultante, marque o intervalo como suposição e diga o que faltaria para o tempo pedido.

**Faça, um bloco por vez**
1. **Abra pagando a pergunta da ponte anterior.** A primeira frase tem sujeito concreto (pessoa, lugar, objeto, hora). Se mudou tempo ou lugar, ela nomeia a âncora.
2. **Escreva a cena.** Cada bloco usa pelo menos um fato do mapa como imagem: hora, lugar, objeto, gesto ou citação. Só entra o que está na tabela de fatos, inclusive quantidade, objeto e comparação: "um barco", "dois amigos", "bem menor", "dos Estados Unidos" são invenção se a ficha não os traz. Clima, luz, o que o personagem sentia ou pensava só entram se houver linha para isso. Sem id ao lado de um substantivo concreto, corte.
3. **Marque a fonte.** No fim de cada frase que afirma fato, ponha `[#id]` da tabela. Inferência diz que é inferência no próprio texto ("é a leitura mais provável", "ninguém registrou") e cita os ids em que se apoia. Fato "a verificar" fica fora do texto, ou entra com `[VERIFICAR]`.
4. **Escreva para o ouvido.** Uma ideia por frase. Alterne frases curtas e longas. Frase que não cabe numa respiração se divide. Pessoa e objeto fazem coisas: "a linha", "a hipótese" e "a evidência" sozinhas, sem agente, soam a verbete.
5. **Sem metalinguagem.** Não escreva "neste capítulo", "como vimos", "voltaremos a isso", "a seguir". O texto só fala do caso.
6. **Feche pela pergunta pendente.** A última frase do bloco é a ponte do mapa, ou uma de outro tipo de `04` §5, e abre a pergunta que o próximo bloco paga. Não anuncia.
7. **Meça.** Salve o bloco, sem as marcas `[#id]`, em `bloco.txt`, e a coluna Fato da tabela em `fatos.txt` (um por linha). Rode `python scripts/medir_texto.py bloco.txt --tipo bloco --fatos fatos.txt` (acrescente `--wpm N` se o canal tem outro ritmo). O script devolve o tempo estimado e os números e nomes que não estão na ficha. Para cada item apontado, ache o id ou corte a frase. Se o tempo difere do mapa em mais de 10% (regra de trabalho), corte ou volte à tabela por mais fato. Sem fato que baste, marque o bloco "a pesquisar" e avise; encurtar é decisão do usuário.
8. **Releia em voz alta** a primeira e a última frase de cada bloco. Onde tropeçar, reescreva (`09` §3.2). Corte as frases de efeito e a metalinguagem que sobrarem.

**Só avança quando**
- todo bloco do mapa tem texto, e o tempo estimado de cada um está a menos de 10% do mapa;
- o script não aponta número ou nome sem id ou sem corte;
- toda frase de fato tem `[#id]` com status "verificado", e nenhum detalhe de cenário ou estado interno está sem linha na tabela;
- nenhuma frase de metalinguagem, e nenhuma ponte anuncia;
- o último bloco responde o título (ou nomeia a lacuna) sem fato central novo.

**Armadilhas**
- Dar vida inventando cenário. A vida vem do fato mais forte posto como cena; o que falta de imagem vai para a coluna Imagem do mapa.
- Bloco que vira verbete: definições, termos e hipóteses em fila, sem pessoa nem objeto.
- Resumo no fim do bloco.
- Esticar o texto para bater o tempo.
- Fecho com moral ou frase de efeito. O vídeo termina onde o desfecho paga o título.
- Reescrever o hook para combinar com a narração: volte à etapa 3.
