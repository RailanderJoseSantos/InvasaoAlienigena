import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa 1 unico alien"""
    def __init__(self, aiSettings, screen):
        """Inicializa o alien e define sua posicao atual"""
        super(Alien, self).__init__()
        self.screen = screen
        self.aiSettings = aiSettings
        # carrega umagem do alien e define atributo rect
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        #inicia cada novo alien proximo a parte sup esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        """desenha o alien na posicao atual"""
        self.screen.blit(self.image, self.rect)
    def checkEdges(self):
        """retorna true se alien estivar na borda tela"""
        screenRect = self.screen.get_rect()
        #se lado direito do alien encostou lado direito da tela
        if self.rect.right >= screenRect.right:
            return True
        #se alien encostou lado esquerdo da nave
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move o alien para direita e esquerda"""
        self.x += (self.aiSettings.alienSpeedFactor * self.aiSettings.fleetDirection)
        self.rect.x = self.x