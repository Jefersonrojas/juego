import pygame
from proyectopoo.source.bala.bala_pelea import Bala

# amarillo = (255,255,0)
rojo = (255, 0, 0)
# blanco= (255,255,255)
verde = (0, 255, 0)
negro = (0, 0, 0)


def load_img(direction):
    return pygame.image.load(direction)


def process(direction, x=120, y=180):
    return pygame.transform.scale(load_img(direction), (x, y))


class Peleador:
    def __init__(self, x, y):
        self.imagen_manzana = pygame.image.load('C://Users//mende//Downloads//Hito//proyectopoo//recursos//image//manzana.webp')
        self.imagen_hamburgesa = pygame.image.load('C://Users//mende//Downloads//Hito//proyectopoo//recursos//image//hamburgesa.webp')
        self.imagen_manzana = pygame.transform.scale(self.imagen_manzana, (50, 50))
        self.imagen_hamburgesa = pygame.transform.scale(self.imagen_hamburgesa, (50, 50))
        self.x = x
        self.y = y
        self.muerto = False
        self.velocidad = 5
        self.saltando = False
        self.velocidad_salto = 10
        self.gravedad = 0.5
        self.suelo = y
        self.impulso_salto = -10
        self.ancho = 80
        self.alto = 180
        self.vida = 100
        self.alcance_ataque = 50
        self.ataq = 1
        self.current_sprite = 0
        self.sprites = [process('Idle/I1.png'), process('Idle/I2.png'), process('Idle/I3.png'),
                        process('Idle/I4.png'), process('Idle/I5.png'), process('Idle/I6.png'),
                        process('Idle/I7.png'), process('Idle/I1.png')]
        self.sprite_animation_counter = 0
        self.mirando_izquierda = False

    def dibujar(self, superficie):
        if not self.muerto:
            sprite = self.sprites[self.current_sprite]
            if self.mirando_izquierda:
                sprite = pygame.transform.flip(sprite, True, False)
            superficie.blit(sprite, (self.x, self.y))

    def mover(self, direccion):
        if not self.muerto:
            if direccion == 'izquierda' and self.x > 0:
                self.x -= self.velocidad
                self.mirando_izquierda = True
            if direccion == 'derecha' and self.x < 1000 - self.ancho:
                self.x += self.velocidad
                self.mirando_izquierda = False

    def saltar(self):
        if not self.saltando:
            self.saltando = True
            self.velocidad_salto = self.impulso_salto

    def atacar(self, objetivo, pantalla):
        if not self.muerto:
            if self.ataq == 1:
                self.ataq = 2



                rect_ataque = pygame.Rect(self.x, self.y, self.ancho + self.alcance_ataque, self.alto)
                rect_objetivo = pygame.Rect(objetivo.x, objetivo.y, objetivo.ancho, objetivo.alto)
                if rect_ataque.colliderect(rect_objetivo):
                    objetivo.recibir_dano(10)

    def disparar(self):
        if not self.muerto:
            if self.ataq == 2:
                bala = Bala(self.x + self.ancho // 2, self.y + self.alto // 2, 10)
                bala.imagen = self.imagen_manzana
                return bala
            return None

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.muerto = True
            print("¡El peleador ha sido derrotado!")

    def actualizar(self):
        if self.saltando:
            self.y += self.velocidad_salto
            self.velocidad_salto += self.gravedad
            if self.y >= self.suelo:
                self.y = self.suelo
                self.saltando = False
        self.sprite_animation_counter += 1
        if not self.muerto:
            # Verifica si es tiempo de cambiar al siguiente sprite
            if self.sprite_animation_counter >= 10:  # Aumenta este número para ralentizar la animación
                self.current_sprite += 1
                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                # Reinicia el contador de animación
                self.sprite_animation_counter = 0


class BarraDeVida:
    def __init__(self, vida, x, y):
        self.vida = vida
        self.x = x
        self.y = y

    def dibujar_vida(self, pantalla):
        ratio = self.vida / 100
        pygame.draw.rect(pantalla, negro, (self.x - 2, self.y - 2, 405, 35), border_radius=10)
        pygame.draw.rect(pantalla, rojo, (self.x, self.y, 400, 30), border_radius=10)
        pygame.draw.rect(pantalla, verde, (self.x, self.y, 400 * ratio, 30), border_radius=10)

    def actualizar(self, nueva_vida):
        self.vida = nueva_vida


class Malos_Habitos(Peleador):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.ataqEne = 3
        # Cargar sprites específicos del enemigo
        self.sprites = [process('Idle/mago1.png', 120, 230),
                        process('Idle/mago2.png', 120, 230),
                        process('Idle/mago3.png', 120, 230)]
        self.mirando_izquierda = False

    def dibujar(self, superficie):
        if not self.muerto:
            sprite = self.sprites[self.current_sprite]
            if self.mirando_izquierda:
                sprite = pygame.transform.flip(sprite, True, False)
            superficie.blit(sprite, (self.x, self.y))

    def mover(self, direccion):
        if not self.muerto:
            if direccion == 'izquierda' and self.x > 0:
                self.x -= self.velocidad
                self.mirando_izquierda = False
            if direccion == 'derecha' and self.x < 1000 - self.ancho:
                self.x += self.velocidad
                self.mirando_izquierda = True

    def atacar(self, objetivo, pantalla):
        if not self.muerto:
            if self.ataqEne == 3:
                self.ataqEne = 4

                # Resta el ancho de la imagen de la zanahoria para que aparezca a la izquierda

                rect_ataque = pygame.Rect(self.x, self.y, self.ancho + self.alcance_ataque, self.alto)
                rect_objetivo = pygame.Rect(objetivo.x, objetivo.y, objetivo.ancho, objetivo.alto)
                if rect_ataque.colliderect(rect_objetivo):
                    objetivo.recibir_dano(10)

    def disparar(self):
        if not self.muerto:
            if self.ataqEne == 4:
                # Resta el ancho de la bala para que salga desde el lado izquierdo
                bala = Bala(self.x - self.ancho + 10, self.y + self.alto // 2, 10)
                bala.imagen = self.imagen_hamburgesa  # Asigna la imagen de la hamburguesa a la bala
                return bala
            return None


