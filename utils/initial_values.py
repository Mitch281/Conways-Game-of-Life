import numpy as np
import pygame
from pygame import font

font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (239, 105, 12)
YELLOW = (255, 243, 60)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

GRID_WIDTH = GRID_LENGTH = 640
INCREMENT = 8
NUM_ROWS = NUM_COLUMNS = GRID_LENGTH // INCREMENT
CONTROL_PANEL_WIDTH = 240
CONTROL_PANEL_LENGTH = GRID_LENGTH
GAP_BETWEEN_BUTTONS = 50

PLAY_BUTTON = pygame.image.load("utils/play_button_resized.png")
STOP_BUTTON = pygame.image.load("utils/stop_button_resized.png")
NEXT_BUTTON = pygame.image.load("utils/next_button.png")
PREVIOUS_BUTTON = pygame.image.load("utils/previous_button.png")

# Get the render position of control text
CONTROL_FONT_SIZE = 30
CONTROL_FONT = pygame.font.SysFont("cambria", CONTROL_FONT_SIZE)
CONTROL_TEXT = CONTROL_FONT.render("Controls", 1, BLUE)
X_CONTROL_TEXT = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - CONTROL_TEXT.get_width() // 2
Y_CONTROL_TEXT = 5

# Get the render position of play button
X_POS_PLAY = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - PLAY_BUTTON.get_width() // 2
Y_POS_PLAY = Y_CONTROL_TEXT + CONTROL_TEXT.get_height() + GAP_BETWEEN_BUTTONS

# Get the render position of stop button
X_POS_STOP = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - STOP_BUTTON.get_width() // 2
Y_POS_STOP = Y_POS_PLAY + PLAY_BUTTON.get_height() + GAP_BETWEEN_BUTTONS

# Get the render positions of next button
X_POS_NEXT = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - NEXT_BUTTON.get_width() // 2
Y_POS_NEXT = Y_POS_STOP + STOP_BUTTON.get_height() + GAP_BETWEEN_BUTTONS

# Get the render positions of previous button
X_POS_PREVIOUS = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - PREVIOUS_BUTTON.get_width() // 2
Y_POS_PREVIOUS = Y_POS_NEXT + NEXT_BUTTON.get_height() + GAP_BETWEEN_BUTTONS

grid = np.zeros((NUM_ROWS, NUM_COLUMNS))
for i in range(NUM_ROWS):
    for j in range(NUM_COLUMNS):
        if i % 2 == 0 and j % 3 == 0:
            grid[i][j] = 1
        if i % 2 == 1 and j % 10 == 1:
            grid[i][j] = 1
        if i % 2 == 0 and j % 4 == 0:
            grid[i][j] = 1
