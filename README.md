# dark-longform-videos

Skill `producing-dark-longform-videos`, versão 2.0.0.

Skill para agentes (Claude Code, claude.ai e compatíveis) que conduz a produção de um vídeo longo de
YouTube (10 a 60+ minutos) para canal dark, narrado e sem apresentador em câmera. Vai da ideia ao texto
narrado, à auditoria antes de publicar e à leitura do Analytics.

Ela nasceu de uma pesquisa multiagente sobre retenção, hooks, thumbnails, storytelling e o algoritmo do
YouTube. Os documentos da pesquisa vêm junto, como base de consulta, com os mapas e as fichas de uma
biblioteca de 27 livros e artigos sobre histórias, atenção, persuasão e retenção em vídeo.

## O que ela faz

Quando o pedido é ideia, título, thumbnail, hook, roteiro, narração, auditoria ou diagnóstico de um vídeo
longo, a skill leva o trabalho por sete etapas. Cada etapa tem um briefing de agente e um critério de saída.

A skill parte de duas metades que não se substituem:

1. **Motivo para clicar e para continuar.** O espectador não conhece o caso. Ele clica por uma cena
   concreta ou uma anomalia que cabe numa frase e fica por uma pergunta central paga aos poucos.
2. **Disciplina de fato e promessa.** Só se afirma o que tem fonte. Só se promete o que o vídeo paga.

Seguir o processo evita erro. Não faz ninguém clicar.

## O fluxo em 7 etapas

| Etapa | Briefing | Só avança quando |
|---|---|---|
| 1. Ideia | `agents/ideia.md` | a anomalia cabe em uma frase, a pergunta-mestra tem resposta esperada ou recompensa entregável, há fatos independentes para a duração e pelo menos 3 têm cena |
| 2. Pacote | `agents/pacote.md` | toda promessa do título e da thumbnail tem bloco e minuto de pagamento, a ficha de layout está completa e a legibilidade foi checada |
| 3. Hook | `agents/hook.md` | o texto medido ocupa 80 a 95 s, a pergunta central aparece uma vez até 60 s e o fecho é um laço aberto |
| 4. Roteiro (mapa e sinopse em três tempos) | `agents/roteiro.md` | a sinopse tem começo, meio e fim, e todo bloco tem fato novo, imagem, motivo concreto para ficar e ponte em forma de pergunta |
| 5. Narração (texto narrado) | `agents/narracao.md` | todo bloco tem texto dentro de 10% do tempo do mapa, toda frase de fato tem fonte e não há metalinguagem |
| 6. Auditoria | `agents/auditor.md` | as checagens por código rodaram, cada item tem trecho citado e nenhum bloqueio está aberto |
| 7. Pós-publicação | `agents/analytics.md` | há hipótese, resultado com nível de evidência e o briefing a mudar |

O projeto vive num dossiê (`dossie-modelo.md`), com uma seção por etapa. Pedido parcial ou com pressa
usa o modo enxuto: menos cerimônia, mesmo critério. Subagente só na auditoria, que recebe o dossiê e
nunca a conversa de quem escreveu.

## Ferramentas por código

Contagem e legibilidade não se medem de cabeça. Três scripts, só com a biblioteca padrão:

| Script | O que faz |
|---|---|
| `scripts/medir_texto.py` | Mede um hook ou bloco narrado: palavras, frases, tempo estimado, perguntas, frases sobre o próprio vídeo e números e nomes que não estão na ficha de fatos. |
| `scripts/checar_thumbnail.py` | Checa uma thumbnail em SVG 1280x720: texto cortado, sobreposto ou fora da área segura, contraste e legibilidade em 320x180. |
| `scripts/checar_pacote.py` | Valida a skill antes de publicar: frontmatter, caminhos e citações, índice, `--help` dos scripts, tamanho dos briefings, arquivos indesejados e segredos. Com `--zip`, monta o pacote para upload. |

`scripts/build_index.py` refaz `references/INDEX.md` depois de editar uma referência.

**O que precisam.** Python 3.10+. Para `checar_thumbnail.py` medir por completo, Playwright com
Chromium instalado. Com `cairosvg`, o fundo é renderizado e as caixas de texto continuam estimadas. Sem
nenhum dos dois, a checagem é estática e parcial, e o relatório avisa. Sem como rodar um script, a skill
escreve "não medi".

Uso rápido, na pasta da skill:

```bash
python scripts/medir_texto.py hook.txt --tipo hook --fatos fatos.txt
python scripts/checar_thumbnail.py thumb.svg --titulo "TÍTULO" --png thumb.png
python scripts/checar_pacote.py --zip producing-dark-longform-videos.zip
```

## Instalação

**Claude Code, para todos os projetos:**

```bash
git clone https://github.com/bnthrxrp/dark-longform-videos.git
cp -r dark-longform-videos/skills/producing-dark-longform-videos ~/.claude/skills/
```

**Claude Code, só em um projeto:** copie a mesma pasta para `.claude/skills/` na raiz do projeto.

A skill aparece na sessão seguinte.

**claude.ai:** use o zip pronto em [`dist/producing-dark-longform-videos.zip`](dist/producing-dark-longform-videos.zip), ou monte o seu com `python scripts/checar_pacote.py --zip producing-dark-longform-videos.zip`
(a pasta da skill fica na raiz do zip) e envie o arquivo na área de Skills das configurações da conta.
O nome do menu muda com o tempo; hoje costuma estar em Configurações > Capacidades. Os scripts só rodam
se o ambiente tiver execução de código. Sem ela, a skill funciona e informa o que não mediu.

## Conteúdo

```
skills/producing-dark-longform-videos/
  SKILL.md              fluxo, regras e entrega
  dossie-modelo.md      modelo do dossiê de um vídeo
  agents/               um briefing por etapa (ideia, pacote, hook, roteiro, narração, auditor, analytics)
  references/           kit de bolso, pesquisa, mapas e fichas da biblioteca, testes + INDEX.md
  scripts/              medir_texto.py, checar_thumbnail.py, checar_pacote.py, build_index.py
```

## O que saber antes de confiar

- **Nenhuma recomendação tem efeito medido em audiência.** A base separa o que é regra oficial da
  plataforma do que é estudo de outro contexto, relato de praticante ou inferência, cada um com etiqueta.
  Marcas de tempo e doses são ponto de partida, a calibrar com os dados do canal.
- **Não há curvas de retenção de terceiros na base.** O YouTube não as publica. A engenharia reversa
  se apoia em transcrições, títulos, thumbnails e contagens públicas de 38 vídeos de alto desempenho,
  sem grupo de comparação.
- **Os mapas e fichas da biblioteca são resumos em palavras próprias**, com citações curtas. Livro de
  autor entra como relato de praticante. Os estudos com dados do YouTube medem duração e fração
  assistida entre vídeos, não o efeito de uma técnica de roteiro.
- **A skill não pesquisa o caso do vídeo.** Sem fonte, os fatos entram como "a verificar" e a narração
  não os afirma.
- **Testes com juízes de IA, etiqueta `[TESTE-IA]`.** O mesmo pedido foi feito a um modelo pequeno sem
  a skill e com cada versão dela, e modelos maiores ordenaram as entregas sem saber a origem. A versão
  de pesquisa perdeu na primeira rodada, as correções a levaram a empatar com o texto sem skill na
  segunda, e o roteiro e o texto narrado nunca foram julgados. Juízes de IA são modelos, não
  espectadores: o resultado não mede clique, retenção nem satisfação. O resumo, com os limites, está em
  `references/21_testes_comparativos.md`. O teste que decide é no seu canal.
- **Testes de uso da versão 2.** Cinco pedidos reais foram feitos a Claude Haiku 5.5 seguindo a skill e
  avaliados por um revisor independente; os dois que falharam foram corrigidos e refeitos. Isso testa se
  as instruções são seguidas, não se o vídeo performa.

## Referências incluídas

| Arquivo | Conteúdo |
|---|---|
| `00_kit_de_bolso.md` | Doses com etiqueta, aberturas reais, checklist de thumbnail e pontes entre blocos |
| `INDEX.md` | Trilha por papel e índice de seções com faixa de linhas, para ler só o necessário |
| `01_master_playbook.md` | Sistema IDEIA → PAYOFF, blueprint do vídeo de 30 minutos, grau de confiança |
| `02_hook_database.md` | 59 estruturas para os primeiros 90 segundos |
| `03_thumbnail_engineering_playbook.md` | Modelo do clique, design, título + thumbnail, testes A/B |
| `04_retention_engineering_blueprint.md` | Leitura de curvas, blocos, loops, fadiga |
| `05_longform_storytelling_framework.md` | Estruturas narrativas e modelos de 10 a 60 minutos |
| `06_engenharia_reversa_padroes.md` | Padrões em 38 vídeos de canais dark em quatro idiomas |
| `07_biblioteca_cientifica.md` | Fichas de estudo: curiosidade, atenção, narrativa, memória |
| `08_algoritmo_e_analytics.md` | Recomendação, métricas e roteiro de leitura do Analytics |
| `09_sistema_avaliacao_pre_publicacao.md` | Portões, rubricas e testes práticos |
| `10_framework_experimentacao.md` | Hipóteses testáveis, desenhos de experimento e como o aprendizado volta |
| `11` a `16` (`*_mapa_*.md`) | Mapas temáticos da primeira leva da biblioteca: hook e curiosidade, estrutura narrativa, viralização, retenção e hábito, persuasão por narrativa, ofício de escrita |
| `17_fichas_da_biblioteca.md` | Uma ficha por obra, 27 obras: manuais de roteiro e de documentário, livros de divulgação e artigos científicos |
| `18_mapa_evidencia_de_retencao_em_video.md` | O que os estudos com dados do YouTube permitem dizer sobre duração, fração assistida e engajamento |
| `19_mapa_narrativa_documental_e_edicao.md` | Narrativa documental e montagem aplicadas a vídeo narrado |
| `20_atualizacao_dos_mapas_11_a_16.md` | O que a segunda leva (12 obras) muda nos mapas da primeira |
| `21_testes_comparativos.md` | Os testes cegos com juízes de IA, a etiqueta `[TESTE-IA]` e os limites do que provam |

`06`, `07`, `15` e `17` são consulta de fundo: não é preciso abri-los para escrever.

## Licença

MIT. Veja [LICENSE](LICENSE). As referências citam trechos curtos de legendas de vídeos de terceiros,
identificados por canal e título, para fins de análise.
