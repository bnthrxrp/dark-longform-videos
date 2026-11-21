# Papel: hook (0 a 90 segundos)

**Objetivo.** Texto narrado de 80 a 95 s (cerca de 180 a 215 palavras a 135 palavras/min) que instala a pergunta central de dentro da história e paga um primeiro pedaço dela.

**Entregue** em `## 4. Hook`: texto contínuo, sem marcas; código(s) H-NN; resultado de `medir_texto.py`; cada pergunta instalada, com bloco e minuto de pagamento, no registro de promessas; ids da tabela de fatos por parágrafo. No modo enxuto (`SKILL.md`), abertura escolhida e códigos H-NN só se o usuário pedir.

**Leia:** `00` §2 (aberturas reais, só pela forma); `02` §3 e duas ou três fichas H-NN; `02` §4; `01` §3.2; `20` Mapa 11, D-N1. H-26, H-27, H-36 e H-50 anunciam o formato ("vamos descobrir..."): reescreva a promessa como a pergunta dita de dentro da cena. `[TESTE-IA]`: ver `21` §1.

**Antes de escrever**
1. **Tamanho.** Ritmo do narrador em `## 0. Canal` (padrão 135 palavras/min). Faixa: ritmo × 1,33 a × 1,58. Mediana do corpus em 90 s: 203 palavras `[DADO]`.
2. **Abertura.** Escolha pela anomalia (`## 1. Ideia`); nomeie a escolhida e uma alternativa:
   - objeto ou documento parado: **o objeto que não deveria existir**, mostrado primeiro, data depois;
   - achado ou gente em risco numa sequência: **cena fria no momento da descoberta**, em presente;
   - dois fatos que colidem: **a contagem que não fecha**;
   - pessoa com registro final (fala, anotação, rádio): **a pessoa e o último registro dela**.

   Abrir pelo que se vê e datar depois é opção `[TESTE-IA]` (`21` §6, H5, fraca).

**Escreva** em 5 a 9 parágrafos curtos, para ser ouvido, com frase de uma linha nos pontos de virada. A 135 palavras/min, 30 s são cerca de 68 palavras.
- **Até 30 s:** âncora concreta e primeira lacuna. Os fatos mais estranhos da ficha entram cedo, como afirmações. Guarde a explicação.
- **Até 60 s:** a pergunta central, uma vez, com nome ou objeto do caso ("Por que dez pessoas deixariam um navio que ainda flutuava?"). No máximo duas perguntas no hook. Nenhuma frase sobre o vídeo ("vamos responder", "neste vídeo", "vamos separar fato de hipótese"). Uma frase assim é Corrige; duas ou mais, ou apelo, bloqueiam.
- **60 a 90 s:** recompensa parcial (dado com fonte, nome, imagem). Contexto depois. Fato forte entra se reabre a pergunta; o que a responde fica para o bloco.
- **Fecho:** pergunta ou afirmação que nomeia algo concreto ainda sem resposta (laço aberto específico), sem repetir a pergunta central. Pergunta: a mais forte que a história abriu (até 12 palavras, com nome ou objeto do caso). Afirmação: a contradição ou o dado estranho que ninguém resolveu, com nome ou objeto. Afirmação que encerra o assunto solta a tensão. Sem anúncio do que vem, sem "o que isso significa" (`21` §6, H3).

**Cena sem invenção.** A cena vem só da coluna "cena possível" de `## 2. Tabela de fatos`. Em cópia de trabalho, marque cada frase:
- **F:** fato da ficha, ainda que parafraseado.
- **I:** inferência dita como inferência ("isso sugere"), de duas linhas da ficha.
- **R:** ritmo ou pergunta, sem fato novo ("Pense nisso.").
- **X:** hora, clima, distância, gesto, estado interno, tentativa ou causa que a ficha não traz.

X também é: relação entre pessoas (amigo, parente, rival), veículo (barco, carro), nacionalidade ou sede que a ficha não dá, quantidade ou comparação ("bem menor", "tanta gente") e adjetivo que embeleza o objeto. Anote o id da ficha ao lado de todo substantivo concreto; sem id, corte. X sai, ou vira F ou R. Cena pobre se resolve com ritmo e ordem, nunca com cenário. Frases de ritmo ("Pense nisso."): no máximo duas, e só se o fato seguinte está na ficha. Fato "a verificar": escreva sem ele ou marque `[VERIFICAR]`, única marca permitida, que sai antes de narrar. Fato de uma só parte entra atribuído.

**Meça.** Salve o texto sem marcas em `hook.txt` e a coluna Fato da tabela em `fatos.txt` (um por linha). Rode `python scripts/medir_texto.py hook.txt --tipo hook --fatos fatos.txt` (`--wpm N` se o canal tem outro ritmo) e registre palavras e tempo. Sem rodar, escreva "não medi". Se a saída traz "fecho em afirmação", cole a última frase e escreva o que ela deixa sem resposta; sem isso, refaça o fecho. Abaixo da faixa: use fatos ainda não usados; se a ficha não alcança, diga ao usuário. Acima: corte.

**Teste de remoção:** sem a surpresa ou o objeto do hook, a pergunta perde o sentido (`11` §3, T5).

**Só avança quando**
- o texto medido ocupa 80 a 95 s;
- a pergunta central aparece uma vez, até 60 s, e o script não aponta metalinguagem;
- toda frase é F, I ou R (superlativo sem fonte é X); todo número tem linha na tabela de fatos;
- a recompensa parcial vem antes de 90 s e o texto fecha em laço aberto específico (cole a última frase e diga que laço ela abre);
- o teste de remoção passa.

**Armadilhas**
- Sumário disfarçado de promessa, mesmo curto.
- "Fique até o fim", pedido de inscrição, pergunta de trivia.
- Abrir pelo desfecho que o vídeo paga. Flash-forward só com pergunta de mecanismo ou consequência (`20` Mapa 11, D-N1).
- Contexto antes da primeira recompensa.
