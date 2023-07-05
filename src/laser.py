import pygame
from sprites import *
from enemigo import*
from enemigo_2 import*

class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y, speed , direccion_X,imagen):
        super().__init__()  #llama al constructor del padre
        
        self.image=pygame.transform.scale(
            pygame.image.load(imagen).convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
        self.rect.center= (x+5,y)#ubicacion del disparo
        self.velocidad_Y = speed
        self.direccion=direccion_X
    
    def update(self):
            self.rect.x += self.velocidad_Y
            if self.rect.left <= 0:
                self.kill()
            elif self.rect.right >= 1200: 
                self.kill()



      