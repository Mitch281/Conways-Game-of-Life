from utils.initial_values import *


# Handles logic and algorithm.
class Puzzle:
    def __init__(self):
        self.grid = grid
        self.game_running = False
        self.births_and_deaths = {}
        self.step_count = 0

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

        else:
            # Cell is in top left corner
            if (row_num, col_num) == (0, 0):
                neighbour_values.append(self.grid[1][0])
                neighbour_values.append(self.grid[1][1])
                neighbour_values.append(self.grid[0][1])

            # Cell is in top right corner
            elif (row_num, col_num) == (0, NUM_COLUMNS - 1):
                neighbour_values.append(self.grid[0][NUM_COLUMNS - 2])
                neighbour_values.append(self.grid[1][NUM_COLUMNS - 2])
                neighbour_values.append(self.grid[1][NUM_COLUMNS - 1])

            # Cell is in bottom right corner
            elif (row_num, col_num) == (NUM_ROWS - 1, NUM_COLUMNS - 1):
                neighbour_values.append(self.grid[NUM_ROWS - 1][NUM_COLUMNS - 2])
                neighbour_values.append(self.grid[NUM_ROWS - 2][NUM_COLUMNS - 2])
                neighbour_values.append(self.grid[NUM_ROWS - 2][NUM_COLUMNS - 2])

            # Cell is in bottom left corner
            elif (row_num, col_num) == (NUM_ROWS - 1, 0):
                neighbour_values.append(self.grid[NUM_ROWS - 2][0])
                neighbour_values.append(self.grid[NUM_ROWS - 2][1])
                neighbour_values.append(self.grid[NUM_ROWS - 1][1])

            # Cell on top boundary but not in a corner.
            elif row_num == 0 and 1 <= col_num <= NUM_COLUMNS - 2:
                for i in range(-1, 2):
                    neighbour_values.append(self.grid[1][col_num + i])
                neighbour_values.append(self.grid[0][col_num - 1])
                neighbour_values.append(self.grid[0][col_num + 1])

            # Cell on right boundary but not in a corner.
            elif 1 <= row_num <= NUM_ROWS - 2 and col_num == NUM_COLUMNS - 1:
                for i in range(-1, 2):
                    neighbour_values.append(self.grid[row_num + i][NUM_COLUMNS - 2])
                neighbour_values.append(self.grid[row_num - 1][NUM_COLUMNS - 1])
                neighbour_values.append(self.grid[row_num - 1][NUM_COLUMNS - 1])

            # Cell on bottom boundary but not in a corner.
            elif row_num == NUM_ROWS - 1 and 1 <= col_num <= NUM_COLUMNS - 2:
                for i in range(-1, 2):
                    neighbour_values.append(self.grid[NUM_ROWS - 2][col_num + i])
                neighbour_values.append(self.grid[NUM_ROWS - 1][col_num - 1])
                neighbour_values.append(self.grid[NUM_ROWS - 1][col_num + 1])

            # Cell on left boundary but not in a corner.
            elif 1 <= row_num <= NUM_ROWS - 2 and col_num == 0:
                for i in range(-1, 2):
                    neighbour_values.append(self.grid[row_num + i][1])
                neighbour_values.append(self.grid[row_num - 1][0])
                neighbour_values.append(self.grid[row_num + 1][0])

        return neighbour_values.count(1)

    # Returns an array of all the indexes of the cells that are to become alive and are to die.
    def get_births_and_deaths(self):
        births = []
        deaths = []
        for row_num in range(NUM_ROWS):
            for col_num in range(NUM_COLUMNS):
                # The cell is currently alive.
                if self.grid[row_num][col_num] == 1:
                    # We kill the cell due to under or over population.
                    if self.get_num_alive_neighbours(row_num, col_num) <= 1 or \
                            self.get_num_alive_neighbours(row_num, col_num) >= 4:
                        deaths.append((row_num, col_num))

                # The cell is currently not alive.
                if self.grid[row_num][col_num] == 0:
                    # A new cell is born.
                    if self.get_num_alive_neighbours(row_num, col_num) == 3:
                        births.append((row_num, col_num))

        return births, deaths

    # The algorithm that runs the game.
    def run_game(self):
        births = self.get_births_and_deaths()[0]
        deaths = self.get_births_and_deaths()[1]

        # Keep track of each step and the births and deaths recorded.
        self.births_and_deaths[self.step_count] = (births, deaths)
        self.step_count += 1

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
