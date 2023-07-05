import pygame
from modo import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, enemigos, plataformas, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.enemigos = enemigos
        self.plataformas = plataformas
        self.img_fondo = imagen_fondo
        

    def actualizar(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_F10:
                    cambiar_modo()
        self.leer_movimientos()
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))
        self.verificar_colision()
        self.dibujar_rectangulos()
    
    def leer_movimientos(self):
        tecla_presionada = pygame.key.get_pressed()
        if tecla_presionada[pygame.K_RIGHT] or tecla_presionada[pygame.K_d]:
            self.jugador.que_hace = 'derecha'
        elif tecla_presionada[pygame.K_LEFT] or tecla_presionada[pygame.K_a]:
            self.jugador.que_hace = 'izquierda'
        elif tecla_presionada[pygame.K_UP] or tecla_presionada[pygame.K_w] or tecla_presionada[pygame.K_SPACE]:
            self.jugador.que_hace = 'salta'
        elif tecla_presionada[pygame.K_f]:
            self.jugador.que_hace = 'golpea'
        else:
            self.jugador.que_hace = 'quieto' 
        
        for enemigo in self.enemigos:
            if not self.jugador.personaje_muerto:
                if enemigo.posicion_actual >= self.jugador.posicion_actual + 70:
                    enemigo.que_hace = 'izquierda'
                elif enemigo.posicion_actual <= self.jugador.posicion_actual - 70:
                    enemigo.que_hace = 'derecha'
        
        #     ultimos_puntos += enemigo.contador_muerte 
        # puntos = ultimos_puntos * 100

    def verificar_colision(self):
        for enemigo in self.enemigos:
            if self.jugador.lados['main'].colliderect(enemigo.lados['main']) and self.jugador.que_hace == 'golpea':
                if enemigo.que_hace != 'lastimado' or self.jugador.que_hace != 'muerte':
                    enemigo.que_hace = 'lastimado'
                    enemigo.vida -= 1
            elif self.jugador.lados['main'].colliderect(enemigo.lados['main']):
                if enemigo.que_hace != 'muerto':
                    enemigo.que_hace = 'golpea'
            
            if enemigo.lados['main'].colliderect(self.jugador.lados['main']) and enemigo.que_hace == 'golpea':
                if self.jugador.que_hace != 'lastimado':
                    self.jugador.que_hace = 'lastimado'
                    self.jugador.vida -= 1
            
            if self.jugador.personaje_muerto:
                enemigo.que_hace = 'quieto'

            if enemigo.vida < 0:
                enemigo.que_hace = 'muerto'
                enemigo.vida = 18

            enemigo.actualizar(self._slave)
        if self.jugador.vida < 0:
            self.jugador.que_hace = 'muerte'
        
        self.jugador.actualizar(self._slave, self.plataformas)

    def dibujar_rectangulos(self):
        if get_mode():
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave, 'Orange', plataforma.lados[lado], 2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, 'Blue',self.jugador.lados[lado], 2)
            
            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, 'RED',enemigo.lados[lado], 2)
        pygame.display.update()