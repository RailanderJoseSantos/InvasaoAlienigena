import pygame as pg
from settings import Settings
from ship import Ship
import gameFunctions as gf
from pygame.sprite import  Group
def runGame():
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    aiSettings = Settings()
    #setando display para tela
    screen = pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Invasão Alien")
    nave = Ship(screen, aiSettings)

    #cria um grupo onde serao armazenados os projeteis
    bullets = Group()

    #laço principal do jogo
    while True:
        gf.checkEvents(aiSettings, screen, nave, bullets)
        nave.update()
        bullets.update()
        gf.updateScreen(aiSettings, screen, nave, bullets)
        # tirando da memora do pc os projeteis que ja foram disparados
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
runGame()