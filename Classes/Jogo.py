from Classes.TelaJogo import TelaJogo

class Jogo():
    def __init__(self):
        self.tela_atual = "TelaJogo"
    
    def inicializa(self):

        if self.tela_atual == "TelaJogo":
            tela=TelaJogo()
            window = tela.inicializa()
            while tela.atualiza_estado():
                tela.desenha(window)
                # # if tela.mudar_tela:
                # #     self.tela_atual = "TelaJogo"
        