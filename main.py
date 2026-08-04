
import pygame
import sys
import math
from settings import WIDTH, HEIGHT, FPS, G_CONST
from physics import apply_gravity, compute_orbit_elements, get_orbit_points
from ship import Ship
 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pvyle Orbital Simulator")
clock = pygame.time.Clock()
CENTER = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
 
r_start = 200
orbital_speed = math.sqrt(G_CONST / r_start)
ship = Ship(CENTER.x + r_start, CENTER.y, 0, -orbital_speed)
 
running = True
while running:
    dt = clock.tick(FPS) / 1000
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ship.update_physics(dt)
    apply_gravity(ship, CENTER, G_CONST, dt)
    apoapsis, periapsis, e, a = compute_orbit_elements(ship.position, ship.velocity, CENTER, G_CONST)
    print(f"Apoapsis: {apoapsis:.1f}, Periapsis: {periapsis:.1f}, e: {e:.3f}")
    orbit_points = get_orbit_points(ship.position, ship.velocity, CENTER, G_CONST)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        ship.adjust_throttle(0.5 * dt)
    if keys[pygame.K_LCTRL]:
        ship.adjust_throttle(-0.5 * dt)
    if keys[pygame.K_z]:
        ship.set_throttle(1.0)
    if keys[pygame.K_x]:
        ship.set_throttle(0.0)
 
    screen.fill((10, 10, 15))
    pygame.draw.lines(screen, (150, 150, 150), True, orbit_points, 1)
    pygame.draw.circle(screen, (80, 140, 255), CENTER, 30)
    ship.draw(screen)
 
    pygame.display.flip()
 
pygame.quit()
sys.exit()
 
