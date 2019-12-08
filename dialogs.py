"""Здесь будет храниться сюжет игры (текст реплик)"""
import pygame

# --- constants --- (UPPER_CASE names)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- classes --- (CamelCase names)

# empty

# --- functions --- (lower_came names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

# - objects -

default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 45)

# - mainloop -

count_time = 1
running = True

while running:

    # --- events ---

    for event in pygame.event.get():
        # close window with button `X`
        if event.type == pygame.QUIT:
            running = False

        # close window with key `ESC`
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- updates (without draws) ---

    label = font_renderer.render(str(count_time), True, WHITE)
    label_rect = label.get_rect()
    # center on screen
    label_rect.center = screen_rect.center

    count_time += 1
    if count_time >= 4:
        running = False

    # --- draws (without updates) ---

    screen.fill(BLACK)
    screen.blit(label, label_rect)
    pygame.display.flip()

    # --- speed ---

    # 1000ms = 1s
    pygame.time.delay(1)

# - end -

pygame.quit()

def say(obj, id):
    pass
