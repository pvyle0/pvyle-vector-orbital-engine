import pygame
import math

def compute_acceleration(position, center, g_const):
    to_center = center - position
    r = to_center.length()
    if r == 0:
        return pygame.Vector2(0, 0)
    force = g_const / (r ** 2)
    direction = to_center.normalize()
    acceleration = direction * force
    return acceleration

def apply_gravity(ship, center, g_const, physics_dt):
    old_acceleration = compute_acceleration(ship.position, center, g_const)
    ship.position += ship.velocity * physics_dt + 0.5 * old_acceleration * (physics_dt ** 2)
    new_acceleration = compute_acceleration(ship.position, center, g_const)
    ship.velocity += 0.5 * (old_acceleration + new_acceleration) * physics_dt

def compute_orbit_elements(position, velocity, center, mu):
    r_vec = position - center
    r = r_vec.length()
    v = velocity.length()

    energy = (v ** 2) / 2 - mu / r

    a = -mu / (2 * energy)

    h = r_vec.x * velocity.y - r_vec.y * velocity.x

    e_squared = 1 + (2 * energy * h ** 2) / (mu ** 2)
    e = math.sqrt(max(e_squared, 0))

    apoapsis = a * (1 + e)
    periapsis = a * (1 - e)

    return apoapsis, periapsis, a, e

def get_orbit_points(position, velocity, center, mu, num_points=100):
    r_vec = position - center
    r = r_vec.length()
    v = velocity.length()
    energy = (v ** 2) / 2 - mu / r
    a = -mu / (2 * energy)

    h = r_vec.x * velocity.y - r_vec.y * velocity.x
    e_squared = 1 + (2 * energy * h ** 2) / (mu ** 2)
    e = math.sqrt(max(e_squared, 0))
    b = a * math.sqrt(max(1 - e ** 2, 0))

    rv_dot = r_vec.x * velocity.x + r_vec.y * velocity.y
    e_vec_x = ((v ** 2 - mu / r) * r_vec.x - rv_dot * velocity.x) / mu
    e_vec_y = ((v ** 2 - mu / r) * r_vec.y - rv_dot * velocity.y) / mu

    periapsis_angle = math.atan2(e_vec_y, e_vec_x)
    ellipse_center_x = center.x - a * e * math.cos(periapsis_angle)
    ellipse_center_y = center.y - a * e * math.sin(periapsis_angle)

    points = []
    for i in range(num_points):
        t = (i / num_points) * 2 * math.pi
        local_x = a * math.cos(t)
        local_y = b * math.sin(t)

        rotated_x = local_x * math.cos(periapsis_angle) - local_y * math.sin(periapsis_angle)
        rotated_y = local_x * math.sin(periapsis_angle) + local_y * math.cos(periapsis_angle)

        world_x = ellipse_center_x + rotated_x
        world_y = ellipse_center_y + rotated_y

        points.append((world_x, world_y))

    return points