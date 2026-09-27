from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
