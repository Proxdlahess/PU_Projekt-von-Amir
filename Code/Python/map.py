# map.py
from dataclasses import dataclass
import pygame
import pytmx
import pyscroll

@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup

class MapManager:
    def __init__(self, screen, player):   
        self.maps = dict()  # "house" -> Map("house, group")
        self.screen = screen
        self.player = player
        self.current_map = "world"

        self.register_map("world")
        self.register_map("house1")

    def register_map(self, name):
        # Charger la carte classique
        tmx_data = pytmx.util_pygame.load_pygame("C:\\Users\\amird\\Desktop\\Programme python\\PU_projekt\\world.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        for obj in tmx_data.objects:
            print(obj.type)

        # Les collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collison":
                walls.append(pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)))

        # Dessiner les différents calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # Créer un objet map
        self.maps[name] = Map(name, walls, group)

    def get_map(self): 
        return self.maps[self.current_map]
        
    def get_group(self): 
        return self.get_map().group

    def get_walls(self): 
        return self.get_map().walls

    def update(self):
        
        self.get_group().update()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)
