import pygame

rojo = (255, 0, 0)
verde = (0, 255, 0)
negro=(0, 0,0)

class Barra_vida:
    def __init__(self, max_vida, x, y):
        self.vida = 100
        self.max_vida = max_vida
        self.x = x
        self.y = y

    def aumentar_kalorias(self, cantidad):
        self.vida += cantidad
        if self.vida > self.max_vida:
            self.vida = self.max_vida

    def disminuir_kalorias(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def dibujar_Kalorias(self, pantalla):
        vida_x = int(self.vida * 400 / self.max_vida)
        if 1900 <= self.vida < 2100:
            color = verde
        else:
            color = rojo

        border_radius = self.y // 2
        pygame.draw.rect(pantalla, negro, (self.x - 2, self.y - 2, 405, 35), border_radius=10)
        pygame.draw.rect(pantalla, color, (self.x, self.y, vida_x, 30), border_radius=10)
