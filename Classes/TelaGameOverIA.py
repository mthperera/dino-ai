import pygame
import pickle
from constantes import *


class TelaGameOverIA:
    def __init__(self, melhor_genoma=None):
        self.tela_atual = "TelaGameOver"
        self.genoma_final = melhor_genoma
        self.texto = FONTE_CORACAO.render("SALVAR GENES", True, PRETO)
        self.image = DINO_METEORO
        self.retangulo_pos = [LARGURA_TELA//2 - 200, 250]
        self.retangulo_dimen = [400, 50]


    def inicializa(self):
        pygame.init()

        largura, altura = (LARGURA_TELA, ALTURA_TELA)
        window = pygame.display.set_mode((largura, altura))
 
        return window
    

    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if ponto_x >= rect_x and ponto_x <= rect_x+rect_w and ponto_y>=rect_y and ponto_y<=rect_y+rect_h:
            return True
        return False


    def salvar_melhor_genoma(self, genoma):
        with open("melhor_genoma.pkl", "wb") as f:
            pickle.dump(genoma, f)


    def desenha(self, window):

        window.fill(AZUL_CLARO)

        window.blit(self.image, (LARGURA_TELA//2 - self.image.get_width()//2, 50))

        pygame.draw.rect(window, CINZA, pygame.Rect(self.retangulo_pos, self.retangulo_dimen))

        window.blit(self.texto, (LARGURA_TELA//2 - len("SALVAR GENES")*15, 275 - 15))
        
        pygame.display.update()


    def atualiza_estado(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if self.colisao_ponto_retangulo(evento.pos[0], evento.pos[1], self.retangulo_pos[0], self.retangulo_pos[1], self.retangulo_dimen[0], self.retangulo_dimen[1]):
                        self.salvar_melhor_genoma(self.genoma_final)

        return True