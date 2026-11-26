# MIND: O Desafio da Inteligência Artificial

Projeto final da disciplina de Introdução a Algoritmos e Programação (PUC Minas), desenvolvido em Python e Pygame.

MIND é um jogo educativo de perguntas e respostas sobre Inteligência Artificial no cotidiano. Cada rodada apresenta uma situação prática envolvendo privacidade, segurança digital, confiabilidade das informações, saúde, educação ou ética, e exige que o jogador escolha a conduta mais responsável.

## Integrantes do grupo

- Pedro Henrique Rocha de Souza
- Crystian Marcondes Oliveira Nascimento
- Fabrício Félix Gomes
- Pedro Afonso Marquetotti

## Estrutura do projeto

- `main.py`: ponto de entrada que inicia o jogo.
- `src/jogo.py`: loop principal, controle de estados (`MENU`, `JOGANDO`, `FEEDBACK`, `FIM`) e interface em Pygame.
- `src/logic.py`: regras da partida (verificação de resposta, pontuação por dificuldade, vidas e condições de fim de jogo).
- `src/questions.py`: lista com 30 perguntas, categorias, níveis de dificuldade e explicações educativas.
- `src/dados.py`: leitura e gravação do recorde em arquivo texto.
- `src/config.py`: dimensões da tela, FPS, cores e caminhos resolvidos a partir da pasta do projeto.
- `src/funcoes.py` e `src/sprites.py`: módulos auxiliares mantidos da estrutura inicial do template.
- `assets/`: pasta do template com recursos visuais (`assets/imagens/spritesheet.bmp`, não utilizado na interface atual).
- `data/recorde.txt`: arquivo texto que guarda a maior pontuação registrada.
- `tests/test_logica.py`: testes automatizados com `pytest`.
- `docs/proposta.md`: proposta e planejamento do projeto.

## Como funciona o jogo

O jogo conta com 30 perguntas divididas nos níveis Fácil, Média e Difícil. O jogador começa a partida com 3 vidas e 0 pontos.

- A cada acerto, a pontuação aumenta conforme a dificuldade da pergunta (+10 Fácil, +20 Média, +30 Difícil).
- A cada erro, o jogador perde 1 vida.
- Após qualquer resposta, uma tela de feedback explica por que aquela decisão é adequada ou arriscada.
- A partida termina com vitória ao responder todas as 30 perguntas mantendo pelo menos 1 vida, ou com derrota (Game Over) quando as vidas chegam a zero.
- Ao final, se a pontuação superar o valor salvo em `data/recorde.txt`, o novo recorde é gravado localmente.

## Controles

- Botão esquerdo do mouse: clicar em uma das três alternativas na tela da pergunta ou avançar na tela de feedback.
- `ENTER` ou `ESPAÇO`: iniciar o jogo no menu, avançar após o feedback e retornar ao menu na tela final.
- `ESC`: sair do jogo na tela final (ou fechar a janela a qualquer momento).

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/pedro976/MIND_GAME.git
cd MIND_GAME
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o jogo

```bash
python main.py
```

## Como executar os testes

```bash
python -m pytest -v
```

## Recursos externos e créditos

- Template oficial da disciplina ([`IntroAlgs_pygame_template`](https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template)): estrutura base de diretórios, `src/sprites.py`, `src/funcoes.py` e o arquivo `assets/imagens/spritesheet.bmp` (mantido do template, sem uso na tela atual).
- `pygame`: biblioteca utilizada para janela, eventos, fontes e desenho 2D.
- `pytest`: biblioteca utilizada para os testes automatizados em `tests/test_logica.py`.
- Fontes tipográficas: fonte de sistema `Arial` carregada via `pygame.font.SysFont`.
- Banco de perguntas e explicações: elaborado pelo grupo sobre o tema Inteligência Artificial no cotidiano.

## Checklist para entrega

- [x] Definição do nome do jogo e dos integrantes.
- [x] Documentação da proposta em `docs/proposta.md`.
- [x] Integração com a estrutura do template oficial da disciplina.
- [x] Implementação das telas, regras, pontuação, vidas e persistência de recorde.
- [x] Testes automatizados para lógica, persistência, caminhos e perguntas.
- [x] Revisão do `README.md` com controles, execução e recursos externos.
