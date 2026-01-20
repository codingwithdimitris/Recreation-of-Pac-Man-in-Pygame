import pygame

pygame.init()

####################
# global variables #
####################

# original game
ORIGINAL_FPS = 60.606061
ORIGINAL_TILE_SIZE = 8
ORIGINAL_SPEED_UNIT = 1     # pacman moves 1px on each movement call

# maze
MAZE = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,4,4,4,4,4,4,4,4,4,4,4,4,5,6,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,9,10,1,1,1,1,1,1,1,1,1,1,1,1,11],
    [8,1,12,13,13,14,1,12,13,13,13,14,1,9,10,1,12,13,13,13,14,1,12,13,13,14,1,11],
    [8,2,9,0,0,10,1,9,0,0,0,10,1,9,10,1,9,0,0,0,10,1,9,0,0,10,2,11],
    [8,1,15,16,16,17,1,15,16,16,16,17,1,15,17,1,15,16,16,16,17,1,15,16,16,17,1,11],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
    [8,1,12,13,13,14,1,12,14,1,12,13,13,13,13,13,13,14,1,12,14,1,12,13,13,14,1,11],
    [8,1,15,16,16,17,1,9,10,1,15,16,16,18,19,16,16,17,1,9,10,1,15,16,16,17,1,11],
    [8,1,1,1,1,1,1,9,10,1,1,1,1,9,10,1,1,1,1,9,10,1,1,1,1,1,1,11],
    [20,21,21,21,21,14,1,9,22,13,13,14,0,9,10,0,12,13,13,23,10,1,12,21,21,21,21,24],
    [0,0,0,0,0,8,1,9,19,16,16,17,0,15,17,0,15,16,16,18,10,1,11,0,0,0,0,0],
    [0,0,0,0,0,8,1,9,10,0,0,0,0,0,0,0,0,0,0,9,10,1,11,0,0,0,0,0],
    [0,0,0,0,0,8,1,9,10,0,25,21,26,27,27,28,21,29,0,9,10,1,11,0,0,0,0,0],
    [4,4,4,4,4,17,1,15,17,0,11,0,0,0,0,0,0,8,0,15,17,1,15,4,4,4,4,4],
    [0,0,0,0,0,0,1,0,0,0,11,0,0,0,0,0,0,8,0,0,0,1,0,0,0,0,0,0],
    [21,21,21,21,21,14,1,12,14,0,11,0,0,0,0,0,0,8,0,12,14,1,12,21,21,21,21,21],
    [0,0,0,0,0,8,1,9,10,0,30,4,4,4,4,4,4,31,0,9,10,1,11,0,0,0,0,0],
    [0,0,0,0,0,8,1,9,10,0,0,0,0,0,0,0,0,0,0,9,10,1,11,0,0,0,0,0],
    [0,0,0,0,0,8,1,9,10,0,12,13,13,13,13,13,13,14,0,9,10,1,11,0,0,0,0,0],
    [3,4,4,4,4,17,1,15,17,0,15,16,16,18,19,16,16,17,0,15,17,1,15,4,4,4,4,7],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,9,10,1,1,1,1,1,1,1,1,1,1,1,1,11],
    [8,1,12,13,13,14,1,12,13,13,13,14,1,9,10,1,12,13,13,13,14,1,12,13,13,14,1,11],
    [8,1,15,16,18,10,1,15,16,16,16,17,1,15,17,1,15,16,16,16,17,1,9,19,16,17,1,11],
    [8,2,1,1,9,10,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,9,10,1,1,2,11],
    [32,13,14,1,9,10,1,12,14,1,12,13,13,13,13,13,13,14,1,12,14,1,9,10,1,12,13,33],
    [34,16,17,1,15,17,1,9,10,1,15,16,16,18,19,16,16,17,1,9,10,1,15,17,1,15,16,35],
    [8,1,1,1,1,1,1,9,10,1,1,1,1,9,10,1,1,1,1,9,10,1,1,1,1,1,1,11],
    [8,1,12,13,13,13,13,23,22,13,13,14,1,9,10,1,12,13,13,23,22,13,13,13,13,14,1,11],
    [8,1,15,16,16,16,16,16,16,16,16,17,1,15,17,1,15,16,16,16,16,16,16,16,16,17,1,11],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11],
    [20,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,24],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
MAZE_WIDTH = len(MAZE[0])
MAZE_HEIGHT = len(MAZE)

# this game
FPS = int(ORIGINAL_FPS)
ZOOM = 3
SPEED_UNIT = ORIGINAL_SPEED_UNIT * ZOOM

# tiles
TILE_SIZE = ORIGINAL_TILE_SIZE * ZOOM
TILES = []
for i in range(36):
    TILES.append(pygame.transform.scale(pygame.image.load("images/maze/" + str(i).zfill(2) + ".png"), (TILE_SIZE, TILE_SIZE)))

# pacman
PACMAN = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
ROW = 4
COL = 1
OFFSET_X = 0
OFFSET_Y = 0
DX = 1
DY = 0

# screen
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# clock
CLOCK = pygame.time.Clock()

# main loop control
RUNNING = True

############################
# functions and procedures #
############################

def main():
    global RUNNING, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY
    
    while RUNNING:
        # poll for events
        for event in pygame.event.get():
            # [X] icon --> quit
            if event.type == pygame.QUIT:
                RUNNING = False
            # check keyboard
            if event.type == pygame.KEYDOWN:
                # ESC key --> quit
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False

        # clear screen
        SCREEN.fill("black")

        # check keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            DX = 0
            DY = -1
        elif keys[pygame.K_DOWN]:
            DX = 0
            DY = 1
        if keys[pygame.K_LEFT]:
            DX = -1
            DY = 0
        elif keys[pygame.K_RIGHT]:
            DX = 1
            DY = 0

        # move pacman
        if DX != 0 and DY == 0:
            OFFSET_X += DX
            if OFFSET_X == 8:
                OFFSET_X = 0
                COL += 1
            elif OFFSET_X == -1:
                OFFSET_X = 7
                COL -= 1
        elif DX == 0 and DY != 0:
            OFFSET_Y += DY
            if OFFSET_Y == 8:
                OFFSET_Y = 0
                ROW += 1
            elif OFFSET_Y == -1:
                OFFSET_Y = 7
                ROW -= 1

        # draw maze
        for i, row in enumerate(MAZE):
            for j, tile in enumerate(row):
                # draw only walls with a border around
                if tile > 2:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))
                    pygame.draw.rect(SCREEN, "#333333", (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        
        # calculate coordinates and draw pacman
        PACMAN.x = COL * TILE_SIZE + OFFSET_X * SPEED_UNIT
        PACMAN.y = ROW * TILE_SIZE + OFFSET_Y * SPEED_UNIT
        pygame.draw.rect(SCREEN, "#00FF00", PACMAN, 1)

        # display current frame
        pygame.display.flip()

        # limits FPS
        CLOCK.tick(FPS)  

    pygame.quit()

if __name__ == "__main__":
    main()