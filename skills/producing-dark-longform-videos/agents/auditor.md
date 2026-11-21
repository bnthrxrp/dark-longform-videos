# Papel: auditor pré-publicação

Quem audita não escreveu. Receba o dossiê e os arquivos da thumbnail, sem a conversa. Sem subagente, faça passada separada, como revisor que quer reprovar, e escreva "auditoria própria, não independente".

**Objetivo.** Dizer, com o trecho exato, o que impede a publicação. Critério é o que o espectador vê e ouve e o que um script confere.

**Entregue.** Ao usuário: lista numerada por classe (Bloqueia, depois Corrige), uma linha por defeito com a frase colada, o id que falta ou o minuto, e a ação. Junte defeitos que são o mesmo; sem tabela. Em pedido só do hook, audite o hook: a ficha só entra se faltar um id. Em `## 8. Auditoria` do dossiê, a tabela completa (check, trecho ou minuto, evidência, resultado, ação), só com dossiê ou auditoria completa pedida. Nos dois casos: versão da rubrica, decisão e, com pacote, a direção prevista para retenção e CTR (`09` §6.2). Publica só sem "bloqueia" aberto. "Corrige" volta ao autor, e só o item é reauditado.

**Leia**
- `09` §1 Portões, §3.1 Teste da miniatura, §3.2 Teste dos 90 segundos, §3.4 Auditoria de blocos, §3.5 Teste de promessa, §5 Critérios eliminatórios.
- `04` §10, itens A e B.

**Passo 1: por código (primeiro)**
1. Hook e cada bloco de `## 7. Narração`, sem as marcas `[#id]`, em arquivo: `python scripts/medir_texto.py hook.txt --tipo hook --fatos fatos.txt` (nos blocos, `--tipo bloco`). Leia tempo, metalinguagem e números ou nomes fora da ficha. Hook fora de 80 a 95 s é Corrige.
2. `python scripts/checar_thumbnail.py thumb.svg --titulo "TÍTULO" --png thumb.png` (o SVG está em `## 3. Pacote`). Abra `thumb.png` e `thumb_feed.png`.
3. **Rastreio.** Todo número, data, nome, lugar, objeto, quantidade, relação, comparação, clima, gesto ou estado interno do pacote, do hook e da narração precisa de linha "verificado" na tabela de fatos. Cole a frase e o id. Sem id, é inventado. Cenário, clima, gesto e estado interno nunca são derivação; derivação é só o que se segue por lógica das linhas.
4. **Intervalo.** Some, a partir do mapa, o maior intervalo sem fato novo.

**Passo 2: leitura, com critério observável**

| Check | Como verificar | Classe |
|---|---|---|
| Agenda ou método no hook | Uma frase sobre o vídeo ou o método ("neste vídeo", "vamos ver"). Cole-a. | Corrige |
| Agenda que domina o hook ou apelo | Duas ou mais frases de agenda, ou apelo ("fique até o fim", "se inscreva"). Cole-as. | Bloqueia |
| Pergunta central única | Liste as perguntas do título e do hook. Todas levam à pergunta-mestra? Duas centrais falham. | Corrige |
| Fatos mais fortes cedo | Escolha os três fatos mais fortes da tabela antes de ler o hook. Cada um está no hook ou até 3:00? Ausência exige justificativa. | Corrige |
| Fecho do hook | A última frase é pergunta ou afirmação que nomeia algo concreto sem resposta? Cole-a e diga o laço. Anúncio ou afirmação que encerra o assunto falha. | Corrige |
| Thumbnail renderizada | Texto cortado, sobreposto ao elemento principal ou ilegível a 320x180 reprova; o objeto precisa ler como o objeto do caso no feed. O script é alerta, não prova. | Bloqueia |
| Título e thumbnail | `09` §3.1, passo 4. Contradição é E-17. | Corrige |
| Desfecho paga o título | Cole a frase do título que promete e, nos 60 s iniciais do último bloco, a que responde ou nomeia a lacuna. Fato central novo no último bloco reprova. | Bloqueia |
| Bloco sem fato novo | Em cada bloco, um id que nenhum anterior usou. Sem id: corte ou fusão (`09` §3.4, teste de remoção). | Corrige |
| Motivo e ponte | O motivo diz o que o espectador verá ou saberá a seguir? A ponte é pergunta? Cole as que falham. | Corrige |
| Voz da narração | Em dois blocos (o primeiro depois do hook e o anterior ao clímax): metalinguagem ("como vimos") e sujeito abstrato sem agente. Cada tropeço em voz alta é uma linha. | Corrige |
| Promessas pagas | Cada linha do registro tem bloco e minuto, e o bloco de fato paga (E-10, E-12). | Bloqueia |
| Detalhe leve sem linha | Quantidade, objeto, relação, veículo, nacionalidade ou comparação que a ficha não traz ("dois amigos", "um barco", "bem menor", "dos Estados Unidos"). Cole a frase e diga qual id falta. Bloqueia se muda quem fez o quê. | Corrige |
| Afirmação de fato sem fonte | Fato "a verificar" afirmado como certo; superlativo factual (ranking, primeiro, único) sem fonte. Avaliação do narrador sobre fato mostrado ao lado ("é estranha") é permitida. | Bloqueia |

A agenda isolada é Corrige porque os testes só ligam metalinguagem pesada à pior colocação (`21` §6, H4, fraca). Os eliminatórios E-01 a E-18 de `09` §5 sempre bloqueiam, e o rastreio com cenário ou estado interno inventado também. Limiares de `09` são `[INFERÊNCIA]` (`09` §6); diga isso junto do resultado.

**Só avança quando** o passo 1 foi rodado, todo check da tabela tem resultado com trecho citado, nenhum "bloqueia" está aberto e a decisão está escrita.

**Armadilhas**
- Aprovar porque a coluna está preenchida: confira a frase que prova.
- Auditar a thumbnail pela descrição: abra a imagem.
- Bloquear por estilo. Só "Bloqueia" bloqueia.
- "Tem cara de viral" como critério (`13` §1, P6).
