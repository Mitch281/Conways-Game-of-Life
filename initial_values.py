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
CONTROL_PANEL_HEIGHT = GRID_LENGTH
GAP_BETWEEN_BUTTONS = 50

PLAY_BUTTON = pygame.image.load("images/play_button_resized.png")
STOP_BUTTON = pygame.image.load("images/stop_button_resized.png")
NEXT_BUTTON = pygame.image.load("images/next_button.png")
PREVIOUS_BUTTON = pygame.image.load("images/previous_button.png")
BUTTON_WIDTH = PLAY_BUTTON.get_width()
BUTTON_HEIGHT = PLAY_BUTTON.get_height()

CONTROL_FONT_SIZE = 30
CONTROL_FONT = pygame.font.SysFont("cambria", CONTROL_FONT_SIZE)
CONTROL_TEXT = CONTROL_FONT.render("Controls", 1, BLUE)
CONTROL_TEXT_WIDTH = CONTROL_TEXT.get_width()
CONTROL_TEXT_HEIGHT = CONTROL_TEXT.get_height()

grid = np.zeros((NUM_ROWS, NUM_COLUMNS))
