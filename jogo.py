from Classes.Jogo import Jogo
import pygame

if __name__ == "__main__":
    jogo=Jogo() 
    jogo.inicializa()

pygame.quit()


# Arrumar para forçar o pygameticks a só contar o tempo quando vc clica no "Jogar" ou no "IA"
# Caso isso não seja feito, se demorar para clicar no botão, o jogo irá bugar, pois o t0 será muito diferente de 0.
# Além disso, alguns objetos como o chão só são gerados quando a TelaJogo ou a TelaJogoIA são iniciadas,
# deixando o chão bugado.