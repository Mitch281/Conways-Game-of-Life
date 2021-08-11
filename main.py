import pygame
from utils.initial_values import *
from puzzle import Puzzle
from display import Screen

pygame.init()

screen = Screen()
puzzle = Puzzle()

def main():
    running = True
    num_times_enter_pressed = 0
    while running:
        screen.display.fill(BLACK, (0, 0, SCREEN_WIDTH, SCREEN_LENGTH))
        screen.display.fill(ORANGE, (SCREEN_WIDTH, 0, CONTROL_PANEL_WIDTH, CONTROL_PANEL_LENGTH))
        screen.draw_lines()
        screen.render_alive_cells()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = pygame.mouse.get_pos()
                puzzle.fill_grid(click_position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    num_times_enter_pressed += 1

        if num_times_enter_pressed % 2 == 1:
            puzzle.run_game()

        pygame.display.update()


main()
