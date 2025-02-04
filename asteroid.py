from constants import *
import pygame
import random

from circleshape import *

class Asteroid(CircleShape):
    containers = []
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_a1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_a1.velocity = v1 * 1.2
        new_a2.velocity = v2 * 1.2

