import pygame
from proyectopoo.source.solitario.personajes import Personaje, Enemigo
from proyectopoo.source.vida.barra_vida import Barra_vida
from proyectopoo.source.menu.menu import  MainMenu

ANCHO = 1000
ALTO = 600

azul = (0, 0, 255)
rojo = (255, 0, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
##aqui ponemos el tiempo en segundos para jugar ya sea para ganr o perder
Tiempo_limite= 60
class Juego:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.bg_img = pygame.image.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//fonts//bgnuevo.jpeg").convert_alpha()
        self.bg_img = pygame.transform.scale(self.bg_img, (1000, 600))
        pygame.mixer.music.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//sound//cancion.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.jugador = Personaje(200, 350, 50, 50)
        self.enemigo = Enemigo(700, 350, 50, 50)
        self.barra_vida = Barra_vida(2800, 20, 20) ## aqui modificamos la vida del personaje

    def main(self):
        clock = pygame.time.Clock()
        juego_activo = True
        tiempo_inicio = pygame.time.get_ticks() // 1000

        while juego_activo:
            clock.tick(60)# Fps

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    juego_activo = False

            keys = pygame.key.get_pressed()
            self.jugador.mover(keys)
            if keys[pygame.K_w] and keys[pygame.K_r]:  # Disminuir las kalorias
                self.barra_vida.disminuir_kalorias(50)

            self.pantalla.blit(self.bg_img, (0, 0))

            keys = pygame.key.get_pressed()
            self.jugador.mover(keys)
            self.enemigo.mover()

            for bala in self.enemigo.balas:
                bala.mover()
                if bala.x > ANCHO:
                    self.enemigo.balas.remove(bala)
                elif self.jugador.x < bala.x < self.jugador.x + self.jugador.ancho and self.jugador.y < bala.y < self.jugador.y + self.jugador.alto:
                    self.barra_vida.aumentar_kalorias(bala.tipo)
                    self.enemigo.balas.remove(bala)

            self.jugador.dibujar(self.pantalla)
            self.enemigo.dibujar(self.pantalla)
            self.barra_vida.dibujar_Kalorias(self.pantalla)

            #dibujo del tiempo q esta transcurriendo
            tiempo_transcurrido = pygame.time.get_ticks() // 1000-tiempo_inicio
            tiempo_restante=Tiempo_limite-tiempo_transcurrido
            font = pygame.font.Font(None,35)
            texto_tiempo=font.render(f"Time: {tiempo_restante}", True,rojo)
            self.pantalla.blit(texto_tiempo, (430,15))

            #dibujo la cantidad de kalorias en la pantalla
            texto_kalorias=font.render(f"Calorias: {self.barra_vida.vida}", True,blanco)
            font=pygame.font.Font(None,20)
            self.pantalla.blit(texto_kalorias, (20,60))

            if tiempo_restante <=0:## tiempo en segundos
                if 1900 <= self.barra_vida.vida <= 2100:
                    font = pygame.font.Font(None, 86)
                    texto = font.render("¡Ganaste!", True, negro)
                    self.pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

                else:
                    font = pygame.font.Font(None, 86)
                    texto = font.render("¡Perdiste!", True, rojo)
                    self.pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))


                juego_activo = False  # Desactivar juego mientras se muestra el resultado
                pygame.display.flip()
                pygame.time.wait(3000)  # Esperar 3 segundos antes de volver al menú
                pygame.mixer.music.stop()
                return MainMenu




            pygame.display.flip()



