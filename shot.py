from typing import override
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    @override
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
