import pygame.font

class Scoreboard():
    """classe para mostrar informacoes de pontuacao"""
    def __init__(self, aiSettings, screen, stats):
        """inicializa atributos de pontuacao"""
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats

        #Configs de fonte para informacao de pontuacao
        self.textColor = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        #prepara imagem das pontuaçoes inicial
        self.prepScore()
        self.prepHighScore()
        self.prepLevel()

    def prepScore(self):
        """transforma a pontuação em uma img renderizada"""
        rounderScore = int(round(self.stats.score, -1))

        scoreStr = "{:,}".format(rounderScore)
        self.scoreImage = self.font.render(scoreStr, True, self.textColor,
                                           self.aiSettings.bgColor)

        #exibe pontuação parte sup direita tela
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def showScore(self):
        """desenha a pontuação e nivel na tela"""
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
    def prepHighScore(self):
        """transforma pontuação maxima em imagem renderizada"""
        highScore = int(round(self.stats.highScore, -1))
        highScoreStr = "{:,}".format(highScore)
        self.highScoreImage = self.font.render(highScoreStr, True, self.textColor, self.aiSettings.bgColor)
        #centraliza pontuação maxima na parte superior da tela
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top
    def prepLevel(self):
        """trasnforma nivel em img renderizada"""
        self.levelImage = self.font.render(str(self.stats.level),True, self.textColor, self.aiSettings.bgColor)

        #oisiciona o nivel abaixo da pontuação
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10