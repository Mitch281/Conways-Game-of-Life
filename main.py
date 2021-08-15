from initial_values import *
from puzzle import Puzzle
from display import Screen
from flags import Flags

pygame.init()

screen = Screen()
puzzle = Puzzle()
flags = Flags()


def main():
    running = True
    while running:
        screen.display.fill(BLACK, (0, 0, GRID_WIDTH, GRID_LENGTH))
        screen.display.fill(ORANGE, (GRID_WIDTH, 0, CONTROL_PANEL_WIDTH, CONTROL_PANEL_HEIGHT))
        screen.draw_lines()
        screen.render_alive_cells()
        screen.render_controls_panel()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flags.mouse_being_clicked = True
                flags.num_times_click += 1
                click_position = pygame.mouse.get_pos()
                if not screen.click_on_grid(click_position):
                    if screen.cursor_on_play_button(click_position):
                        flags.game_running = True
                    elif screen.cursor_on_stop_button(click_position):
                        flags.game_running = False
                    elif screen.cursor_on_next_button(click_position):
                        flags.game_running = True
                        flags.only_want_next_step = True
                    elif screen.cursor_on_previous_button(click_position) and puzzle.step_count >= 1:
                        flags.get_previous_step = True

            if event.type == pygame.MOUSEBUTTONUP:
                flags.mouse_being_clicked = False
                flags.num_times_click += 1

        if flags.num_times_click >= 1 and flags.num_times_click % 2 == 0:
            if screen.click_on_grid(click_position):
                puzzle.fill_grid(click_position)

        # Highlight control buttons or cells if cursor is hovering over them.
        cursor_position = pygame.mouse.get_pos()
        if not flags.mouse_being_clicked:
            screen.highlight_control(cursor_position)
            screen.highlight_cell(cursor_position)

        if flags.game_running and flags.only_want_next_step:
            puzzle.run_game()
            flags.game_running = False
            flags.only_want_next_step = False

        elif flags.game_running and not flags.only_want_next_step:
            puzzle.run_game()

        elif flags.get_previous_step:
            puzzle.go_back_one_step()
            flags.get_previous_step = False

        pygame.display.update()


main()
