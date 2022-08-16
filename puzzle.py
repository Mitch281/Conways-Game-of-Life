from initial_values import *
import random


class Puzzle:
    """
    Class that handles the logic of the puzzle
    """

    def __init__(self):
        """
        Initialise the object
        :param self.grid: matrix of 1's and 0's. 1 means cell is alive, 0 means cell is dead (list)
        :param self.births_and_deaths: a dictionary containing each step number of the algorithm, and the corresponding
        cells that were birthed and died in the step (dict)
        :param self.step_count: counts the step the algorithm is on (starting at 0) (int)
        """
        self.grid = grid
        self.births_and_deaths = {}
        self.step_count = 0

    def click_in_bounds(self, click_position):
        x_pos = click_position[0]
        y_pos = click_position[1]
        if 0 <= x_pos <= GRID_WIDTH and 0 <= y_pos <= GRID_LENGTH:
            return True
        return False

    def fill_grid(self, click_position):
        """
        makes a cell alive if clicked on
        :param click_position: the x, y coordinates of the click
        :return: None
        """
        if self.click_in_bounds(click_position):
            x_pos = click_position[0]
            y_pos = click_position[1]
            col_num = x_pos // INCREMENT
            row_num = y_pos // INCREMENT
            self.grid[row_num][col_num] = 1

    # Returns true if a cell is not on a boundary, false otherwise.
    def not_on_boundary(self, row_num, col_num):
        """
        checks if a certain cell is on the boundary of the grid
        :param row_num: the row number that the cell belongs to
        :param col_num: the column number that the cell belongs to
        :return: bool
        """
        if 1 <= row_num <= NUM_ROWS - 2 and 1 <= col_num <= NUM_COLUMNS - 2:
            return True
        return False

    # Gets the status of all neighbours of a specific cell.
    def get_num_alive_neighbours(self, row_num, col_num):
        """
        gets the number of alive numbers of a cell
        :param row_num: the row number that the cell belongs to
        :param col_num: the column number that the cell belongs to
        :return: int
        """
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
                neighbour_values.append(
                    self.grid[NUM_ROWS - 1][NUM_COLUMNS - 2])
                neighbour_values.append(
                    self.grid[NUM_ROWS - 2][NUM_COLUMNS - 2])
                neighbour_values.append(
                    self.grid[NUM_ROWS - 2][NUM_COLUMNS - 2])

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
                    neighbour_values.append(
                        self.grid[row_num + i][NUM_COLUMNS - 2])
                neighbour_values.append(
                    self.grid[row_num - 1][NUM_COLUMNS - 1])
                neighbour_values.append(
                    self.grid[row_num - 1][NUM_COLUMNS - 1])

            # Cell on bottom boundary but not in a corner.
            elif row_num == NUM_ROWS - 1 and 1 <= col_num <= NUM_COLUMNS - 2:
                for i in range(-1, 2):
                    neighbour_values.append(
                        self.grid[NUM_ROWS - 2][col_num + i])
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
        """
        gives all the cells (there indexes) that are to be birthed and die
        :return: tuple
        """
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

    def run_game(self):
        """
        performs the births and deaths
        :return: None
        """
        births = self.get_births_and_deaths()[0]
        deaths = self.get_births_and_deaths()[1]

        # Keep track of each step and the births and deaths recorded.
        self.step_count += 1
        self.births_and_deaths[self.step_count] = (births, deaths)

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

    def go_back_one_step(self):
        """
        undoes one step of algorithm
        :return: None
        """
        births_to_be_reversed = self.births_and_deaths[self.step_count][0]
        deaths_to_be_reversed = self.births_and_deaths[self.step_count][1]
        self.step_count -= 1

        for position in births_to_be_reversed:
            row_num = position[0]
            col_num = position[1]
            self.grid[row_num][col_num] = 0

        for position in deaths_to_be_reversed:
            row_num = position[0]
            col_num = position[1]
            self.grid[row_num][col_num] = 1

    def generate_random_board(self):
        """
        generates a random board
        :return: None
        """
        num_cells = NUM_COLUMNS * NUM_ROWS
        num_alive_cells = random.randint(1, num_cells)
        current_num_alive_cells = 0
        while current_num_alive_cells < num_alive_cells:
            row_num = random.randint(0, NUM_COLUMNS - 1)
            col_num = random.randint(0, NUM_ROWS - 1)
            if self.grid[row_num][col_num] != 1:
                self.grid[row_num][col_num] = 1
                current_num_alive_cells += 1

    def reset_grid(self):
        """
        resets the grid (all cells dead)
        :return: None
        """
        for row_num in range(NUM_ROWS):
            for col_num in range(NUM_COLUMNS):
                self.grid[row_num][col_num] = 0
