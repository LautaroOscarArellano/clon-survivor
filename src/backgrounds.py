import pygame
from config import SIZE_SCREEN

class Background(pygame.sprite.Sprite):
    def __init__(self, path_imagen) -> None:
        self.image=path_imagen
        self.size_background=SIZE_SCREEN
    def update(self):
        pass
