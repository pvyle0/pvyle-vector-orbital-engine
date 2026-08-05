
import pygame
import sys
import math
from settings import WIDTH, HEIGHT, FPS, G_CONST, KM_PER_PIXEL, M_PER_PIXEL, TIME_WARP_LEVELS, PLANET_VISUAL_RADUIS
from physics import apply_gravity, compute_orbit_elements, get_orbit_points
from ship import Ship
warp_index = 0
pygame.init()
font = pygame.font.SysFont("Consolas", 18)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pvyle Orbital Simulator")
clock = pygame.time.Clock()
CENTER = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
r_start = 300
orbital_speed = math.sqrt(G_CONST / r_start)
ship = Ship(CENTER.x + r_start, CENTER.y, 0, -orbital_speed, thrust_power=orbital_speed * 0.01)
 
running = True
while running:
    dt = clock.tick(FPS) / 1000
    physics_dt = dt * TIME_WARP_LEVELS[warp_index]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                warp_index = min(warp_index + 1, len(TIME_WARP_LEVELS) - 1)
            if event.key == pygame.K_COMMA:
                warp_index = min(warp_index - 1, 0)
    ship.update_physics(physics_dt)
    apply_gravity(ship, CENTER, G_CONST, physics_dt)
    apoapsis, periapsis, a, e = compute_orbit_elements(ship.position, ship.velocity, CENTER, G_CONST)
    telemetry_lines = [
        f"Time Warp: {TIME_WARP_LEVELS[warp_index]}",
        f"Apoapsis: {apoapsis * KM_PER_PIXEL:.0f} km",
        f"Periapsis: {periapsis * KM_PER_PIXEL:.0f} km",
        f"Eccentricity: {e:.3f}",
        f"Speed: {ship.velocity.length() * M_PER_PIXEL:.2f} m/s",
        f"Throttle: {ship.throttle*100:.0f}%",
    ]

    orbit_points = get_orbit_points(ship.position, ship.velocity, CENTER, G_CONST)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        ship.adjust_throttle(0.5 * physics_dt)
    if keys[pygame.K_LCTRL]:
        ship.adjust_throttle(-0.5 * physics_dt)
    if keys[pygame.K_z]:
        ship.set_throttle(1.0)
    if keys[pygame.K_x]:
        ship.set_throttle(0.0)
    if keys[pygame.K_LEFT]:
        ship.rotate(-1, dt)
    if keys[pygame.K_RIGHT]:
        ship.rotate(1, dt)
    screen.fill((10, 10, 15))
    pygame.draw.lines(screen, (150, 150, 150), True, orbit_points, 1)
    pygame.draw.circle(screen, (80, 140, 255), CENTER, PLANET_VISUAL_RADUIS)
    ship.draw(screen)
    for i, line in enumerate(telemetry_lines):
        text_surface = font.render(line, True, (200, 255, 200))
        screen.blit(text_surface, (10, 10 + i * 22))
    pygame.display.flip()
 
pygame.quit()
sys.exit()
 
