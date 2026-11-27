# ==============================================================================
# ARQUIVO: src/sprites.py
# O QUE FAZ: Função utilitária para manipulação de assets gráficos em formato BMP.
#            Carrega spritesheets, extrai recortes específicos e aplica transparência
#            baseada em cor (colorkey) e redimensionamento.
# ESTÁ LINCADO COM:
#   - assets/imagens/spritesheet.bmp (fonte do gráfico)
# ==============================================================================

# Importa o Pygame para carregar imagens, recortar superfícies e redimensionar sprites.
import pygame


def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""
    # 1. Carrega a folha inteira de sprites (BMP) e usa .convert() para otimizar o desenho na tela.
    sheet = pygame.image.load(local_arquivo).convert()

    # 2. Cria uma superfície em branco do tamanho exato (largura x altura) do recorte desejado.
    image = pygame.Surface((width, height))

    # 3. Copia para 'image' apenas a região da spritesheet que começa em (x, y) com tamanho (width, height).
    image.blit(sheet, (0, 0), (x, y, width, height))

    # 4. Lê a cor do pixel no canto superior esquerdo (0, 0) para identificar a cor de fundo do BMP.
    cor_do_fundo = image.get_at((0, 0))

    # Define essa cor como transparente (colorkey) para que o fundo não apareça ao desenhar o sprite.
    image.set_colorkey(cor_do_fundo)

    # 5. Se a escala for diferente de 1, redimensiona proporcionalmente a largura e a altura do sprite.
    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))

    # Devolve o sprite recortado, com fundo transparente e pronto para uso.
    return image
