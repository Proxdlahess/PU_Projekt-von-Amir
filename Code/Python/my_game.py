# my_game.py
import pygame
import pytmx
import pyscroll
from map import MapManager
from player_file import Player

class Game:

    def __init__(self):
        self.running = True
        self.map = "world"
        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((1600, 680))
        pygame.display.set_caption("BasiqueGame")

        # Générer le joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()


    def update(self):
        self.map_manager.update()


    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            clock.tick(60)

        pygame.quit()
