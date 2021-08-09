import numpy as np
import pygame

pygame.init()

GRID_WIDTH = GRID_LENGTH = 640
CONTROL_BAR_WIDTH = 200
CONTROL_BAR_LENGTH = GRID_LENGTH
INCREMENT = 8
NUM_ROWS = NUM_COLUMNS = int(GRID_LENGTH / INCREMENT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

CONTROLS_FONT_SIZE = 30
CONTROL_FONT = pygame.font.SysFont("cambria", CONTROLS_FONT_SIZE)
PLAY_BUTTON = pygame.image.load("utils/play_button.png")
STOP_BUTTON = pygame.image.load("utils/stop_button.png")
FORWARD_ARROW = pygame.image.load("utils/forward_arrow.png")
BACKWARDS_ARROW = pygame.image.load("utils/backwards_arrow.png")
GAP_BETWEEN_BUTTONS = 40

grid = np.zeros((NUM_ROWS, NUM_COLUMNS))
