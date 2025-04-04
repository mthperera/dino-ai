import pygame
import random
import neat
from constantes import *
from Classes.Dinossauro import Dinossauro
from Classes.Chao import *
from Classes.Cactus import *


class TelaJogoIA:
    def __init__(self):
        self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.geracao = 0
        self.dinossauro = Dinossauro()
        self.grupo_dinossauro = pygame.sprite.Group()
        self.grupo_cactus = pygame.sprite.Group()
        self.lista_cactus = list()
        self.chao_1 = Chao_1()
        self.chao_2 = Chao_2()
        self.texto_coracao = FONTE_CORACAO.render(CORACAO, True, VERMELHO)
        self.texto_pontuacao = FONTE_PONTUACAO.render(f"Pontuação: {self.chao_1.pontuacao}", True, PRETO)
        self.texto_geracao = FONTE_PONTUACAO.render(f"Geracao: {self.geracao}", True, PRETO)
        self.t0 = 0
        self.delta_t = 5000
        self.lista_dinossauros = list()
        self.indices_para_remover = list()
        self.lista_genomas = list()
        self.redes = list()


    def inicializa(self, genomas, config):
        pygame.init()

        self.geracao += 1

        self.cria_dinossauros(genomas, config)

        return


    def cria_cactus(self):

        tamanho = random.choice(["Pequeno", "Grande"])
        quantidade = random.randint(1, 3)

        if tamanho == "Pequeno":
            cactus_pequeno = CactusPequeno(quantidade)
            self.grupo_cactus.add(cactus_pequeno)
            self.lista_cactus.append(cactus_pequeno)
        else:
            cactus_grande = CactusGrande(quantidade)
            self.grupo_cactus.add(cactus_grande)
            self.lista_cactus.append(cactus_grande)
    

    def cria_dinossauros(self, genomas, config):
        
        for _ , genoma in genomas:

            genoma.fitness = 0
            self.lista_genomas.append(genoma)

            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            self.redes.append(rede)

            dinossauro = Dinossauro()
            self.grupo_dinossauro.add(dinossauro)
            self.lista_dinossauros.append(dinossauro)
    

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
        
        self.chao_1.desenhar(window)
        self.chao_2.desenhar(window)

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
        
        self.t1 = pygame.time.get_ticks()
        self.divisor = self.t1//self.delta_t
        if self.divisor > 0 and len(self.lista_cactus) == 0:
            self.cria_cactus()
            self.delta_t += 5000
        
        
        for cactus in self.grupo_cactus:
            cactus.movimentar()
            if cactus.pos_x < -150:
                cactus.kill()
                self.lista_cactus.remove(cactus)
            for i, dinossauro in enumerate(self.lista_dinossauros):
                if self.verifica_colisao(cactus, dinossauro):
                    dinossauro.kill()
                    self.lista_genomas[i].fitness += (-1 + self.chao_1.pontuacao / 10)
                    self.indices_para_remover.append(i)
        
        for indice in sorted(self.indices_para_remover, reverse=True):
            if indice < len(self.lista_dinossauros):
                self.lista_dinossauros.pop(indice)
                self.lista_genomas.pop(indice)
                self.redes.pop(indice)

        self.indices_para_remover = list()

        
        if len(self.lista_dinossauros) == 0:
            return False

        for i, dinossauro in enumerate(self.lista_dinossauros):

            distancia_cactus_1 = self.lista_cactus[0].pos_x - dinossauro.pos_x if len(self.lista_cactus) > 0 else 1000
            distancia_cactus_2 = self.lista_cactus[1].pos_x - dinossauro.pos_x if len(self.lista_cactus) > 1 else 2000
            output = self.redes[i].activate((distancia_cactus_1, distancia_cactus_2))

            if output[0] > 0.5 and dinossauro.pos_y == POSICAO_Y and not dinossauro.pulo_ativo:
                dinossauro.pulo_ativo = True
                dinossauro.velocidade_y = VELOCIDADE_Y_PULO
        
        for dinossauro in self.grupo_dinossauro:
            if dinossauro.pulo_ativo:
                dinossauro.pular()

        self.chao_1.movimentar()
        self.chao_2.movimentar()

        self.texto_pontuacao = FONTE_PONTUACAO.render(f"Pontuação: {self.chao_1.pontuacao}", True, PRETO)
        self.texto_geracao = FONTE_PONTUACAO.render(f"Geracao: {self.geracao}", True, PRETO)

        return True
