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
        self.y = self.rect.y
        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor