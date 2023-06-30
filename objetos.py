import pygame
from config import *
from archivos import *

class Trash:
    def __init__(self, animaciones):
        self.trash_hace = 'quieto'
        self.imagen = pygame.image.load(r'Los Chinardos\images\objetos\trash\5.png')
        self.imagen = pygame.transform.scale(self.imagen,(60,70))
        rectangulo = self.imagen.get_rect()
        rectangulo.x = 70
        rectangulo.y = ALTO - 115
        self.lados = obtener_rectangulos(rectangulo)
        self.animaciones = animaciones

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados['main'])    
        self.contador_pasos += 1

        def actualizar(self, pantalla):
                pantalla.blit(self.imagen, (70, ALTO - 115))
                match self.trash_hace:
                    case 'quieto':
                        self.animar(pantalla, 'quieto')
                    case 'golpeado_derecha':
                        self.animar(pantalla, 'golpeado_derecha')
                    case 'golpeado_izquierda':
                        self.animar(pantalla, 'golpeado_izquierda')
