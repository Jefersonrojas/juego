from proyectopoo.source.bala1.bala import *
from proyectopoo.source.vida.barra_vida import Barra_vida

ANCHO = 1000
ALTO = 600

rojo = (255, 0, 0)
verde = (0, 255, 0)
negro = (0, 0, 0)
blanco = (255, 255, 255)  # Cambiado a blanco (255, 255, 255)

def load_img(direction):
    return pygame.image.load(direction)

def process(direction, x=120, y=180):
    return pygame.transform.scale(load_img(direction), (x, y))

class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.x = x
        self.y = y
        self.cantidad_salto = 10
        self.velocidad = 4
        self.saltando = False
        self.agachado=False
        self.saltando_una_vez=False
        self.barra_vida = Barra_vida(2000, 20, 20)  # Inicializa la barra de vida aquí
        self.sprites = [process('Idle/I1.png'), process('Idle/I2.png'), process('Idle/I3.png'),
                        process('Idle/I4.png'), process('Idle/I5.png'), process('Idle/I6.png'),
                        process('Idle/I7.png'), process('Idle/I1.png')]
        self.sprite_animation_counter = 0
        self.mirando_izquierda = False
        self.current_sprite = 0  # Inicializa el sprite actual
        self.animation_speed = 0.2  # Velocidad de animación

    def dibujar(self, pantalla):
        sprite = self.sprites[self.current_sprite]
        if self.mirando_izquierda:
            sprite = pygame.transform.flip(sprite, True, False)
        pantalla.blit(sprite, (self.x, self.y))


    def mover(self, keys):
        if keys[pygame.K_a] and self.x - self.velocidad >= 0:
            self.x -= self.velocidad
            self.mirando_izquierda = True
        if keys[pygame.K_d] and self.x + self.velocidad <= ANCHO // 2:
            self.x += self.velocidad
            self.mirando_izquierda =False

        if not self.saltando:
            if keys[pygame.K_w]:
                self.saltando = True
                self.mirando_izquierda = False
        else:
            if self.cantidad_salto >= -10:
                neg = 1
                if self.cantidad_salto < 0:
                    neg = -1
                self.y -= (self.cantidad_salto ** 2) * 0.5 * neg
                self.cantidad_salto -= 1
            else:
                self.saltando = False
                self.cantidad_salto = 10
        if keys[pygame.K_s] and not self.agachado:
            self.agachado = True
            self.y += 30  #  se agacha
        elif not keys[pygame.K_s] and self.agachado:
            self.y -= 30  # Vuelva a ssu posiccion
            self.agachado = False



        if keys[pygame.K_w] and keys[pygame.K_r] :  # Disminuir la vida con la tecla "r"
            self.barra_vida.disminuir_kalorias(50)


class Enemigo(Personaje):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)
        self.direccion = random.choice(["izquierda", "derecha", "arriba"])
        self.balas = []
        self.saltando = False
        self.cantidad_salto = 10
        self.sprites = [process('Idle/mago1.png', 120, 230),
                        process('Idle/mago2.png', 120, 230),
                        process('Idle/mago3.png', 120, 230)]
        self.current_sprite = 0
        self.mirando_izquierda = False

    def dibujar(self, pantalla):
        super().dibujar(pantalla)
        for bala in self.balas:
            bala.dibujar(pantalla)  # Cambiado a dibujar
        sprite = self.sprites[self.current_sprite]

        if self.mirando_izquierda:
            sprite = pygame.transform.flip(sprite, True, False)
        pantalla.blit(sprite, (self.x, self.y))

    def mover(self):
        if self.direccion == 'izquierda' and self.x - self.velocidad >= ANCHO // 2:
            self.x -= self.velocidad
        elif self.direccion == 'derecha' and self.x + self.ancho + self.velocidad <= ANCHO:
            self.x += self.velocidad
        elif self.direccion == 'arriba' and not self.saltando:
            self.saltando = True
        else:
            self.direccion = random.choice(['izquierda', 'derecha', 'arriba'])

        if self.saltando:
            if self.cantidad_salto >= -10:
                neg = 1
                if self.cantidad_salto < 0:
                    neg = -1
                self.y -= (self.cantidad_salto ** 2) * 0.5 * neg
                self.cantidad_salto -= 1
            else:
                self.saltando = False
                self.cantidad_salto = 10
        if random.randint(1, 100) == 1:
            self.atacar()



    def atacar(self):
        tipo_bala = random.choice([100, 400])
        bala = Bala(self.x, self.y + self.ancho // 2, 40, 40, tipo_bala,-5)
        self.balas.append(bala)




