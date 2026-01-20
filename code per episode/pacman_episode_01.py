import pygame

pygame.init()

####################
# global variables #
####################

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pac-Man")
CLOCK = pygame.time.Clock()
RUNNING = True

def main():
    global RUNNING
    
    while RUNNING:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        # clear screen
        SCREEN.fill("black")

        # RENDER YOUR GAME HERE

        # display current frame
        pygame.display.flip()

        # limits FPS to 60
        CLOCK.tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()