import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main() -> None:
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
