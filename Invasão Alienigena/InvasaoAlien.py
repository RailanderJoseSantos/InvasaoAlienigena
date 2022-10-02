import pygame as pg
from settings import Settings
from ship import Ship
import gameFunctions as gf
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
        gf.checkEvents(nave)
        nave.update()
        gf.upgradeScreen(aiSettings, screen, nave)
runGame()