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

    
    # Returns true if a cell is not on a boundary, false otherwise.
    def not_on_boundary(self, row_num, col_num):
        if 1 <= row_num <= NUM_ROWS - 2 and 1 <= col_num <= NUM_COLUMNS - 2:
            return True
        return False

    # Gets the status of all neighbours of a specific cell.

    def get_num_alive_neighbours(self, row_num, col_num):
        neighbour_values = []

        # Ensures that the cell is not on a boundary.
        if self.not_on_boundary(row_num, col_num):
            for i in range(-1, 2):
                neighbour_values.append(grid[row_num - 1][col_num + i])
                neighbour_values.append(grid[row_num + 1][col_num + i])
            neighbour_values.append(grid[row_num][col_num + 1])
            neighbour_values.append(grid[row_num][col_num - 1])

        return neighbour_values.count(1)

    # Returns an array of all the indexes of the cells that are to become alive and are to die.

    def get_births_and_deaths(self):
        births = []
        deaths = []
        for row_num in range(NUM_ROWS):
            for col_num in range(NUM_COLUMNS):

                # The cell is currently alive.
                if self.grid[row_num][col_num] == 1:
                    if self.not_on_boundary(row_num, col_num):
                        # We kill the cell due to under or over population.
                        if self.get_num_alive_neighbours(row_num, col_num) <= 1 or \
                            self.get_num_alive_neighbours(row_num, col_num) >= 4:
                            deaths.append((row_num, col_num))

                # The cell is currently not alive.
                if self.grid[row_num][col_num] == 0:
                    if self.not_on_boundary(row_num, col_num):
                        # A new cell is born.
                        if self.get_num_alive_neighbours(row_num, col_num) == 3:
                            births.append((row_num, col_num))

        return births, deaths
                    
    # The algorithm that runs the game.

    def run_game(self):
        births = self.get_births_and_deaths()[0]
        deaths = self.get_births_and_deaths()[1]

        # Give birth to the cells to be birthed.
        for position in births:
            row_num = position[0]
            col_num = position[1]
            self.grid[row_num][col_num] = 1

        # Kill the cells to be killed.
        for position in deaths:
            row_num = position[0]
            col_num = position[1]
            self.grid[row_num][col_num] = 0

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    puzzle.run_game()

        pygame.display.update()


main()
