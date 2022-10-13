class GameStats():
    """Armazena dados estatisticos do jogo"""
    def __init__(self, aiSettings):
        """inicializa dados"""
        self.aiSettings = aiSettings
        self.resetStats()
        self.gameActive = False
        # a pontuação maxima jamais devera ser reinciada
        self.highScore = 0
    def resetStats(self):
        """inicializa dados que podem mudar durante jogo"""
        self.shipsLeft = self.aiSettings.shipLimit
        self.score = 0