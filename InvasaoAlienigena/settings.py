class Settings():
    """Classe para configurações de jogo"""
    def __init__(self):
        """Inicializa confg do jogo"""
        self.screenWidth = 900
        self.escreenHeidth = 600
        self.bgColor = (230,230,230)

        #configuracoes da espaconave
        self.shipLimit = 3

        #Configurações dos projeteis
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60,60,60)
        #num maximo projeteis
        self.bulletsAllowed = 3

        #configs dos aliens
        self.fleetDropSpeed = 10

        #taxa com que a velocidade do game aumenta
        self.speedupScale = 1.1

        # a taxa com que os pontos para cada alien aumentam
        self.scoreScale = 1.5

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        """inicializa as confg que mudam no decorrer do jogo"""
        self.shipSpeedFactor = 1.5
        self.alienSpeedFactor = 1
        self.speed = 1
        self.bulletSpeedFactor = 3
        # fleetDirection = 1 representa direita, -1 a esquerda
        self.fleetDirection = 1
        #pontuação
        self.alienPoints = 50

    def increaseSpeed(self):
        """aumenta config de velocidade"""
        self.shipSpeedFactor = (self.shipSpeedFactor * self.speedupScale)
        self.speed = (self.speed * self.speedupScale)
        self.bulletSpeedFactor = (self.bulletSpeedFactor * self.speedupScale)
        self.alienSpeedFactor = (self.alienSpeedFactor * self.speedupScale)
        self.alienPoints = int(self.alienSpeedFactor  * self.scoreScale)
