import sys
import pygame
from bullets import Bullet
def checkKeyDowmEvents(event, aiSettings, screen, ship, bullets):
    """Responde a pressionamento das teclas"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings,screen,ship,bullets)

def checkKeyUpEvents(event, ship):
    """Responde ao soltar teclas"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
def checkEvents(aiSettings,screen, ship, bullets):
    """ESCUTA EVENTOS DO TECLADO E MOUSE"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #QUANDO PRESSIONAR SETA DIREITA OU ESQUERDA , MOVE A NAVE
        elif event.type == pygame.KEYDOWN:
            checkKeyDowmEvents(event, aiSettings ,screen, ship, bullets)
            #QUANDO SOLTAR SETA DIREITA OU ESQUERDA , PARA A NAVE
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)


def updateScreen(aiSettings, screen, ship, bullets):
    # redesenha a tela a cada passada pelo laço
    screen.fill(aiSettings.bgColor)
    #redesenha todos os projeteis atras na nave e aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    # deixa tela mais recente visivel
    pygame.display.flip()

def updateBullets(bullets):
    """Atualiza a posicao dos projeteis e se livra dos antigos"""
    bullets.update()
    # tirando da memoria do pc os projeteis que ja foram disparados
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fireBullet(aiSettings,screen,ship,bullets):
    # verifica se ja tem o limite de projeteis na tela
    if len(bullets) < aiSettings.bulletsAllowed:
        # cria um novo projetil e o adiciona ao grupo de projeteis
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)