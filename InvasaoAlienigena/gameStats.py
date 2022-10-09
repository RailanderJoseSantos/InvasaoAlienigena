class GameStats():
    """Armazena dados estatisticos do jogo"""
    def __init__(self, aiSettings):
        """inicializa dados"""
        self.aiSettings = aiSettings
        self.resetStats()
        self.gameActive = True
    def resetStats(self):
        """inicializa dados que podem mudar durante jogo"""
        self.shipsLeft = self.aiSettings.shipLimit