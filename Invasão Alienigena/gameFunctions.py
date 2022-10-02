import sys
import pygame
def checkEvents(ship):
    """ESCUTA EVENTOS DO TECLADO E MOUSE"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #QUANDO PRESSIONAR SETA DIREITA
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #MOVE PARA DIREITA
                ship.movingRight = True
                #QUANDO SOLTAR
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            #QUANDO PRESSIONAR SETA ESQUERDA
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #MOVE PARA DIREITA
                ship.movingLeft = True
                #QUANDO SOLTAR
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.movingLeft = False


def upgradeScreen(aiSettings, screen, ship):
    # redesenha a tela a cada passada pelo laço
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    # deixa tela mais recente visivel
    pygame.display.flip()