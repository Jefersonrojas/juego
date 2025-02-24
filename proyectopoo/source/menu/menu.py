from proyectopoo.source.menu.boton import Button

import pygame
import sys
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//fonts//fonnddd.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (1000, 600))
        self.buttons = [
            Button(400, 200, 200, 50, 'Pelear 1VS1', (255, 0, 0), (255, 255, 255)),
            Button(400, 300, 200, 50, 'Modo Solo', (0, 255, 0), (255, 255, 255)),
            Button(400, 400, 200, 50, 'Consejos', (0, 0, 255), (blanco))
        ]

    def show(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))  # Corregido para mostrar el fondo
            for button in self.buttons:
                button.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.buttons[0].is_clicked(mouse_pos):
                        return "pelea_1vs1"
                    elif self.buttons[1].is_clicked(mouse_pos):
                        return "start"
                    elif self.buttons[2].is_clicked(mouse_pos):
                        return "tips"


class TipsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("C://Users//mende//Downloads//Hito//proyectopoo//recursos//fonts//consejos.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (1000, 600))
        self.font = pygame.font.Font(None, 36)
        self.back_button = Button(400, 500, 200, 50, "Regresar", (0, 0, 255), (blanco))

    def show(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_clicked(event.pos):
                        running = False

            self.screen.blit(self.background, (0, 0))  # Corregido para mostrar el fondo
            y = 50
            tips = [
                "Consejos sobre la buena alimentación:",
                "1. Come alimentos saludables.",
                "2. Evita consumir comida chatarra.",
                "3. Consume verduras.",
                "4. Evita el consumo excesivo de azúcares.",
                "5. Consume frutas.",


                "CONSEJOS SOBRE EL JUEGO",
                "1.Consejos para el modo 1VS1",
                "- Para que el personaje lance manzanas presionar tecla espacio mas tecla ¨f¨ ",
                "- Para que el enemigo lance amburguesas presionar teclas ¨o¨ mas ¨p¨",
                "2. Consejos para el modo solo:",
                "- para saltar presionar tecla ¨w¨",
                "- Para agacharse presionar tecla ¨s¨",
                "- Para disminuir las calorias presionar teclas ¨w¨ mas ¨r¨"



            ]
            for tip in tips:
                self.font = pygame.font.Font(None, 30)
                text = self.font.render(tip, True, (verde))
                self.screen.blit(text, (50, y))
                y += 32

            self.back_button.draw(self.screen)
            pygame.display.flip()

