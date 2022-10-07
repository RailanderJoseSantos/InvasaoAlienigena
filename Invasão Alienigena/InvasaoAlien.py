import pygame as pg
from settings import Settings
from ship import Ship
from alien import Alien
import gameFunctions as gf
from pygame.sprite import  Group
def runGame():
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    aiSettings = Settings()
    #setando display para tela
    screen = pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Aniquila comunismo")
    nave = Ship(screen, aiSettings)

    #cria um grupo onde serao armazenados os projeteis
    bullets = Group()
    #criando um grupode de alienigena
    aliens = Group()

    gf.createFeet(aiSettings, screen, aliens)
    #laço principal do jogo
    while True:
        gf.checkEvents(aiSettings, screen, nave, bullets)
        nave.update()
        gf.updateBullets(bullets)
        gf.updateScreen(aiSettings, screen, nave, aliens, bullets)
        #print(len(bullets))
runGame()