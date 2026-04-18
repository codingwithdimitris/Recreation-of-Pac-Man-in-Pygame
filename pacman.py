import pygame, random, math

pygame.init()

####################
# global variables #
####################

# original game
ORIGINAL_FPS = 60.606061
ORIGINAL_TILE_SIZE = 8
ORIGINAL_SPEED_UNIT = 1     # characters move 1px on each movement call
ORIGINAL_MAX_SPEED = 1.25   # maximum speed is 1.25px per frame

# maze
ORIGINAL_MAZE = [
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
MAZE_WIDTH = len(ORIGINAL_MAZE[0])
MAZE_HEIGHT = len(ORIGINAL_MAZE)

# this game
FPS = int(ORIGINAL_FPS)
ZOOM = int(pygame.display.Info().current_h // (ORIGINAL_TILE_SIZE * MAZE_HEIGHT))
SPEED_UNIT = ORIGINAL_SPEED_UNIT * ZOOM
MAX_SPEED = ORIGINAL_MAX_SPEED * ZOOM

# tiles
TILE_SIZE = ORIGINAL_TILE_SIZE * ZOOM
HALF_TILE = int(TILE_SIZE // 2)
DOUBLE_TILE = TILE_SIZE * 2
TILES = []
for i in range(72):
    TILES.append(pygame.transform.scale(pygame.image.load("images/maze/" + str(i).zfill(2) + ".png"), (TILE_SIZE, TILE_SIZE)))

# sprites 
SPRITES = []
for i in range(125):
    SPRITES.append(pygame.transform.scale(pygame.image.load("images/sprites/" + str(i).zfill(3) + ".png"), (DOUBLE_TILE, DOUBLE_TILE)))

# symbols
SYMBOLS = []
for i in range(5):
    SYMBOLS.append(pygame.transform.scale(pygame.image.load("images/symbols/" + str(i).zfill(2) + ".png"), (TILE_SIZE, TILE_SIZE)))

# font
FONT = pygame.font.Font("font/press_start_2p.ttf", TILE_SIZE)

# colors
ORANGE = "#FFB851"
CYAN = "#00FFFF"
PINK = "#FFB8AE"
MAGENTA = "#FFB8FF"

# directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# faces
DEATH = 4

# pacman
PACMAN = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
PACMAN_ANIM = [
    [23, 23, 23, 24, 24, 24, 2, 2, 2, 24, 24, 24],  # up
    [31, 31, 31, 32, 32, 32, 2, 2, 2, 32, 32, 32],  # down
    [14, 14, 14, 15, 15, 15, 2, 2, 2, 15, 15, 15],  # left
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1],           # right
]
death_anim = []
for sprite in range(3, 14):
    for i in range(8):
        death_anim.append(sprite)
PACMAN_ANIM.append(death_anim)

# pacman's normal speed table
PACMAN_SPEED_NORMAL = [0.80]
PACMAN_SPEED_NORMAL.extend([0.90] * 3)
PACMAN_SPEED_NORMAL.extend([1.00] * 16)
PACMAN_SPEED_NORMAL.extend([0.90] * 236)

# pacman's speed table when in frightened mode
PACMAN_SPEED_FRIGHT = [0.90]
PACMAN_SPEED_FRIGHT.extend([0.95] * 3)
PACMAN_SPEED_FRIGHT.extend([1.00] * 252)

# bonus items
# 33: 🍒 Cherry 100,    34: 🍓 Strawberry 300,  35: 🟠 Orange 500,  36: 🍎 Apple 700, 
# 37: 🍈 Melon 1000,    38: 🚀 Galaxian 2000,   39: 🔔 Bell 3000,   40: 🔑 Key 5000
ITEMS = [33, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]
ITEMS.extend([40] * 244)
ITEM_POINTS = [100, 300, 500, 500, 700, 700, 1000, 1000, 2000, 2000, 3000, 3000]
ITEM_POINTS.extend([5000] * 244)
ITEM_POINTS_SPRITE = [98, 99, 100, 100, 101, 101, 102, 102, 109, 109, 115, 115]
ITEM_POINTS_SPRITE.extend([121] * 244)
ITEM_PELLETS1 = 70                  # show item after ITEM_PELLETS1 pellets eaten
ITEM_PELLETS2 = 140                 # show item after ITEM_PELLETS2 pellets eaten
ITEM = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
ITEM.x = 13 * TILE_SIZE
ITEM.y = 20 * TILE_SIZE - HALF_TILE

# ghosts
G = []
for i in range(4):
    G.append(pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE))
G_FIXED_TARGET = [(0, 25), (0, 2), (34, 27), (34, 0)]
G_ANIM = [
    [   # blinky
        [45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46], # up
        [47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48], # down
        [43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44], # left
        [41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42], # right
        [49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50], # frightened blue
        [51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52], # frightened white
        [90] * 16, # 200
        [91] * 16, # 400
        [92] * 16, # 800
        [93] * 16, # 1600
        [63] * 16, # eyes up
        [64] * 16, # eyes down
        [62] * 16, # eyes left
        [61] * 16, # eyes right
    ],
    [   # pinky
        [57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58], # up
        [59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60], # down
        [55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56], # left
        [53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54], # right
        [49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50], # frightened blue
        [51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52], # frightened white
        [90] * 16, # 200
        [91] * 16, # 400
        [92] * 16, # 800
        [93] * 16, # 1600
        [63] * 16, # eyes up
        [64] * 16, # eyes down
        [62] * 16, # eyes left
        [61] * 16, # eyes right
    ],
    [   # inky
        [69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70], # up
        [71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72], # down
        [67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68], # left
        [65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66], # right
        [49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50], # frightened blue
        [51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52], # frightened white
        [90] * 16, # 200
        [91] * 16, # 400
        [92] * 16, # 800
        [93] * 16, # 1600
        [63] * 16, # eyes up
        [64] * 16, # eyes down
        [62] * 16, # eyes left
        [61] * 16, # eyes right
    ],
    [   # clyde
        [82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83], # up
        [84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85], # down
        [80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81], # left
        [78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79], # right
        [49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50], # frightened blue
        [51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52], # frightened white
        [90] * 16, # 200
        [91] * 16, # 400
        [92] * 16, # 800
        [93] * 16, # 1600
        [63] * 16, # eyes up
        [64] * 16, # eyes down
        [62] * 16, # eyes left
        [61] * 16, # eyes right
    ]
]

# ghost normal speed table
G_SPEED_NORMAL = [0.75, 0.85, 0.85, 0.85]
G_SPEED_NORMAL.extend([0.95] * 252)

# ghost speed table when entering or leaving a tunnel
G_SPEED_TUNNEL = [0.40, 0.45, 0.45, 0.45]
G_SPEED_TUNNEL.extend([0.50] * 252)

# ghost speed table when in frightened mode
G_SPEED_FRIGHT = [0.50, 0.55, 0.55, 0.55]
G_SPEED_FRIGHT.extend([0.60] * 252)

# ghost points
G_POINTS = [200, 400, 800, 1600]

# pellet counter limits for pinky, inky and clyde
G_PELLET_COUNTER_LIMIT = [[None, 0, 30, 60], [None, 0, 0, 50]]
G_PELLET_COUNTER_LIMIT.extend([[None, 0, 0, 0]] * 254)

# mode (scatter - chase)
MODE_TABLE = ["SCATTER", "CHASE", "SCATTER", "CHASE", "SCATTER", "CHASE", "SCATTER", "CHASE"]
MODE_DURATION = []
MODE_DURATION.extend([[7, 20, 7, 20, 5, 20, 5, -1]] * 1)
MODE_DURATION.extend([[7, 20, 7, 20, 5, 1033, 1 / FPS, -1]] * 3)
MODE_DURATION.extend([[5, 20, 5, 20, 5, 1037, 1 / FPS, -1]] * 252)

# frightened mode
FRIGHT_DURATION = [6, 5, 4, 3, 2, 5, 2, 2, 1, 5, 2, 1, 1, 3, 1, 1, 0, 1]
FRIGHT_DURATION.extend([0] * 238)
FRIGHT_FLASHES = [5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 3, 3, 5, 3, 3, 0 ,3]
FRIGHT_FLASHES.extend([0] * 238)

# score
SCORE = 0
HIGH_SCORE = 0
SCORE_BLINK_COUNTER = 0
SCORE_BLINK_FULL_TIME = 48  # number of frames for a full cycle
SCORE_BLINK_HALF_TIME = int(SCORE_BLINK_FULL_TIME // 2)

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
GAME_FLOW = "PRESS_START"

############################
# functions and procedures #
############################

def calculate_distance(start_pos, end_pos):
    return math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2)

def clear_screen():
    SCREEN.fill("black")

def display_current_frame():
    pygame.display.flip()   # display current frame
    CLOCK.tick(FPS)         # limits FPS

def draw_bonus_items():
    # draw bonus items on bottom (COLS: 24, 22, 20, 18, 16, 14, 12)
    for item, col in enumerate(range(24, 11, -2)):
        if item < len(ITEM_LIST):
            SCREEN.blit(SPRITES[ITEM_LIST[item]], (col * TILE_SIZE, 34 * TILE_SIZE))

def draw_ghosts():
    for i in range(len(G)):
        SCREEN.blit(SPRITES[G_ANIM[i][G_FACE[i]][G_SPRITE_IDX]], (G[i].x - HALF_TILE, G[i].y - HALF_TILE))

def draw_highscore():
    type("HIGH SCORE", 0, 9)
    if HIGH_SCORE > 0: type(str(HIGH_SCORE).rjust(8, " "), 1, 9)

def draw_pacman():
    if PACMAN_VISIBLE:
        #pygame.draw.rect(SCREEN, "#FFFF00", PACMAN, 1)
        SCREEN.blit(SPRITES[PACMAN_ANIM[FACE][PACMAN_SPRITE_IDX]], (PACMAN.x - HALF_TILE, PACMAN.y - HALF_TILE))

def draw_remaining_lives():
    # draw remaining lives (COLS: 2, 4, 6, 8, 10)
    for life, col in enumerate(range(2, 11, 2)):
        if life < LIVES - 1:
            SCREEN.blit(SPRITES[15], (col * TILE_SIZE, 34 * TILE_SIZE))

def draw_score():
    # draw score
    if SCORE_BLINK_COUNTER < SCORE_BLINK_HALF_TIME: type("1UP", 0, 3)
    if SCORE == 0:
        type("00", 1, 5)
    else:
        type(str(SCORE).rjust(7, " "), 1, 0)

def draw_maze(mode = -1):
    # mode: -1 = draw normal, 0 = draw only blue walls, 1 = draw only white walls
    for i, row in enumerate(MAZE):
        for j, tile in enumerate(row):
            if mode == -1:
                if tile == 2: # energizer
                    if NRG_BLINK_COUNTER < NRG_BLINK_HALF_TIME:
                        SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))    
                elif tile > 0:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))
            elif mode == 0:
                if tile > 2 and tile != 27:
                    SCREEN.blit(TILES[tile], (j * TILE_SIZE, i * TILE_SIZE))
            elif mode == 1:
                if tile > 2 and tile != 27:
                    SCREEN.blit(TILES[tile + 36], (j * TILE_SIZE, i * TILE_SIZE))

def eat_pellet(type = 1):
    global MAZE, SCORE, HIGH_SCORE, LIVES, MODE
    global PACMAN_SKIP_FRAMES, PELLETS, GAME_FLOW, ITEM_VISIBLE
    global G_REVERSE_DIR, G_POINTS_IDX, G_STATE, G_WAS_EATEN, G_PELLET_COUNTER
    global FRIGHTENED, FRIGHT_TOTAL_TIME, FRIGHT_FLASH_TIME, FRIGHT_FLASH_FRAME
    global PELLET_COUNTER_TYPE, GLOBAL_PELLET_COUNTER, PELLET_TIMER
    
    # remove pellet from the maze
    MAZE[ROW][COL] = 0
    
    # normal pellet
    if type == 1:
        SCORE += 10
        PACMAN_SKIP_FRAMES += 1
    # power pellet
    elif type == 2:
        SCORE += 50
        PACMAN_SKIP_FRAMES += 3
        # set mode to frightened, prepare ghosts
        FRIGHTENED = True
        FRIGHT_TOTAL_TIME = FRIGHT_DURATION[LEVEL] * FPS
        FRIGHT_FLASH_TIME = FRIGHT_FLASHES[LEVEL] * 28
        FRIGHT_FLASH_FRAME = 0
        G_REVERSE_DIR = [True, True, True, True]
        G_POINTS_IDX = -1
        for i in range(len(G)):
            if G_STATE[i] in {"SCATTER", "CHASE"}: G_STATE[i] = "FRIGHTENED"
            G_WAS_EATEN[i] = False

    # increase pellet counter
    PELLETS += 1

    # check high score
    if SCORE >= HIGH_SCORE: HIGH_SCORE = SCORE

    # if no pellets on the maze, go to the next level
    if PELLETS == 244: GAME_FLOW = "NEXT_LEVEL"

    # show bonus item if necessary
    if PELLETS in {ITEM_PELLETS1, ITEM_PELLETS2} and not ITEM_VISIBLE: ITEM_VISIBLE = True

    # reset pellet timer
    PELLET_TIMER = 0

    # update pellet counters
    if PELLET_COUNTER_TYPE == "PERSONAL":
        exiting_index = get_exiting_index()
        if exiting_index != -1: G_PELLET_COUNTER[exiting_index] += 1
    elif PELLET_COUNTER_TYPE == "GLOBAL":
        GLOBAL_PELLET_COUNTER += 1
        match GLOBAL_PELLET_COUNTER:
            case 7:
                if G_STATE[1] == "CAGED": G_STATE[1] = "EXITING"
            case 17:
                if G_STATE[2] == "CAGED": G_STATE[2] = "EXITING"
            case 32:
                if G_STATE[3] == "CAGED": 
                    G_STATE[3] = "EXITING"
                    GLOBAL_PELLET_COUNTER = 0
                    PELLET_COUNTER_TYPE = "PERSONAL"
            
def game_complete():
    global GAME_FLOW

    # display game complete and pause for 5 seconds
    frame_counter = 0
    while frame_counter < 5 * FPS and GAME_FLOW == "GAME_COMPLETE":
        poll_events()
        clear_screen()
        draw_maze()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        type("GAME", 14, 12, "yellow")
        type("COMPLETE", 20, 10, "yellow")
        update_timers()
        display_current_frame()
        frame_counter += 1

    GAME_FLOW = "PRESS_START"

def game_over():
    global GAME_FLOW

    # display game over and pause for 5 seconds
    frame_counter = 0
    while frame_counter < 5 * FPS and GAME_FLOW == "GAME_OVER":
        poll_events()
        clear_screen()
        draw_maze()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        type("GAME  OVER", 20, 9, "red")
        update_timers()
        display_current_frame()
        frame_counter += 1

    GAME_FLOW = "PRESS_START"

def get_exiting_index():
    global G_STATE
    exiting_index = -1
    for i in range(1, 4):
        if G_STATE[i] == "CAGED":
            exiting_index = i
            break
    return exiting_index

def get_ready():
    global GAME_FLOW, LIVES

    # if game starts for first time
    if LEVEL == 0 and PELLETS == 0:

        # wait for 2 seconds
        frame_counter = 0
        while frame_counter < 2 * FPS and GAME_FLOW == "GET_READY":
            poll_events()
            clear_screen()
            draw_maze()
            draw_score()
            draw_highscore()
            draw_remaining_lives()
            draw_bonus_items()
            type("PLAYER ONE", 14, 9, CYAN)
            type("READY", 20, 11, "yellow")
            SCREEN.blit(SYMBOLS[4], (16 * TILE_SIZE, 20 * TILE_SIZE))
            update_timers()
            display_current_frame()
            frame_counter += 1
        
        # subtract one life from lives counter
        LIVES -= 1

    # wait for another 2 seconds
    frame_counter = 0
    while frame_counter < 2 * FPS and GAME_FLOW == "GET_READY":
        poll_events()
        clear_screen()
        draw_maze()
        draw_pacman()
        draw_ghosts()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        type("READY", 20, 11, "yellow")
        SCREEN.blit(SYMBOLS[4], (16 * TILE_SIZE, 20 * TILE_SIZE))
        update_timers()
        display_current_frame()
        frame_counter += 1

    GAME_FLOW = "PLAY"   

def handle_bonus_item():
    global ITEM_VISIBLE, ITEM_DISPLAY_TIME, ITEM_POINTS_TIME, SCORE

    # show bonus items
    if ITEM_VISIBLE:
        if ITEM_DISPLAY_TIME > 0:
            SCREEN.blit(SPRITES[ITEMS[LEVEL]], (ITEM.x, ITEM.y))
            ITEM_DISPLAY_TIME -= 1
            if ITEM_DISPLAY_TIME == 0:
                ITEM_DISPLAY_TIME = int(random.uniform(9, 10) * FPS)
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
                ITEM_DISPLAY_TIME = int(random.uniform(9, 10) * FPS)
                ITEM_POINTS_TIME = 2 * FPS

def init_characters():

    global GAME_FLOW, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY, ACC, FACE
    global PACMAN_SPRITE_IDX, PACMAN_SKIP_FRAMES, PACMAN_SPEED, PACMAN_VISIBLE
    global G_ROW, G_COL, G_OFF_X, G_OFF_Y, G_DX, G_DY, G_ACC
    global G_FACE, G_SPRITE_IDX, G_SPEED, G_REVERSE_DIR, G_STATE
    global G_POINTS_IMG, G_POINTS_IDX, G_PAUSE_TIME, G_WAS_EATEN
    global MODE_INDEX, MODE, MODE_TIME, FRIGHTENED
    global ITEM_DISPLAY_TIME, ITEM_POINTS_TIME, ITEM_VISIBLE
    global GLOBAL_PELLET_COUNTER, PELLET_TIMER
   
    # mode
    MODE_INDEX = 0
    MODE = MODE_TABLE[MODE_INDEX]
    MODE_TIME = MODE_DURATION[LEVEL][MODE_INDEX] * FPS

    # frightened
    FRIGHTENED = False

    # pacman
    ROW = 26
    COL = 13
    OFFSET_X = 4
    OFFSET_Y = 0
    DX = -1
    DY = 0
    ACC = 0
    FACE = LEFT
    PACMAN_SPRITE_IDX = 6
    PACMAN_SKIP_FRAMES = 0
    PACMAN_VISIBLE = True
    PACMAN_SPEED = PACMAN_SPEED_NORMAL[LEVEL] * MAX_SPEED
    PACMAN.x = COL * TILE_SIZE + OFFSET_X * SPEED_UNIT
    PACMAN.y = ROW * TILE_SIZE + OFFSET_Y * SPEED_UNIT

    # ghosts
    G_ROW = [14, 17, 17, 17]
    G_COL = [13, 13, 11, 15]
    G_OFF_X = [4, 4, 4, 4]
    G_OFF_Y = [0, 0, 0, 0]
    G_DX = [-1, 0, 0, 0]
    G_DY = [0, 1, -1, -1]
    G_ACC = [0, 0, 0, 0]
    G_FACE = [LEFT, DOWN, UP, UP]
    G_SPRITE_IDX = 0
    G_REVERSE_DIR = [False, False, False, False]
    G_STATE = [MODE, "CAGED", "CAGED", "CAGED"]
    G_WAS_EATEN = [False, False, False, False]
    G_POINTS_IMG = [None, None, None, None]
    G_POINTS_IDX = -1
    G_PAUSE_TIME = 0
    G_SPEED = [G_SPEED_NORMAL[LEVEL] * MAX_SPEED] * 4
    for i in range(len(G)):
        G[i].x = G_COL[i] * TILE_SIZE + G_OFF_X[i] * SPEED_UNIT
        G[i].y = G_ROW[i] * TILE_SIZE + G_OFF_Y[i] * SPEED_UNIT

    # bonus item
    ITEM_DISPLAY_TIME = int(random.uniform(9, 10) * FPS)    # number of frames that item stays on screen
    ITEM_POINTS_TIME = 2 * FPS                              # number of frames that points stays on screen (2 sec)
    ITEM_VISIBLE = False                                    # true when item is visible

    # global pellet counter
    GLOBAL_PELLET_COUNTER = 0

    # pellet timer
    PELLET_TIMER = 0

    # get ready scene
    GAME_FLOW = "GET_READY"

def init_level():
    global GAME_FLOW, MAZE, PELLETS, ITEM_LIST
    global G_PELLET_COUNTER, PELLET_COUNTER_TYPE, PELLET_TIMER_LIMIT

    # copy data from original maze to the game's maze
    MAZE = []
    for row in ORIGINAL_MAZE:
        temp_row = []
        for value in row:
            temp_row.append(value)
        MAZE.append(temp_row)

    # pellets
    PELLETS = 0

    # item list
    ITEM_LIST = []
    for i in range(max(0, LEVEL - 6), LEVEL + 1, 1): ITEM_LIST.append(ITEMS[i])

    # ghost pellet counter
    G_PELLET_COUNTER = [None, 0, 0, 0]

    # pellet counter type (personal or global)
    PELLET_COUNTER_TYPE = "PERSONAL"

    # pellet timer limits
    if LEVEL < 5:
        PELLET_TIMER_LIMIT = 4 * FPS    # levels 1-4, 4 seconds
    else:
        PELLET_TIMER_LIMIT = 3 * FPS    # levels 5+, 3 seconds

    # initialize characters
    GAME_FLOW = "INIT_CHARACTERS"

def lost_life():

    global FACE, PACMAN_SPRITE_IDX, LIVES, GAME_FLOW

    # pause for 1 second
    frame_counter = 0
    while frame_counter < FPS and GAME_FLOW == "LOST_LIFE":
        poll_events()
        clear_screen()
        draw_maze()
        draw_pacman()
        draw_ghosts()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        update_timers()
        display_current_frame()
        frame_counter += 1
    
    # play death sequence
    FACE = DEATH
    PACMAN_SPRITE_IDX = 0
    while PACMAN_SPRITE_IDX < len(PACMAN_ANIM[DEATH]) and GAME_FLOW == "LOST_LIFE":
        poll_events()
        clear_screen()
        draw_maze()
        draw_pacman()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        update_timers()
        display_current_frame()
        PACMAN_SPRITE_IDX += 1
    
    # pause for another 1 second
    frame_counter = 0
    while frame_counter < FPS and GAME_FLOW == "LOST_LIFE":
        poll_events()
        clear_screen()
        draw_maze()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        update_timers()
        display_current_frame()
        frame_counter += 1
    
    # reduce pacman lives by 1
    LIVES -= 1

    if LIVES == 0:
        # end game
        GAME_FLOW = "GAME_OVER"
    else:
        # reset pacman and ghosts
        GAME_FLOW = "INIT_CHARACTERS"

def move_ghosts():

    global PACMAN_SKIP_FRAMES, PACMAN_VISIBLE, SCORE
    global G_ACC, G_ROW, G_COL, G_OFF_X, G_OFF_Y, G_DX, G_DY
    global G_FACE, G_SPEED, G_SPRITE_IDX, GAME_FLOW, G_STATE
    global G_POINTS_IMG, G_POINTS_IDX, G_PAUSE_TIME, G_WAS_EATEN
    global G_PELLET_COUNTER, PELLET_COUNTER_TYPE

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

                    # reverse direction if mode has changed
                    if G_REVERSE_DIR[i]:
                        G_DX[i] = -G_DX[i]
                        G_DY[i] = -G_DY[i]
                        G_REVERSE_DIR[i] = False

                    # target tile
                    if G_STATE[i] == "SCATTER":
                        dir = pick_shortest_path(G_FIXED_TARGET[i], G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        G_DX[i] = dir[0]
                        G_DY[i] = dir[1]
                    elif G_STATE[i] == "CHASE":
                        match i:
                            # blinky
                            case 0:
                                # target --> pacman's tile
                                target = (ROW, COL)
                            # pinky
                            case 1:
                                # target --> four tiles forward to pacman's tile
                                target = (ROW + DY * 4, COL + DX * 4)
                                # exception when pacman is facing up: four tiles forward + four tiles to the left
                                if DY == -1:
                                    target = (target[0], target[1] - 4)
                            # inky
                            case 2:
                                # target --> T = B + 2 * (Poff - B)
                                # T: target, B: blinky's tile, Poff: pacman's tile with a 2-tiles forward offset
                                blinky_tile = (G_ROW[0], G_COL[0])
                                pacman_tile = (ROW + DY * 2, COL + DX * 2)
                                vector = (pacman_tile[0] - blinky_tile[0], pacman_tile[1] - blinky_tile[1])
                                target = (blinky_tile[0] + 2 * vector[0], blinky_tile[1] + 2 * vector[1])
                            # clyde
                            case 3:
                                # calculate euclidean distance between clyde and pacman
                                # if distance is eight or more tiles, target pacman's tile, else, target clyde's fixed tile
                                clyde_tile = (G_ROW[3], G_COL[3])
                                pacman_tile = (ROW, COL)
                                distance = calculate_distance(clyde_tile, pacman_tile)
                                if distance >= 8:
                                    target = pacman_tile
                                else:
                                    target = G_FIXED_TARGET[3]
                        # pick shortest path
                        dir = pick_shortest_path(target, G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        G_DX[i] = dir[0]
                        G_DY[i] = dir[1]
                    elif G_STATE[i] == "FRIGHTENED":
                        # pick random path
                        dir = pick_random_path(G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        G_DX[i] = dir[0]
                        G_DY[i] = dir[1]
                    elif G_STATE[i] == "EYES":
                        # pick shortest path to tile (14, 13)
                        target = (14, 13)
                        dir = pick_shortest_path(target, G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        G_DX[i] = dir[0]
                        G_DY[i] = dir[1]

            # move ghost
            if G_PAUSE_TIME == 0 or G_STATE[i] in {"EYES", "ENTERING"}:
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

            # check other ghost states
            # caged
            if G_STATE[i] == "CAGED":
                if G_ROW[i] == 16 and G_OFF_Y[i] == 4:
                    G_DY[i] = -G_DY[i]
                    G_FACE[i] = DOWN
                elif G_ROW[i] == 17 and G_OFF_Y[i] == 4:
                    G_DY[i] = -G_DY[i]
                    G_FACE[i] =UP
                if PELLET_COUNTER_TYPE == "PERSONAL":
                    if G_PELLET_COUNTER[i] == G_PELLET_COUNTER_LIMIT[LEVEL][i]:
                        G_STATE[i] = "EXITING"
            # eyes
            elif G_STATE[i] == "EYES":
                if G_ROW[i] == 14 and G_COL[i] == 13 and G_OFF_X[i] == 4:
                    G_STATE[i] = "ENTERING"
                    G_DX[i] = 0
                    G_DY[i] = 1
                    G_FACE[i] = 11
            # entering
            elif G_STATE[i] == "ENTERING":
                if G_ROW[i] == 17 and G_COL[i] == 13 and G_OFF_X[i] == 4:
                    match i:
                        # make blinky look up, revive and release him
                        case 0:
                            G_DX[i] = 0
                            G_DY[i] = -1
                            G_FACE[i] = UP
                            G_STATE[i] = "EXITING"
                        # make pinky look up, keep him in the cage
                        case 1:
                            G_DX[i] = 0
                            G_DY[i] = -1
                            G_FACE[i] = UP
                            G_STATE[i] = "CAGED"
                        # move inky to the left side
                        case 2:
                            G_DX[i] = -1
                            G_DY[i] = 0
                            G_FACE[i] = 12
                        # move clyde to the right side
                        case 3:
                            G_DX[i] = 1
                            G_DY[i] = 0
                            G_FACE[i] = 13
                if G_ROW[i] == 17 and G_COL[i] in {11, 15} and G_OFF_X[i] == 4:
                    G_DX[i] = 0
                    G_DY[i] = -1
                    G_FACE[i] = UP
                    G_STATE[i] = "CAGED"
            # exiting
            elif G_STATE[i] == "EXITING":
                # if ghost is on the left side of the cage, move to the center
                if G_COL[i] == 11:
                    G_ROW[i] = 17
                    G_OFF_Y[i] = 0
                    G_DX[i] = 1
                    G_DY[i] = 0
                    G_FACE[i] = RIGHT
                # if ghost is on the right side of the cage, move to the center
                elif G_COL[i] == 15:
                    G_ROW[i] = 17
                    G_OFF_Y[i] = 0
                    G_DX[i] = -1
                    G_DY[i] = 0
                    G_FACE[i] = LEFT
                # if ghost is in the center, move up
                elif G_ROW[i] == 17 and G_COL[i] == 13 and G_OFF_X[i] == 4:
                    G_DX[i] = 0
                    G_DY[i] = -1
                    G_FACE[i] = UP
                # stop outside of the door, change state
                elif G_ROW[i] == 14 and G_COL[i] == 13 and G_OFF_X[i] == 4 and G_OFF_Y[i] == 0:
                    if FRIGHTENED and not G_WAS_EATEN[i]:
                        G_STATE[i] = "FRIGHTENED"
                    else:
                        G_STATE[i] = MODE
                    match G_STATE[i]:
                        case "SCATTER":
                            dir = pick_shortest_path(G_FIXED_TARGET[i], G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        case "CHASE":
                            dir = pick_shortest_path((ROW, COL), G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                        case "FRIGHTENED":
                            dir = pick_random_path(G_ROW[i], G_COL[i], G_DX[i], G_DY[i])
                    G_DX[i] = dir[0]
                    G_DY[i] = dir[1]

            # select animation sequence
            if G_STATE[i] in {"SCATTER", "CHASE"}:
                match (G_DX[i], G_DY[i]):
                    case ( 0, -1): G_FACE[i] = UP
                    case ( 0,  1): G_FACE[i] = DOWN
                    case (-1,  0): G_FACE[i] = LEFT
                    case ( 1,  0): G_FACE[i] = RIGHT
            elif FRIGHTENED and not G_WAS_EATEN[i] and not G_STATE[i] in {"EATEN", "EYES"}:
                if FRIGHT_FLASH_FRAME < 14:
                    G_FACE[i] = 4
                else:
                    G_FACE[i] = 5
            elif G_STATE[i] == "EATEN":
                G_FACE[i] = G_POINTS_IMG[i]
            if G_STATE[i] == "EYES":
                match (G_DX[i], G_DY[i]):
                    case ( 0, -1): G_FACE[i] = 10
                    case ( 0,  1): G_FACE[i] = 11
                    case (-1,  0): G_FACE[i] = 12
                    case ( 1,  0): G_FACE[i] = 13

            # adjust ghost speed
            if G_STATE[i] == "EYES":
                G_SPEED[i] = 2 * G_SPEED_NORMAL[LEVEL] * MAX_SPEED
            elif G_ROW[i] == 17 and (G_COL[i] < 5 or G_COL[i] > 22):
                G_SPEED[i] = G_SPEED_TUNNEL[LEVEL] * MAX_SPEED
            elif G_STATE[i] == "FRIGHTENED":
                G_SPEED[i] = G_SPEED_FRIGHT[LEVEL] * MAX_SPEED
            elif G_STATE[i] == "CAGED":
                G_SPEED[i] = 0.4 * MAX_SPEED
            else:
                G_SPEED[i] = G_SPEED_NORMAL[LEVEL] * MAX_SPEED

            # update ghost position
            G[i].x = G_COL[i] * TILE_SIZE + G_OFF_X[i] * SPEED_UNIT
            G[i].y = G_ROW[i] * TILE_SIZE + G_OFF_Y[i] * SPEED_UNIT

            # collision with pacman
            if G[i].colliderect(PACMAN):
                if G_STATE[i] in {"SCATTER", "CHASE"}:
                    GAME_FLOW = "LOST_LIFE"
                    PELLET_COUNTER_TYPE = "GLOBAL"
                elif G_STATE[i] == "FRIGHTENED":
                    G_STATE[i] = "EATEN"
                    G_WAS_EATEN[i] = True
                    G_POINTS_IDX += 1
                    G_POINTS_IMG[i] = 6 + G_POINTS_IDX
                    SCORE += G_POINTS[G_POINTS_IDX]
                    G_PAUSE_TIME = FPS
                    PACMAN_SKIP_FRAMES = FPS
                    PACMAN_VISIBLE = False

            # reduce fractional accumulator by speed unit
            G_ACC[i] -= SPEED_UNIT

    # animate ghost
    if GAME_FLOW == "PLAY":
        G_SPRITE_IDX += 1
        if G_SPRITE_IDX == len(G_ANIM[i][G_FACE[i]]): G_SPRITE_IDX = 0

def move_pacman():

    global ACC, PACMAN_SPEED, ROW, COL, OFFSET_X, OFFSET_Y, DX, DY, FACE, GAME_FLOW
    global MAZE, PELLETS, SCORE, HIGH_SCORE, PACMAN_SKIP_FRAMES, PACMAN_SPRITE_IDX, ITEM_VISIBLE
    global FRIGHTENED, FRIGHT_TOTAL_TIME, FRIGHT_FLASH_TIME, FRIGHT_FLASH_FRAME
    global MODE, G_STATE, G_REVERSE_DIR, G_POINTS_IDX

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
                if MAZE[ROW][COL] in {1, 2}:
                    eat_pellet(MAZE[ROW][COL])

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

def next_level():
    global LEVEL, GAME_FLOW

    # pause for 1 second
    frame_counter = 0
    while frame_counter < FPS and GAME_FLOW == "NEXT_LEVEL":
        poll_events()
        clear_screen()
        draw_maze()
        draw_pacman()
        draw_ghosts()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        update_timers()
        display_current_frame()
        frame_counter += 1

    # flash the maze 4 times
    frame_counter = 0
    flash_counter = 0
    drawing_mode = 1

    while frame_counter < 112 and GAME_FLOW == "NEXT_LEVEL":
        poll_events()
        clear_screen()
        draw_maze(drawing_mode)
        draw_pacman()
        draw_score()
        draw_highscore()
        draw_remaining_lives()
        draw_bonus_items()
        update_timers()
        display_current_frame()
        if flash_counter < 14:
            flash_counter += 1
        else:
            flash_counter = 0
            drawing_mode = 1 - drawing_mode
        frame_counter += 1

    # advance to the next level
    LEVEL += 1

    if LEVEL == 256:
        # end game
        GAME_FLOW = "GAME_COMPLETE"
    else:
        # initialize next level
        init_level()

def pick_random_path(row, col, dx, dy):
    # create a list for adding the free paths where the ghost can turn
    can_turn = []

    # look around, add all free path directions to the list
    if not wall_collision(row - 1, col) and not dy == 1: can_turn.append((0, -1))
    if not wall_collision(row + 1, col) and not dy == -1: can_turn.append((0, 1))
    if not wall_collision(row, col - 1) and not dx == 1: can_turn.append((-1, 0))
    if not wall_collision(row, col + 1) and not dx == -1: can_turn.append((1, 0))

    # pick a random direction
    return random.choice(can_turn)

def pick_shortest_path(target, row, col, dx, dy):
    # distance from each direction to the target tile (up, down,left, right)
    # -1 means that distance is not available
    dist = [-1] * 4

    # calculate distances
    if not wall_collision(row - 1, col) and not dy == 1:
        if not((row == 14 or row == 26) and (col == 12 or col == 15)): 
            dist[0] = calculate_distance((row - 1, col), target)
    if not wall_collision(row + 1, col) and not dy == -1: dist[1] = calculate_distance((row + 1, col), target)
    if not wall_collision(row, col - 1) and not dx == 1: dist[2] = calculate_distance((row, col - 1), target)
    if not wall_collision(row, col + 1) and not dx == -1: dist[3] = calculate_distance((row, col + 1), target)

    # pick the path with the shortest distance
    min_val = min((i for i in dist if i != -1), default = None)
    if min_val != None:
        match dist.index(min_val):
            case 0: return (0, -1)
            case 1: return (0,  1)
            case 2: return (-1, 0)
            case 3: return ( 1, 0)

def poll_events():
    global RUNNING, GAME_FLOW

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
                GAME_FLOW = ""
            elif GAME_FLOW == "PRESS_START": GAME_FLOW = "NEW_GAME"

def press_start():
    poll_events()
    clear_screen()
    type("PUSH ANY KEY TO START", 16, 4, ORANGE)
    type("1 PLAYER ONLY", 20, 8, CYAN)
    type("BONUS PAC-MAN FOR 10000", 24, 1, PINK)
    # draw PTS
    for i in range(3):
        SCREEN.blit(SYMBOLS[i], ((25 + i) * TILE_SIZE, 24 * TILE_SIZE))
    # draw (C)
    SCREEN.blit(SYMBOLS[3], (4 * TILE_SIZE, 28 * TILE_SIZE))
    type("1980 MIDWAY MFG. CO.", 28, 6, MAGENTA)
    draw_score()
    draw_highscore()
    display_current_frame()

def setup_new_game():
    global GAME_FLOW, LEVEL, LIVES, SCORE, HIGH_SCORE
    global SCORE_BLINK_COUNTER, SCORE_BLINK_HALF_TIME, SCORE_BLINK_FULL_TIME
    global NRG_BLINK_COUNTER, NRG_BLINK_HALF_TIME, NRG_BLINK_FULL_TIME

    # level
    LEVEL = 0

    # lives
    LIVES = 4

    # score
    SCORE = 0
    SCORE_BLINK_COUNTER = 0
    SCORE_BLINK_FULL_TIME = 48  # number of frames for a full cycle
    SCORE_BLINK_HALF_TIME = int(SCORE_BLINK_FULL_TIME // 2)

    # energizers
    NRG_BLINK_COUNTER = 0
    NRG_BLINK_FULL_TIME = 30  # number of frames for a full cycle
    NRG_BLINK_HALF_TIME = int(NRG_BLINK_FULL_TIME // 2)

    # initialize level
    GAME_FLOW = "INIT_LEVEL"

def type(string, row, col, color = "#dedeff"):
    text = FONT.render(string, False, color)
    SCREEN.blit(text, (col * TILE_SIZE, row * TILE_SIZE))

def update_timers():
    global SCORE_BLINK_COUNTER, NRG_BLINK_COUNTER
    global MODE, MODE_INDEX, MODE_TIME, MODE_PREVIOUS
    global G_STATE, G_REVERSE_DIR, G_WAS_EATEN
    global G_PAUSE_TIME, PACMAN_VISIBLE, G_POINTS_IDX
    global FRIGHTENED, FRIGHT_TOTAL_TIME, FRIGHT_FLASH_TIME, FRIGHT_FLASH_FRAME
    global PELLET_TIMER

    # 1up blinking
    SCORE_BLINK_COUNTER += 1
    if SCORE_BLINK_COUNTER == SCORE_BLINK_FULL_TIME: SCORE_BLINK_COUNTER = 0

    # power pellets blinking
    if GAME_FLOW == "PLAY" or GAME_FLOW == "LOST_LIFE":
        NRG_BLINK_COUNTER += 1
        if NRG_BLINK_COUNTER == NRG_BLINK_FULL_TIME: NRG_BLINK_COUNTER = 0
    
    # while playing
    if GAME_FLOW == "PLAY":
        # ghost pause time when eaten
        if G_PAUSE_TIME > 0:
            G_PAUSE_TIME -= 1
            if G_PAUSE_TIME == 0:
                PACMAN_VISIBLE = True
                for i in range(len(G)):
                    if G_STATE[i] == "EATEN": G_STATE[i] = "EYES"
        # frightened mode
        elif FRIGHTENED:
            if FRIGHT_TOTAL_TIME > 0:
                FRIGHT_TOTAL_TIME -= 1
                if FRIGHT_TOTAL_TIME < FRIGHT_FLASH_TIME:
                    FRIGHT_FLASH_FRAME += 1
                    if FRIGHT_FLASH_FRAME == 28: FRIGHT_FLASH_FRAME = 0
            else:
                FRIGHTENED = False
                G_POINTS_IDX = -1
                for i in range(len(G)):
                    if G_STATE[i] == "FRIGHTENED": G_STATE[i] = MODE
                    G_WAS_EATEN[i] = False
        # scatter/chase mode
        elif MODE in {"SCATTER", "CHASE"}:
            if MODE_DURATION[LEVEL][MODE_INDEX] != -1:
                MODE_TIME -= 1
                if MODE_TIME == 0:
                    MODE_INDEX += 1
                    MODE = MODE_TABLE[MODE_INDEX]
                    MODE_TIME = MODE_DURATION[LEVEL][MODE_INDEX] * FPS
                    for i in range(len(G)):
                        if G_STATE[i] in ["SCATTER", "CHASE"]:
                            G_STATE[i] = MODE
                            G_REVERSE_DIR = [True, True, True, True]
        # pellet timer
        if G_PAUSE_TIME == 0:
            exiting_index = get_exiting_index()
            if exiting_index != -1:
                PELLET_TIMER += 1
                if PELLET_TIMER == PELLET_TIMER_LIMIT:
                    G_STATE[exiting_index] = "EXITING"
                    PELLET_TIMER = 0

def wall_collision(row, col):
    collision = False
    if row >= 0 and row < MAZE_HEIGHT:
        if col >= 0 and col < MAZE_WIDTH:
            if MAZE[row][col] > 2:
                collision = True
    return collision

def main():

    while RUNNING:
        
        match GAME_FLOW:
            case "PRESS_START":
                press_start()
            case "NEW_GAME":
                setup_new_game()
            case "INIT_LEVEL":
                init_level()
            case "INIT_CHARACTERS":
                init_characters()
            case "GET_READY":
                get_ready()
            case "PLAY":
                poll_events()
                clear_screen()
                move_pacman()
                move_ghosts()
                draw_maze()
                handle_bonus_item()
                draw_pacman()
                draw_ghosts()
                draw_score()
                draw_highscore()
                draw_remaining_lives()
                draw_bonus_items()
                update_timers()
                display_current_frame()
            case "NEXT_LEVEL":
                next_level()
            case "LOST_LIFE":
                lost_life()
            case "GAME_OVER":
                game_over()
            case "GAME_COMPLETE":
                game_complete()

    pygame.mouse.set_visible(True)
    pygame.quit()

if __name__ == "__main__":
    main()