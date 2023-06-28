from typing import Any
import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,path_imagen,size_platform,ubicacion) -> None:
        super().__init__()
        self.image=pygame.transform.scale(
            pygame.image.load(path_imagen).convert_alpha(),size_platform)
        self.rect=self.image.get_rect()
        self.rect.topleft = ubicacion
