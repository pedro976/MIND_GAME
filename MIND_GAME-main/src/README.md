# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, eventos, atualização e renderização.
- `config.py`: constantes globais (tela, cores, caminhos do projeto, FPS).
- `logic.py`: regras de resposta, pontuação, vidas e fim de jogo, usadas por `jogo.py`.
- `questions.py`: perguntas e alternativas, usadas por `jogo.py`.
- `funcoes.py`: funções auxiliares genéricas.
- `sprites.py`: carregamento e recorte de spritesheet (disponível para uso na interface).
- `dados.py`: leitura e gravação de dados (recorde/ranking).

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.
