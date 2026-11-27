# ==============================================================================
# ARQUIVO: src/config.py
# O QUE FAZ: Define as configurações globais do jogo, incluindo dimensões da tela,
#            taxa de quadros por segundo (FPS), título, paleta de cores RGB e
#            caminhos para arquivos de dados (recorde) e assets (spritesheet).
# ESTÁ LINCADO COM: 
#   - src/jogo.py (utiliza resoluções, cores, título e caminho do recorde)
#   - data/recorde.txt (destino da leitura/escrita do recorde)
#   - assets/imagens/spritesheet.bmp (recurso gráfico do jogo)
# ==============================================================================

# Importa 'os' para montar caminhos de pastas e arquivos de forma compatível com qualquer sistema.
import os

# Descobre a pasta raiz do projeto (MIND_GAME) subindo dois níveis a partir deste arquivo (src/config.py -> src -> MIND_GAME).
PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Configurações da janela e desempenho ---
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60  # Quantidade máxima de quadros desenhados por segundo.

TITULO_JOGO = "MIND — O Desafio da IA"

# --- Paleta de cores no padrão RGB (Vermelho, Verde, Azul de 0 a 255) ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_ESCURO = (45, 45, 45)
CINZA_CLARO = (212, 212, 212)
AZUL_IA = (0, 102, 204)
VERDE_ACERTO = (46, 139, 87)
VERMELHO_ERRO = (178, 34, 34)
AMARELO_DESTAQUE = (255, 215, 0)

# --- Caminhos de arquivos persistentes e recursos gráficos ---
# Usa os.path.join para que os caminhos funcionem independente do diretório onde o comando for executado.
CAMINHO_RECORDE = os.path.join(PASTA_PROJETO, "data", "recorde.txt")
CAMINHO_SPRITES = os.path.join(PASTA_PROJETO, "assets", "imagens", "spritesheet.bmp")

