import pygame
from constantes import *
from random import randint

class Dinossauro(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pos_x = POSICAO_X
        self.pos_y = POSICAO_Y
        self.aceleracao_y = ACELERACAO_Y
        self.velocidade_y = VELOCIDADE_Y_PULO
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.image = DINOSSAURO_CORRENDO[1]
        self.mask = MASKS_DINOSSAURO_CORRENDO[1]
        self.t0 = 0
        self.pulo_ativo = False
    

    def pular(self):

        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1-self.t0)/1000

        if self.t0 >= 0:
            self.velocidade_y += self.aceleracao_y*self.dt
            if self.pos_y <= POSICAO_Y:
                self.pos_y += self.velocidade_y*self.dt
            else:
                self.pos_y = POSICAO_Y
                self.pulo_ativo = False

        self.t0 = self.t1
    

    def draw(self, window):

        if self.pulo_ativo:
            self.image = DINOSSAURO_PULANDO 
            self.rect = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
            window.blit(self.image, (self.rect.x, self.rect.y))
            pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)

        else:
            self.animar_corrida()

            self.rect = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
            window.blit(self.image, (self.rect.x, self.rect.y))
            pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)

    
    def animar_corrida(self):

        self.t2 = pygame.time.get_ticks()

        if self.t2 % 1000 >= 500:
            self.image = DINOSSAURO_CORRENDO[0]
            self.mask = MASKS_DINOSSAURO_CORRENDO[0]
        else:
            self.image = DINOSSAURO_CORRENDO[1]
            self.mask = MASKS_DINOSSAURO_CORRENDO[1]


    


        


