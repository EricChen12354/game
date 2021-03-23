import pygame
import sys

pygame.init()

# ---------- GAME MODES ----------------
# Game mode 1: Classic
#   Classic space invaders, one life, enemies have health, enemies cannot shoot lasers, only shoot one laser at
#   a time, one enemies reach the bottom of your screen you lose, enemies move side to side and down as a group.
#     - Easy:
#     - Medium:
#     - Hard:

# Game mode 2: Heist
#   Safe with certain amount of health at the top of the screen, win by destroying the safe within a certain amount
#   of time, enemies have health, enemies spawn at certain rates, enemies shoot back, certain number of lives,
#   enemies move randomly
#     - Easy:
#     - Medium:
#     - Hard:

# Game mode 3:
#     - Easy:
#     - Medium:
#     - Hard:

# ---------- FUNCTIONS -----------------
def background_asteroids(coordinates, original_list):
    for i in range(len(coordinates)):
        coordinates[i][0] += 5
        coordinates[i][1] += 6
        if coordinates[i][0] >= WIDTH + 20 or coordinates[i][1] >= HEIGHT + 24:
            coordinates[i][0] = original_list[i][0]
            coordinates[i][1] = original_list[i][1]
        pygame.draw.ellipse(screen, YELLOW, [coordinates[i][0], coordinates[i][1], asteroids_size, asteroids_size])

    return coordinates


# The fade_window() function was taken from a TechWithTim video
# https://www.youtube.com/watch?v=H2r2N7D56Uw
def fade_window():
    f = pygame.Surface(SIZE)
    f.fill(BLACK)
    for a in range(0, 255):
        f.set_alpha(a)
        screen.blit(f, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


# ---------- SCREEN VARIABLES ----------
WIDTH = 500
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# ---------- COLOURS -------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# ---------- DISPLAY -------------------
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Space Fighters')
FONT_SIZE = 40
font = pygame.font.SysFont('Monospace', FONT_SIZE)

# ---------- GAME STATE ----------------
game_over = False
loading_screen = True
main_menu = False

# ---------- BACKGROUND ASTEROIDS ------
asteroids_size = 30
menu_asteroids = [[-5, 0], [-18, 150], [200, -5], [-19, 400]]
menu_asteroids_original = [[-5, 0], [-18, 150], [200, -5], [-5, 400]]

# ---------- FADING MAIN MENU TEXT -----
FADE_WIDTH = 310
FADE_HEIGHT = 20
FADE_SIZE = (FADE_WIDTH, FADE_HEIGHT)
fade = pygame.Surface(FADE_SIZE)
fade.fill(BLACK)
alpha = 1
change = 5

# ---------- GAME MODE SELECTION -------
RECT_WIDTH = 300
RECT_HEIGHT = 100
BACK_WIDTH = 300
BACK_HEIGHT = 50

# ---------- MAIN GAME LOOP-------------
while not game_over:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if loading_screen is True:
                fade_window()
                loading_screen = False
                main_menu = True

        elif event.type == pygame.KEYDOWN:
            if loading_screen is True:
                fade_window()
                loading_screen = False
                main_menu = True

    # LOADING SCREEN
    if loading_screen is True:

        screen.fill(BLACK)

        # Display game title
        font = pygame.font.SysFont('Monospace', 30)
        title_text = font.render('welcome to', True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
        screen.blit(title_text, title_text_rect)

        font = pygame.font.SysFont('Monospace', 55)
        title_text = font.render('SPACE FIGHTERS', True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(title_text, title_text_rect)

        # Next step instructions (fade in and out)
        font = pygame.font.SysFont('Monospace', 20)
        instructions_text = font.render('Press any key to continue.', True, WHITE)
        instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(instructions_text, instructions_text_rect)

        if alpha >= 255 or alpha <= 0:
            change *= -1
        alpha += change
        fade.set_alpha(alpha)
        screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, (HEIGHT - FADE_HEIGHT) / 2 + 50))

        # Draw and move background asteroids
        menu_asteroids = background_asteroids(menu_asteroids, menu_asteroids_original)

        pygame.display.update()

    # MAIN MENU, GAME SELECTION
    elif main_menu is True:

        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 50, RECT_WIDTH, RECT_HEIGHT], 3)
        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 200, RECT_WIDTH, RECT_HEIGHT], 3)
        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 350, RECT_WIDTH, RECT_HEIGHT], 3)
        pygame.draw.rect(screen, WHITE, [(WIDTH - BACK_WIDTH) / 2, 500, BACK_WIDTH, BACK_HEIGHT], 3)

        pygame.display.update()

    clock.tick(30)

