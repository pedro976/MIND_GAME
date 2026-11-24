# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida as regras usadas pelo jogo em `src/logic.py`, os caminhos dos recursos e a persistencia do recorde em `src/dados.py`.

## Como executar

```bash
python -m pytest
```

## Boas praticas

- Crie testes para toda regra de pontuacao, vidas e condicoes de fim de jogo.
- Mantenha as regras do jogo testaveis no modulo `src/logic.py`.
