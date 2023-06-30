import pygame
from pygame.locals import *
from archivos import diccionario_enemigo, diccionario_personaje
from config import *
from modo import *
from personajes import Personaje, Enemigo
from suelo import Suelo
from objetos import *

# Personajes
posicion_inicial = (ANCHO / 2, ALTO - 300)
escala = (160, 200)
mi_personaje = Personaje(escala, diccionario_personaje, posicion_inicial, 12)

def generar_enemigos(cantidad):
    enemigos = []
    escala = (160, 200)
    velocidad = 6
    for cant in range(cantidad):
        posicion = obtener_valor_random()
        posicion_inicial = (posicion, ALTO - 300)
        enemigo = Enemigo(escala, diccionario_enemigo, posicion_inicial, velocidad)
        enemigos.append(enemigo)
    return enemigos

enemigos = generar_enemigos(3)

# Piso
piso = Suelo(PANTALLA, mi_personaje.lados['main'],0, 0, ANCHO, 20) 

# Objeto
trash = Trash(diccionario_trash)

# Puntos
puntos = 0
ultimos_puntos = 0

# Timer
timer = 1

pygame.init()
while jugando:
    #segundos_transcurridos = pygame.time.get_ticks() / 1000
    #print(int(segundos_transcurridos))
    clock.tick(FPS)
    ultimos_puntos = 0
    for evento in pygame.event.get():
        if evento.type == QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F10:
                cambiar_modo()
            if evento.key == pygame.K_ESCAPE:
                jugando = False
    tecla_presionada = pygame.key.get_pressed()

    if tecla_presionada[pygame.K_RIGHT] or tecla_presionada[pygame.K_d]:
        mi_personaje.que_hace = 'derecha'
    elif tecla_presionada[pygame.K_LEFT] or tecla_presionada[pygame.K_a]:
        mi_personaje.que_hace = 'izquierda'
    elif tecla_presionada[pygame.K_UP] or tecla_presionada[pygame.K_w] or tecla_presionada[pygame.K_SPACE]:
        mi_personaje.que_hace = 'salta'
    elif tecla_presionada[pygame.K_f]:
        mi_personaje.que_hace = 'golpea'
    else:
        mi_personaje.que_hace = 'quieto'   

    for enemigo in enemigos:
        if not mi_personaje.personaje_muerto:
            if enemigo.posicion_actual >= mi_personaje.posicion_actual + 70:
                enemigo.que_hace = 'izquierda'
            elif enemigo.posicion_actual <= mi_personaje.posicion_actual - 70:
                enemigo.que_hace = 'derecha'
            
        ultimos_puntos += enemigo.contador_muerte 
    puntos = ultimos_puntos * 100
    actualizar_pantalla(PANTALLA,mi_personaje, enemigos, puntos, fondo, piso.lados)

    if get_mode():
        for lado in piso.lados:
            pygame.draw.rect(PANTALLA, 'Orange', piso.lados[lado], 2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, 'Blue',mi_personaje.lados[lado], 2)
        
        for enemigo in enemigos:
            for lado in enemigo.lados:
                pygame.draw.rect(PANTALLA, 'RED',enemigo.lados[lado], 2)
    pygame.display.update()

pygame.quit()