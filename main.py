import pygame
from utils.initial_values import *
from puzzle import Puzzle
from display import Screen

pygame.init()

screen = Screen()
puzzle = Puzzle()

def main():
    running = True
    only_want_next_step = False
    get_previous_step = False
    while running:
        screen.display.fill(BLACK, (0, 0, GRID_WIDTH, GRID_LENGTH))
        screen.display.fill(ORANGE, (GRID_WIDTH, 0, CONTROL_PANEL_WIDTH, CONTROL_PANEL_LENGTH))
        screen.draw_lines()
        screen.render_alive_cells()
        screen.render_controls_panel()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                if screen.click_on_grid(click_position):
                    puzzle.fill_grid(click_position)
                else:
                    if screen.get_control_clicked(click_position) == "play":
                        puzzle.game_running = True
                    elif screen.get_control_clicked(click_position) == "stop":
                        puzzle.game_running = False
                    elif screen.get_control_clicked(click_position) == "next":
                        puzzle.game_running = True
                        only_want_next_step = True
                    elif screen.get_control_clicked(click_position) == "previous" and puzzle.step_count >= 1:
                        get_previous_step = True

        if puzzle.game_running and only_want_next_step:
            puzzle.run_game()
            puzzle.game_running = False
            only_want_next_step = False

        elif puzzle.game_running and not only_want_next_step:
            puzzle.run_game()

        elif get_previous_step:
            puzzle.go_back_one_step()
            get_previous_step = False

        pygame.display.update()


main()
