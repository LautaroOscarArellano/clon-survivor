import pygame
from sprites import *
from config import *
from laser import Laser

class Personaje(pygame.sprite.Sprite):
    def __init__(self , spawn_point : tuple) -> None:
        super().__init__()
    
        self.animaciones=get_animations()
        self.indice=0
        self.image=self.animaciones[self.indice]
        self.contador_animacion=0
        self.rect=self.image.get_rect()

        self.rect.center= spawn_point
        self.velocidad_x=0
        self.velocidad_y=0
        self.salto=False
        self.fuerza_salto=20
        self.gravedad=2
        self.flag_movimiento=True
        self.flag_direccion_derecha=True
        self.flag_direccion_izquierda=True
        self.velocidad_disparo=5
        
        
        

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.rect.y += self.gravedad

        #Movimiento derecha , flag para fixear el movimiento
        if self.velocidad_x > 0:
            if self.flag_movimiento:
                self.indice=8
                self.flag_movimiento=False
            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1
                self.contador_animacion = 0
            if self.indice >= 15:
                self.indice=8
            self.flag_direccion_derecha=True
            self.flag_direccion_izquierda=False

        #Movimiento izquierda , flag para fixear el movimiento
        if self.velocidad_x < 0 :
            self.flag_movimiento=True
            self.contador_animacion+=1
            if self.contador_animacion == 3:
                self.indice += 1
                self.contador_animacion = 0
            if self.indice >= 7 :
                self.indice = 0
            self.flag_direccion_derecha=False
            self.flag_direccion_izquierda=True
            

        #Quedarse quieto
        elif self.velocidad_x==0:
            if self.flag_direccion_derecha == True and (self.flag_direccion_izquierda != True):
                self.indice=16
                self.velocidad_disparo=5
    
            elif self.flag_direccion_derecha != True and (self.flag_direccion_izquierda == True):
                self.indice=17
                self.velocidad_disparo=-5
        self.image=self.animaciones[self.indice]
       
        #Colisiones con la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= 1200:
            self.rect.right = 1200
        elif self.rect.top <= 0:
                self.rect.top = 0 
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500

        #Saltar
        if self.salto:
            self.rect.y -=  self.fuerza_salto
            self.fuerza_salto-=1
            if self.fuerza_salto< -20:
                self.salto=False
                self.fuerza_salto=20


            
    def disparar(self, sound, sprites, disparos):
        if self.velocidad_x > 0:# disparar si mira a la derecha
            laser = Laser(self.rect.right, self.rect.centery,self.velocidad_disparo
            , self.velocidad_x,"./assets/images/clon shot/laserd.png")
            sound.play()
            sprites.add(laser)#?
            disparos.add(laser)#dibuja
        elif self.velocidad_x < 0: # disparar si mira a la izquierda
            laser = Laser(self.rect.left,self.rect.centery,self.velocidad_disparo 
            , self.velocidad_x ,"./assets/images/clon shot/laserz.png")
            sound = pygame.mixer.Sound(sound)
            sound.play()
            sprites.add(laser)
            disparos.add(laser)
        else:#disparar del lado que se quede mirando
            if self.flag_direccion_derecha != True and (self.flag_direccion_izquierda == True):
                x=self.rect.left
                y=self.rect.centery
                imagen="./assets/images/clon shot/laserz.png"

            if self.flag_direccion_derecha == True and (self.flag_direccion_izquierda != True):
                x=self.rect.right
                y=self.rect.centery
                imagen="./assets/images/clon shot/laserd.png"

            laser = Laser(x, y,self.velocidad_disparo , self.velocidad_x,imagen)
            sound = pygame.mixer.Sound(sound)
            sound.play()
            sprites.add(laser)
            disparos.add(laser)
     
        