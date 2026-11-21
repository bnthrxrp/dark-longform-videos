# Papel: pacote (título + thumbnail)

**Objetivo.** Título e thumbnail que se completam e prometem a anomalia do caso e a pergunta central, nada além. Cada promessa tem pagamento no vídeo; o pagamento pode ser o desfecho honesto ("não há resposta; eis o que se sabe").

**Entregue** em `## 3. Pacote`: três títulos de famílias diferentes e o escolhido (com o número de caracteres medido); a tensão em uma frase; a ficha da thumbnail e o arquivo SVG; o resultado de `checar_thumbnail.py`; o registro de promessas (onde, promessa, bloco, minuto).

**Leia**
- `00` §3 (checklist de thumbnail)
- `01` §2.2 TÍTULO, §2.3 THUMBNAIL, §4.6; `03` §2.4, §2.8, §3.4, §5.3

`[TESTE-IA]`: `21` §1. `[PRATICANTE]` e `[aposta]`: sem medida.

**1. Título.** Três opções de famílias diferentes: citação do que se disse ou escreveu; antítese de dois fatos; comportamento anômalo; pergunta que contém o fato estranho. Escolha por este teste: lido sem a thumbnail, o título conta a anomalia?
- Leva a tensão não resolvida e o nome conhecido do caso, se houver.
- A ressalva de precisão vai para a narração e a descrição, nunca para o título. Exceção: acusado sem sentença definitiva continua "acusado" (`03` §2.8).
- Comprimento: alvo de até 70 caracteres `[TESTE-IA]`; as referências não dão teto. Conte com `python -c "print(len('TÍTULO'))"` (o script `medir_texto.py` mede texto narrado, não título). Acima de 75, escreva a razão.

**2. Thumbnail**, em ficha:
1. **Ponto focal:** um objeto do caso, reconhecível em 320×180, de um lado, com cerca de 35% da altura ou mais `[aposta]`.
2. **Frase de destaque** no outro lado, em linguagem comum, que afirma ou nega o fato estranho ("SEM PEGADAS DE VOLTA"). Use o mínimo de palavras que diz a anomalia; a mediana de breakouts é 5 `[DADO fornecedor, 03 §2.4]`. Texto cortado, sobreposto ou ilegível, e rótulo (nome e data) no lugar da frase, perdem `[TESTE-IA]`.
3. **Área segura:** nada a menos de 5% da borda (64 px em 1280×720). Canto inferior direito livre para o selo de duração `[PRATICANTE]`.
4. **Nada por cima de nada:** texto não cobre o objeto nem outro texto. Reserve uma área limpa para ele.
5. **Contraste alto:** texto claro só sobre região escura, e o inverso; contorno ou caixa quando o fundo tem a mesma luminosidade.
6. **Tamanho de letra:** frase principal com pelo menos 1/9 da altura da imagem (80 px em 1280×720); apoio com pelo menos 40 px `[aposta]`. Se não cabe, reduza a letra ou quebre a linha.
7. **Leitura em 320×180:** diga qual palavra se perde primeiro.
8. Número ao lado de substantivo não pode ler errado ("1590 colonos" quando 1590 é o ano).
9. Se você desenha o arquivo, use um objeto de até 5 formas; evite figura humana e avião em perspectiva. A tensão vai no texto.
10. **Objeto reconhecível no feed:** abra `thumb_feed.png` e escreva em uma frase o que o objeto parece, sem o texto. Se lê como outra coisa, redesenhe. Forma geométrica genérica (triângulo, círculo) pode ler como ícone: um triângulo lê como botão de play. Carta: retângulo com aba em V ou selo.

Salve o SVG (1280×720) e rode `python scripts/checar_thumbnail.py thumb.svg --titulo "TÍTULO" --png thumb.png`. O script grava também `thumb_feed.png` (320×180): abra os dois, porque o script é alerta e não prova (ele não julga se o objeto é reconhecível). Aviso de "fonte ausente" quer dizer medida aproximada. Corrija até dar PASSOU. Sem o arquivo ou sem o script, escreva "thumbnail não checada" e entregue a ficha.

**3. Título e thumbnail se completam.** O título dá o fato ou a pergunta; a thumbnail mostra o objeto e afirma ou nega o fato. Não repetem as mesmas palavras de conteúdo, salvo uma frase citada do caso, com a decisão anotada (o `--titulo` do script lista as repetidas).

**4. Registro de promessas:** cada palavra-promessa do título e cada elemento da thumbnail, com bloco e minuto em que o vídeo paga. Antes do roteiro, o minuto é a meta que o roteirista cumpre. Pista pode aparecer no pacote; a resposta da pergunta central, não (`11` §2, D4; regra provisória).

**Só avança quando**
- toda promessa tem bloco e minuto, ou foi retirada;
- título e thumbnail não se contradizem em sujeito nem em escopo e não repetem palavras sem decisão anotada;
- o título, lido sozinho, conta a anomalia, e o número de caracteres está medido;
- a ficha da thumbnail está completa e `checar_thumbnail.py` deu PASSOU, ou a entrega diz que não checou;
- nada na thumbnail responde a pergunta central.

**Armadilhas**
- Ressalva jurídica dentro do título.
- Título-rótulo ou lista de substantivos. O formato "Caso (ano): descrição" é só aposta contra (`21` §6, H9, fraca).
- Superlativo sem critério verificável ("o maior", "o mais cruel") e verbos que o vídeo não paga ("escondido", "esquecido"). O limite é o minuto de pagamento, não o tom.
- Pessoa identificável, vítima ou cena de sofrimento sem checar `03` §2.8.
- Justificar uma escolha com "funciona melhor". Diga a etiqueta de evidência; rosto contra objeto, quantidade de texto e cor são apostas.
