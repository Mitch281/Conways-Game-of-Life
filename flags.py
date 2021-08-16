class Flags:
    """
    Handles flags that are used to create button animation when buttons are clicked
    """
    def __init__(self):
        """
        Initialise the object
        :param self.game_running: checks if game is running or not: (bool)
        :param self.only_want_next_step: if the next button was pressed, then this is true (we only want the next
        step of the algorithm to run) (bool)
        :param self.get_previous_step: if the previous button was pressed, then this is true (we want to go back
        one step in the algorithm) (bool)
        :param self.mouse_being_clicked: if the mouse is being clicked, this is true. This is to not highlight a button
        or cell when the mouse is being clicked to give the buttons a clicking animation (bool)
        :param self.num_times_click: counts the number of times the mouse button has not only been clicked
        (mouse button down), but released a clicked (mouse button up) (bool)
        """
        self.game_running = False
        self.only_want_next_step = False
        self.get_previous_step = False
        self.mouse_being_clicked = False
        self.num_times_click = 0
