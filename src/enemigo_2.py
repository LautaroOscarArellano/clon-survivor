import pygame
from config import *

class Enemigo_2(pygame.sprite.Sprite):
    def __init__(self, path_imagen:str , spawn:tuple):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image=pygame.transform.scale(
            pygame.image.load(path_imagen).convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (spawn)
        self.speed = 3
        self.gravedad=2

    def update(self):
        self.rect.x -= self.speed 
        self.rect.y += self.gravedad
  

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= 1200:
            self.rect.right = 1200
        elif self.rect.top <= 0:
                self.rect.top = 0 
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500