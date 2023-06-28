import pygame
from sprites import *
from config import *
from laser import Laser


class Personaje(pygame.sprite.Sprite):
    def __init__(self , spawn_point : tuple,enemigos) -> None:
        super().__init__()
        
        # self.image=pygame.transform.scale(
        #     pygame.image.load(path_imagen).convert_alpha(),size_persona)
        self.animaciones=get_animations()
        self.indice=0
        self.image=self.animaciones[self.indice]
        self.contador_animacion=0
        self.controlador=True

        self.rect=self.image.get_rect()
        self.rect.center= spawn_point
        self.velocidad_x=0
        self.velocidad_y=0
        self.salto=False
        self.fuerza_salto=20
        self.gravedad=2
        self.enemigos=enemigos
        #self.sonido=pygame.mixer.Sound("./images/ork dead.mp3")
        

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.rect.y += self.gravedad

        """sprite moviendose derecha"""
        if self.velocidad_x > 0:
            print(self.velocidad_x)
            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1 
                self.contador_animacion = 0  
            if self.indice >= 7:
                self.indice = 0  
        #sprite moviendose izquierda"""            
        elif self.velocidad_x < 0:    
            #print(self.velocidad_x)
            if self.controlador:
                self.indice = 8
                self.controlador=False
            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1 
                self.contador_animacion = 0
            if self.indice >= 15:
                self.indice = 8
                self.controlador=True  
        self.image=self.image=self.animaciones[self.indice]

        
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= 1200:
            self.rect.right = 1200
        elif self.rect.top <= 0:
                self.rect.top = 0 
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500
        
        if self.salto:
            self.rect.y -=  self.fuerza_salto
            self.fuerza_salto-=1
            if self.fuerza_salto< -20:
                self.salto=False
                self.fuerza_salto=20


    def disparar(self, sound, speed, sprites, disparos,enemigo):
        laser = Laser(self.rect.right, self.rect.centery,speed,enemigo)
        sound = pygame.mixer.Sound(sound)
        sound.play()
        sprites.add(laser)#?
        disparos.add(laser)#dibuja
        ##
    