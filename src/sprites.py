import pygame

def get_animations():
    #lista de surface
    animaciones = [
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 1.png").convert_alpha(),(100,100)),#0
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 2.png").convert_alpha(),(100,100)),#1
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 3.png").convert_alpha(),(100,100)),#2
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 4.png").convert_alpha(),(100,100)),#3
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 5.png").convert_alpha(),(100,100)),#4
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 6.png").convert_alpha(),(100,100)),#5
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 7.png").convert_alpha(),(100,100)),#6
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 8.png").convert_alpha(),(100,100)),#7
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 1.png").convert_alpha(),(100,100)),#8
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 2.png").convert_alpha(),(100,100)),#9
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 3.png").convert_alpha(),(100,100)),#10
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 4.png").convert_alpha(),(100,100)),#11
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 5.png").convert_alpha(),(100,100)),#12
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 6.png").convert_alpha(),(100,100)),#13
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 7.png").convert_alpha(),(100,100)),#14
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 8.png").convert_alpha(),(100,100)),#15
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon stand/quieto der.png").convert_alpha(),(100,100)),#16
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon stand/quieto iz.png").convert_alpha(),(100,100)),#17

        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#1/ground 1.png").convert_alpha(),(100,100)),#18
        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#1/ground 2.png").convert_alpha(),(100,100)),#19
        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#1/ground 3.png").convert_alpha(),(100,100)),#20
        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#1/ground 4.png").convert_alpha(),(100,100)),#21

        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#2/fly 1.png").convert_alpha(),(100,100)),#22
        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#2/fly 2.png").convert_alpha(),(100,100)),#23
        pygame.transform.scale(
        pygame.image.load("./assets/images/bug#2/fly 3.png").convert_alpha(),(100,100)),#24
        ]
    return animaciones