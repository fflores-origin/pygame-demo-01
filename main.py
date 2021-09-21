import pygame
from pygame.constants import QUIT

pygame.init()

# CONST
FPS = 60
HEIGHT = 800
WIDTH = 400

# COLORS


# GAME SETTINGS
SCREEN = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('GAME')



test_surface = pygame.Surface((100,100))
test_surface.fill('Red')
def main():

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            handleExit(event)
            
        # DRAW ELEMENTS
        handleDraw()


        # UPDATE WINDOW
        pygame.display.update()
        clock.tick(FPS)

def handleDraw():

    SCREEN.blit(test_surface, (0,0))

    pass

def handleExit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

if __name__ == "__main__" :
    main()
    