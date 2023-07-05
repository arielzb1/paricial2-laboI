import pygame
from niveles.nivel import Nivel
from clases.suelo import Suelo
from clases.personajes import Personaje,Enemigo
from config import obtener_valor_random
from archivos import *

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()
    
        pygame.display.set_caption('Los chinardos')
        
        fondo = pygame.image.load(r"Los Chinardos\images\escenarios\chino\chino.png")
        fondo = pygame.transform.scale(fondo,(W,H))
        posicion_inicial = (W / 2, 500)
        escala = (160, 200)

        diccionario_enemigo = {}
        diccionario_enemigo['quieto_derecha'] = enemigo_quieto_derecha
        diccionario_enemigo['quieto_izquierda'] = enemigo_quieto_izquierda
        diccionario_enemigo['camina_derecha'] = enemigo_camina_derecha
        diccionario_enemigo['camina_izquierda'] = enemigo_camina_izquierda
        diccionario_enemigo['golpea_izquierda'] = enemigo_golpea_izquierda
        diccionario_enemigo['golpea_derecha'] = enemigo_golpea_derecha
        diccionario_enemigo['lastimado_derecha'] = enemigo_lastimado_derecha
        diccionario_enemigo['lastimado_izquierda'] = enemigo_lastimado_izquierda
        diccionario_enemigo['muerto_izquierda'] = enemigo_muerto_izquierda
        diccionario_enemigo['muerto_derecha'] = enemigo_muerto_derecha

        diccionario_personaje = {}
        diccionario_personaje['quieto_izquierda'] = personaje_quieto_izquierda
        diccionario_personaje['quieto_derecha'] = personaje_quieto_derecha
        diccionario_personaje['camina_izquierda'] = personaje_camina_izquierda
        diccionario_personaje['camina_derecha'] = personaje_camina
        diccionario_personaje['salta'] = personaje_salta
        diccionario_personaje['golpea_izquierda'] = personaje_golpea_izquierda
        diccionario_personaje['golpea_derecha'] = personaje_golpea_derecha
        diccionario_personaje['lastimado_izquierda'] = personaje_lastimado_izquierda
        diccionario_personaje['lastimado_derecha'] = personaje_lastimado_derecha
        diccionario_personaje['muerte_izquierda'] = personaje_muerte_izquierda
        diccionario_personaje['muerte_derecha'] = personaje_muerte_derecha
        diccionario_personaje['tirado_izquierda'] = personaje_tirado_izquierda
        diccionario_personaje['tirado_derecha'] = personaje_tirado_derecha

        mi_personaje = Personaje(escala, diccionario_personaje, posicion_inicial, 12)

        piso = Suelo(pantalla, mi_personaje.lados['main'],0, 0, W, 20) 
        lista_plataformas = [piso]
        
        def generar_enemigos(cantidad):
            enemigos = []
            escala = (160, 200)
            velocidad = 6
            for cant in range(cantidad):
                posicion = obtener_valor_random()
                posicion_inicial = (posicion, 500)
                enemigo = Enemigo(escala, diccionario_enemigo, posicion_inicial, velocidad)
                enemigos.append(enemigo)
            return enemigos
        
        enemigos = generar_enemigos(3)


        super().__init__(pantalla, mi_personaje, enemigos,lista_plataformas, fondo)