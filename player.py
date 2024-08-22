from typing import Any

import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation: int = 0

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
        pygame.draw.polygon(
            screen, pygame.Color(255, 255, 255, 255), self.triangle(), 2
        )
