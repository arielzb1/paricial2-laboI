import pygame
from config import girar_imagenes

try: 
    # Trash
    trash_quieto = [pygame.image.load(r'Los Chinardos\images\objetos\trash\5.png')]

    trash_golpeado_derecha = [pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\1.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\2.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\3.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\4.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\5.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\6.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\7.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\8.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\9.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\10.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\11.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\12.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\13.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\14.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\15.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\16.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\17.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\18.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\19.png'),
                              pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\20.png')]

    trash_golpeado_izquierda = girar_imagenes(trash_golpeado_derecha, True, False)

    trash_tirado = [pygame.image.load(r'Los Chinardos\images\objetos\trash\golpeado_derecha\20.png')]

    # Animaciones Enemigo
    enemigo_camina_derecha = [pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\1.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\2.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\3.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\4.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\5.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\6.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\7.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\camina\8.png')]

    enemigo_camina_izquierda = girar_imagenes(enemigo_camina_derecha, True, False)

    enemigo_quieto_derecha = [pygame.image.load(r'Los Chinardos\images\movimiento enemigo\quieto\1.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\quieto\2.png'),
                      pygame.image.load(r'Los Chinardos\images\movimiento enemigo\quieto\3.png')]
    
    enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto_derecha, True, False)

    enemigo_golpea_derecha = [pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\1.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\2.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\3.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\4.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\5.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\6.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\7.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\8.png'),
                              pygame.image.load(r'Los Chinardos\images\movimiento enemigo\golpe\9.png')]
    
    enemigo_golpea_izquierda = girar_imagenes(enemigo_golpea_derecha, True, False)

    enemigo_lastimado_derecha = [pygame.image.load(r'Los Chinardos\images\movimiento enemigo\lastimado\1.png')]

    enemigo_lastimado_izquierda = girar_imagenes(enemigo_lastimado_derecha, True, False)

    enemigo_muerto_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\1.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\2.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\3.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\4.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\5.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\6.png'),
                                pygame.image.load(r'Los Chinardos\images\movimiento enemigo\muerto\7.png')]

    enemigo_muerto_derecha = girar_imagenes(enemigo_muerto_izquierda, True, False)

    # Animaciones jugador
    personaje_camina = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina normal\1.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina normal\2.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina normal\3.png')]

    personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

    personaje_en_guardia = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\1.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\2.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\3.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\4.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\5.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\6.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\7.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\camina combate\8.png'),]

    personaje_quieto_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\quieto\1.png'),
                    pygame.image.load(r'Los Chinardos\images\movimiento jugador\quieto\2.png'),
                    pygame.image.load(r'Los Chinardos\images\movimiento jugador\quieto\3.png'),
                    pygame.image.load(r'Los Chinardos\images\movimiento jugador\quieto\4.png')]

    personaje_quieto_derecha = girar_imagenes(personaje_quieto_izquierda, True, False)

    personaje_salta = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\salto\4.png')]

    personaje_golpea_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\1.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\2.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\3.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\4.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\5.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\6.png'),
                        pygame.image.load(r'Los Chinardos\images\movimiento jugador\golpe\7.png')]
    
    personaje_golpea_derecha = girar_imagenes(personaje_golpea_izquierda, True, False)

    personaje_lastimado_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\lastimado\1.png')]

    personaje_lastimado_derecha = girar_imagenes(personaje_lastimado_izquierda, True, False)

    personaje_muerte_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\1.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\2.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\3.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\4.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\5.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\6.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\7.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\8.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\9.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\10.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\11.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\12.png'),
                                  pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\13.png')]
    
    personaje_muerte_derecha = girar_imagenes(personaje_muerte_izquierda, True, False)
    
    personaje_tirado_izquierda = [pygame.image.load(r'Los Chinardos\images\movimiento jugador\muere\13.png')]

    personaje_tirado_derecha = girar_imagenes(personaje_tirado_izquierda, True, False)

except FileNotFoundError:
    print('Error al ingresar documentos')

# Animaciones Trash
diccionario_trash = {}
diccionario_trash['golpeado_derecha'] = trash_golpeado_derecha
diccionario_trash['golpeado_izquierda'] = trash_golpeado_izquierda
diccionario_trash['quieto'] = trash_quieto
diccionario_trash['tirado'] = trash_tirado

# Animaciones Enemigo
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

# Animaciones Personaje
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
