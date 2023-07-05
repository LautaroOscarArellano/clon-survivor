import pygame,random
from config import *
from sprites import *


class Enemigo(pygame.sprite.Sprite):
    def __init__(self , posicion ):
        super().__init__()
        self.animaciones=get_animations()
        self.indice=0  
        self.image=self.animaciones[self.indice]  
        self.rect = self.image.get_rect()
        
        self.contador_animacion=0
        self.rect.center=posicion
        self.speed_x = -3
        self.gravedad=2
        self.reset=0
        self.flag_movimiento=True

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.gravedad#para que no aparesca flotando

        if self.rect.bottom >= 400:
            self.gravedad=0
            
        if self.speed_x < 0 :
            if self.flag_movimiento:
                self.indice=18
                self.flag_movimiento=False

            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1
                self.contador_animacion = 0
            if self.indice >= 21 :
                self.indice = 18

        self.image=self.animaciones[self.indice]

        if self.rect.x <= 0:
            self.kill()
     

