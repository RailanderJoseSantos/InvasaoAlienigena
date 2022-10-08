class Settings():
    """Classe para configurações de jogo"""
    def __init__(self):
        """Inicializa confg do jogo"""
        self.screenWidth = 900
        self.escreenHeidth = 600
        self.bgColor = (230,230,230)

        #configurações da nave
        self.shipSpeedFactor = 1.5
        self.shipLimit = 3

        #Configurações dos projeteis
        self.bulletSpeedFactor = 3
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60,60,60)
        #num maximo projeteis
        self.bulletsAllowed = 3

        #configs dos aliens
        self.alienSpeedFactor = 1
        self.fleetDropSpeed = 10

        #fleetDirection = 1 representa direita, -1 a esquerda
        self.fleetDirection = 1


