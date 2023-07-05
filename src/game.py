import pygame ,sys , random
from config import *
from personaje import Personaje
from plataformas import Plataforma
from enemigo import Enemigo
from enemigo_2 import Enemigo_2
import json


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.sonido =pygame.mixer.Sound("./assets/sounds/blaster.mp3")#sacar el hardcodeo
        #Pantalla
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        #Menu principal
        self.menu=pygame.image.load("./assets/images/menu/menu.png").convert()
        self.menu=pygame.transform.scale( self.menu , (SIZE_SCREEN))
        #perder
        self.over=pygame.image.load("./assets/images/menu/game over.png").convert()
        self.over=pygame.transform.scale(self.over, (SIZE_SCREEN))
        #Puntaje
        self.puntaje=0
        #Background del juego
        self.fondo = pygame.image.load("./assets/images/niveles/city.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
        #Titulo
        pygame.display.set_caption("Clon survivor")
        #Relog
        self.reloj=pygame.time.Clock()
        #Creacion de grupos
        self.all_sprites=pygame.sprite.Group()
        self.plataformas=pygame.sprite.Group()
        self.main_characters=pygame.sprite.Group()
        self.disparos=pygame.sprite.Group()
        self.enemigo_terrestre=pygame.sprite.Group()
        self.enemigo_volador=pygame.sprite.Group()
        self.generar_enemigos = True
        self.contador=0
        self.contador_2=0
        #Constructores
        self.main_character=Personaje((0,400))
        self.plataforma=Plataforma("./assets/images/plataforma.png",(10000,50),(0,400))
        #Sprites
        self.all_sprites.add(self.main_character)
        self.all_sprites.add(self.plataforma)  
        #Añadir los elementos creados a sus grupos
        self.plataformas.add(self.plataforma)
        self.main_characters.add(self.main_character)
        self.disparos.add(self.disparos)
        #Flags
        self.esta_jugando=True
        self.generar_enemigos = True
        self.pantalla_inicio = True
        self.controlador_juego = False
        self.perdio = False
        #Flags para niveles
        self.flag_nivel2=True
        self.flag_nivel3=True
        self.flag_nivel4=True
        #Sistema de pausado
        self.pausa=False
        #Enemigos iniciales
        self.cantidad_enemigo_1=5
        self.cantidad_enemigo_2=5
        self.multiplicador_terrestre=2
        self.multiplicador_aereo=1
        #Fuente
        self.fuente_estandar = pygame.font.Font("./assets/fonts/starship-troopers/MOBILE4.TTF",30)
        #Registro de jugador
        self.jugador=0
        self.jugadores = {}#<- Para guardar el jugador en formato json
        #Musica
        pygame.mixer.music.load("./assets/sounds/sountrack.mp3")
        pygame.mixer.music.set_volume(0.5)  
        
        

    #Creacion de enemigos
    def agregar_sprite(self, sprite):
        self.all_sprites.add(sprite)  
    def agregar_enemigo_tipo1(self, enemigo): # agregar el enemigo creado a su grupo
            self.enemigo_terrestre.add(enemigo)
    def agregar_sprite_volador(self, sprite):
        self.all_sprites.add(sprite) 
    def agregar_enemigo_volador(self, enemigo): 
        self.enemigo_volador.add(enemigo)
     
    def play(self):
        pygame.mixer.music.play(-2)#loop
        while self.esta_jugando:
            if self.pantalla_inicio:
                self.menu_principal()
                
            if self.controlador_juego:  
                self.reloj.tick(FPS)
                self.render()
                self.update()
                self.event_handler()

            if self.perdio:
                self.guardar_puntaje()
                self.menu_game_over()
                self.esta_jugando=False
           
    def event_handler(self):
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
                    if self.pausa==False:#para que al pausar no se siga disparando
                        self.main_character.disparar(self.sonido, self.all_sprites, self.disparos)
                elif event.key==pygame.K_p:# al presionar cambia de estado
                    if self.pausa:
                        self.pausa = False
                    else:
                        self.pausa = True
  
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
        if self.pausa==False:
            self.generar_enemigo_terrestre()
            self.generar_enemigo_volador()
            
            #Colision jugador con plataforma
            colision=pygame.sprite.spritecollide(self.main_character ,  self.plataformas,False )
            if colision:
                colision=colision[0]
                self.main_character.rect.bottom=colision.rect.top

            #Colisiones disparo con enemigo
            colision_eemigo_1=pygame.sprite.groupcollide(self.disparos, self.enemigo_terrestre, True, True)
            if colision_eemigo_1:
                self.puntaje += 1 
            colision_eemigo_2=pygame.sprite.groupcollide(self.disparos, self.enemigo_volador, True, True)
            if colision_eemigo_2:
                self.puntaje += 5

            #Colision jugador con enemigo
            colision_muerte_1=pygame.sprite.groupcollide(self.main_characters, self.enemigo_terrestre, True, True)
            if colision_muerte_1:
                self.perdio=True
                self.controlador_juego=False
            colision_muerte_2=pygame.sprite.groupcollide(self.main_characters, self.enemigo_volador, True, True)
            if colision_muerte_2:
                self.perdio=True
                self.controlador_juego=False

            #Niveles
            if self.puntaje > 50  and self.flag_nivel2:
                self.fondo = pygame.image.load("./assets/images/niveles/city2.jpg").convert_alpha()
                self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
                self.multiplicador_terrestre=5
                self.multiplicador_aereo=3
                self.flag_nivel2=False
            if self.puntaje >100 and self.flag_nivel3:
                self.flag_nivel3=False
                self.fondo = pygame.image.load("./assets/images/niveles/oscure.png").convert_alpha()
                self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
                self.multiplicador_terrestre=10
                self.multiplicador_aereo=7
            if self.puntaje > 200 and self.flag_nivel4:
                self.fondo = pygame.image.load("./assets/images/niveles/caves.png").convert_alpha()
                self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
                self.multiplicador_terrestre=21
                self.multiplicador_aereo=17
                self.flag_nivel4=False
            self.all_sprites.update() 

    def render(self): 
        self.screen.blit(self.fondo , (0,0))
        self.screen.blit(self.fuente_estandar.render("Puntaje : "+str(self.puntaje) , True , "Blue"),(10,10))
        self.screen.blit(self.plataforma.image ,self.plataforma.rect)
        self.all_sprites.draw(self.screen)
        if self.pausa:
                fuente=pygame.font.Font("./assets/fonts/starship-troopers/MOBILE4.TTF",70)
                self.generar_texto("Juego pausado ",fuente,"Yellow",300,100)
                pygame.display.flip()
        pygame.display.flip()

    def menu_principal(self):
        if self.pantalla_inicio:
            self.screen.blit(self.menu,(0,0))
            fuente=pygame.font.Font("./assets/fonts/starship-troopers/MOBILE4.TTF",50)
            self.generar_texto("Clon Survivor",fuente,"White",380,50)
            self.generar_texto("Espacio para jugar",fuente,"White",320,200)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                elif event.type == pygame.KEYDOWN:                
                    if event.key == pygame.K_SPACE:
                        self.pantalla_inicio=False
                        self.controlador_juego=True

    def reinicar_juego(self):
        self.puntaje = 0
        self.all_sprites.empty()
        self.enemigo_terrestre.empty()
        self.enemigo_volador.empty()
        self.disparos.empty()
        #Constructores
        self.main_character=Personaje((0,400))
        self.plataforma=Plataforma("./assets/images/plataforma.png",(10000,50),(0,400))
        #Sprites
        self.all_sprites.add(self.main_character)
        self.all_sprites.add(self.plataforma)  
        #Añadir los elementos creados a sus grupos
        self.plataformas.add(self.plataforma)
        self.main_characters.add(self.main_character)
        self.disparos.add(self.disparos)
        self.perdio = False
        self.controlador_juego = False
        self.esta_jugando=True
        self.pantalla_inicio = True
        #Escenario
        self.fondo = pygame.image.load("./assets/images/niveles/city.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (SIZE_SCREEN))
        #flags niveles
        self.flag_nivel2=True
        self.flag_nivel3=True
        self.flag_nivel4=True

        self.play()

    def menu_game_over(self):
        flag  = True
        while flag:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_n:
                        flag = False
                    if evento.key ==pygame.K_y:
                        self.reinicar_juego()

            self.screen.blit(self.over,(0,0))
            self.generar_texto("Game over",self.fuente_estandar,"White",500,50)
            self.generar_texto(f"Score P{self.jugador} : {str(self.puntaje)}",self.fuente_estandar,"White",900,50)
            self.generar_texto("Continuar ? : Y o N",self.fuente_estandar,"White",450,150)
            pygame.display.flip()

    #Generador de texto                       
    def generar_texto(self,texto:str , fuente:str , texto_color:str , pos_x:int ,pos_y):
        imagen = fuente.render(texto,True,texto_color)
        self.screen.blit(imagen , (pos_x,pos_y))

    #Creacion de enemigos
    def generar_enemigo_terrestre(self):
        self.contador+=1 #delay para reaparicion de enemigos
        if self.contador== 1:
            if len(self.enemigo_terrestre) == 0: #si el grupo esta vacio 
                for i in range(self.cantidad_enemigo_1):
                    posicion=(random.randrange(1500, 2500), random.randrange(200, 400))
                    enemigo = Enemigo(posicion) 
                    self.agregar_enemigo_tipo1 (enemigo)
                    self.agregar_sprite(enemigo)     
        if self.contador>=500:
            self.contador=0 
            self.cantidad_enemigo_1+=2

    def generar_enemigo_volador(self):
        self.contador_2+=1 
        if self.contador_2== 500:
            if len(self.enemigo_volador) == 0: #si el grupo esta vacio 
                for i in range(self.cantidad_enemigo_2):
                    posicion=(random.randrange(1500, 2500), random.randrange(100, 250))
                    enemigo = Enemigo_2(posicion) 
                    self.agregar_enemigo_volador (enemigo)
                    self.agregar_sprite_volador(enemigo)

        if self.contador_2>=500:#tiempo en que aparescan los enemigos 
            self.contador_2=0
            self.cantidad_enemigo_2+=1

    def guardar_puntaje(self):
        self.jugador+=1
        self.jugadores[f"Jugador Numero {self.jugador}"]= self.puntaje
        with open("puntaje.json", "w") as archivo:
            json.dump(self.jugadores, archivo)
        pygame.mixer.music.stop() 


jugar=Game()  
jugar.play()

