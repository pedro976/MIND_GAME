# ==============================================================================
# ARQUIVO: src/dados.py
# O QUE FAZ: Gerencia a persistência de dados do jogo em arquivos de texto (I/O).
#            Possui funções para salvar e carregar a pontuação máxima (recorde).
# ESTÁ LINCADO COM:
#   - src/config.py (recebe o caminho do arquivo definido em CAMINHO_RECORDE)
#   - src/jogo.py (chama 'carregar_recorde' ao iniciar e 'salvar_recorde' ao bater recorde)
#   - data/recorde.txt (arquivo físico onde a pontuação é lida/gravada)
# ==============================================================================

# Importa o módulo padrão 'os' para lidar com caminhos de arquivos e criação de pastas.
import os


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto. Retorna True se salvar com sucesso."""
    # O bloco 'try' tenta executar as operações de arquivo e conversão;
    # se ocorrer algum erro previsto (como falta de permissão ou valor inválido), cai no 'except'.
    try:
        # Converte o caminho para texto, transforma em caminho absoluto e extrai só o diretório (pasta) onde o arquivo ficará.
        pasta = os.path.dirname(os.path.abspath(str(caminho_arquivo)))
        # Se existir um caminho de pasta válido, garante que ela (e suas subpastas) exista antes de salvar.
        # 'exist_ok=True' evita erro caso a pasta já esteja criada.
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        # Abre o arquivo no modo escrita ("w", sobrescrevendo o conteúdo anterior) com codificação UTF-8.
        # O 'with' garante que o arquivo será fechado automaticamente ao terminar.
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            # Converte a pontuação para inteiro (valida se é número) e depois para texto para gravar no arquivo.
            arquivo.write(str(int(pontuacao)))
        # Se tudo deu certo até aqui, retorna True indicando que o recorde foi salvo.
        return True
    # Captura erros de sistema/arquivo (OSError) ou de conversão para inteiro (ValueError) sem travar o jogo.
    except (OSError, ValueError):
        return False


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir ou for inválido."""
    # O bloco 'try' tenta abrir, ler e converter o recorde salvo;
    # se o arquivo ainda não existir ou tiver texto inválido, cai no 'except'.
    try:
        # Abre o arquivo no modo leitura ("r") com codificação UTF-8 e fecha automaticamente ao final do 'with'.
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            # Lê todo o conteúdo do arquivo e remove espaços e quebras de linha das pontas (.strip()).
            conteudo = arquivo.read().strip()
            # Converte o texto lido para número inteiro (gera ValueError se não for um número válido).
            valor = int(conteudo)
            # Retorna o recorde apenas se ele for maior ou igual a zero; valores negativos viram 0.
            return valor if valor >= 0 else 0
    # Se o arquivo não existir/não puder ser lido (OSError) ou não contiver um número válido (ValueError), retorna 0.
    except (OSError, ValueError):
        return 0
