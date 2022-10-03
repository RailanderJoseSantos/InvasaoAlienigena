import pygame
class Ship():
    def __init__(self, screen, aiSettings):
        """ Inicializa a espaçonave e define sua posicao inicial"""
        self.screen = screen
        self.aiSettings = aiSettings
        #carrega imagem da nave e obtem seu rect
        self.image = pygame.image.load('image/ship.bmp')
        # a imagem é inserida num retangulo, assim o pygame sabera omde
        # inicia a imagem da nave
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova espaconave em sua posicao atual
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.movingRight = False
        self.movingLeft = False
    def update(self):
        """ATUALIZA POSICAO ESPACONAVE DE ACORDO COM FLAG DE MOVIMENTO (move a nave enquanto tecla tiver pressionada"""
        if self.movingRight:
            self.rect.centerx+=self.aiSettings.speed
        if self.movingLeft:
            self.rect.centerx-=self.aiSettings.speed
    def blitme(self):
        """Desenha a espaconave em sua posicao atual"""
        self.screen.blit(self.image, self.rect)