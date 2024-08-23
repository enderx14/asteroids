from typing import Any

import pygame
from pygame.key import ScancodeWrapper

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation: float = 0

    # in the player class
    def triangle(self):
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation + 90) * (
            self.radius / 1.5
        )
        a: pygame.Vector2 = self.position + pygame.Vector2(forward * self.radius)
        b: Any = self.position - pygame.Vector2(forward * self.radius) - right
        c: Any = self.position - pygame.Vector2(forward * self.radius) + right
        return [a, b, c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys: ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt: float) -> None:
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
