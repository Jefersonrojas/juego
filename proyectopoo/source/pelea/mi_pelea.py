import pygame, sys

from proyectopoo.source.menu.menu import MainMenu
from proyectopoo.source.pelea.pelea import *

class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Presiona una tecla para comenzar", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(1000 // 2, 600 // 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def wait_for_keypress(self, esperando):
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    esperando = False  # sale del bucle cuando se presiona una tecla
                    self.screen.fill((0, 0, 0))  # limpia la pantalla
                    pygame.display.flip()  # actualiza la pantalla
                    return


class JuegoPelea:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((1000, 600))
        self.bg_img = pygame.image.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//fonts//bgnuevo.jpeg").convert_alpha()
        # Hago que la imagen de cualquier tamaño se acolpe al tamaño de la pantalla
        self.bg_img = pygame.transform.scale(self.bg_img, (1000, 600))
        self.start_screen = StartScreen(self.pantalla)
        pygame.mixer.music.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//sound//cancion.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.sonido_personaje_muerto = pygame.mixer.Sound("C://Users//mende//Downloads//Hito//proyectopoo//recursos//sound//Mario_muerte.wav")
        # Crea instancias de Peleador y Mala_alimentacion
        self.peleador = Peleador(200, 350)
        self.Mala_alimentacion = Malos_Habitos(700, 350)
        self.reloj = pygame.time.Clock()
        self.balas = []
        self.balas2 = []
        self.barra_vida_jugador = BarraDeVida(self.peleador.vida, 20, 20)
        self.barra_vida_enemigo = BarraDeVida(self.Mala_alimentacion.vida, 580, 20)

    def ejecutar(self):
        ejecutando = True
        esperar = True
        muerte = True
        estado = "jugando"
        while ejecutando:
            if estado == "jugando":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if esperar:
                    self.start_screen.draw()
                    self.start_screen.wait_for_keypress(esperar)
                    esperar = False
                pygame.display.flip()
                self.pantalla.blit(self.bg_img, (0, 0))
                self.reloj.tick(60)
                # Resto de tu código para manejar las teclas, balas, colisiones, etc.
                teclas = pygame.key.get_pressed()
                if teclas[pygame.K_a]:
                    self.peleador.mover('izquierda')
                if teclas[pygame.K_d]:
                    self.peleador.mover('derecha')
                if teclas[pygame.K_w] and not self.peleador.saltando:
                    self.peleador.saltar()
                if teclas[pygame.K_f] and teclas[pygame.K_SPACE]:
                    print("no se puede")
                else:
                    if not self.Mala_alimentacion.muerto:
                        if teclas[pygame.K_f]:
                            self.peleador.atacar(self.Mala_alimentacion, self.pantalla)
                            self.peleador.ataq = 2
                        if teclas[pygame.K_SPACE]:
                            bala = self.peleador.disparar()
                            if bala:
                                self.balas.append(bala)
                            self.peleador.ataq = 1
                        for bala in self.balas:
                            bala.mover()
                            bala.dibujar(self.pantalla)
                            if pygame.Rect(bala.x, bala.y, bala.ancho, bala.alto).colliderect(
                                    pygame.Rect(self.Mala_alimentacion.x, self.Mala_alimentacion.y,
                                                self.Mala_alimentacion.ancho, self.Mala_alimentacion.alto)):
                                self.Mala_alimentacion.recibir_dano(10)  # Daño causado por la bala
                                self.balas.remove(bala)
                if teclas[pygame.K_LEFT]:
                    self.Mala_alimentacion.mover('izquierda')
                if teclas[pygame.K_RIGHT]:
                    self.Mala_alimentacion.mover('derecha')
                if teclas[pygame.K_UP] and not self.Mala_alimentacion.saltando:
                    self.Mala_alimentacion.saltar()
                if teclas[pygame.K_o] and teclas[pygame.K_p]:
                    print("no se puede")
                else:
                    if not self.peleador.muerto:
                        if teclas[pygame.K_o]:
                            self.Mala_alimentacion.atacar(self.peleador, self.pantalla)
                            self.Mala_alimentacion.ataqEne = 4
                        if teclas[pygame.K_p]:
                            bala2 = self.Mala_alimentacion.disparar()
                            if bala2:
                                self.balas2.append(bala2)
                            self.Mala_alimentacion.ataqEne = 3

                        for bala2 in self.balas2:
                            bala2.mover_izq()
                            bala2.dibujar(self.pantalla)
                            if pygame.Rect(bala2.x, bala2.y, bala2.ancho, bala2.alto).colliderect(
                                    pygame.Rect(self.peleador.x, self.peleador.y, self.peleador.ancho,
                                                self.peleador.alto)):
                                self.peleador.recibir_dano(10)  # Daño causado por la bala
                                self.balas2.remove(bala2)

                    # Dibujar las barras de vida
                self.barra_vida_enemigo.dibujar_vida(self.pantalla)
                self.barra_vida_jugador.dibujar_vida(self.pantalla)
                self.barra_vida_jugador.actualizar(self.peleador.vida)
                self.barra_vida_enemigo.actualizar(self.Mala_alimentacion.vida)
                if not self.peleador.muerto:
                    self.peleador.actualizar()
                    self.peleador.dibujar(self.pantalla)
                if not self.Mala_alimentacion.muerto:
                    self.Mala_alimentacion.actualizar()
                    self.Mala_alimentacion.dibujar(self.pantalla)

                if self.peleador.muerto and muerte:
                    pygame.mixer.music.stop()
                    self.sonido_personaje_muerto.play()
                    muerte = False
                    estado = "muerte"
                    return MainMenu

                if self.Mala_alimentacion.muerto and muerte:
                    pygame.mixer.music.stop()
                    self.sonido_personaje_muerto.play()
                    muerte = False
                    estado = "muerto"
                    return MainMenu
                pygame.display.flip()
            elif estado == "muerto":
                self.pantalla_motivadora.mostrar()
                pygame.mixer.music.stop()
                pygame.display.flip()
        pygame.quit()

