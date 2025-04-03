import pygame
import os

# Propriedade dos tamanhos das telas:
LARGURA_TELA = 1280/2
ALTURA_TELA = 960/2

# Carregando as imagens:
CACTUS_PEQUENO = [
    pygame.image.load(os.path.join("Assets\Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("Assets\Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("Assets\Cactus", "SmallCactus3.png")),
]

CACTUS_GRANDE = [
    pygame.image.load(os.path.join("Assets\Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("Assets\Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("Assets\Cactus", "LargeCactus3.png")),
]

DINOSSAURO_CORRENDO = [
    pygame.image.load(os.path.join("Assets\Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("Assets\Dino", "DinoRun2.png")),
]

DINOSSAURO_PULANDO = pygame.image.load(os.path.join("Assets\Dino", "DinoJump.png"))

CHAO = pygame.image.load(os.path.join("Assets\Outro", "Track.png"))

# As masks das imagens:

MASKS_CACTUS_PEQUENO = [
    pygame.mask.from_surface(CACTUS_PEQUENO[0]),
    pygame.mask.from_surface(CACTUS_PEQUENO[1]),
    pygame.mask.from_surface(CACTUS_PEQUENO[2]),
]

MASKS_CACTUS_GRANDE = [
    pygame.mask.from_surface(CACTUS_GRANDE[0]),
    pygame.mask.from_surface(CACTUS_GRANDE[1]),
    pygame.mask.from_surface(CACTUS_GRANDE[2]),
]

MASKS_DINOSSAURO_CORRENDO = [
    pygame.mask.from_surface(DINOSSAURO_CORRENDO[0]),
    pygame.mask.from_surface(DINOSSAURO_CORRENDO[1]),
]

MASKS_DINOSSAURO_PULANDO = pygame.mask.from_surface(DINOSSAURO_PULANDO)

# Fonte dos textos
pygame.font.init()
FONTE_CORACAO = pygame.font.Font("assets/font/PressStart2P.ttf", 30)
FONTE_PONTUACAO = pygame.font.Font("assets/font/PressStart2P.ttf", 18)

# Propriedades iniciais do Dinossauro:
POSICAO_X = 30
POSICAO_Y = ALTURA_TELA // 2
VELOCIDADE_Y_PULO = - 400
ACELERACAO_Y = 550

# Propriedades do Chão:
VELOCIDADE_CHAO = - 300

# Cores:
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Caracteres:
CORACAO = chr(9829)
