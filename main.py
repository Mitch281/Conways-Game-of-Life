import pygame
from utils.initial_values import *
from puzzle import Puzzle
from display import Screen

pygame.init()

screen = Screen()
puzzle = Puzzle()

def main():
    running = True
    run_game = True
    num_times_enter_pressed = 0
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    num_times_enter_pressed += 1

        if puzzle.game_running:
            puzzle.run_game()

        pygame.display.update()


main()
