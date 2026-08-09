import pygame

def draw_panel(screen, font, x, y, width, title, lines, color=(150, 220, 150), show_separator=True):
    line_height = 22
    padding = 10
    height = padding * 2 + line_height * (len(lines) + 1)


    title_surface = font.render(title, True, color)
    screen.blit(title_surface, (x + padding, y + padding))
    separator_y = y + padding + line_height - 4
    pygame.draw.line(screen, color, (x, separator_y), (x + width, separator_y), 1)
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, (220, 255, 200))
        line_y = y + padding + line_height * (i + 1)
        screen.blit(line_surface, (x + padding, line_y))

    return height

def draw_grid_lines(screen, width, height, left_panel_width, bottom_panel_y, color=(80, 100, 80)):
    pygame.draw.line(screen, color, (left_panel_width, 0), (left_panel_width, height), 1)
    pygame.draw.line(screen, color, (0, bottom_panel_y), (left_panel_width, bottom_panel_y), 1)
    pygame.draw.line(screen, color, (left_panel_width, bottom_panel_y), (width, bottom_panel_y), 1)
    pygame.draw.rect(screen, color, (0, 0, width, height), 1)
    return height

def draw_naviball_placeholder(screen, font, x, y, width, height, color=(150, 220, 150)):
    title_surface = font.render("NAVBALL", True, color)
    screen.blit(title_surface, (x + 10, y + 10))

    circle_center_x = x + width // 2
    circle_center_y = y + 40 + (height - 40) // 2
    radius = min(width, height - 40) // 3

    pygame.draw.circle(screen, color, (circle_center_x, circle_center_y), radius, 1)
    pygame.draw.line(screen, color, (circle_center_x - radius, circle_center_y), (circle_center_x + radius, circle_center_y), 1)
    pygame.draw.line(screen, color, (circle_center_x, circle_center_y - radius), (circle_center_x, circle_center_y + radius), 1)

    return height