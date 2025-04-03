from constantes import *
from random import randint

class Cactus:
    def __init__(self, numero_cactus):
        self.velocidade_x = VELOCIDADE_CHAO
        self.indice = numero_cactus - 1
        self.pos_x = LARGURA_TELA + randint(10, 30)
        self.t0 = 0

    def movimentar(self):

        self.t1 = pygame.time.get_ticks()
        if self.t0 > 0:
            self.dt = (self.t1-self.t0)/1000
            self.pos_x += self.velocidade_x*self.dt
            self.centro = (self.pos_x + self.image.get_width()//2, self.pos_y + self.image.get_height()//2)

        self.t0 = self.t1

    def draw(self, window):
        window.blit(self.image[self.type], self.rect)


class CactusPequeno(Cactus, pygame.sprite.Sprite):
    def __init__(self, numero_cactus):
        super().__init__(numero_cactus)
        pygame.sprite.Sprite.__init__(self)
        self.pos_y = POSICAO_Y + 30
        self.image = CACTUS_PEQUENO[self.indice]
        self.mask = MASKS_CACTUS_PEQUENO[self.indice]
        self.centro = (self.pos_x + self.image.get_width()//2, self.pos_y + self.image.get_height()//2)


class CactusGrande(Cactus, pygame.sprite.Sprite):
    def __init__(self, numero_cactus):
        super().__init__(numero_cactus)
        pygame.sprite.Sprite.__init__(self)
        self.pos_y = POSICAO_Y + 5
        self.image = CACTUS_GRANDE[self.indice]
        self.mask = MASKS_CACTUS_GRANDE[self.indice]
        self.centro = (self.pos_x + self.image.get_width()//2, self.pos_y + self.image.get_height()//2)