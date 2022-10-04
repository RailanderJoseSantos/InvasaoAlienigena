import sys
import pygame
from bullets import Bullet
def checkKeyDowmEvents(event, ship):
    """Responde a pressionamento das teclas"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
def checkKeyUpEvents(event, ship):
    """Responde ao soltar teclas"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
def checkEvents(event, aiSettings, screen, ship, bullet):
    """ESCUTA EVENTOS DO TECLADO E MOUSE"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #QUANDO PRESSIONAR SETA DIREITA OU ESQUERDA , MOVE A NAVE
        elif event.type == pygame.KEYDOWN:
            checkKeyDowmEvents(event, ship)
            #QUANDO SOLTAR SETA DIREITA OU ESQUERDA , PARA A NAVE
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)


def upgradeScreen(aiSettings, screen, ship):
    # redesenha a tela a cada passada pelo laço
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    # deixa tela mais recente visivel
    pygame.display.flip()