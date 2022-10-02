import pygame
#nave
class Ship():
    def __init__(self, screen):
        """ Inicializa a espaçonave e define sua posicao inicial"""
        self.screen = screen

        #carrega imagem da nave e obtem seu rect
        self.image = pygame.image.load('image/ship.bmp')