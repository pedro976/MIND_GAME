# ==============================================================================
# ARQUIVO: main.py
# O QUE FAZ: Ponto de entrada principal do jogo MIND.
# ESTÁ LINCADO COM:
#   - src/jogo.py (importa e executa a função 'executar_jogo')
# ==============================================================================

# Importa a função principal que inicializa o Pygame e inicia o loop do jogo.
from src.jogo import executar_jogo


# Garante que o jogo só será iniciado quando este arquivo for executado diretamente
# (evita abrir a janela caso outro módulo ou teste importe algo daqui).
if __name__ == "__main__":
    executar_jogo()
