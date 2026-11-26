# ==============================================================================
# ARQUIVO: src/dados.py
# O QUE FAZ: Gerencia a persistência de dados do jogo em arquivos de texto (I/O).
#            Possui funções para salvar e carregar a pontuação máxima (recorde).
# ESTÁ LINCADO COM:
#   - src/config.py (recebe o caminho do arquivo definido em CAMINHO_RECORDE)
#   - src/jogo.py (chama 'carregar_recorde' ao iniciar e 'salvar_recorde' ao bater recorde)
#   - data/recorde.txt (arquivo físico onde a pontuação é lida/gravada)
# ==============================================================================

import os


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto. Retorna True se salvar com sucesso."""
    try:
        pasta = os.path.dirname(os.path.abspath(str(caminho_arquivo)))
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(str(int(pontuacao)))
        return True
    except (OSError, ValueError):
        return False


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir ou for inválido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            valor = int(conteudo)
            return valor if valor >= 0 else 0
    except (OSError, ValueError):
        return 0
