import pygame
class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y, speed, enemigo):
        super().__init__()  #llama al constructor del padre
        
        self.image = pygame.Surface((30, 5))

        self.image=pygame.transform.scale(
            pygame.image.load("./assets/images/clon shot/laser.png").convert_alpha(),(100,100))
        self.rect = self.image.get_rect()
        self.rect.center= (x+5,y)#ubicacion del disparo
        self.enemigo =enemigo 

        self.velocidad_Y = speed
    
    def update(self):
        self.rect.x += self.velocidad_Y
        colisiones = pygame.sprite.spritecollide(self, self.enemigo, True)
        if colisiones:
            self.kill()
