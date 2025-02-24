import pygame

class Bala:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.velocidad = vel
        self.ancho = 10
        self.alto = 5
        self.imagen = None
    def mover(self):
        self.x += self.velocidad
    def mover_izq(self):
        self.x -= self.velocidad
    def dibujar(self, pantalla):
        if self.imagen:
            pantalla.blit(self.imagen, (self.x, self.y))
        else:
            # Dibuja una bala como un rectángulo si no hay imagen
            pygame.draw.rect(pantalla, (0, 0, 0), (self.x, self.y, 10, 10))