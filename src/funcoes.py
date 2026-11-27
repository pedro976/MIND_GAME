# ==============================================================================
# ARQUIVO: src/funcoes.py
# O QUE FAZ: Contém funções utilitárias gerais para cálculos de pontuação, gerenciamento
#            de vida, limitação de valores (clamp) e verificação de colisão geométrica.
# ESTÁ LINCADO COM:
#   - Funções de suporte genéricas que podem ser utilizadas em módulos de lógica ou testes.
# ==============================================================================

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    # Retorna o novo total acumulado após somar os pontos recebidos.
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    # Subtrai o dano informado do total de vida restante.
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    # Retorna True se as vidas chegaram a zero (ou ficaram negativas).
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    # Se estiver abaixo do piso permitido, trava no valor mínimo.
    if valor < minimo:
        return minimo
    # Se ultrapassar o teto permitido, trava no valor máximo.
    if valor > maximo:
        return maximo
    # Caso contrário, o valor já está dentro da faixa válida.
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    # Usa o método colliderect do pygame.Rect para checar se os dois retângulos se encostam.
    return retangulo_1.colliderect(retangulo_2)
