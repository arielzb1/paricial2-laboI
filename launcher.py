import pygame, sys
from niveles.nivel_uno import NivelUno
from pygame.locals import *
from gui.GUI_menu import Menu

puntos = 0
ultimos_puntos = 0

W,H = 1800, 800
ESCALA_PANTALLA = (W,H)
FPS = 20
timer = 1 

clock = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(ESCALA_PANTALLA)

interfaz = Menu(PANTALLA, H / 2, 100, 900, 350, 'Gold', 'Magenta', 5, True)
pygame.init()
nivel_actual = NivelUno(PANTALLA)

while True:
    clock.tick(FPS)
    ultimos_puntos = 0
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    PANTALLA.fill('black')
    interfaz.actualizar(eventos)
    #nivel_actual.actualizar(eventos)

    pygame.display.update()