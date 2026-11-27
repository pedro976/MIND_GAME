# ==============================================================================
# ARQUIVO: src/logic.py
# O QUE FAZ: Contém a lógica de negócio principal do jogo MIND (validação de respostas,
#            cálculo de pontuação por dificuldade, controle de vidas e avanço de perguntas).
# ESTÁ LINCADO COM:
#   - src/jogo.py (importa e utiliza todas as funções de lógica para gerenciar o fluxo do jogo)
#   - src/questions.py (recebe as perguntas para validação da resposta correta)
#   - tests/test_logica.py (utilizado pelo pytest para validar a corretude das regras)
# ==============================================================================

def verificar_resposta(pergunta, indice_selecionado):
    """
    Verifica se a resposta selecionada está correta.
    Retorna True se correta, False caso contrário.
    """
    # Compara o índice da alternativa correta (0, 1 ou 2) com o índice clicado pelo jogador.
    return pergunta["correta"] == indice_selecionado


def atualizar_pontuacao(pontuacao_atual, acerto, dificuldade="Média"):
    """
    Calcula a nova pontuação baseada no acerto e dificuldade.
    """
    # Se o jogador errou, mantém a pontuação sem somar nada.
    if not acerto:
        return pontuacao_atual

    # Tabela de pontos ganhos de acordo com o nível da pergunta.
    bonus = {"Fácil": 10, "Média": 20, "Difícil": 30}
    # Busca o bônus correspondente; se vier uma dificuldade desconhecida, usa 10 como padrão.
    return pontuacao_atual + bonus.get(dificuldade, 10)


def atualizar_vidas(vidas_atuais, acerto):
    """
    Reduz uma vida se o jogador errou.
    """
    # Em caso de erro, desconta 1 vida; em caso de acerto, preserva o total atual.
    if not acerto:
        return vidas_atuais - 1
    return vidas_atuais


def esta_morto(vidas):
    """Verifica se o jogador perdeu todas as vidas."""
    # Retorna True quando não restam mais vidas (0 ou menor).
    return vidas <= 0


def jogo_concluido(indice_pergunta, total_perguntas):
    """Verifica se todas as perguntas foram respondidas."""
    # Quando o índice alcança ou passa o total de perguntas, não há mais rodadas pela frente.
    return indice_pergunta >= total_perguntas

