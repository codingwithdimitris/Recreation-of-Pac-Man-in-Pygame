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
HALF_TILE = int(TILE_SIZE // 2)
DOUBLE_TILE = TILE_SIZE * 2
TILES = []
for i in range(36):
    TILES.append(pygame.transform.scale(pygame.image.load("images/maze/" + str(i).zfill(2) + ".png"), (TILE_SIZE, TILE_SIZE)))

# sprites 
SPRITES = []
for i in range(125):
    SPRITES.append(pygame.transform.scale(pygame.image.load("images/sprites/" + str(i).zfill(3) + ".png"), (DOUBLE_TILE, DOUBLE_TILE)))

# font
FONT = pygame.font.Font("font/press_start_2p.ttf", TILE_SIZE)

# scores
SCORE = 0
HIGH_SCORE = 0
SCORE_BLINK_COUNTER = 0
SCORE_BLINK_FULL_TIME = 48  # number of frames for a full cycle
SCORE_BLINK_HALF_TIME = int(SCORE_BLINK_FULL_TIME // 2)

# energizers
NRG_BLINK_COUNTER = 0
NRG_BLINK_FULL_TIME = 30  # number of frames for a full cycle
NRG_BLINK_HALF_TIME = int(NRG_BLINK_FULL_TIME // 2)

# directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# pacman
PACMAN = pygame.Rect(0, 0, DOUBLE_TILE, DOUBLE_TILE)
ROW = 26
COL = 13
OFFSET_X = 4
OFFSET_Y = 0
DX = -1
DY = 0
FACE = LEFT
PACMAN_ANIM = [
    [23, 23, 23, 24, 24, 24, 2, 2, 2, 24, 24, 24],  # up
    [31, 31, 31, 32, 32, 32, 2, 2, 2, 32, 32, 32],  # down
    [14, 14, 14, 15, 15, 15, 2, 2, 2, 15, 15, 15],  # left
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1],           # right
]
PACMAN_SPRITE_IDX = 0

# lives
LIVES = 3

# screen
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")
pygame.mouse.set_visible(False)

# clock
CLOCK = pygame.time.Clock()

# main loop control
RUNNING = True

############################
# functions and procedures #
############################

def type(string, row, col):
    text = FONT.render(string, False, "#dedeff")
    SCREEN.blit(text, (col * TILE_SIZE, row * TILE_SIZE))

def wall_collision(row, col):
    collision = False
    if row >= 0 and row < MAZE_HEIGHT:
        if col >= 0 and col < MAZE_WIDTH:
            if MAZE[row][col] > 2:
                collision = True
    return collision

def main():
    global RUNNING, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY, SCORE, HIGH_SCORE
    global PACMAN_SPRITE_IDX, FACE, SCORE_BLINK_COUNTER, NRG_BLINK_COUNTER
    
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

        # when pacman is inside the maze
        if ROW >= 0 and ROW < MAZE_HEIGHT:
            if COL >= 0 and COL < MAZE_WIDTH:

                # early turning
                if OFFSET_X == 7 and DX == 1:
                    dir_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]     # -1: up, 0: nothing, 1: down
                    if dir_y != 0 and not wall_collision(ROW + dir_y, COL + 1):
                        COL += 1
                        OFFSET_X = 0
                        OFFSET_Y = 0
                        DX = 0
                        DY = dir_y
                elif OFFSET_X == 1 and DX == -1:
                    dir_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]     # -1: up, 0: nothing, 1: down
                    if dir_y != 0 and not wall_collision(ROW + dir_y, COL):
                        OFFSET_X = 0
                        OFFSET_Y = 0
                        DX = 0
                        DY = dir_y

                if OFFSET_Y == 1 and DY == -1:
                    dir_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]     # -1: left, 0: nothing, 1: right
                    if dir_x != 0 and not wall_collision(ROW, COL + dir_x):
                        OFFSET_X = 0
                        OFFSET_Y = 0
                        DX = dir_x
                        DY = 0
                elif OFFSET_Y == 7 and DY == 1:
                    dir_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]     # -1: left, 0: nothing, 1: right
                    if dir_x != 0 and not wall_collision(ROW + 1, COL + dir_x):
                        ROW += 1
                        OFFSET_X = 0
                        OFFSET_Y = 0
                        DX = dir_x
                        DY = 0                

                # if pacman is on a junction point
                if OFFSET_X == 0 and OFFSET_Y == 0:

                    # eat pellet
                    if MAZE[ROW][COL] == 1:
                        MAZE[ROW][COL] = 0
                        SCORE += 10
                        if SCORE >= HIGH_SCORE: HIGH_SCORE = SCORE
                    # eat power pellet
                    elif MAZE[ROW][COL] == 2:
                        MAZE[ROW][COL] = 0
                        SCORE += 50
                        if SCORE >= HIGH_SCORE: HIGH_SCORE = SCORE

                    # stop movement if there is a wall in front
                    if wall_collision(ROW + DY, COL + DX):
                        DX = 0
                        DY = 0

                    # check arrow keys and free pathways
                    dir_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]     # -1: up, 0: nothing, 1: down
                    if dir_y != 0 and not wall_collision(ROW + dir_y, COL):
                        DX = 0
                        DY = dir_y
                    dir_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]  # -1: left, 0: nothing, 1: right
                    if  dir_x != 0 and not wall_collision(ROW, COL + dir_x):
                        DX = dir_x
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

            # animate pacman
            if DX != 0 or DY != 0:
                if   DY == -1: FACE = UP
                elif DY ==  1: FACE = DOWN
                elif DX == -1: FACE = LEFT
                elif DX ==  1: FACE = RIGHT
                PACMAN_SPRITE_IDX += 1
                if PACMAN_SPRITE_IDX >= len(PACMAN_ANIM[FACE]): PACMAN_SPRITE_IDX = 0

        # draw maze
        for i, row in enumerate(MAZE):
            for j, tile in enumerate(row):
                if tile == 2: # energizer
                    if NRG_BLINK_COUNTER < NRG_BLINK_HALF_TIME:
                        SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))    
                elif tile > 0:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))
        
        # calculate coordinates and draw pacman
        PACMAN.x = COL * TILE_SIZE + OFFSET_X * SPEED_UNIT - HALF_TILE
        PACMAN.y = ROW * TILE_SIZE + OFFSET_Y * SPEED_UNIT - HALF_TILE
        #pygame.draw.rect(SCREEN, "#FFFF00", PACMAN, 1)
        SCREEN.blit(SPRITES[PACMAN_ANIM[FACE][PACMAN_SPRITE_IDX]], (PACMAN.x, PACMAN.y))

        # draw score
        if SCORE_BLINK_COUNTER < SCORE_BLINK_HALF_TIME: type("1UP", 0, 3)
        type(str(SCORE).rjust(7, " "), 1, 0)

        # draw high score
        type("HIGH SCORE", 0, 9)
        type(str(HIGH_SCORE).rjust(8, " "), 1, 9)

        # draw remaining lives
        for life, col in enumerate(range(2, 7, 2)):
            if life < LIVES - 1:
                SCREEN.blit(SPRITES[15], (col * TILE_SIZE, 34 * TILE_SIZE))

        # blinking items
        SCORE_BLINK_COUNTER += 1
        if SCORE_BLINK_COUNTER == SCORE_BLINK_FULL_TIME: SCORE_BLINK_COUNTER = 0
        NRG_BLINK_COUNTER += 1
        if NRG_BLINK_COUNTER == NRG_BLINK_FULL_TIME: NRG_BLINK_COUNTER = 0

        # display current frame
        pygame.display.flip()

        # limits FPS
        CLOCK.tick(FPS)  

    pygame.mouse.set_visible(True)
    pygame.quit()

if __name__ == "__main__":
    main()