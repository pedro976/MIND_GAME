# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

**Nome:**

MIND — O Desafio da Inteligência Artificial

## 2. Integrantes do grupo

- Nome 1: Pedro Henrique Rocha de Souza
- Nome 2: Crystian Marcondes Oliveira Nascimento
- Nome 3:Fabrício Félix Gomes
- Nome 4:Pedro Afonso Marquetotti

## 3. Tema escolhido

**Tema:**

Confiabilidade das informações geradas por Inteligência Artificial e uso responsável da tecnologia no cotidiano.

**Aspecto de uso responsável abordado:**

Confiabilidade e análise crítica dos resultados da IA, com apoio de privacidade e segurança digital. O jogo ensina que uma resposta de IA nem sempre está correta e que é preciso conferir a informação, proteger dados pessoais e decidir com responsabilidade.

**Por que esse tema é relevante?**

Ferramentas de IA já fazem parte da rotina de estudantes e de pessoas em geral: assistentes virtuais, chatbots, recomendações em redes sociais e conteúdos gerados automaticamente. Usar esses recursos sem senso crítico pode levar a erros, desinformação e exposição de dados pessoais.

**Como esse tema se relaciona com o jogo?**

O tema é a própria mecânica do jogo, e não apenas o visual. Cada rodada apresenta uma situação do cotidiano com IA, como uma resposta duvidosa de um chatbot, um pedido de dados pessoais ou um conteúdo suspeito em rede social. O jogador precisa analisar a situação e escolher a decisão mais responsável. Acertar aumenta a pontuação, errar custa uma vida, e após cada resposta o jogo explica por que aquela decisão era (ou não) a mais adequada. Ou seja, o conhecimento sobre uso responsável da IA é o que faz o jogador avançar ou perder.

## 4. Tipo de jogo

**Tipo escolhido:**

Jogo de perguntas e respostas (quiz), com temática de investigação e tecnologia.

## 5. Descrição geral do jogo

**Descrição:**

MIND é um jogo educativo no qual o jogador assume o papel de um investigador que precisa resolver desafios relacionados à Inteligência Artificial no cotidiano.

Na tela são apresentadas situações envolvendo o uso da IA, acompanhadas de três alternativas de resposta. O jogador usa o mouse para selecionar a alternativa que considerar mais responsável ou correta.

Após cada escolha, o jogo informa se a resposta está correta ou incorreta e mostra uma explicação educativa. A partida conta com sistema de pontuação, vidas e indicador de progresso (pergunta atual do total), tornando a experiência mais interativa.

**Categorias de situações previstas:**

- Informações incorretas ou inventadas por IA (confiabilidade).
- Privacidade e compartilhamento de dados pessoais.
- Segurança digital e golpes.
- Redes sociais e conteúdo gerado por IA.
- Uso da IA nos estudos.

**Fluxo de telas previsto:**

Tela inicial → tela de pergunta → tela de explicação após a resposta → tela final (vitória ou derrota) com opção de jogar novamente ou sair.

## 6. Objetivo do jogador

**Objetivo:**

Responder corretamente ao maior número possível de perguntas sobre Inteligência Artificial, acumulando pontos e evitando perder todas as vidas. O jogador deve demonstrar que sabe reconhecer aplicações, limitações e formas responsáveis de usar essa tecnologia.

## 7. Regras principais

- Regra 1: O jogador começa a partida com três vidas.
- Regra 2: Cada pergunta apresenta três alternativas, sendo apenas uma correta.
- Regra 3: Cada resposta correta aumenta a pontuação do jogador.
- Regra 4: Cada resposta incorreta reduz uma vida.
- Regra 5: Após cada resposta, correta ou incorreta, o jogo exibe uma explicação sobre o assunto.
- Regra 6: A partida termina quando todas as perguntas forem respondidas ou quando o jogador perder todas as vidas.
- Regra 7: Se a pontuação final superar o recorde salvo, o recorde é atualizado.

## 8. Condição de vitória

**Condição de vitória:**

O jogador vence ao responder todas as perguntas disponíveis mantendo pelo menos uma vida. Ao concluir os desafios, é exibida uma tela de vitória com a pontuação final e o recorde.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:**

O jogador perde quando as três vidas acabam antes de concluir todas as perguntas. A partida também é encerrada normalmente quando todos os desafios são concluídos. Em ambos os casos, é exibida uma tela final com o resultado e a opção de jogar novamente ou sair.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** O jogador é representado por um investigador que analisa situações relacionadas à Inteligência Artificial.
- **Obstáculos ou desafios:** Perguntas sobre privacidade, segurança digital, confiabilidade das informações, redes sociais e uso da IA na educação.
- **Itens ou objetos de interação:** Botões com as alternativas de resposta e botões para iniciar, avançar e reiniciar a partida.
- **Pontuação, vidas, tempo ou progresso:** Pontuação por acertos, três vidas iniciais, contador de perguntas (progresso) e recorde salvo localmente.
- **Informações na tela:** Pontuação, vidas, número da pergunta atual e recorde exibidos durante a partida.

## 11. Controles previstos

**Controles:**

- Mouse: selecionar as alternativas e interagir com os botões.
- ENTER ou ESPAÇO: iniciar a partida ou avançar para a próxima tela/pergunta.
- ESC: sair do jogo.

## 12. Principais dificuldades esperadas

- Dificuldade 1: Desenvolver uma interface organizada e funcional com Pygame, incluindo botões clicáveis e várias telas.
- Dificuldade 2: Implementar corretamente a lógica das perguntas, alternativas, pontuação, vidas e transição entre as telas.
- Dificuldade 3: Organizar o código em módulos, escrever testes automatizados e salvar o recorde em arquivo.
- Dificuldade 4: Escrever perguntas e explicações corretas, claras e originais, que de fato exercitem o uso responsável da IA.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**

A versão final do MIND deverá ter:

- tela inicial;
- sequência de pelo menos dez perguntas sobre IA, com três alternativas cada;
- sistema de pontuação e três vidas;
- aviso de resposta correta ou incorreta, com explicação educativa após cada resposta;
- condições de vitória e derrota, com tela final de resultado e opção de jogar novamente;
- recorde salvo em arquivo local;
- código organizado em funções e módulos;
- testes automatizados para as principais regras;
- `README.md` e `docs/proposta.md` atualizados.

## 14. Possíveis melhorias, caso haja tempo

- Melhoria 1: Adicionar efeitos sonoros, animações e melhorias visuais à interface.
- Melhoria 2: Implementar níveis de dificuldade e novas categorias de perguntas.
- Melhoria 3: Criar um ranking com as melhores pontuações (`data/ranking.txt`).
- Melhoria 4: Embaralhar a ordem das perguntas e das alternativas a cada partida.

---

## 15. Organização inicial do código

O projeto parte do template oficial da disciplina e mantém sua estrutura de pastas. O código será organizado em módulos:

- `main.py`: ponto de entrada, que inicia o jogo.
- `src/jogo.py`: loop principal, telas e interface gráfica.
- `src/funcoes.py`: regras do jogo, como pontuação, vidas, avaliação da resposta e condições de vitória e derrota.
- `src/perguntas.py`: perguntas, alternativas e explicações.
- `src/dados.py`: leitura e escrita do recorde em arquivo.
- `src/config.py`: constantes (tela, cores, caminhos de arquivos).
- `tests/test_logica.py`: testes automatizados das funções de lógica.
- `docs/`: proposta e documentação do projeto.
- `assets/` e `data/`: recursos visuais e arquivos de dados, conforme o template.

## 16. Estruturas de dados previstas

- **Lista:** guarda todas as perguntas do jogo, na ordem em que serão apresentadas.
- **Dicionário:** representa cada pergunta, com chaves como `enunciado`, `alternativas`, `correta`, `explicacao` e `categoria`.
- **Lista de strings:** as três alternativas de cada pergunta.
- **Tuplas:** cores e posições na tela.
- **Variáveis de estado:** pontuação, vidas, índice da pergunta atual e recorde.

## 17. Arquivos e testes planejados

**Arquivos:** o recorde do jogador será salvo em arquivo de texto (`data/recorde.txt`), permitindo recuperar a maior pontuação mesmo após fechar o jogo. Como melhoria, um ranking poderá usar `data/ranking.txt`.

**Testes:** serão feitos com pytest, em `tests/test_logica.py`, e deverão verificar:

- soma de pontos ao acertar;
- redução de vidas ao errar;
- avaliação de resposta correta e incorreta;
- condições de derrota (vidas zeradas) e de vitória (todas as perguntas respondidas com vidas restantes);
- leitura e escrita do recorde.

## 18. Recursos

- **Linguagem e bibliotecas:** Python, Pygame (interface, eventos e desenho) e pytest (testes).
- **Template:** estrutura oficial da disciplina (IntroAlgs_pygame_template).
- **Imagens, sons e fontes:** serão usados os recursos do template e, caso o grupo inclua outros, a origem e a licença serão registradas no `README.md`.
- **Conteúdo:** perguntas, alternativas e explicações escritas pelo próprio grupo.

## 19. Declaração de originalidade

O grupo declara que a proposta do MIND foi desenvolvida para este trabalho prático, com foco educativo e abordagem própria sobre Inteligência Artificial no cotidiano. O jogo não reutiliza projetos de semestres anteriores nem é cópia de tutoriais, repositórios ou exemplos prontos.

O desenvolvimento será feito em Python e Pygame, usando o template oficial da disciplina como estrutura inicial. Caso sejam utilizados recursos externos, como imagens, sons, fontes ou códigos, suas origens serão identificadas no `README.md`.

Todos os integrantes devem compreender e ser capazes de explicar o funcionamento das principais partes do código.
