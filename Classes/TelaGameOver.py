import pygame
from constantes import *


class TelaGameOver:
    def __init__(self):
        self.tela_atual = "TelaGameOver"
        self.pontuacao = 0
        self.texto_1 = FONTE_CORACAO.render("GAMEOVER", True, CINZA)
        self.texto_2 = FONTE_CORACAO.render(f"PONTUAÇÃO: {self.pontuacao}", True, CINZA)
        self.image = DINO_METEORO


    def inicializa(self):
        pygame.init()

        largura, altura = (LARGURA_TELA, ALTURA_TELA)
        window = pygame.display.set_mode((largura, altura))
 
        return window


    def desenha(self, window):

        window.fill(AZUL_CLARO)

        window.blit(self.image, (LARGURA_TELA//2 - self.image.get_width()//2, 50))

        window.blit(self.texto_1, (LARGURA_TELA//2 - len("GAMEOVER")*15, 275 - 15))
        window.blit(self.texto_2, (LARGURA_TELA//2 - len(f"Pontuação: {self.pontuacao}")*15, 375 - 15))
        
        pygame.display.update()


    def atualiza_estado(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
        
        self.texto_2 = FONTE_CORACAO.render(f"PONTUAÇÃO: {self.pontuacao}", True, CINZA)

        return True