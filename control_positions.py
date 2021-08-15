from initial_values import *


class ControlPositions:
    def __init__(self):
        self.x_control_text, self.y_control_text = 0, 0
        self.x_play, self.y_play = 0, 0
        self.x_stop, self.y_stop = 0, 0
        self.x_next, self.y_next = 0, 0
        self.x_previous, self.y_previous = 0, 0

    def set_control_text_pos(self):
        self.x_control_text = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - CONTROL_TEXT_WIDTH // 2
        self.y_control_text = 5

    def set_play_button_pos(self):
        self.set_control_text_pos()
        self.x_play = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_play = self.y_control_text + CONTROL_TEXT.get_height() + GAP_BETWEEN_BUTTONS

    def set_stop_button_pos(self):
        self.set_play_button_pos()
        self.x_stop = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_stop = self.y_play + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_next_button_pos(self):
        self.set_stop_button_pos()
        self.x_next = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_next = self.y_stop + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_previous_button_pos(self):
        self.set_next_button_pos()
        self.x_previous = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_previous = self.y_next + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_all_control_positions(self):
        self.set_control_text_pos()
        self.set_play_button_pos()
        self.set_stop_button_pos()
        self.set_next_button_pos()
        self.set_previous_button_pos()
