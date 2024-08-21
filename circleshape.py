from typing_extensions import override
import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.Surface):
        pass

    @override
    def update(self, dt: int) -> None:
        pass

    def checkCollision(self, cs: object) -> bool:
        dist = self.position.distance_to(cs.position)
        return dist < self.radius + cs.radius
