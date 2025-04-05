import pygame
from constantes import *


class TelaInicial:
    def __init__(self):
        self.tela_atual = "TelaInicial"
        self.texto_1 = FONTE_TEXTO.render("Jogar", True, PRETO)
        self.texto_2 = FONTE_TEXTO.render("IA", True, PRETO)
        self.image = DINO_METEORO
        self.retangulo_1_pos = [LARGURA_TELA//2 - 150, 275]
        self.retangulo_2_pos = [LARGURA_TELA//2 - 150, 375]
        self.retangulo_dimen = [300, 50]


    def inicializa(self):
        pygame.init()

        largura, altura = (LARGURA_TELA, ALTURA_TELA)
        window = pygame.display.set_mode((largura, altura))
 
        return window
    

    def colisao_ponto_retangulo(self, ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h):
        if ponto_x >= rect_x and ponto_x <= rect_x+rect_w and ponto_y>=rect_y and ponto_y<=rect_y+rect_h:
            return True
        return False


    def desenha(self, window):
        window.fill(AZUL_CLARO)

        window.blit(self.image, (LARGURA_TELA//2 - self.image.get_width()//2, 50))

        pygame.draw.rect(window, CINZA, pygame.Rect(self.retangulo_1_pos, self.retangulo_dimen))
        pygame.draw.rect(window, CINZA, pygame.Rect(self.retangulo_2_pos, self.retangulo_dimen))

        window.blit(self.texto_1, (LARGURA_TELA//2 - len("Jogar")*12, 300 - 12))
        window.blit(self.texto_2, (LARGURA_TELA//2 - len("IA")*12, 400 - 12))
        
        pygame.display.update()


    def atualiza_estado(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if self.colisao_ponto_retangulo(evento.pos[0], evento.pos[1], self.retangulo_1_pos[0], self.retangulo_1_pos[1], self.retangulo_dimen[0], self.retangulo_dimen[1]):
                        self.tela_atual = "TelaJogo"
                    if self.colisao_ponto_retangulo(evento.pos[0], evento.pos[1], self.retangulo_2_pos[0], self.retangulo_2_pos[1], self.retangulo_dimen[0], self.retangulo_dimen[1]):
                        self.tela_atual = "TelaJogoIA"
        return True