import sys
import pygame
from bullets import Bullet
from alien import Alien
from time import  sleep
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


def checkPlayButton(stats, playButton, mouseX, mouseY):
    """inicia novo jogo qnd clicar no play"""
    if playButton.rect.collidepoint(mouseX,mouseY):
        stats.gameActive = True


def checkEvents(aiSettings,screen, stats, playButton, ship, bullets):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(stats, playButton, mouseX, mouseY)


def updateScreen(aiSettings, screen, stats, ship, aliens, bullets, playButton):
    # redesenha a tela a cada passada pelo laço
    screen.fill(aiSettings.bgColor)
    #redesenha todos os projeteis atras na nave e aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.gameActive:
        playButton.drawButton()

    # deixa tela mais recente visivel
    pygame.display.flip()

def updateBullets(aiSettings, screen, ship, aliens, bullets):
    """Atualiza a posicao dos projeteis e se livra dos antigos"""
    bullets.update()
    # tirando da memoria do pc os projeteis que ja foram disparados
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # verifica se algum projetil colidiu, se colidir livra se do projetil e alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #destroi projeteis existente e cria nova frota
        bullets.empty()
        createFeet(aiSettings, screen, ship, aliens)

def fireBullet(aiSettings,screen,ship,bullets):
    # verifica se ja tem o limite de projeteis na tela
    if len(bullets) < aiSettings.bulletsAllowed:
        # cria um novo projetil e o adiciona ao grupo de projeteis
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)

def getNumberRows(aiSettings, shipHeight, alienHeight):
    """Determinar o nmr de linhas com aliens que cabem na tela"""
    availableSpaceY = (aiSettings.escreenHeidth - (3 * alienHeight) - shipHeight)
    numberRow = int(availableSpaceY / (2 *alienHeight))
    return numberRow

def getNumberAliensX(aiSettings, alienWidth):
    """Determina nmr de aliens que cabem em 1 linha"""
    availablbeSpaceX = aiSettings.screenWidth - 2 * alienWidth
    numberAliensX = int(availablbeSpaceX / (2 * alienWidth))
    return numberAliensX

def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
    """Cria 1 alien e o posiciona na linha"""
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

def createFeet(aiSettings, screen, ship, aliens):
    """cria frota completa de aliens"""
    #cria um alien e calcula numero de aliens em uma linha
    #o espacamento entre oas aliens é igual a largura de outro
    alien= Alien(aiSettings, screen )
    numberAliensX = getNumberAliensX(aiSettings, alien.rect.width)
    numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)

    for rowNumber in range(numberRows):
        #Cria linha de aliens
        for alienNumber in range(numberAliensX):
            createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)

def checkFleetEges(aiSettings, aliens):
    """responde apropriadamente se algum alien alcançou borda"""
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break

def updateAliens(aiSettings, stats, screen, ship, aliens, bullets):
    """verufuca se a frota esta em uma das bordas e então atualiza as posicoes de tds os aliens da frota"""
    checkFleetEges(aiSettings, aliens)
    aliens.update()
    #verifica se houve colisao entre alien e nave
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(aiSettings, stats, screen, ship, aliens, bullets)
    #verifica se algum alien atingiu inferior tela
    checkAliensBottom(aiSettings, stats, screen, ship,aliens, bullets)

def  changeFleetDirection(aiSettings, aliens):
    """faz toda frota desces e muda direção"""
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1

def shipHit(aiSettings, stats, screen, ship, aliens, bullets):
    """responde a colisão nave e alien"""
    if stats.shipsLeft > 0:
        # decrementa shipsLeft
        stats.shipsLeft -= 1
        # esvazia lista de aliens e projeteis
        aliens.empty()
        bullets.empty()

        # cria nova frota e centraliza nave
        createFeet(aiSettings, screen, ship, aliens)
        ship.centerShip()

        # faz uma pausa
        sleep(0.5)
    else:
        stats.gameActive = False
def checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets):
    """verifica se alien tocou parte inferior de tela"""
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            #trata colisao
            shipHit(aiSettings, stats, screen, ship, aliens, bullets)

