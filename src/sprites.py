import pygame

def get_animations():
    #lista de surface
    animaciones = [pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 1.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 2.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 3.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 4.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 5.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 6.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 7.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/dcorrer 8.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 1.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 2.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 3.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 4.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 5.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 6.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 7.png").convert_alpha(),(100,100)),
        pygame.transform.scale(
        pygame.image.load("./assets/images/clon running/zcorrer 8.png").convert_alpha(),(100,100)),
        
        ]
    return animaciones