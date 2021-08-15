from initial_values import *


class ControlPositions:
    """
    Class to get the render positions of buttons in control panel.
    """
    def __init__(self):
        """
        Initialise the object
        :param (x_control_text, y_control_text): x and y render positions for the text (int, int)
        :param (x_play, y_play): x and y render positions for play button (int, int)
        :param (x_stop, y_stop): x and y render positions for stop button (int, int)
        :param (x_next, y_next): x and y render positions for next button (int, int)
        :param (x_previous, y_previous): x and y render positions for previous button (int, int)
        :param (x_random, y_random): x and y render positions for random button (int, int)
        :param (x_reset, y_reset): x and y render positions for reset button (int, int)
        """
        self.x_control_text, self.y_control_text = 0, 0
        self.x_play, self.y_play = 0, 0
        self.x_stop, self.y_stop = 0, 0
        self.x_next, self.y_next = 0, 0
        self.x_previous, self.y_previous = 0, 0
        self.x_random, self.y_random = 0, 0
        self.x_reset, self.y_reset = 0, 0

    def set_control_text_pos(self):
        """
        set the x and y render positions for text
        :return: None
        """
        self.x_control_text = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - CONTROL_TEXT_WIDTH // 2
        self.y_control_text = 5

    def set_play_button_pos(self):
        """
        set the x and y render positions for play button
        :return: None
        """
        self.set_control_text_pos()
        self.x_play = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_play = self.y_control_text + CONTROL_TEXT_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_stop_button_pos(self):
        """
        set the x and y render positions for stop button
        :return: None
        """
        self.set_play_button_pos()
        self.x_stop = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_stop = self.y_play + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_next_button_pos(self):
        """
        set the x and y render positions for next button
        :return: None
        """
        self.set_stop_button_pos()
        self.x_next = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_next = self.y_stop + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_previous_button_pos(self):
        """
        set the x and y positions for previous button
        :return: None
        """
        self.set_next_button_pos()
        self.x_previous = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_previous = self.y_next + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_random_button_pos(self):
        """
        set x and y positions for random button
        :return: None
        """
        self.set_previous_button_pos()
        self.x_random = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_random = self.y_previous + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_reset_button_pos(self):
        """
        set x and y positions for reset button
        :return: None
        """
        self.set_random_button_pos()
        self.x_reset = GRID_WIDTH + CONTROL_PANEL_WIDTH // 2 - BUTTON_WIDTH // 2
        self.y_reset = self.y_random + BUTTON_HEIGHT + GAP_BETWEEN_BUTTONS

    def set_all_control_positions(self):
        """
        calls all of the above methods
        :return: None
        """
        self.set_control_text_pos()
        self.set_play_button_pos()
        self.set_stop_button_pos()
        self.set_next_button_pos()
        self.set_previous_button_pos()
        self.set_random_button_pos()
        self.set_reset_button_pos()
