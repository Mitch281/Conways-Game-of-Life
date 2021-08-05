import pygame

pygame.init()

SCREEN_WIDTH = SCREEN_LENGTH = 645
INCREMENT = 15
NUM_ROWS = NUM_COLUMNS = int(SCREEN_LENGTH / INCREMENT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
        self.caption = pygame.display.set_caption("Conway's Game of Life")

    def draw_lines(self):
        for i in range(0, SCREEN_LENGTH, INCREMENT):
            pygame.draw.line(self.display, WHITE, (i, 0), (i, SCREEN_LENGTH))
            pygame.draw.line(self.display, WHITE, (0, i), (SCREEN_WIDTH, i))


screen = Screen()


def main():
    running = True
    while running:
        screen.display.fill(BLACK)
        screen.draw_lines()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


main()
