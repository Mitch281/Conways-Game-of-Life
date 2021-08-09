from pygame import font
from utils.initial_values import *
from puzzle import Puzzle

font.init()

puzzle = Puzzle()


# Handles the whole display (grid + instructions)
class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((GRID_WIDTH + CONTROL_BAR_WIDTH, GRID_LENGTH))
        self.caption = pygame.display.set_caption("Conway's Game of Life")

    def draw_lines(self):
        for i in range(0, GRID_LENGTH, INCREMENT):
            # Vertical lines
            pygame.draw.line(self.display, WHITE, (i + CONTROL_BAR_WIDTH, 0), \
                             (i + CONTROL_BAR_WIDTH, GRID_LENGTH))

            # Horizontal lines
            pygame.draw.line(self.display, WHITE, (CONTROL_BAR_WIDTH, i), (GRID_WIDTH + CONTROL_BAR_WIDTH, i))

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

    def render_instruction_font(self):
        control_text = CONTROL_FONT.render("Controls", 1, BLACK)
        control_text_width = control_text.get_width()
        x_pos = CONTROL_BAR_WIDTH // 2 - control_text_width // 2
        y_pos = 5
        self.display.blit(control_text, (x_pos, y_pos))

    def render_controls(self):
        # Render play button
        play_button_width = PLAY_BUTTON.get_width()
        play_button_height = PLAY_BUTTON.get_height()
        x_pos_play = CONTROL_BAR_WIDTH // 2 - play_button_width // 2
        y_pos_play = 80
        self.display.blit(PLAY_BUTTON, (x_pos_play, y_pos_play))

        # Render stop button
        stop_button_width = STOP_BUTTON.get_width()
        stop_button_height = STOP_BUTTON.get_height()
        x_pos_stop = CONTROL_BAR_WIDTH // 2 - stop_button_width // 2
        y_pos_stop = y_pos_play + play_button_height + GAP_BETWEEN_BUTTONS
        self.display.blit(STOP_BUTTON, (x_pos_stop, y_pos_stop))

        # Render go one step forward button
        forward_arrow_width = FORWARD_ARROW.get_width()
        forward_arrow_height = FORWARD_ARROW.get_height()
        x_pos_forward = CONTROL_BAR_WIDTH // 2 - forward_arrow_width // 2
        y_pos_forward = y_pos_stop + stop_button_height + GAP_BETWEEN_BUTTONS
        self.display.blit(FORWARD_ARROW, (x_pos_forward, y_pos_forward))

        # Render one step backwards button
        backwards_arrow_width = BACKWARDS_ARROW.get_width()
        x_pos_backwards = CONTROL_BAR_WIDTH // 2 - backwards_arrow_width // 2
        y_pos_backwards = y_pos_forward + forward_arrow_height + GAP_BETWEEN_BUTTONS
        self.display.blit(BACKWARDS_ARROW, (x_pos_backwards, y_pos_backwards))

screen = Screen()
