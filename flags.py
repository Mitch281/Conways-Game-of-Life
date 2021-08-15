# Class to handle all of the flags involved in button animation.
class Flags:
    def __init__(self):
        self.game_running = False
        self.only_want_next_step = False
        self.get_previous_step = False
        self.mouse_being_clicked = False

        # Number of times mouse is clicked or relased.
        self.num_times_click = 0
