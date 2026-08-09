import pygame
import math

class Ship:
    def __init__(self, x, y, vx, vy, thrust_power=2, dry_mass=500, fuel_mass=200, fuel_consumption=5 ):
        self.dry_mass = dry_mass
        self.fuel_mass = fuel_mass
        self.fuel_consumption = fuel_consumption
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(vx, vy)
        self.thrust_power = thrust_power
        self.throttle = 0.0
        self.angle = -math.pi / 2
        self.turn_speed = 3.0
    def draw(self, screen):
        size = 10
        nose = self.position + pygame.Vector2(
            math.cos(self.angle) * size,
            math.sin(self.angle) * size
        )

        left_wing = self.position + pygame.Vector2(
            math.cos(self.angle + 2.5) * size * 0.6,
            math.sin(self.angle + 2.5) * size * 0.6
        ) 
        right_wing = self.position + pygame.Vector2(
            math.cos(self.angle - 2.5) * size * 0.6,
            math.sin(self.angle - 2.5) * size * 0.6
        )
        pygame.draw.polygon(screen, (255, 255, 255), [nose, left_wing, right_wing])
 
    def update_physics(self, dt):
        if self.throttle > 0 and self.fuel_mass > 0:
            fuel_to_burn = self.fuel_consumption * self.throttle * dt
            fuel_to_burn = min(fuel_to_burn, self.fuel_mass)
            self.fuel_mass -= fuel_to_burn
            current_mass = self.dry_mass + self.fuel_mass
            thrust_direction = pygame.Vector2(
                math.cos(self.angle),
                math.sin(self.angle)
            )
            thrust_force = self.thrust_power * self.throttle
            acceleration = thrust_force / current_mass
            self.velocity += thrust_direction * acceleration * dt

    def adjust_throttle(self, amount):
        self.throttle = max(0.0, min(1.0, self.throttle + amount))
 
    def set_throttle(self, value):
        self.throttle = max(0.0, min(1.0, value))

    def rotate(self, direction, dt):
        self.angle += direction * self.turn_speed * dt