# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main() -> None:
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shots)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for up in updatable:
            up.update(dt)

        _ = screen.fill("black")

        for dr in drawable:
            dr.draw(screen)

        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("\ngame over\n")
                return
            for shot in shots:
                if shot.checkCollision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
