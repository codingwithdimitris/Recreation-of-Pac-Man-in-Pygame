import pygame, random

pygame.init()

####################
# global variables #
####################

# original game
ORIGINAL_FPS = 60.606061
ORIGINAL_TILE_SIZE = 8
ORIGINAL_SPEED_UNIT = 1     # characters move 1px on each movement call
ORIGINAL_MAX_SPEED = 1.25   # maximum speed is 1.25px per frame

# this game
FPS = int(ORIGINAL_FPS)
ZOOM = 3
SPEED_UNIT = ORIGINAL_SPEED_UNIT * ZOOM
MAX_SPEED = ORIGINAL_MAX_SPEED * ZOOM

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

# level
LEVEL = 0

# directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# pacman
PACMAN = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
ROW = 26
COL = 13
OFFSET_X = 4
OFFSET_Y = 0
DX = -1
DY = 0
ACC = 0
FACE = LEFT
PACMAN_ANIM = [
    [23, 23, 23, 24, 24, 24, 2, 2, 2, 24, 24, 24],  # up
    [31, 31, 31, 32, 32, 32, 2, 2, 2, 32, 32, 32],  # down
    [14, 14, 14, 15, 15, 15, 2, 2, 2, 15, 15, 15],  # left
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1],           # right
]
PACMAN_SPRITE_IDX = 0
PACMAN_SKIP_FRAMES = 0

# pacman's normal speed table
PACMAN_SPEED_NORMAL = [0.80]
PACMAN_SPEED_NORMAL.extend([0.90] * 3)
PACMAN_SPEED_NORMAL.extend([1.00] * 16)
PACMAN_SPEED_NORMAL.extend([0.90] * 236)

# pacman's speed table when in frightened mode
PACMAN_SPEED_FRIGHT = [0.90]
PACMAN_SPEED_FRIGHT.extend([0.95] * 3)
PACMAN_SPEED_FRIGHT.extend([1.00] * 252)

# pacman's start speed
PACMAN_SPEED = PACMAN_SPEED_NORMAL[LEVEL] * MAX_SPEED

# lives
LIVES = 3

# pellets
PELLETS = 0

# score
SCORE = 0
HIGH_SCORE = 0
SCORE_BLINK_COUNTER = 0
SCORE_BLINK_FULL_TIME = 48  # number of frames for a full cycle
SCORE_BLINK_HALF_TIME = int(SCORE_BLINK_FULL_TIME // 2)

# energizers
NRG_BLINK_COUNTER = 0
NRG_BLINK_FULL_TIME = 30  # number of frames for a full cycle
NRG_BLINK_HALF_TIME = int(NRG_BLINK_FULL_TIME // 2)

# bonus items
# 33: 🍒 Cherry 100,    34: 🍓 Strawberry 300,  35: 🟠 Orange 500,  36: 🍎 Apple 700, 
# 37: 🍈 Melon 1000,    38: 🚀 Galaxian 2000,   39: 🔔 Bell 3000,   40: 🔑 Key 5000
ITEMS = [33, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]
ITEMS.extend([40] * 244)
ITEM_POINTS = [100, 300, 500, 500, 700, 700, 1000, 1000, 2000, 2000, 3000, 3000]
ITEM_POINTS.extend([5000] * 244)
ITEM_POINTS_SPRITE = [98, 99, 100, 100, 101, 101, 102, 102, 109, 109, 115, 115]
ITEM_POINTS_SPRITE.extend([121] * 244)
ITEM_DISPLAY_TIME = 10 * FPS        # number of frames that item stays on screen (10 sec)
ITEM_POINTS_TIME = 2 * FPS          # number of frames that points stays on screen (2 sec)
ITEM_PELLETS1 = 70                  # show item after ITEM_PELLETS1 pellets eaten
ITEM_PELLETS2 = 140                 # show item after ITEM_PELLETS2 pellets eaten
ITEM_VISIBLE = False                # true when item is visible
ITEM = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
ITEM.x = 13 * TILE_SIZE
ITEM.y = 20 * TILE_SIZE - HALF_TILE
ITEM_LIST = []
for i in range(max(0, LEVEL - 6), LEVEL + 1, 1): ITEM_LIST.append(ITEMS[i])

# ghosts
G = []
for i in range(4):
    G.append(pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE))
G_ROW = [14, 14, 14, 14]
G_COL = [13, 15, 11, 17]
G_OFF_X = [4, 4, 4, 4]
G_OFF_Y = [0, 0, 0, 0]
G_DX = [-1, -1, 1, 1]
G_DY = [0, 0, 0, 0]
G_ACC = [0, 0, 0, 0]
G_ANIM = [
    [   # blinky
        [45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46], # up
        [47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48], # down
        [43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44], # left
        [41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42]  # right
    ],
    [   # pinky
        [57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58],  # up
        [59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60],  # down
        [55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56],  # left
        [53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54]   # right
    ],
    [   # inky
        [69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70],  # up
        [71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72],  # down
        [67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68],  # left
        [65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66]   # right
    ],
    [   # clyde
        [82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83],  # up
        [84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85],  # down
        [80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81],  # left
        [78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79]   # right
    ]
]
G_FACE = [LEFT, LEFT, RIGHT, RIGHT]
G_SPRITE_IDX = [0, 0, 0, 0]

# ghost normal speed table
G_SPEED_NORMAL = [0.75, 0.85, 0.85, 0.85]
G_SPEED_NORMAL.extend([0.95] * 252)

# ghost speed table when entering or leaving a tunnel
G_SPEED_TUNNEL = [0.40, 0.45, 0.45, 0.45]
G_SPEED_TUNNEL.extend([0.50] * 252)

# ghost speed table when in frightened mode
G_SPEED_FRIGHT = [0.50, 0.55, 0.55, 0.55]
G_SPEED_FRIGHT.extend([0.60] * 252)

# ghost's start speed
G_SPEED = [G_SPEED_NORMAL[LEVEL] * MAX_SPEED] * 4

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

def clear_screen():
    SCREEN.fill("black")

def draw_ghosts():
    global G_SPRITE_IDX
    for i in range(len(G)):
        SCREEN.blit(SPRITES[G_ANIM[i][G_FACE[i]][G_SPRITE_IDX[i]]], (G[i].x - HALF_TILE, G[i].y - HALF_TILE))
        G_SPRITE_IDX[i] += 1
        if G_SPRITE_IDX[i] == len(G_ANIM[i][G_FACE[i]]): G_SPRITE_IDX[i] = 0

def draw_pacman():
    SCREEN.blit(SPRITES[PACMAN_ANIM[FACE][PACMAN_SPRITE_IDX]], (PACMAN.x - HALF_TILE, PACMAN.y - HALF_TILE))
    #pygame.draw.rect(SCREEN, "#FFFF00", PACMAN, 1)

def draw_maze():
    # draw maze
    for i, row in enumerate(MAZE):
        for j, tile in enumerate(row):
            if tile == 2: # energizer
                if NRG_BLINK_COUNTER < NRG_BLINK_HALF_TIME:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))    
            elif tile > 0:
                SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))

def handle_bonus_item():
    global ITEM_VISIBLE, ITEM_DISPLAY_TIME, ITEM_POINTS_TIME, SCORE

    # show bonus items
    if ITEM_VISIBLE:
        if ITEM_DISPLAY_TIME > 0:
            SCREEN.blit(SPRITES[ITEMS[LEVEL]], (ITEM.x, ITEM.y))
            ITEM_DISPLAY_TIME -= 1
            if ITEM_DISPLAY_TIME == 0:
                ITEM_DISPLAY_TIME = 10 * FPS
                ITEM_POINTS_TIME = 2 * FPS
                ITEM_VISIBLE = False
            # check collision with pacman
            elif PACMAN.colliderect(ITEM):
                SCORE += ITEM_POINTS[LEVEL]
                ITEM_DISPLAY_TIME = 0
        else:
            if ITEM_POINTS_TIME > 0:
                SCREEN.blit(SPRITES[ITEM_POINTS_SPRITE[LEVEL]], (ITEM.x, ITEM.y))
                if ITEM_POINTS_SPRITE[LEVEL] == 102:
                    SCREEN.blit(SPRITES[ITEM_POINTS_SPRITE[LEVEL] + 1], (ITEM.x + DOUBLE_TILE, ITEM.y))
                elif ITEM_POINTS_SPRITE[LEVEL] > 102:
                    SCREEN.blit(SPRITES[ITEM_POINTS_SPRITE[LEVEL] - 1], (ITEM.x - DOUBLE_TILE, ITEM.y))
                    SCREEN.blit(SPRITES[ITEM_POINTS_SPRITE[LEVEL] + 1], (ITEM.x + DOUBLE_TILE, ITEM.y))
                ITEM_POINTS_TIME -= 1
            else:
                ITEM_VISIBLE = False
                ITEM_DISPLAY_TIME = 10 * FPS
                ITEM_POINTS_TIME = 2 * FPS

def move_ghosts():

    global G_ACC, G_ROW, G_COL, G_OFF_X, G_OFF_Y, G_DX, G_DY, G_FACE, G_SPEED

    # move ghosts
    for i in range(len(G)):

        # add ghost's speed to the fractional accumulator
        G_ACC[i] += G_SPEED[i]

        # if accumulator is greater or equal to game's speed unit,
        # move ghost at least one time
        while  G_ACC[i] >= SPEED_UNIT:

            # when ghost in inside the maze
            if G_COL[i] >= 0 and G_COL[i] < MAZE_WIDTH - 1:

                # if ghost is on a junction point
                if G_OFF_X[i] == 0 and G_OFF_Y[i] == 0:

                    # create a list for adding the free paths where the ghost can turn
                    can_turn = []

                    # look around, add all free path directions to the list
                    if not wall_collision(G_ROW[i] - 1, G_COL[i]) and not G_DY[i] == 1:
                        if not((G_ROW[i] == 14 or G_ROW[i] == 26) and (G_COL[i] == 12 or G_COL[i] == 15)): 
                            can_turn.append([0, -1])
                    if not wall_collision(G_ROW[i] + 1, G_COL[i]) and not G_DY[i] == -1: can_turn.append([0, 1])
                    if not wall_collision(G_ROW[i], G_COL[i] - 1) and not G_DX[i] == 1: can_turn.append([-1, 0])
                    if not wall_collision(G_ROW[i], G_COL[i] + 1) and not G_DX[i] == -1: can_turn.append([1, 0])

                    # pick a random direction
                    dir = random.choice(can_turn)

                    # set the new direction
                    G_DX[i] = dir[0]
                    G_DY[i] = dir[1]

                    # set face for animation
                    match dir:
                        case [ 0, -1]: G_FACE[i] = UP
                        case [ 0,  1]: G_FACE[i] = DOWN
                        case [-1,  0]: G_FACE[i] = LEFT
                        case [ 1,  0]: G_FACE[i] = RIGHT

            # move ghost
            G_OFF_X[i] += G_DX[i]
            G_OFF_Y[i] += G_DY[i]
            if G_OFF_X[i] == 8:
                G_OFF_X[i] = 0
                G_COL[i] += 1
            elif G_OFF_X[i] == -1:
                G_OFF_X[i] = 7
                G_COL[i] -= 1
            elif G_OFF_Y[i] == 8:
                G_OFF_Y[i] = 0
                G_ROW[i] += 1
            elif G_OFF_Y[i] == -1:
                G_OFF_Y[i] = 7
                G_ROW[i] -= 1

            # check for wrap tunnels
            if G_COL[i] == MAZE_WIDTH:
                G_COL[i] = -1
                G_OFF_X[i] = 0
            elif G_COL[i] == -2:
                G_COL[i] = MAZE_WIDTH
                G_OFF_X[i] = 0

            # adjust ghost speed when entering a tunnel
            if G_ROW[i] == 17 and (G_COL[i] < 5 or G_COL[i] > 22):
                G_SPEED[i] = G_SPEED_TUNNEL[LEVEL] * SPEED_UNIT
            else:
                G_SPEED[i] = G_SPEED_NORMAL[LEVEL] * SPEED_UNIT

            # update ghost position
            G[i].x = G_COL[i] * TILE_SIZE + G_OFF_X[i] * SPEED_UNIT
            G[i].y = G_ROW[i] * TILE_SIZE + G_OFF_Y[i] * SPEED_UNIT

            # reduce fractional accumulator by speed unit
            G_ACC[i] -= SPEED_UNIT

def move_pacman():

    global ACC, PACMAN_SPEED, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY, FACE
    global MAZE, PELLETS, SCORE, HIGH_SCORE, PACMAN_SKIP_FRAMES, PACMAN_SPRITE_IDX, ITEM_VISIBLE

    # add pacman's speed to the fractional accumulator
    ACC += PACMAN_SPEED

    # if accumulator is greater or equal to game's speed unit,
    # move pacman at least one time
    while ACC >= SPEED_UNIT:

        # check keys
        keys = pygame.key.get_pressed()

        # when pacman is inside the maze
        if COL >= 0 and COL < MAZE_WIDTH - 1:

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
                    PELLETS += 1
                    if PELLETS == ITEM_PELLETS1 or PELLETS == ITEM_PELLETS2 and not ITEM_VISIBLE:
                        ITEM_VISIBLE = True
                    PACMAN_SKIP_FRAMES += 1
                # eat power pellet
                elif MAZE[ROW][COL] == 2:
                    MAZE[ROW][COL] = 0
                    SCORE += 50
                    if SCORE >= HIGH_SCORE: HIGH_SCORE = SCORE
                    PELLETS += 1
                    if PELLETS == ITEM_PELLETS1 or PELLETS == ITEM_PELLETS2 and not ITEM_VISIBLE:
                        ITEM_VISIBLE = True
                    PACMAN_SKIP_FRAMES += 3

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

        # check for wrap tunnels
        if COL == MAZE_WIDTH:
            COL = -1
            OFFSET_X = 0
        elif COL == -2:
            COL = MAZE_WIDTH
            OFFSET_X = 0

        # if there is no need for skipping this frame
        if PACMAN_SKIP_FRAMES == 0:
            # move pacman
            OFFSET_X += DX
            OFFSET_Y += DY
            if OFFSET_X == 8:
                OFFSET_X = 0
                COL += 1
            elif OFFSET_X == -1:
                OFFSET_X = 7
                COL -= 1
            elif OFFSET_Y == 8:
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
        # else reduce the skipping frame counter by one
        else:
            PACMAN_SKIP_FRAMES -= 1

        # update pacman's position
        PACMAN.x = COL * TILE_SIZE + OFFSET_X * SPEED_UNIT
        PACMAN.y = ROW * TILE_SIZE + OFFSET_Y * SPEED_UNIT
        
        # reduce fractional accumulator by speed unit
        ACC -= SPEED_UNIT

def poll_events():
    global RUNNING

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
    global PELLETS, ITEM_VISIBLE, ITEM_DISPLAY_TIME, ITEM_POINTS_TIME
    global PACMAN_SKIP_FRAMES, ACC
    global G, G_ROW, G_COL, G_OFF_X, G_OFF_Y, G_DX, G_DY, G_ACC, G_SPEED, G_SPRITE_IDX, G_FACE
    
    while RUNNING:

        poll_events()

        clear_screen()

        move_pacman()

        move_ghosts()

        draw_maze()

        handle_bonus_item()

        draw_pacman()

        draw_ghosts()
        

        # draw score
        if SCORE_BLINK_COUNTER < SCORE_BLINK_HALF_TIME: type("1UP", 0, 3)
        if SCORE == 0:
            type("00", 1, 5)
        else:
            type(str(SCORE).rjust(7, " "), 1, 0)

        # draw high score
        type("HIGH SCORE", 0, 9)
        if HIGH_SCORE > 0: type(str(HIGH_SCORE).rjust(8, " "), 1, 9)

        # draw remaining lives (COLS: 2, 4, 6, 8, 10)
        for life, col in enumerate(range(2, 11, 2)):
            if life < LIVES - 1:
                SCREEN.blit(SPRITES[15], (col * TILE_SIZE, 34 * TILE_SIZE))

        # draw bonus items on bottom (COLS: 24, 22, 20, 18, 16, 14, 12)
        for item, col in enumerate(range(24, 11, -2)):
            if item < len(ITEM_LIST):
                SCREEN.blit(SPRITES[ITEM_LIST[item]], (col * TILE_SIZE, 34 * TILE_SIZE))
        
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