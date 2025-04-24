import neat
import os
from Classes.TelaInicial import TelaInicial
from Classes.TelaJogo import TelaJogo
from Classes.TelaJogoIA import TelaJogoIA
from Classes.TelaGameOverIA import TelaGameOverIA

def rodar(caminho_config):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                caminho_config)

    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())

    return populacao, config



class Jogo():
    def __init__(self):
        self.tela_atual = "TelaInicial"
        self.caminho = os.path.dirname(__file__)
        self.caminho_config = os.path.join('config.txt')
        self.geracao_atual = -1
        self.geracao_max = 20
        self.fitness_max = 100
    
    
    def avaliar_genomas(self, genomas, config):
        self.tela_jogo_ia = TelaJogoIA()
        self.geracao_atual += 1
        self.tela_jogo_ia.geracao = self.geracao_atual
        self.tela_jogo_ia.geracao_max = self.geracao_max
        self.tela_jogo_ia.fitness_max = self.fitness_max
        self.tela_jogo_ia.inicializa(genomas, config)

        while self.tela_jogo_ia.atualiza_estado():
            self.tela_jogo_ia.desenha(self.tela_jogo_ia.window)
            if self.tela_jogo_ia.tela_atual != "TelaJogoIA":
                self.tela_atual = self.tela_jogo_ia.tela_atual
                break


    def inicializa(self):

        if self.tela_atual == "TelaInicial":
            tela_inicial = TelaInicial()
            window = tela_inicial.inicializa()
            while tela_inicial.atualiza_estado():
                tela_inicial.desenha(window)
                if tela_inicial.tela_atual != "TelaInicial":
                    self.tela_atual = tela_inicial.tela_atual
                    break

        if self.tela_atual == "TelaJogo":
            tela_jogo = TelaJogo()
            window = tela_jogo.inicializa()
            while tela_jogo.atualiza_estado():
                tela_jogo.desenha(window)
                if tela_jogo.tela_atual != "TelaJogo":
                    self.tela_atual = tela_jogo.tela_atual
                    break
        
        if self.tela_atual == "TelaGameOver":
            tela_game_over = tela_jogo.tela_game_over
            window = tela_game_over.inicializa()
            while tela_game_over.atualiza_estado():
                tela_game_over.desenha(window)

        if self.tela_atual == "TelaJogoIA":
            populacao, config = rodar(self.caminho_config)
            populacao.run(self.avaliar_genomas, self.geracao_max)
        
        if self.tela_atual == "TelaGameOverIA":
            tela_game_over_ia = TelaGameOverIA(melhor_genoma=self.tela_jogo_ia.melhor_genoma)
            window = tela_game_over_ia.inicializa()
            while tela_game_over_ia.atualiza_estado():
                tela_game_over_ia.desenha(window)
        