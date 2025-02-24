import pygame
from proyectopoo.source.menu.menu import MainMenu, TipsScreen
from proyectopoo.source.solitario.desde0 import Juego
from proyectopoo.source.pelea.mi_pelea import JuegoPelea

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Battle for Nutrition")
    menu = MainMenu(pantalla)

    while True:
        option = menu.show()
        if option == "start":
            juego = Juego(1000, 600)
            juego.main()
        elif option == "tips":
            tips = TipsScreen(pantalla)
            tips.show()
        elif option == "pelea_1vs1":
            juego_pelea = JuegoPelea()
            juego_pelea.ejecutar()


main()
