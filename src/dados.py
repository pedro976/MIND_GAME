# ==============================================================================
# ARQUIVO: src/dados.py
# O QUE FAZ: Gerencia a persistência de dados do jogo em arquivos de texto (I/O).
#            Possui funções para salvar e carregar a pontuação máxima (recorde).
# ESTÁ LINCADO COM:
#   - src/config.py (recebe o caminho do arquivo definido em CAMINHO_RECORDE)
#   - src/jogo.py (chama 'carregar_recorde' ao iniciar e 'salvar_recorde' ao bater recorde)
#   - data/recorde.txt (arquivo físico onde a pontuação é lida/gravada)
# ==============================================================================

def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir ou for inválido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            return int(conteudo) if conteudo.isdigit() else 0
    except (FileNotFoundError, ValueError):
        return 0
