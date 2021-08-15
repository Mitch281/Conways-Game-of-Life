from initial_values import *
from puzzle import Puzzle
from control_positions import ControlPositions

font.init()
puzzle = Puzzle()
control_positions = ControlPositions()


# Handles GUI
class Screen:
    def __init__(self):
        control_positions.set_all_control_positions()
        self.display = pygame.display.set_mode((GRID_WIDTH + CONTROL_PANEL_WIDTH, GRID_LENGTH))
        self.caption = pygame.display.set_caption("Conway's Game of Life")
        self.x_control_text, self.y_control_text = control_positions.x_control_text, control_positions.y_control_text
        self.x_play, self.y_play = control_positions.x_play, control_positions.y_play
        self.x_stop, self.y_stop = control_positions.x_stop, control_positions.y_stop
        self.x_next, self.y_next = control_positions.x_next, control_positions.y_next
        self.x_previous, self.y_previous = control_positions.x_previous, control_positions.y_previous

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

    def highlight_cell(self, cursor_position):
        if self.click_on_grid(cursor_position):
            row_num = cursor_position[0] // INCREMENT
            col_num = cursor_position[1] // INCREMENT
            y_pos = col_num * INCREMENT
            x_pos = row_num * INCREMENT
            pygame.draw.rect(self.display, YELLOW, (x_pos, y_pos, INCREMENT, INCREMENT), 2)

    # Detects if the click was on the grid or not.
    def click_on_grid(self, click_position):
        x_pos = click_position[0]
        if 0 < x_pos < GRID_WIDTH:
            return True
        return False

    def cursor_on_play_button(self, cursor_position):
        x_pos = cursor_position[0]
        y_pos = cursor_position[1]
        if self.x_play <= x_pos <= self.x_play + BUTTON_WIDTH:
            if self.y_play <= y_pos <= self.y_play + BUTTON_HEIGHT:
                return True
        return False

    def cursor_on_stop_button(self, cursor_position):
        x_pos = cursor_position[0]
        y_pos = cursor_position[1]
        if self.x_stop <= x_pos <= self.x_stop + BUTTON_WIDTH:
            if self.y_stop <= y_pos <= self.y_stop + BUTTON_HEIGHT:
                return True
        return False

    def cursor_on_next_button(self, cursor_position):
        x_pos = cursor_position[0]
        y_pos = cursor_position[1]
        if self.x_next <= x_pos <= self.x_next + BUTTON_WIDTH:
            if self.y_next <= y_pos <= self.y_next + BUTTON_HEIGHT:
                return True
        return False

    def cursor_on_previous_button(self, cursor_position):
        x_pos = cursor_position[0]
        y_pos = cursor_position[1]
        if self.x_previous <= x_pos <= self.x_previous + BUTTON_WIDTH:
            if self.y_previous <= y_pos <= self.y_previous + BUTTON_HEIGHT:
                return True
        return False

    def highlight_control(self, cursor_position):
        if self.cursor_on_play_button(cursor_position):
            pygame.draw.rect(self.display, GREEN, (
                self.x_play, self.y_play, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
        elif self.cursor_on_stop_button(cursor_position):
            pygame.draw.rect(self.display, GREEN,
                             (self.x_stop, self.y_stop, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
        elif self.cursor_on_next_button(cursor_position):
            pygame.draw.rect(self.display, GREEN,
                             (self.x_next, self.y_next, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
        elif self.cursor_on_previous_button(cursor_position):
            pygame.draw.rect(self.display, GREEN,
                             (self.x_previous,self.y_previous, BUTTON_WIDTH,
                              BUTTON_HEIGHT), 2)

    def render_controls_panel(self):
        self.display.blit(CONTROL_TEXT, (self.x_control_text, self.y_control_text))
        self.display.blit(PLAY_BUTTON, (self.x_play, self.y_play))
        self.display.blit(STOP_BUTTON, (self.x_stop, self.y_stop))
        self.display.blit(NEXT_BUTTON, (self.x_next, self.y_next))
        self.display.blit(PREVIOUS_BUTTON, (self.x_previous, self.y_previous))


screen = Screen()
