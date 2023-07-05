import pygame

from config import *
from sprites import *

class Enemigo_2(pygame.sprite.Sprite):
    def __init__(self,  posicion:tuple):
        super().__init__()
        self.animaciones=get_animations()
        self.indice=0  
        self.image=self.animaciones[self.indice]  
        self.rect = self.image.get_rect()
        
        self.contador_animacion=0
        self.rect.center=posicion
        self.velocidad_x = -3
        self.velocidad_y = 2
        self.reset=0
        self.flag_movimiento=True

       

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.y <50:
            self.velocidad_y=2
        elif self.rect.y > 350 :
            self.velocidad_y = -2
  

        if self.velocidad_x < 0 :
            if self.flag_movimiento:
                self.indice=22
                self.flag_movimiento=False

            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1
                self.contador_animacion = 0
            if self.indice >= 24 :
                self.indice = 22#[1]

        self.image=self.animaciones[self.indice]
        if self.rect.x <= 0:
            self.kill()
     
