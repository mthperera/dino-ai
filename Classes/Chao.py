from constantes import *


class Chao():
    
    def __init__(self):
        self.image = CHAO
        self.t0 = 0
        self.velocidade_x = VELOCIDADE_CHAO
        self.pos_y = POSICAO_Y - 8 + DINOSSAURO_PULANDO.get_width()
        self.pos_x = 0
        self.color = (255, 255, 255)
        self.pontuacao = 0


    def movimentar(self):
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1-self.t0)/1000

        if self.t0 >= 0:
            if self.pos_x >= - self.image.get_width() + LARGURA_TELA:
                self.pos_x += self.velocidade_x*self.dt
            else:
                self.pos_x = 0

        self.t0 = self.t1

        self.pontuacao = self.t1 // 1000


    def desenhar(self, window):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        window.blit(self.image, (self.rect.x, self.rect.y))

        
        

