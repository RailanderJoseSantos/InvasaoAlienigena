import pygame.font

class Scoreboard():
    """classe para mostrar informacoes de pontuacao"""
    def __init__(self, aiSettings, screen, stats):
        """inicializa atributos de pontuacao"""
        self.screen = screen
        self.screeRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats

        #Configs de fonte para informacao de pontuacao
        self.textColor = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        #prepara imagem da pontuaçao inicial
        self.prepScore()

    def prepScore(self):
        """transforma a pontuação em uma img renderizada"""
        scoreStr = str(self.stats.score)
        self.scoreImage = self.font.render(scoreStr, True, self.textColor,
                                           self.aiSettings.bgColor)

        #exibe pontuação parte sup direita tela
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screeRect.right - 20
        self.scoreRect.top = 20

    def showScore(self):
        """desenha a pontuação na tela"""
        self.screen.blit(self.scoreImage, self.scoreRect)