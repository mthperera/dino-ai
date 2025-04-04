import neat
import os
from Classes.TelaJogo import TelaJogo
from Classes.TelaJogoIA import TelaJogoIA

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
        self.tela_atual = "TelaJogoIA"
        self.caminho = os.path.dirname(__file__)
        self.caminho_config = os.path.join('config.txt')
    
    def avaliar_genomas(self, genomas, config):
        tela = TelaJogoIA()
        tela.inicializa(genomas, config)

        while tela.atualiza_estado():
            tela.desenha(tela.window)


    
    def inicializa(self):


        if self.tela_atual == "TelaJogo":
            tela=TelaJogo()
            window = tela.inicializa()
            while tela.atualiza_estado():
                tela.desenha(window)
                # # if tela.mudar_tela:
                # #     self.tela_atual = "TelaJogo"

        if self.tela_atual == "TelaJogoIA":
            populacao, config = rodar(self.caminho_config)
            populacao.run(self.avaliar_genomas, 10)
        