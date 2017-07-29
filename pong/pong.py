#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import sys
from pygame.locals import *

# Constantes
#tamaño de ventana
WIDTH = 640
HEIGHT = 480

# Funciones
# ---------------------------------------------------------------------
#funcion para cargar imagenes en el juego
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()#convertir imagen a tipo pygame
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

#definir un metodo para poner texto
def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.SysFont("Arial", 30)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

#metodo para poner musica
def cargar_sonido(nombre):
    try:
        #sonido = pygame.mixer.Sound(nombre)
        pygame.mixer.music.load(nombre)
        pygame.mixer.music.play(-1)
    except:
        print('no se puede cargar el sonido')

# ---------------------------------------------------------------------

def main():
    from bola import Bola
    from pala import Pala
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego del Pong en Python / Practica Juan Manuel Rguez Perez")
    #cargar fondo
    background_image = load_image('imagenes/fondo.jpg')
    bola = Bola()#creamos la bola del juego
    pala_jug = Pala(30)#creamos la pala1 del jugador
    pala_cpu = Pala(WIDTH - 30)#pala cpu
    
    clock = pygame.time.Clock()#crear reloj para marcar movimientos del juego

    puntos = [0, 0]#puntos iniciales
    #cargr musica
    cargar_sonido("sonido/fondo.mp3")
    #bucle infinito para mantener la ventana abierta
    while True:
        time = clock.tick(30)#establecer tiempo de refresco
        keys = pygame.key.get_pressed()#control de teclas
        
        
        for eventos in pygame.event.get():#comprueba los eventos de pygame ejecutandose
            if eventos.type == pygame.QUIT:
                exit(1)
                
        puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos)#actualizar movimiento de la bola
        pala_jug.mover(time, keys)#mover la pala jugador
        pala_cpu.ia(time, bola)#movimiento pala cpu
        
        p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)#poner puntuacion del jugador
        p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)#poner puntuacion de la cpu
        nombreJugador, posicionNombre = texto("Jugador", WIDTH/4, 15)
        nombreCpu, posicionNomCpu = texto("CPU", WIDTH-WIDTH/4, 15)
        
        screen.blit(background_image, (0, 0))#añadir el fondo a la ventana
        screen.blit(bola.image, bola.rect)#añadir la bola a la ventana
        screen.blit(pala_jug.image, pala_jug.rect)#añadir la pala jugador
        screen.blit(pala_cpu.image, pala_cpu.rect)#añadir la pala CPU
        screen.blit(nombreJugador, posicionNombre)
        screen.blit(nombreCpu, posicionNomCpu )
        screen.blit(p_jug, p_jug_rect)#añadir a la ventana la puntuacion del jugador
        screen.blit(p_cpu, p_cpu_rect)#añadir a la ventana la puntuacion de la cpu
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()
