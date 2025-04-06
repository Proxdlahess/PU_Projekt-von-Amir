import pygame
import pytmx
import pygame
import pyscroll

def lahess():
    class Player(pygame.sprite.Sprite):

            def __init__(self, x, y):
                super().__init__()
                self.sprite_sheet = pygame.image.load("Player.png")
                self.image = self.get_image(0, 0)
                self.image.set_colorkey([0, 0, 0])
                self.rect = self.image.get_rect()
                self.position = [x, y]
                self.images = {
                    "down": self.get_image(0, 0),
                    "left": self.get_image(0, 32),
                    "right": self.get_image(0, 64),
                    "up": self.get_image(0, 96),
                }
                self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
                self.old_position = self.position.copy()
                self.speed = 3
            
            def save_location(self):
                self.old_position = self.position.copy()
            
            def change_animation(self, name): 
                self.image = self.images[name]
                self.image.set_colorkey((0, 0, 0))

        
            def move_right(self):
                self.position[0] += self.speed

            def move_left(self):
                self.position[0] -= self.speed

            def move_up(self):  
                self.position[1] -= self.speed
                
            def move_down(self):
                self.position[1] += self.speed

            
            def update(self):
                self.rect.topleft = self.position
                self.feet.midbottom = self.rect.midbottom

            def move_back(self):
                self.position = self.old_position
                self.rect.topleft = self.position
                self.feet.midbottom = self.rect.midbottom

            def get_image(self, x, y):
                image = pygame.Surface([32, 32])
                image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32 ))
                image.set_colorkey((0, 0, 0))
                return image

# player_file.py
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Player.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            "down": self.get_image(0, 0),
            "left": self.get_image(0, 32),
            "right": self.get_image(0, 64),
            "up": self.get_image(0, 96),
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 3

    def save_location(self):
        self.old_position = self.position.copy()

    def change_animation(self, name): 
        if name in self.images:
            self.image = self.images[name]
            self.image.set_colorkey((0, 0, 0))

    def move_right(self):
        self.position[0] += self.speed
        self.change_animation("right")

    def move_left(self):
        self.position[0] -= self.speed
        self.change_animation("left")

    def move_up(self):
        self.position[1] -= self.speed
        self.change_animation("up")
        
    def move_down(self):
        self.position[1] += self.speed
        self.change_animation("down")

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image
