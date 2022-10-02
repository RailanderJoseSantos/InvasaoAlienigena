import sys
import pygame as pg
from settings import Settings
def runGame():
    aiSettings = Settings()
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    #setando display para tela  
    screen =  pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Invasão Alien")

    #laço principal do jogo
    while True:
        #escuta evento de teclado e mouse
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        #redesenha a tela a cada passada pelo laço
        screen.fill(aiSettings.bgColor)

        # deixa tela mais recente visivel
        pg.display.flip()
runGame()