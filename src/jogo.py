# ==============================================================================
# ARQUIVO: src/jogo.py
# O QUE FAZ: Módulo principal de execução do jogo. Gerencia estados da tela (Menu,
#            Jogando, Feedback, Fim), loop principal, eventos do Pygame, renderização
#            de interface, interface do usuário (UI) e interação com o jogador.
# ESTÁ LINCADO COM:
#   - src/config.py (importa configurações e constantes)
#   - src/questions.py (importa o banco de perguntas)
#   - src/logic.py (importa funções de lógica de negócio)
#   - src/dados.py (importa persistência de dados/recorde)
#   - main.py (é invocado como ponto de entrada)
# ==============================================================================

# --- Importações ---
import pygame  # Biblioteca gráfica e de eventos 2D.
import sys     # Usado para encerrar o processo Python ao sair do jogo.

# Constantes de tela, cores e caminho do arquivo de recorde.
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    BRANCO,
    CINZA_ESCURO,
    CINZA_CLARO,
    AZUL_IA,
    VERDE_ACERTO,
    VERMELHO_ERRO,
    AMARELO_DESTAQUE,
    CAMINHO_RECORDE,
)
# Lista com as 30 perguntas do quiz.
from src.questions import PERGUNTAS
# Regras puras do jogo (validação, pontuação, vidas e condições de fim).
from src.logic import (
    verificar_resposta,
    atualizar_pontuacao,
    atualizar_vidas,
    esta_morto,
    jogo_concluido,
)
# Funções para ler e salvar o recorde em arquivo texto.
from src.dados import salvar_recorde, carregar_recorde

# --- Estados do jogo (controlam qual tela é exibida e quais eventos são aceitos) ---
MENU = "MENU"
JOGANDO = "JOGANDO"
FEEDBACK = "FEEDBACK"
FIM = "FIM"

# --- Layout dos botões de alternativa (compartilhado entre desenho e detecção de clique) ---
BOTAO_X = 50
BOTAO_Y_INICIAL = 240
BOTAO_LARGURA = 700
BOTAO_ALTURA = 85
BOTAO_ESPACO = 100


# ==============================================================================
# FUNÇÕES AUXILIARES DE LAYOUT E TEXTO
# ==============================================================================

def obter_retangulo_alternativa(indice):
    """Retorna o retângulo clicável da alternativa pelo seu índice."""
    # Calcula a posição vertical somando o deslocamento inicial com o espaço ocupado pelos botões anteriores.
    return pygame.Rect(
        BOTAO_X,
        BOTAO_Y_INICIAL + indice * BOTAO_ESPACO,
        BOTAO_LARGURA,
        BOTAO_ALTURA,
    )


def quebrar_texto(texto, fonte, largura_max):
    """Divide o texto em linhas que cabem dentro de largura_max."""
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""

    # Vai juntando palavra por palavra enquanto a largura em pixels couber em largura_max.
    for palavra in palavras:
        candidato = f"{linha_atual} {palavra}".strip()
        if fonte.size(candidato)[0] <= largura_max:
            linha_atual = candidato
        else:
            # Quando ultrapassa o limite, fecha a linha anterior e começa uma nova com a palavra atual.
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra

    # Adiciona a última linha restante após o loop.
    if linha_atual:
        linhas.append(linha_atual)

    return linhas


def desenhar_texto(tela, texto, fonte, cor, x, y, largura_max=None, centralizado=False):
    """Desenha texto na tela com suporte a quebra de linha opcional."""
    # Se largura_max for informada, quebra o texto em várias linhas; caso contrário, mantém uma única linha.
    linhas = quebrar_texto(texto, fonte, largura_max) if largura_max else [texto]
    espaco_linha = fonte.get_height() + 5

    # Renderiza cada linha como imagem (Surface) e posiciona na tela.
    for i, linha in enumerate(linhas):
        txt_surf = fonte.render(linha, True, cor)
        txt_rect = txt_surf.get_rect()
        if centralizado:
            txt_rect.centerx = x
        else:
            txt_rect.x = x
        txt_rect.y = y + i * espaco_linha
        tela.blit(txt_surf, txt_rect)


def desenhar_cabecalho(tela, fonte_ui, indice_pergunta, total_perguntas, vidas, pontos):
    """Desenha a barra superior com progresso, vidas e pontuação."""
    # Faixa azul fixa no topo da janela (altura 60px).
    pygame.draw.rect(tela, AZUL_IA, (0, 0, LARGURA_TELA, 60))
    desenhar_texto(tela, f"Pergunta {indice_pergunta + 1}/{total_perguntas}", fonte_ui, BRANCO, 20, 20)
    # Destaca as vidas em vermelho quando restar apenas 1 vida.
    desenhar_texto(tela, f"Vidas: {vidas}", fonte_ui, VERMELHO_ERRO if vidas == 1 else BRANCO, 350, 20)
    desenhar_texto(tela, f"Pontos: {pontos}", fonte_ui, AMARELO_DESTAQUE, 650, 20)


# ==============================================================================
# FUNÇÕES DE RENDERIZAÇÃO DAS TELAS
# ==============================================================================

def desenhar_menu(tela, fontes, recorde):
    """Desenha a tela inicial do jogo."""
    desenhar_texto(tela, "MIND", fontes["titulo"], AZUL_IA, LARGURA_TELA // 2, 120, centralizado=True)
    desenhar_texto(tela, "O Desafio da Inteligência Artificial", fontes["pergunta"], BRANCO, LARGURA_TELA // 2, 190, centralizado=True)

    # Etiqueta visual do modo de jogo.
    pygame.draw.rect(tela, AZUL_IA, (LARGURA_TELA // 2 - 100, 240, 200, 40), border_radius=5)
    desenhar_texto(tela, "MODO INVESTIGADOR", fontes["ui"], BRANCO, LARGURA_TELA // 2, 250, centralizado=True)

    # Breve instrução e chamada para iniciar a partida.
    desenhar_texto(tela, "Analise as situações e tome as decisões corretas", fontes["texto"], CINZA_CLARO, LARGURA_TELA // 2, 310, centralizado=True)
    desenhar_texto(tela, "para garantir o uso ético e seguro da tecnologia.", fontes["texto"], CINZA_CLARO, LARGURA_TELA // 2, 340, centralizado=True)

    desenhar_texto(tela, "Pressione ESPAÇO para começar", fontes["pergunta"], AMARELO_DESTAQUE, LARGURA_TELA // 2, 450, centralizado=True)
    desenhar_texto(tela, f"Recorde: {recorde}", fontes["ui"], BRANCO, LARGURA_TELA // 2, 520, centralizado=True)


def desenhar_jogando(tela, fontes, pergunta, indice_pergunta, total_perguntas, vidas, pontos):
    """Desenha a tela de pergunta e alternativas."""
    desenhar_cabecalho(tela, fontes["ui"], indice_pergunta, total_perguntas, vidas, pontos)

    # Exibe o enunciado com quebra automática e os metadados da pergunta.
    desenhar_texto(tela, pergunta["enunciado"], fontes["pergunta"], BRANCO, 50, 80, largura_max=700)
    desenhar_texto(
        tela,
        f"Categoria: {pergunta['categoria']} | Dificuldade: {pergunta['dificuldade']}",
        fontes["ui"],
        CINZA_CLARO,
        50,
        200,
    )

    # Lê a posição atual do mouse para aplicar efeito de destaque (hover) no botão sob o cursor.
    mouse_pos = pygame.mouse.get_pos()
    espaco_linha = fontes["texto"].get_height() + 5
    for i, alt in enumerate(pergunta["alternativas"]):
        rect = obter_retangulo_alternativa(i)
        cor_btn = (0, 153, 255) if rect.collidepoint(mouse_pos) else AZUL_IA
        pygame.draw.rect(tela, cor_btn, rect, border_radius=10)

        # Centraliza verticalmente o texto da alternativa dentro da caixa do botão.
        texto_alt = f"{i + 1}. {alt}"
        linhas = quebrar_texto(texto_alt, fontes["texto"], BOTAO_LARGURA - 40)
        altura_texto = len(linhas) * espaco_linha - 5
        y_texto = rect.y + (rect.height - altura_texto) // 2
        desenhar_texto(tela, texto_alt, fontes["texto"], BRANCO, rect.x + 20, y_texto, largura_max=BOTAO_LARGURA - 40)


def desenhar_feedback(tela, fontes, msg, cor, explicacao, indice_pergunta, total_perguntas, vidas, pontos):
    """Desenha o feedback educativo após a resposta."""
    desenhar_cabecalho(tela, fontes["ui"], indice_pergunta, total_perguntas, vidas, pontos)
    desenhar_texto(tela, msg, fontes["titulo"], cor, LARGURA_TELA // 2, 110, centralizado=True)
    desenhar_texto(tela, "Por quê?", fontes["pergunta"], BRANCO, 50, 200)
    desenhar_texto(tela, explicacao, fontes["texto"], CINZA_CLARO, 50, 250, largura_max=700)
    desenhar_texto(tela, "Pressione ESPAÇO ou clique para continuar", fontes["ui"], AMARELO_DESTAQUE, LARGURA_TELA // 2, 510, centralizado=True)


def desenhar_fim(tela, fontes, vidas, pontos, recorde):
    """Desenha a tela final de vitória ou derrota."""
    # Define o título e a cor conforme o jogador tenha terminado com vidas ou zerado.
    titulo_fim = "VITÓRIA!" if vidas > 0 else "GAME OVER"
    cor_fim = VERDE_ACERTO if vidas > 0 else VERMELHO_ERRO

    desenhar_texto(tela, titulo_fim, fontes["titulo"], cor_fim, LARGURA_TELA // 2, 150, centralizado=True)
    desenhar_texto(tela, f"Pontuação Final: {pontos}", fontes["pergunta"], BRANCO, LARGURA_TELA // 2, 250, centralizado=True)
    desenhar_texto(tela, f"Recorde: {recorde}", fontes["ui"], AMARELO_DESTAQUE, LARGURA_TELA // 2, 300, centralizado=True)
    desenhar_texto(tela, "Pressione ESPAÇO para o Menu ou ESC para Sair", fontes["texto"], CINZA_CLARO, LARGURA_TELA // 2, 450, centralizado=True)


# ==============================================================================
# CONTROLE DE FLUXO E LOOP PRINCIPAL
# ==============================================================================

def avancar_apos_feedback(indice_pergunta, total_perguntas, vidas, pontos, recorde):
    """Define o próximo estado após o feedback e atualiza o recorde ao encerrar."""
    # Se acabou as vidas ou respondeu a última pergunta, encerra a partida e salva recorde se bateu o anterior.
    if esta_morto(vidas) or jogo_concluido(indice_pergunta + 1, total_perguntas):
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)
        return FIM, indice_pergunta, recorde
    # Caso contrário, passa para a próxima pergunta.
    return JOGANDO, indice_pergunta + 1, recorde


def executar_jogo():
    """Inicializa o Pygame, controla eventos e executa o loop principal do jogo."""
    # --- Inicialização da janela, relógio e fontes ---
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = {
        "titulo": pygame.font.SysFont("Arial", 48, bold=True),
        "pergunta": pygame.font.SysFont("Arial", 24, bold=True),
        "texto": pygame.font.SysFont("Arial", 20),
        "ui": pygame.font.SysFont("Arial", 18, bold=True),
    }

    # --- Variáveis de estado da partida ---
    estado_atual = MENU
    indice_pergunta = 0
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)  # Carrega o maior recorde salvo em disco.
    feedback_msg = ""
    feedback_cor = BRANCO
    feedback_explicacao = ""

    # --- Loop principal (roda até o jogador fechar a janela ou apertar ESC na tela final) ---
    rodando = True
    while rodando:
        # Limita a taxa de atualização para FPS quadros por segundo.
        relogio.tick(FPS)

        # --- Processamento de eventos (teclado, mouse e fechamento da janela) ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif estado_atual == MENU:
                # No menu, ENTER ou ESPAÇO inicia uma nova partida zerando pontos e vidas.
                if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if PERGUNTAS:
                        estado_atual = JOGANDO
                        indice_pergunta = 0
                        pontos = 0
                        vidas = 3

            elif estado_atual == JOGANDO:
                # Durante a pergunta, verifica clique esquerdo em uma das 3 caixas de alternativa.
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    pergunta = PERGUNTAS[indice_pergunta]
                    for i in range(len(pergunta["alternativas"])):
                        if obter_retangulo_alternativa(i).collidepoint(evento.pos):
                            acertou = verificar_resposta(pergunta, i)
                            feedback_explicacao = pergunta["explicacao"]
                            feedback_msg = "CORRETO!" if acertou else "INCORRETO!"
                            feedback_cor = VERDE_ACERTO if acertou else VERMELHO_ERRO
                            pontos = atualizar_pontuacao(pontos, acertou, pergunta["dificuldade"])
                            vidas = atualizar_vidas(vidas, acertou)
                            estado_atual = FEEDBACK
                            break

            elif estado_atual == FEEDBACK:
                # Na tela de feedback, teclado (ENTER/ESPAÇO) ou clique avança para a próxima etapa.
                avancou_tecla = evento.type == pygame.KEYDOWN and evento.key in (pygame.K_RETURN, pygame.K_SPACE)
                avancou_mouse = evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1
                if avancou_tecla or avancou_mouse:
                    estado_atual, indice_pergunta, recorde = avancar_apos_feedback(
                        indice_pergunta,
                        len(PERGUNTAS),
                        vidas,
                        pontos,
                        recorde,
                    )

            elif estado_atual == FIM:
                # Na tela final, ENTER/ESPAÇO volta ao menu e ESC encerra o jogo.
                if evento.type == pygame.KEYDOWN:
                    if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                        estado_atual = MENU
                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

        # --- Renderização da tela correspondente ao estado atual ---
        tela.fill(CINZA_ESCURO)

        if estado_atual == MENU:
            desenhar_menu(tela, fontes, recorde)
        elif estado_atual == JOGANDO:
            desenhar_jogando(tela, fontes, PERGUNTAS[indice_pergunta], indice_pergunta, len(PERGUNTAS), vidas, pontos)
        elif estado_atual == FEEDBACK:
            desenhar_feedback(
                tela,
                fontes,
                feedback_msg,
                feedback_cor,
                feedback_explicacao,
                indice_pergunta,
                len(PERGUNTAS),
                vidas,
                pontos,
            )
        elif estado_atual == FIM:
            desenhar_fim(tela, fontes, vidas, pontos, recorde)

        # Atualiza a janela visível com tudo o que foi desenhado neste quadro.
        pygame.display.flip()

    # --- Encerramento limpo do Pygame e do programa ---
    pygame.quit()
    sys.exit()

