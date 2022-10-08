class GameStats():
    """Armazena dados estatusticos da invasão alien"""
    def __init__(self, aiSettings):
        """inicializa os dados estatisticos"""
        self.aiSettings = aiSettings
        self.resetStats()

    def resetStats(self):
        """inicializa os dados estatisticos que podem mudar durante jogo"""
        self.shipLeft = self.aiSettings.shipLimit