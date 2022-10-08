import pygame as pg
from settings import Settings
from ship import Ship
from alien import Alien
import gameFunctions as gf
from pygame.sprite import Group
from gameStats import GameStats
def runGame():
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    aiSettings = Settings()
    #setando display para tela
    screen = pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Invasão Alienígena")

    #cria uma instanacia para armazenar dados estatisticos
    stats = GameStats(aiSettings)

    nave = Ship(screen, aiSettings)

    #cria um grupo onde serao armazenados os projeteis
    bullets = Group()
    #criando um grupode de alienigena
    aliens = Group()

    gf.createFeet(aiSettings, screen, nave, aliens)
    #laço principal do jogo
    while True :
        gf.checkEvents(aiSettings, screen, nave, bullets)
        nave.update()
        gf.updateBullets(aiSettings, screen, nave, aliens, bullets)
        gf.updateAliens(aiSettings, stats, screen,  nave, aliens, bullets)
        gf.updateScreen(aiSettings, screen, nave, aliens, bullets)
        #print(len(bullets))
runGame()