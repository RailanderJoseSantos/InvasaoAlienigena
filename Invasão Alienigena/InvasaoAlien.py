import sys
import pygame as pg
from settings import Settings
from ship import Ship
def runGame():
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    aiSettings = Settings()
    #setando display para tela
    screen = pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Invasão Alien")
    nave = Ship(screen)

    #laço principal do jogo
    while True:
        #escuta evento de teclado e mouse
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        #redesenha a tela a cada passada pelo laço
        screen.fill(aiSettings.bgColor)
        nave.blitme()
        # deixa tela mais recente visivel
        pg.display.flip()
runGame()