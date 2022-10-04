import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que adminstra projeteis disparados pela nave"""
    def __init__(self, aiSettings, screen, ship):
        """cria um objeto para um projetil na posicao atual da nave"""
        super(Bullet, self).__init__()
        self.screen = screen

        #cria um retangulo para o projetil em(0,0) em seguida define a posic
        # ao correta
        self.rect = pygame.Rect(0,0, aiSettings.bulletWidth, aiSettings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posicao do projetil
        self.y = float(self.rect.y)
        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor
    def update(self):
        """Move o projetil para cima da tela"""
        self.y-= self.speedFactor
        #atualiza a posicao do rect
        self.rect.y = self.y

    def drawBullet(self):
        """Desenha o projetil"""
        pygame.draw.rect(self.screen, self.color, self.rect)