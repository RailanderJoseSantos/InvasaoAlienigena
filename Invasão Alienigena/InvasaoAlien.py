import sys
import pygame as pg
def runGame():
    """Inicializa o jogo e cria um objeto para tela"""
    pg.init()
    #setando display para tela
    sreen =  pg.display.set_mode((1000,600))
    pg.display.set_caption("Invasão Alien")

    #laço principal do jogo
    while True:
        #escuta evento de teclado e mouse
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        # deixa tela mais recente visivel
        pg.display.flip()
runGame()