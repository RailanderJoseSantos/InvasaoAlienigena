import pygame.font
class Button():
    def __init__(self, aiSettings, screen, msg):
        """inicializa os atributos do botão"""
        self.screen = screen
        self.screenRect = screen.get_rect()
        #define dimensoes e propriedades botão
        self.width, self.height = 200, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #constroi objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center
        #mensagem do botão é preparada apenas 1 vez
        self.preMsg(msg)
    def preMsg(self, msg):
        """transforma msg em imagem renderizada e centraliza texto no botão"""
        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center

    def drawButton(self):
        """desenha 1 botão em branco em seguida a msg"""
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)
