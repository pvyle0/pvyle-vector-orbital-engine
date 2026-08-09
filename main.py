
import pygame
import sys
import math
from settings import WIDTH, HEIGHT, FPS, G_CONST, KM_PER_PIXEL, M_PER_PIXEL, TIME_WARP_LEVELS, PLANET_VISUAL_RADUIS
from physics import apply_gravity, compute_orbit_elements, get_orbit_points, compute_acceleration
from ui import draw_panel, draw_grid_lines, draw_naviball_placeholder
from ship import Ship
from ships_data import SHIP_PRESETS

ship_index = 0
warp_index = 0
left_panel_width = WIDTH * 3 // 4
bottom_panel_y = HEIGHT * 3 // 4
right_column_width = WIDTH - left_panel_width - 10
r_start = 300

pygame.init()
font = pygame.font.SysFont("Consolas", 18, bold=True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pvyle Orbital Simulator")
clock = pygame.time.Clock()
CENTER = pygame.Vector2(left_panel_width // 2, bottom_panel_y // 2)
orbital_speed = math.sqrt(G_CONST / r_start)
ship = Ship(CENTER.x + r_start, CENTER.y, 0, -orbital_speed, thrust_power=orbital_speed * 0.01 * 700)

def create_ship(index):
    preset = SHIP_PRESETS[index]
    return Ship(
        CENTER.x + r_start, CENTER.y, 0, -orbital_speed,
        thrust_power=preset["thrust_power"] * (preset["dry_mass"] + preset["fuel_mass"]) / 700,
        dry_mass=preset["dry_mass"],
        fuel_mass=preset["fuel_mass"],
        fuel_consumption=preset["fuel_consumption"]
    )
ship = create_ship(ship_index)

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
                warp_index = max(warp_index - 1, 0)
            if event.key == pygame.K_1:
                ship_index = 0
                ship = create_ship(ship_index)
            if event.key == pygame.K_2:
                ship_index = 1
                ship = create_ship(ship_index)
            if event.key == pygame.K_3:
                ship_index = 2
                ship = create_ship(ship_index)
            if event.key == pygame.K_4:
                ship_index = 3
                ship = create_ship(ship_index)
            if event.key == pygame.K_5:
                ship_index = 4
                ship = create_ship(ship_index)

    ship.update_physics(physics_dt)

    apply_gravity(ship, CENTER, G_CONST, physics_dt)
    apoapsis, periapsis, a, e = compute_orbit_elements(ship.position, ship.velocity, CENTER, G_CONST)
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
    draw_grid_lines(screen, WIDTH, HEIGHT, left_panel_width, bottom_panel_y)
    screen.set_clip((0, 0, left_panel_width, bottom_panel_y))
    pygame.draw.lines(screen, (150, 150, 150), True, orbit_points, 1)
    pygame.draw.circle(screen, (80, 140, 255), CENTER, PLANET_VISUAL_RADUIS)
    ship.draw(screen)
    screen.set_clip(None)

    g_local = compute_acceleration(ship.position, CENTER, G_CONST).length()
    max_thrust_force = ship.thrust_power
    current_mass = ship.dry_mass + ship.fuel_mass
    twr = max_thrust_force / (current_mass * g_local) if g_local > 0 else 0

    telemetry_lines = [
        f"Apoapsis: {apoapsis * KM_PER_PIXEL:.0f} km",
        f"Periapsis: {periapsis * KM_PER_PIXEL:.0f} km",
        f"Eccentricity: {e:.3f}",
    ]
    telemetry_height = draw_panel(screen, font, WIDTH - right_column_width - 10, 10, right_column_width, "FLIGHT TELEMETRY", telemetry_lines)

    resources_lines = [
        f"Fuel: {ship.fuel_mass:.0f} kg",
        f"TWR: {twr:.0f}",
        f"Mass: {ship.dry_mass:.0f} kg",
    ]
    resources_height = draw_panel(screen, font, WIDTH - right_column_width - 10, 10 + telemetry_height + 10, right_column_width, "EQUIPMENT & RESOURCES", resources_lines)

    ship_list_lines = []
    for i, preset in enumerate(SHIP_PRESETS):
        marker = ">" if i == ship_index else " "
        ship_list_lines.append(f"{marker} [{i+1}] {preset['name']}")
    draw_panel(screen, font, WIDTH - right_column_width - 10, 10 + telemetry_height + 10 + resources_height + 10, right_column_width, "SHIP SELECT [1-5]", ship_list_lines, show_separator=False)

    vector_lines = [
        f"Speed: {ship.velocity.length() * M_PER_PIXEL:.1f} m/s",
        f"Throttle: {ship.throttle*100:.0f}%",
        f"Time Warp: x{TIME_WARP_LEVELS[warp_index]}",
    ]
    draw_naviball_placeholder(screen, font, WIDTH - right_column_width - 10, bottom_panel_y + 10, right_column_width, HEIGHT - bottom_panel_y - 20)
    draw_panel(screen, font, 10, HEIGHT - 110, left_panel_width - 20, "TRAJECTORY VECTOR", vector_lines, show_separator=False)

    pygame.display.flip()
 
pygame.quit()
sys.exit()
 