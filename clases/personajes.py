import pygame
from config import reescalar_imagenes, obtener_rectangulos,obtener_valor_random
class Personaje:
    def __init__(self, escala, animaciones, posicion_inicial, velocidad):
        self.ancho = escala[0]
        self.alto = escala[1]
        self.contador_pasos = 0
        self.que_hace = 'quieto'
        self.animaciones = animaciones
        self.mira_derecha = False
        self.reescalar_animaciones()
        rectangulo = self.animaciones['golpea_izquierda'][6].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1] 
        self.lados = obtener_rectangulos(rectangulo)
        self.posicion_actual = posicion_inicial[0]
        self.velocidad = velocidad
        self.gravedad = 1
        self.potencia_salto = -25
        self.velocidad_caida = 15
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.vida = 18
        self.personaje_muerto = False

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados['main'])    
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
        self.posicion_actual += velocidad
    
    def aplicar_gravedad(self, pantalla, pisos):
        if self.esta_saltando:
            self.animar(pantalla, 'salta')

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for piso in pisos:
            if self.lados['bottom'].colliderect(piso.lados['top']):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados['main'].bottom = piso.lados['main'].top

    def actualizar(self, pantalla, piso):
        if not self.personaje_muerto:
            match self.que_hace:
                case 'quieto':
                    if not self.esta_saltando:
                        if self.mira_derecha:
                            self.animar(pantalla, 'quieto_derecha')
                        else:
                            self.animar(pantalla, 'quieto_izquierda')
                case 'derecha':
                    if not self.esta_saltando:
                        self.animar(pantalla, 'camina_derecha')
                    self.mover(self.velocidad)
                    self.mira_derecha = True
                case 'izquierda':
                    if not self.esta_saltando:
                        self.animar(pantalla, 'camina_izquierda')
                    self.mover(self.velocidad*(-1))
                    self.mira_derecha = False
                case 'salta':
                    if not self.esta_saltando:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                case 'golpea':
                    if not self.esta_saltando:
                        if self.mira_derecha:
                            self.animar(pantalla, 'golpea_derecha')
                        else:
                            self.animar(pantalla, 'golpea_izquierda')
                case 'lastimado':
                    if not self.esta_saltando:
                        if self.mira_derecha:
                            self.animar(pantalla, 'lastimado_derecha')
                        else:
                            self.animar(pantalla, 'lastimado_izquierda')
                case 'muerte':
                    if not self.esta_saltando:
                        if self.mira_derecha:
                            self.animar(pantalla, 'muerte_derecha')
                        else:
                            self.animar(pantalla, 'muerte_izquierda')
                        self.personaje_muerto = True
        else:
            if self.mira_derecha:
                self.animar(pantalla, 'tirado_derecha')
            else:
                self.animar(pantalla, 'tirado_izquierda')

        self.aplicar_gravedad(pantalla, piso)

class Enemigo:
    def __init__(self, escala, animaciones, posicion_inicial, velocidad):
        self.ancho = escala[0]
        self.alto = escala[1]
        self.que_hace = 'quieto'
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.vida = 18
        rectangulo = self.animaciones['golpea_izquierda'][6].get_rect()
        diccionario_enemigo = {}
        diccionario_enemigo['rectangulo'] = rectangulo
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.posicion_actual = posicion_inicial[0]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.mira_izquierda = False
        self.contador_muerte = 0

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados['main'])    
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
        self.posicion_actual += velocidad

    def actualizar(self, pantalla):
        match self.que_hace:
            case 'quieto':
                    if self.mira_izquierda:
                        self.animar(pantalla, 'quieto_derecha')
                    else:
                        self.animar(pantalla, 'quieto_izquierda')
            case 'derecha':
                self.animar(pantalla, 'camina_derecha')
                self.mover(self.velocidad)
                self.mira_izquierda = True
            case 'izquierda':
                self.animar(pantalla, 'camina_izquierda')
                self.mover(self.velocidad*(-1))
                self.mira_izquierda = False
            case 'golpea':
                if self.mira_izquierda:
                    self.animar(pantalla, 'golpea_derecha')
                else:
                    self.animar(pantalla, 'golpea_izquierda')
            case 'lastimado':
                    if self.mira_izquierda:
                        self.animar(pantalla, 'lastimado_derecha')
                    else:
                        self.animar(pantalla, 'lastimado_izquierda')
            case 'muerto':
                    if self.mira_izquierda:
                        self.animar(pantalla, 'muerto_derecha')
                    else:
                        self.animar(pantalla, 'muerto_izquierda')
                    self.contador_muerte += 1
                    valor_random = obtener_valor_random()

                    for lado in self.lados:
                        self.lados[lado].x = valor_random
                    self.posicion_actual = valor_random

