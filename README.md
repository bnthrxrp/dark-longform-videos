# dark-longform-videos

Skill `producing-dark-longform-videos`.

Skill para agentes (Claude Code e compatíveis) que conduz a produção de um vídeo longo de YouTube
(10 a 60+ minutos) para canal dark — narrado, sem apresentador em câmera — da ideia à leitura do
Analytics.

Ela nasceu de uma pesquisa multiagente sobre retenção, hooks, thumbnails, storytelling e o algoritmo
do YouTube. Os dez documentos dessa pesquisa vêm junto, como base de consulta, com os mapas e as fichas de uma
biblioteca de livros e artigos sobre histórias, atenção e persuasão.

## O que ela faz

Quando o pedido é roteiro, hook, título, thumbnail, auditoria ou diagnóstico de um vídeo longo, a
skill leva o vídeo por seis etapas. Cada etapa tem um briefing de agente e um critério de saída:

| Etapa | Agente | Só avança quando |
|---|---|---|
| Ideia | `agents/ideia.md` | há pergunta-mestra com resposta esperada e fontes para 3+ blocos |
| Pacote | `agents/pacote.md` | cada promessa do título e da thumbnail tem bloco e minuto de pagamento |
| Hook | `agents/hook.md` | âncora antes de 30 s, promessa entre 30 e 60 s, recompensa antes de 90 s |
| Roteiro | `agents/roteiro.md` | cada bloco tem pergunta, recompensa, ponte e motivo para ficar |
| Auditoria | `agents/auditor.md` | rubrica aplicada por quem não escreveu, só com o dossiê |
| Pós-publicação | `agents/analytics.md` | leitura na ordem oficial e um experimento de uma variável |

Cada vídeo ganha um dossiê (`dossie-modelo.md`) com tabela de fatos, registro de promessas, hook,
mapa de blocos, auditoria e experimento.

## Instalação

**Claude Code, para todos os projetos:**

```bash
git clone https://github.com/bnthrxrp/dark-longform-videos.git
cp -r dark-longform-videos/skills/producing-dark-longform-videos ~/.claude/skills/
```

**Claude Code, só em um projeto:** copie a mesma pasta para `.claude/skills/` na raiz do projeto.

A skill aparece na sessão seguinte.

## Conteúdo

```
skills/producing-dark-longform-videos/
  SKILL.md              fluxo, regras e erros comuns
  dossie-modelo.md      modelo do dossiê de um vídeo
  agents/               um briefing por papel
  references/           os dez documentos da pesquisa, os mapas e fichas da biblioteca + INDEX.md (índice por seção)
  scripts/build_index.py  refaz o índice depois de editar uma referência
```

## O que saber antes de confiar

- **Nenhuma recomendação tem efeito medido sobre retenção.** A base separa o que é regra oficial da
  plataforma do que é estudo de outro contexto, relato de praticante ou inferência. Marcas de tempo
  e doses são ponto de partida, a calibrar com os dados do canal.
- **Não há curvas de retenção de terceiros na base**: o YouTube não as publica. A engenharia reversa
  se apoia em transcrições, títulos, thumbnails e contagens públicas de 38 vídeos de alto desempenho,
  sem grupo de comparação.
- **Os mapas e fichas da biblioteca são resumos em palavras próprias**, com citações curtas. Livro de autor entra como
  relato de praticante; nenhuma das obras mede retenção em vídeo longo.
- **A skill não pesquisa o caso do vídeo.** Sem fonte, os fatos entram como "a verificar" e o texto
  narrado não os afirma.
- **Testes.** A skill foi escrita a partir de cenários de pressão rodados com e sem ela. Foram
  exercitadas as etapas de criação e de leitura de Analytics; o papel de auditor e o despacho real de
  subagentes ainda não.

## Referências incluídas

| Arquivo | Conteúdo |
|---|---|
| `01_master_playbook.md` | Sistema IDEIA → PAYOFF, blueprint do vídeo de 30 minutos, grau de confiança |
| `02_hook_database.md` | 59 estruturas para os primeiros 90 segundos |
| `03_thumbnail_engineering_playbook.md` | Modelo do clique, design, título + thumbnail, testes A/B |
| `04_retention_engineering_blueprint.md` | Leitura de curvas, blocos, loops, fadiga |
| `05_longform_storytelling_framework.md` | Estruturas narrativas e modelos de 10 a 60 minutos |
| `06_engenharia_reversa_padroes.md` | Padrões em 38 vídeos de canais dark em quatro idiomas |
| `07_biblioteca_cientifica.md` | Fichas de estudo: curiosidade, atenção, narrativa, memória |
| `08_algoritmo_e_analytics.md` | Recomendação, métricas e roteiro de leitura do Analytics |
| `09_sistema_avaliacao_pre_publicacao.md` | Portões, rubricas e testes práticos |
| `10_framework_experimentacao.md` | Hipóteses testáveis e desenhos de experimento |
| `11` a `16` (`*_mapa_*.md`) | Mapas temáticos de uma biblioteca de 15 livros e artigos: hook e curiosidade, estrutura narrativa, viralização, retenção e hábito, persuasão por narrativa, ofício de escrita |
| `17_fichas_da_biblioteca.md` | Uma ficha por obra (McKee, Truby, Snyder, King, Heath, Berger, Kane, Eyal, Hall e quatro artigos científicos lidos na íntegra) |

## Licença

MIT. Veja [LICENSE](LICENSE). As referências citam trechos curtos de legendas de vídeos de terceiros, identificados por canal e título, para fins de análise.
