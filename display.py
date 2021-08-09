import pygame
from utils.initial_values import *
from puzzle import Puzzle

puzzle = Puzzle()

# Handles GUI
class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
        self.caption = pygame.display.set_caption("Conway's Game of Life")

    def draw_lines(self):
        for i in range(0, SCREEN_LENGTH, INCREMENT):
            pygame.draw.line(self.display, WHITE, (i, 0), (i, SCREEN_LENGTH))
            pygame.draw.line(self.display, WHITE, (0, i), (SCREEN_WIDTH, i))

    # Renders a green box on top of the cells that are alive.
    def render_alive_cells(self):
        for row_num in range(NUM_ROWS):
            if 1 in puzzle.grid[row_num]:
                for col_num in range(NUM_COLUMNS):
                    if puzzle.grid[row_num][col_num] == 1:
                        y_pos = row_num * INCREMENT
                        x_pos = col_num * INCREMENT
                        pygame.draw.rect(self.display, GREEN,
                                         (x_pos, y_pos, INCREMENT, INCREMENT))

screen = Screen()