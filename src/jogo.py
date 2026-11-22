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

import pygame
import sys
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    BRANCO,
    PRETO,
    CINZA_ESCURO,
    CINZA_CLARO,
    AZUL_IA,
    VERDE_ACERTO,
    VERMELHO_ERRO,
    AMARELO_DESTAQUE,
    CAMINHO_RECORDE,
)
from src.questions import PERGUNTAS
from src.logic import (
    verificar_resposta,
    atualizar_pontuacao,
    atualizar_vidas,
    esta_morto,
    jogo_concluido,
)
from src.dados import salvar_recorde, carregar_recorde

# Estados do Jogo
MENU = "MENU"
JOGANDO = "JOGANDO"
FEEDBACK = "FEEDBACK"
FIM = "FIM"

def desenhar_texto(tela, texto, fonte, cor, x, y, largura_max=None, centralizado=False):
    """Desenha texto na tela com suporte a quebra de linha opcional."""
    if largura_max:
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""
        for palavra in palavras:
            test_line = linha_atual + palavra + " "
            if fonte.size(test_line)[0] < largura_max:
                linha_atual = test_line
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "
        linhas.append(linha_atual)
        
        for i, linha in enumerate(linhas):
            txt_surf = fonte.render(linha, True, cor)
            txt_rect = txt_surf.get_rect()
            if centralizado:
                txt_rect.centerx = x
                txt_rect.y = y + i * (fonte.get_height() + 5)
            else:
                txt_rect.x = x
                txt_rect.y = y + i * (fonte.get_height() + 5)
            tela.blit(txt_surf, txt_rect)
    else:
        txt_surf = fonte.render(texto, True, cor)
        txt_rect = txt_surf.get_rect()
        if centralizado:
            txt_rect.centerx = x
            txt_rect.y = y
        else:
            txt_rect.x = x
            txt_rect.y = y
        tela.blit(txt_surf, txt_rect)

def executar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    
    # Fontes
    fonte_titulo = pygame.font.SysFont("Arial", 48, bold=True)
    fonte_pergunta = pygame.font.SysFont("Arial", 28, bold=True)
    fonte_texto = pygame.font.SysFont("Arial", 22)
    fonte_ui = pygame.font.SysFont("Arial", 18, bold=True)

    # Estado Inicial
    estado_atual = MENU
    indice_pergunta = 0
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    feedback_msg = ""
    feedback_cor = BRANCO
    feedback_explicacao = ""
    
    rodando = True
    while rodando:
        tempo_delta = relogio.tick(FPS)
        eventos = pygame.event.get()
        
        for evento in eventos:
            if evento.type == pygame.QUIT:
                rodando = False
            
            if estado_atual == MENU:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                        estado_atual = JOGANDO
                        indice_pergunta = 0
                        pontos = 0
                        vidas = 3
            
            elif estado_atual == JOGANDO:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # Verificar clique nas alternativas
                    for i in range(3):
                        rect = pygame.Rect(50, 250 + i * 80, 700, 60)
                        if rect.collidepoint(pos):
                            pergunta = PERGUNTAS[indice_pergunta]
                            acertou = verificar_resposta(pergunta, i)
                            
                            feedback_explicacao = pergunta["explicacao"]
                            if acertou:
                                feedback_msg = "CORRETO!"
                                feedback_cor = VERDE_ACERTO
                            else:
                                feedback_msg = "INCORRETO!"
                                feedback_cor = VERMELHO_ERRO
                            
                            pontos = atualizar_pontuacao(pontos, acertou, pergunta["dificuldade"])
                            vidas = atualizar_vidas(vidas, acertou)
                            estado_atual = FEEDBACK
            
            elif estado_atual == FEEDBACK:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                        if esta_morto(vidas) or jogo_concluido(indice_pergunta + 1, len(PERGUNTAS)):
                            estado_atual = FIM
                            if pontos > recorde:
                                recorde = pontos
                                salvar_recorde(CAMINHO_RECORDE, recorde)
                        else:
                            indice_pergunta += 1
                            estado_atual = JOGANDO
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    # Também avançar com clique
                    if esta_morto(vidas) or jogo_concluido(indice_pergunta + 1, len(PERGUNTAS)):
                        estado_atual = FIM
                        if pontos > recorde:
                            recorde = pontos
                            salvar_recorde(CAMINHO_RECORDE, recorde)
                    else:
                        indice_pergunta += 1
                        estado_atual = JOGANDO

            elif estado_atual == FIM:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                        estado_atual = MENU
                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False

        # Renderização
        tela.fill(CINZA_ESCURO)
        
        if estado_atual == MENU:
            desenhar_texto(tela, "MIND", fonte_titulo, AZUL_IA, LARGURA_TELA//2, 120, centralizado=True)
            desenhar_texto(tela, "O Desafio da Inteligência Artificial", fonte_pergunta, BRANCO, LARGURA_TELA//2, 190, centralizado=True)
            
            # Tema do Investigador
            pygame.draw.rect(tela, AZUL_IA, (LARGURA_TELA//2 - 100, 240, 200, 40), border_radius=5)
            desenhar_texto(tela, "MODO INVESTIGADOR", fonte_ui, BRANCO, LARGURA_TELA//2, 250, centralizado=True)
            
            desenhar_texto(tela, "Analise as situações e tome as decisões corretas", fonte_texto, CINZA_CLARO, LARGURA_TELA//2, 310, centralizado=True)
            desenhar_texto(tela, "para garantir o uso ético e seguro da tecnologia.", fonte_texto, CINZA_CLARO, LARGURA_TELA//2, 340, centralizado=True)
            
            desenhar_texto(tela, "Pressione ESPAÇO para começar", fonte_pergunta, AMARELO_DESTAQUE, LARGURA_TELA//2, 450, centralizado=True)
            desenhar_texto(tela, f"Recorde: {recorde}", fonte_ui, BRANCO, LARGURA_TELA//2, 520, centralizado=True)

        elif estado_atual == JOGANDO:
            pergunta = PERGUNTAS[indice_pergunta]
            
            # Header UI
            pygame.draw.rect(tela, AZUL_IA, (0, 0, LARGURA_TELA, 60))
            desenhar_texto(tela, f"Pergunta {indice_pergunta + 1}/{len(PERGUNTAS)}", fonte_ui, BRANCO, 20, 20)
            desenhar_texto(tela, f"Vidas: {vidas}", fonte_ui, VERMELHO_ERRO if vidas == 1 else BRANCO, 350, 20)
            desenhar_texto(tela, f"Pontos: {pontos}", fonte_ui, AMARELO_DESTAQUE, 650, 20)
            
            # Pergunta
            desenhar_texto(tela, pergunta["enunciado"], fonte_pergunta, BRANCO, 50, 100, largura_max=700)
            desenhar_texto(tela, f"Categoria: {pergunta['categoria']} | Dificuldade: {pergunta['dificuldade']}", fonte_ui, CINZA_CLARO, 50, 210)

            # Alternativas
            mouse_pos = pygame.mouse.get_pos()
            for i, alt in enumerate(pergunta["alternativas"]):
                rect = pygame.Rect(50, 250 + i * 80, 700, 60)
                cor_btn = AZUL_IA
                if rect.collidepoint(mouse_pos):
                    cor_btn = (0, 153, 255)
                
                pygame.draw.rect(tela, cor_btn, rect, border_radius=10)
                desenhar_texto(tela, f"{i+1}. {alt}", fonte_texto, BRANCO, 70, 265 + i * 80)

        elif estado_atual == FEEDBACK:
            desenhar_texto(tela, feedback_msg, fonte_titulo, feedback_cor, LARGURA_TELA//2, 100, centralizado=True)
            desenhar_texto(tela, "Por que?", fonte_pergunta, BRANCO, 50, 200)
            desenhar_texto(tela, feedback_explicacao, fonte_texto, CINZA_CLARO, 50, 250, largura_max=700)
            
            desenhar_texto(tela, "Pressione ESPAÇO para continuar", fonte_ui, AMARELO_DESTAQUE, LARGURA_TELA//2, 500, centralizado=True)

        elif estado_atual == FIM:
            titulo_fim = "VITÓRIA!" if vidas > 0 else "GAME OVER"
            cor_fim = VERDE_ACERTO if vidas > 0 else VERMELHO_ERRO
            
            desenhar_texto(tela, titulo_fim, fonte_titulo, cor_fim, LARGURA_TELA//2, 150, centralizado=True)
            desenhar_texto(tela, f"Pontuação Final: {pontos}", fonte_pergunta, BRANCO, LARGURA_TELA//2, 250, centralizado=True)
            desenhar_texto(tela, f"Recorde: {recorde}", fonte_ui, AMARELO_DESTAQUE, LARGURA_TELA//2, 300, centralizado=True)
            
            desenhar_texto(tela, "Pressione ESPAÇO para o Menu ou ESC para Sair", fonte_texto, CINZA_CLARO, LARGURA_TELA//2, 450, centralizado=True)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

