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
    [8,2,1,1,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,10,1,1,2,11],
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
ZOOM = 3
FPS = int(ORIGINAL_FPS)
SPEED_UNIT = ORIGINAL_SPEED_UNIT * ZOOM 

# tiles
TILE_SIZE = ORIGINAL_TILE_SIZE * ZOOM
TILES = []
for i in range(36):
    TILES.append(pygame.transform.scale(pygame.image.load("images/maze/" + str(i).zfill(2) + ".png"), (TILE_SIZE, TILE_SIZE)))

# score
SCORE = 0

# pacman
PACMAN = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
ROW = 4
COL = 1
OFFSET_X = 0
OFFSET_Y = 0
DX = 1
DY = 0

# directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# screen
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# clock
CLOCK = pygame.time.Clock()

# main loop control
RUNNING = True

###########################
# funtions and procedures #
###########################

def wall_collision(row, col):
    collision = False
    if col >= 0 and col < MAZE_WIDTH:
        if row >= 0 and row < MAZE_HEIGHT:
            if MAZE[row][col] > 2:
                collision = True
    return collision

def main():
    global RUNNING, PACMAN, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY, MAZE, SCORE
    
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

        # when pacman is on a junction point
        if OFFSET_X == 0 and OFFSET_Y == 0:

            # eat regular pellet
            if MAZE[ROW][COL] == 1:
                MAZE[ROW][COL] = 0
                SCORE += 10
            # eat power pellet
            elif MAZE[ROW][COL] == 2:
                MAZE[ROW][COL] = 0
                SCORE += 50

            # stop movement if there is a wall in front
            if wall_collision(ROW + DY, COL + DX):
                DX = 0
                DY = 0

            # look around for free paths
            up = not wall_collision(ROW - 1, COL)
            down = not wall_collision(ROW + 1, COL)
            left = not wall_collision(ROW, COL - 1)
            right = not wall_collision(ROW, COL + 1)

            # mark down where pacman can turn
            can_turn = [up, down, left, right]

            # check keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and not keys[pygame.K_DOWN] and can_turn[UP]:
                DX = 0
                DY = -1
            elif keys[pygame.K_DOWN] and not keys[pygame.K_UP] and can_turn[DOWN]:
                DX = 0
                DY = 1
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and can_turn[LEFT]:
                DX = -1
                DY = 0
            elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and can_turn[RIGHT]:
                DX = 1
                DY = 0

            # check for warp tunnels
            if COL == MAZE_WIDTH:
                COL = -1
                OFFSET_X = 0
            elif COL == -2:
                COL = MAZE_WIDTH
                OFFSET_X = 0
                       
        # move pacman
        if DX != 0 and DY == 0:
            OFFSET_X += DX
            if OFFSET_X == 7:
                OFFSET_X = 0
                COL += 1
            elif OFFSET_X == -1:
                OFFSET_X = 7
                COL -= 1
        if DX == 0 and DY != 0:
            OFFSET_Y += DY
            if OFFSET_Y == 7:
                OFFSET_Y = 0
                ROW += 1
            elif OFFSET_Y == -1:
                OFFSET_Y = 7
                ROW -= 1

        # draw maze
        for i, row in enumerate(MAZE):
            for j, tile in enumerate(row):
                if tile > 0:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))
                    # walls
                    if tile > 2:
                        pygame.draw.rect(SCREEN, "#333333", (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

        # calculate coordinates and draw pacman
        PACMAN.x = COL * TILE_SIZE + OFFSET_X * SPEED_UNIT
        PACMAN.y = ROW * TILE_SIZE + OFFSET_Y * SPEED_UNIT
        pygame.draw.rect(SCREEN, "#00FF00", PACMAN, 1)

        # show pacman's position
        print(f"ROW: {ROW}, COL:{COL}, OFFSET_X:{OFFSET_X}, OFFSET_Y:{OFFSET_Y}, SCORE:{SCORE}")

        # display current frame
        pygame.display.flip()

        # limit fps
        CLOCK.tick(FPS)  

    pygame.quit()

if __name__ == "__main__":
    main()