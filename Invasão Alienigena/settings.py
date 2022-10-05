class Settings():
    """Classe para configurações de jogo"""
    def __init__(self):
        """Inicializa confg do jogo"""
        self.screenWidth = 900
        self.escreenHeidth = 600
        self.bgColor = (230,230,230)
        self.speed = 1

        #Configurações dos projeteis
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60,60,60)
        #num maximo projeteis
        self.bulletsAllowed = 3
