import pygame
import random

class Bala:
    def __init__(self, x, y,ancho,alto,tipo,velocidad):
        self.x = x
        self.y = y
        self.velocidad=velocidad
        self.ancho =ancho
        self.alto = alto
        self.tipo = tipo
        if self.tipo == 100:
            self.image = pygame.transform.scale((pygame.image.load('C://Users//mende//Downloads//Hito//proyectopoo//recursos//image//manzana.webp').convert_alpha()), (50, 50))
        elif self.tipo == 400:
            self.image = pygame.transform.scale((pygame.image.load('C://Users//mende//Downloads//Hito//proyectopoo//recursos//image//hamburgesa.webp').convert_alpha()), (50, 50))
    def mover(self):
        self.x += self.velocidad
    def dibujar(self, pantalla):
        pantalla.blit(self.image,(self.x,self.y))