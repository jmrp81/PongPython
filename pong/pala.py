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

class Pala(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image("imagenes/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.35#velocidad de las palas menor velocidad van mas suaves (normal 0.5)

    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
                
    def ia(self, time, ball):#metodo de inteligencia para dar movimiento a la pala de la CPU,necesita saber la posicion de la bola, por eso la recibe de parametro
        if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:#comprueba la bola se mueva hacia la pala y pase del centro de la ventana
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time

    #funcion para cargar imagenes en el juego
    def load_image(self,filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()#convertir imagen a tipo pygame
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
