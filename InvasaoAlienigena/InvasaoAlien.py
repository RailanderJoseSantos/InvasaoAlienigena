import pygame as pg
from settings import Settings
from ship import Ship
from alien import Alien
from gameStats import  GameStats
import gameFunctions as gf
from pygame.sprite import  Group
from button import Button
from scoreboard import Scoreboard
def runGame():
    "Inicializa o jogo e cria um objeto para tela"
    pg.init()
    aiSettings = Settings()
    #setando display para tela
    screen = pg.display.set_mode((aiSettings.screenWidth,aiSettings.escreenHeidth))
    pg.display.set_caption("Invasão Alienígena")
    #cria o botão play
    playButton = Button(aiSettings, screen, "Play")
    #cria instancia para armazenar dados do game e cria painel  de pontuacao
    stats = GameStats(aiSettings)
    sb = Scoreboard(aiSettings, screen, stats)
    nave = Ship(screen, aiSettings)

    #cria um grupo onde serao armazenados os projeteis
    bullets = Group()
    #criando um grupode de alienigena
    aliens = Group()

    gf.createFeet(aiSettings, screen, nave, aliens)
    #laço principal do jogo
    while True:
        gf.checkEvents(aiSettings,screen, stats,sb, playButton, nave, aliens, bullets)
        if stats.gameActive:
            nave.update()
            gf.updateBullets(aiSettings, screen,stats, sb, nave, aliens, bullets)
            gf.updateAliens(aiSettings, stats, screen, nave, aliens, bullets)
        gf.updateScreen(aiSettings, screen, stats, sb, nave, aliens, bullets, playButton)
        #print(len(bullets))
runGame()