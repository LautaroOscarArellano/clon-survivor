import pygame ,sys , random
from config import *
from personaje import Personaje
from plataformas import Plataforma
from laser import Laser
from enemigo import Enemigo
from enemigo_2 import Enemigo_2


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.is_playing=False
        self.sonido = ("./assets/sounds/laser.mp3")#sacar el hardcodeo
        """Fondos"""
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.fondo = pygame.image.load("./assets/images/city.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
        """"""
        self.a=0
        pygame.display.set_caption("Clon vs gatos")
        """Relog"""
        self.reloj=pygame.time.Clock()
        """Creacion de grupos"""
        self.sprites=pygame.sprite.Group()
        self.plataformas=pygame.sprite.Group()
        self.main_characters=pygame.sprite.Group()
        self.disparos=pygame.sprite.Group()
        self.enemigos=pygame.sprite.Group()
        self.enemigos_2=pygame.sprite.Group()

        self.generar_enemigos = True

        """cosas"""
        self.main_character=Personaje((0,400),self.enemigos)
        self.plataforma=Plataforma("./assets/images/plataforma.png",(10000,50),(0,400))
        self.enemigo = Enemigo("./assets/images/gato.png",(1200,400)) 
        self.enemigo_2 = Enemigo_2("./assets/images/gato2.jpg",(1100,30)) 
        """Agregar sprites"""
        self.sprites.add(self.main_character)
        self.sprites.add(self.plataforma)  
        self.sprites.add(self.enemigo)  
        self.sprites.add(self.enemigo_2)  
        """LA DUDA"""
        self.plataformas.add(self.plataforma)
        self.main_characters.add(self.main_character)
        self.disparos.add(self.disparos)
        self.enemigos.add(self.enemigo)
        self.enemigos_2.add(self.enemigo_2) 
        #   
     
    def play(self):
        self.is_playing=True
        while self.is_playing:
            self.reloj.tick(FPS)
            self.render()
            self.update()
            self.manejador_eventos()

    def manejador_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            elif event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                    self.main_character.velocidad_x = -SPEED_MC
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    self.main_character.velocidad_x  = SPEED_MC
                elif event.key == pygame.K_UP or event.key == pygame.K_w: 
                    self.main_character.salto=True
                elif event.key == pygame.K_DOWN  or event.key ==pygame.K_s: 
                    self.main_character.velocidad_y = SPEED_MC  
                elif event.key==pygame.K_SPACE:
                    self.main_character.salto=True
                elif event.key==pygame.K_x:
                    self.main_character.disparar(self.sonido, 5, self.sprites, self.disparos,self.enemigos)

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and (self.main_character.velocidad_x<0):  
                    self.main_character.velocidad_x=0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (self.main_character.velocidad_x> 0): 
                    self.main_character.velocidad_x=0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and (self.main_character.velocidad_y < 0): 
                    self.main_character.velocidad_y=0
                elif (event.key == pygame.K_DOWN  or event.key == pygame.K_s) and (self.main_character.velocidad_y > 0): 
                    self.main_character.velocidad_y=0
          

    def update(self):
        self.sprites.update() 
        #colision=pygame.sprite.collide_rect(self.main_character, self.plataforma)
        colision=pygame.sprite.spritecollide (self.main_character ,  self.plataformas,False )
        if colision:
            colision=colision[0] #<- fichar indices plataforma[0] , character[1]
            self.main_character.rect.bottom=colision.rect.top

        # for i in range(3):  # Genera 5 enemigos
        #     posicion=(1200,random.randrange(0,700))
        #     enemigo = Enemigo("./assets/images/gato.png",posicion)  # Cambia la posición de cada enemigo
        #     colision_2=pygame.sprite.spritecollide(self.enemigo , self.plataformas,False )
        #     if colision_2:
        #         colision_2=colision_2[0]
        #         self.enemigo.rect.bottom=colision_2.rect.top
        #         break
        # self.enemigos.add(enemigo)
        # self.sprites.add(enemigo)
        
        if self.generar_enemigos:   
            for i in range(5):  # Genera 3 enemigos
                posicion = (1200, random.randrange(0, 700))
                enemigo = Enemigo("./assets/images/gato.png", posicion)
                colision_2 = pygame.sprite.spritecollide(enemigo, self.plataformas, False)
                if colision_2:
                    colision_2 = colision_2[0]
                    enemigo.rect.bottom = colision_2.rect.top
                self.enemigos.add(enemigo)
                self.sprites.add(enemigo)
            self.generar_enemigos = False
            

        colision_3=pygame.sprite.spritecollide(self.enemigo_2 , self.plataformas,False )
        if colision_3:
            colision_3=colision_3[0]
            self.enemigo_2.rect.bottom=colision_3.rect.top
        #colision disparo contra el enemigo
        pygame.sprite.groupcollide(self.disparos, self.enemigos, True, True)
      
        
        


        
    

        # for i in colision:
        #     if i:
        #         print(i[0])
                # self.main_character.rect.y = 350
                # self.main_character.gravedad=0
                # self.a+=1
                # print("activadp" , self.a )
                # # else:
                # #     print("osa")
                # #     self.main_character.gravedad=2


        

    
    def render(self): 
        self.screen.blit(self.fondo , (0,0))
        self.screen.blit(self.plataforma.image ,self.plataforma.rect)
        self.sprites.draw(self.screen)
        pygame.display.flip()

jugar=Game() 
jugar.play()