from typing import override

import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    @override
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid1_vector = self.velocity.rotate(random_angle)
        asteroid2_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = asteroid1_vector * 1.2
        asteroid2.velocity = asteroid2_vector * 1.2
