import pygame
from archivos import *
import random

def obtener_valor_random():
    posicion_aleatoria = random.randint(-700, 2500)
    while posicion_aleatoria >= 0 and posicion_aleatoria <= 1800:
        posicion_aleatoria = random.randint(-700, 2500)
    return posicion_aleatoria

def escribir_texto(pantalla, mensaje, altura, x, y):
    fuente = pygame.font.SysFont('Verdana', altura)
    texto = fuente.render(mensaje, True, 'Black')
    texto_rect = texto.get_rect()
    texto_rect.midtop = (x,y)
    pantalla.blit(texto, texto_rect)

def mostrar_textos(pantalla, puntos):
    escribir_texto(pantalla, str('Puntos'),20, ANCHO / 2 + 500, 190)
    escribir_texto(pantalla, str(puntos),20, 1652, 215)

def reescalar_imagenes(lista_imagenes, escala):
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], (escala))

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []

    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen,flip_x, flip_y))
    return lista_girada    

def obtener_rectangulos(principal)->dict:
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario ["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

def actualizar_pantalla(pantalla, personaje, enemigos, puntos, fondo, lados_piso):
    pantalla.blit(fondo, (0,0))

    mostrar_textos(pantalla, puntos)
    verificar_colision(personaje, enemigos, PANTALLA, lados_piso)

def verificar_colision(personaje, enemigos, pantalla, lados_piso):
    for enemigo in enemigos:
        if personaje.lados['main'].colliderect(enemigo.lados['main']) and personaje.que_hace == 'golpea':
            if enemigo.que_hace != 'lastimado':
                enemigo.que_hace = 'lastimado'
                enemigo.vida -= 1
        elif personaje.lados['main'].colliderect(enemigo.lados['main']):
            if enemigo.que_hace != 'muerto':
                enemigo.que_hace = 'golpea'
        
        if enemigo.lados['main'].colliderect(personaje.lados['main']) and enemigo.que_hace == 'golpea':
            if personaje.que_hace != 'lastimado':
                personaje.que_hace = 'lastimado'
                personaje.vida -= 1
        
        if personaje.personaje_muerto:
            enemigo.que_hace = 'quieto'


        if enemigo.vida < 0:
            enemigo.que_hace = 'muerto'
            enemigo.vida = 18

        enemigo.actualizar(pantalla)
    if personaje.vida < 0:
        personaje.que_hace = 'muerte'
    
    personaje.actualizar(pantalla, lados_piso)

# PANTALLA
ANCHO = 1800
ALTO = 800
ESCALA_PANTALLA = (ANCHO, ALTO)
PANTALLA =  pygame.display.set_mode((ESCALA_PANTALLA))

pygame.display.set_caption('Los chinardos')

# Abrir juego 
jugando = True

fondo = pygame.image.load(r"Los Chinardos\images\escenarios\chino\chino.png")
fondo = pygame.transform.scale(fondo,ESCALA_PANTALLA)

# FPS
FPS = 20
clock = pygame.time.Clock()