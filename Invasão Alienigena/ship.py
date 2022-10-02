import pygame
#nave
class Ship():
    def __init__(self, screen):
        """ Inicializa a espaçonave e define sua posicao inicial"""
        self.screen = screen

        #carrega imagem da nave e obtem seu rect
        self.image = pygame.image.load('image/ship.bmp')
        # a imagem é inserida num retangulo, assim o pygame sabera omde
        # inicia a imagem da nave
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova espaconave em sua posicao atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Desenha a espaconave em sua posicao atual"""
        self.screen.blit(self.image, self.rect)