import pygame
from config import *


class Suelo:
    def __init__(self,pantalla,mi_personaje, left:float, top:float, width:float, height:float):
        self.piso = pygame.Rect(left, top, width, height)
        self.piso.top = mi_personaje.bottom
        self.lados = obtener_rectangulos(self.piso)

