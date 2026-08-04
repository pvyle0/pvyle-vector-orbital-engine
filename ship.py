import pygame

class Ship:
    def __init__(self, x, y, vx, vy):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(vx, vy)
        self.thrust_power = 2
        self.throttle = 0.0
 
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 5)
 
    def update_physics(self, dt):
        if self.throttle > 0 and self.velocity.length() > 0:
            direction = self.velocity.normalize()
            self.velocity += direction * (self.thrust_power * self.throttle) * dt
            
    def adjust_throttle(self, amount):
        self.throttle = max(0.0, min(1.0, self.throttle + amount))
 
    def set_throttle(self, value):
        self.throttle = max(0.0, min(1.0, value))
