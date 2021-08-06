import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = SCREEN_LENGTH = 645
INCREMENT = 15
NUM_ROWS = NUM_COLUMNS = int(SCREEN_LENGTH / INCREMENT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

grid = np.zeros((NUM_ROWS, NUM_COLUMNS))

# Handles logic and algorithm.
class Puzzle:
    def __init__(self):
        self.grid = grid

    # Changes the grid number to 1 if a square is clicked.
    def fill_grid(self, click_position):
        x_pos = click_position[0]
        y_pos = click_position[1]
        col_num = x_pos // INCREMENT
        row_num = y_pos // INCREMENT
        self.grid[row_num][col_num] = 1

    # Gets the status of all neighbours of a specific cell.
    def get_neighbours(self, row_num, col_num):
        neighbour_values = []

        # Cell is in top left corner
        if row_num == 0 and col_num == 0:
            neighbour_values.append(self.grid[0][1])
            neighbour_values.append(self.grid[1][1])
            neighbour_values.append(self.grid[1][0])

        # Cell is in bottom left corner
        elif row_num == NUM_ROWS - 1 and col_num == 0:
            neighbour_values.append(self.grid[NUM_ROWS - 2][0])
            neighbour_values.append(self.grid[NUM_ROWS - 2][1])
            neighbour_values.append(self.grid[NUM_ROWS - 1][1])

        # Cell is in top right corner
        elif row_num == 0 and col_num = NUM_COLUMNS - 1:
            neighbour_values.append(self.grid[0][NUM_COLUMNS - 2])
            neighbour_values.append(self.grid[1][NUM_COLUMNS - 2])
            neighbour_values.append(self.grid[1][NUM_COLUMNS - 1])

        # Cell is in bottom right corner
        elif row_num == NUM_ROWS - 1 and col_num == NUM_COLUMNS - 1:
            neighbour_values.append(self.grid[NUM_ROWS - 2][NUM_COLUMNS - 1])
            neighbour_values.append(self.grid[NUM_ROWS - 2][NUM_COLUMNS - 2])
            neighbour_values.append(self.grid[NUM_ROWS - 1][NUM_COLUMNS - 2])

        # Cell is in a non corner position
        else:
            neighbour_values.append(self.grid[row_num - 1][col_num - 1])
            neighbour_values.append(self.grid[row_num - 1][col_num])
            neighbour_values.append(self.grid[row_num - 1][col_num + 1])
            neighbour_values.append(self.grid[row_num][col_num + 1])
            neighbour_values.append(self.grid[row_num + 1][col_num + 1])
            neighbour_values.append(self.grid[row_num + 1][col_num])
            neighbour_values.append(self.grid[row_num + 1][col_num - 1])
            neighbour_values.append(self.grid[row_num][col_num - 1])


    # Returns an array of all the indexes of the cells that are to become alive.
    def get_births(self):
        for row_num in range(NUM_ROWS):

            # First, we check if there are any cells to be birthed in row 0. This is only possible if there are alive
            # cells in row 1.
            if row_num == 0:
                if 1 in self.grid[row_num + 1]:
                    for col_num in range(NUM_COLUMNS):
                        if self.grid[row_num][col_num] == 0:


    # The algorithm that runs the game.
    def game_runner(self):
        pass

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
                        pygame.draw.rect(self.display, GREEN, (x_pos, y_pos, INCREMENT, INCREMENT))

screen = Screen()
puzzle = Puzzle()


def main():
    running = True
    while running:
        screen.display.fill(BLACK)
        screen.draw_lines()
        screen.render_alive_cells()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                puzzle.fill_grid(click_position)

        pygame.display.update()


main()
