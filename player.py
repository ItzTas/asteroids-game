from typing import Any, override
import pygame
from pygame.sprite import Group
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation = 0
        self.containers: tuple[Group[Any]] = tuple()
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    @override
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown > 0:
                return
            self.shoot()
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        vel = pygame.Vector2(0, 1)
        vel = vel.rotate(self.rotation)
        vel *= PLAYER_SHOOT_SPEED
        shot.velocity = vel
