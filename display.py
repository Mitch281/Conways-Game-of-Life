from pygame import font
from utils.initial_values import *
from puzzle import Puzzle

font.init()
puzzle = Puzzle()

# Handles GUI
class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((GRID_WIDTH + CONTROL_PANEL_WIDTH, GRID_LENGTH))
        self.caption = pygame.display.set_caption("Conway's Game of Life")

    def draw_lines(self):
        for i in range(0, GRID_LENGTH, INCREMENT):
            pygame.draw.line(self.display, WHITE, (i, 0), (i, GRID_LENGTH))
            pygame.draw.line(self.display, WHITE, (0, i), (GRID_WIDTH, i))

    # Renders a green box on top of the cells that are alive.
    def render_alive_cells(self):
        for row_num in range(NUM_ROWS):
            if 1 in puzzle.grid[row_num]:
                for col_num in range(NUM_COLUMNS):
                    if puzzle.grid[row_num][col_num] == 1:
                        y_pos = row_num * INCREMENT
                        x_pos = col_num * INCREMENT
                        pygame.draw.rect(self.display, YELLOW,
                                         (x_pos, y_pos, INCREMENT, INCREMENT))

    # Detects if the click was on the grid or not.
    def click_on_grid(self, click_position):
        x_pos = click_position[0]
        if 0 < x_pos < GRID_WIDTH:
            return True
        return False

    # Detects the control button clicked.
    def get_control_clicked(self, click_position):
        x_pos = click_position[0]
        y_pos = click_position[1]
        if X_POS_PLAY <= x_pos <= X_POS_PLAY + CONTROL_PANEL_WIDTH:
            if Y_POS_PLAY <= y_pos <= Y_POS_PLAY + PLAY_BUTTON.get_height():
                return "play"
            elif Y_POS_STOP <= y_pos <= Y_POS_STOP + STOP_BUTTON.get_height():
                return "stop"

    def render_controls_panel(self):
        self.display.blit(CONTROL_TEXT, (X_CONTROL_TEXT, Y_CONTROL_TEXT))
        self.display.blit(PLAY_BUTTON, (X_POS_PLAY, Y_POS_PLAY))
        self.display.blit(STOP_BUTTON, (X_POS_STOP, Y_POS_STOP))

screen = Screen()