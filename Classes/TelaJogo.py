import pygame
import random
from constantes import *
from Classes.Dinossauro import Dinossauro
from Classes.Chao import Chao
from Classes.Cactus import *


class TelaJogo:
    def __init__(self):
        self.dinossauro = Dinossauro()
        self.grupo_dinossauro = pygame.sprite.Group()
        self.grupo_dinossauro.add(self.dinossauro)
        self.grupo_cactus = pygame.sprite.Group()
        self.chao = Chao()
        self.texto_coracao = FONTE_CORACAO.render(CORACAO, True, VERMELHO)
        self.texto_pontuacao = FONTE_PONTUACAO.render(f"Pontuação: {self.chao.pontuacao}", True, PRETO)
        self.t0 = 0
        self.delta_t = 6000


    def inicializa(self):
        pygame.init()

        largura, altura = (LARGURA_TELA, ALTURA_TELA)
        window = pygame.display.set_mode((largura, altura))
 
        return window


    def cria_cactus(self):

        tamanho = random.choice(["Pequeno", "Grande"])
        quantidade = random.randint(1, 3)

        if tamanho == "Pequeno":
            cactus_pequeno = CactusPequeno(quantidade)
            self.grupo_cactus.add(cactus_pequeno)
        else:
            cactus_grande = CactusGrande(quantidade)
            self.grupo_cactus.add(cactus_grande)
    

    def verifica_colisao(self, entidade_1, entidade_2):
        
        delta_x = entidade_2.pos_x - entidade_1.pos_x
        delta_y = entidade_2.pos_y - entidade_1.pos_y

        if entidade_2.mask.overlap(entidade_1.mask, (delta_x, delta_y)) is None:
            return False
        
        return True


    def desenha(self, window):
        window.fill(BRANCO)
        window.blit(self.texto_coracao, (10, 10))
        window.blit(self.texto_pontuacao, (LARGURA_TELA - 275, 10))

        for dinossauro in self.grupo_dinossauro:
            dinossauro.draw(window)
        
        self.chao.desenhar(window)

        for cactus in self.grupo_cactus:
            window.blit(cactus.image, (cactus.pos_x, cactus.pos_y))
        
        for dinossauro in self.grupo_dinossauro:
            for cactus in self.grupo_cactus:
                pygame.draw.line(window, dinossauro.color, (dinossauro.pos_x + 54, dinossauro.pos_y + 12), cactus.centro, 2)
        
        pygame.display.update()


    def atualiza_estado(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not self.dinossauro.pulo_ativo:
                    self.dinossauro.pulo_ativo = True
                    self.dinossauro.velocidade_y = VELOCIDADE_Y_PULO
        
        self.t1 = pygame.time.get_ticks()
        self.divisor = self.t1//self.delta_t
        if self.divisor > 0:
            self.cria_cactus()
            self.delta_t += 6000
        
        
        for cactus in self.grupo_cactus:
            cactus.movimentar()
            if cactus.pos_x < -150:
                cactus.kill()
            for dinossauro in self.grupo_dinossauro:
                if self.verifica_colisao(cactus, dinossauro):
                    self.dinossauro.kill()
        
        if len(self.grupo_dinossauro) == 0:
            return False

        for dinossauro in self.grupo_dinossauro:
            if dinossauro.pulo_ativo:
                dinossauro.pular()
    
        self.chao.movimentar()
        
        self.texto_pontuacao = FONTE_PONTUACAO.render(f"Pontuação: {self.chao.pontuacao}", True, PRETO)

        return True
