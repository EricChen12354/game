import pygame
import sys
import json

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

# Game mode 3: Escort
#   Another ship carrying a shipment, need to escort the shipment. Use wasd to move, win by delivering to the
#   finish line, lose if shipment gets destroyed or if you die. Enemies shoot back and can only move side to side
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
def fade_out():
    f_out = pygame.Surface(SIZE)
    f_out.fill(BACKGROUND_COLOUR)
    for a in range(0, 255):
        f_out.set_alpha(a)
        screen.blit(f_out, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


def fade_in():
    f_in = pygame.Surface(SIZE)
    f_in.fill(BACKGROUND_COLOUR)
    for a in range(255, -1, -1):
        f_in.set_alpha(a)
        screen.blit(f_in, (0, 0))
        pygame.display.update()


# ---------- SCREEN VARIABLES ----------
WIDTH = 500
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# ---------- COLOURS -------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_PURPLE = (15, 0, 15)
BACKGROUND_COLOUR = DARK_PURPLE

# ---------- DISPLAY -------------------
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Space Fighters')
FONT_SIZE = 40
font = pygame.font.SysFont('Monospace', FONT_SIZE)

# ---------- GAME STATE ----------------
game_over = False
loading_screen = True
log_in = False
profile_screen = False
main_menu = False
classic_difficulty_selection = False
heist_difficulty_selection = False
escort_difficulty_selection = False

# ---------- BACKGROUND ASTEROIDS ------
asteroids_size = 30
menu_asteroids = [[-5, 0], [-18, 150], [200, -5], [-19, 400]]
menu_asteroids_original = [[-5, 0], [-18, 150], [200, -5], [-5, 400]]

# ---------- FADING MAIN MENU TEXT -----
FADE_WIDTH = 310
FADE_HEIGHT = 20
FADE_SIZE = (FADE_WIDTH, FADE_HEIGHT)
fade = pygame.Surface(FADE_SIZE)
fade.fill(BACKGROUND_COLOUR)
alpha = 1
change = 5

# ---------- USER LOG IN ---------------
username = ''
BOX_WIDTH = 400
BOX_HEIGHT = 100
CLEAR_WIDTH = 175
CLEAR_HEIGHT = 50

# ---------- PROFILE PAGE --------------
with open('usernames.json', 'r') as f:
    usernames = json.load(f)

message = ''

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
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if loading_screen is True:
                fade_out()
                loading_screen = False
                log_in = True

            elif log_in is True:
                # Clear button
                if 50 <= mouse_x <= 225 and 400 <= mouse_y <= 450:
                    username = ''

                # Save button
                elif 275 <= mouse_x <= 450 and 400 <= mouse_y <= 450:
                    fade_out()
                    log_in = False
                    profile_screen = True

            elif main_menu is True:
                # Back button
                if 100 <= mouse_x <= 400 and 500 <= mouse_y <= 550:
                    fade_out()
                    main_menu = False
                    log_in = True

                # Classic mode
                if 100 <= mouse_x <= 400 and 50 <= mouse_y <= 150:
                    fade_out()
                    main_menu = False
                    classic_difficulty_selection = True

                # Heist mode
                if 100 <= mouse_x <= 400 and 200 <= mouse_y <= 300:
                    fade_out()
                    main_menu = False
                    heist_difficulty_selection = True

                # Escort mode
                if 100 <= mouse_x <= 400 and 350 <= mouse_y <= 450:
                    fade_out()
                    main_menu = False
                    escort_difficulty_selection = True

            elif profile_screen is True:
                fade_out()
                profile_screen = False
                main_menu = True

        elif event.type == pygame.KEYDOWN:
            # usernames have a maximum length of 20 characters and can contain numbers and lower case letters
            # CHANGE USERNAME TO UPPERCASE AND SAVE WHEN USER PRESSES ENTER
            if log_in is True and len(username) < 16:
                if event.key == pygame.K_a:
                    username += 'A'
                elif event.key == pygame.K_b:
                    username += 'B'
                elif event.key == pygame.K_c:
                    username += 'C'
                elif event.key == pygame.K_d:
                    username += 'D'
                elif event.key == pygame.K_e:
                    username += 'E'
                elif event.key == pygame.K_f:
                    username += 'F'
                elif event.key == pygame.K_g:
                    username += 'G'
                elif event.key == pygame.K_h:
                    username += 'H'
                elif event.key == pygame.K_i:
                    username += 'I'
                elif event.key == pygame.K_j:
                    username += 'J'
                elif event.key == pygame.K_k:
                    username += 'K'
                elif event.key == pygame.K_l:
                    username += 'L'
                elif event.key == pygame.K_m:
                    username += 'M'
                elif event.key == pygame.K_n:
                    username += 'N'
                elif event.key == pygame.K_o:
                    username += 'O'
                elif event.key == pygame.K_p:
                    username += 'P'
                elif event.key == pygame.K_q:
                    username += 'Q'
                elif event.key == pygame.K_r:
                    username += 'R'
                elif event.key == pygame.K_s:
                    username += 'S'
                elif event.key == pygame.K_t:
                    username += 'T'
                elif event.key == pygame.K_u:
                    username += 'U'
                elif event.key == pygame.K_v:
                    username += 'V'
                elif event.key == pygame.K_w:
                    username += 'W'
                elif event.key == pygame.K_x:
                    username += 'X'
                elif event.key == pygame.K_y:
                    username += 'Y'
                elif event.key == pygame.K_z:
                    username += 'Z'
                elif event.key == pygame.K_SPACE:
                    username += ' '
                elif event.key == pygame.K_0:
                    username += '0'
                elif event.key == pygame.K_1:
                    username += '1'
                elif event.key == pygame.K_2:
                    username += '2'
                elif event.key == pygame.K_3:
                    username += '3'
                elif event.key == pygame.K_4:
                    username += '4'
                elif event.key == pygame.K_5:
                    username += '5'
                elif event.key == pygame.K_6:
                    username += '6'
                elif event.key == pygame.K_7:
                    username += '7'
                elif event.key == pygame.K_8:
                    username += '8'
                elif event.key == pygame.K_9:
                    username += '9'
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

            if log_in is True:
                if event.key == pygame.K_RETURN:
                    fade_out()
                    log_in = False
                    profile_screen = True

            elif loading_screen is True:
                fade_out()
                loading_screen = False
                log_in = True

            elif profile_screen is True:
                fade_out()
                profile_screen = False
                main_menu = True

    # LOADING SCREEN
    if loading_screen is True:

        screen.fill(BACKGROUND_COLOUR)

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

    # USER LOG IN
    elif log_in is True:

        screen.fill(BACKGROUND_COLOUR)

        # Box around username
        pygame.draw.rect(screen, WHITE, [(WIDTH - BOX_WIDTH) / 2, (HEIGHT - BOX_HEIGHT) / 2, BOX_WIDTH, BOX_HEIGHT], 3)

        # "Sign in" text
        font = pygame.font.SysFont('Monospace', 50)
        sign_in = font.render('Sign in:', True, WHITE)
        sign_in_rect = sign_in.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        screen.blit(sign_in, sign_in_rect)

        # Username text
        font = pygame.font.SysFont('Monospace', 30)
        username_text = font.render(f'{username}', True, WHITE)
        username_text_rect = username_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(username_text, username_text_rect)

        # Clear button
        pygame.draw.rect(screen, WHITE, [50, 400, CLEAR_WIDTH, CLEAR_HEIGHT])

        clear_text = font.render('CLEAR', True, BACKGROUND_COLOUR)
        clear_text_rect = clear_text.get_rect(center=(WIDTH / 2 - 115, HEIGHT / 2 + CLEAR_HEIGHT / 2 + 100))
        screen.blit(clear_text, clear_text_rect)

        # Save button
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 25, 400, CLEAR_WIDTH, CLEAR_HEIGHT])

        save_text = font.render('SAVE', True, BACKGROUND_COLOUR)
        save_text_rect = save_text.get_rect(center=(WIDTH / 2 + 110, HEIGHT / 2 + CLEAR_HEIGHT / 2 + 100))
        screen.blit(save_text, save_text_rect)

        # Draw and move background asteroids
        menu_asteroids = background_asteroids(menu_asteroids, menu_asteroids_original)

        pygame.display.update()

    # PROFILE PAGE
    elif profile_screen is True:

        # Display player name
        # ERROR: DISPLAYS "WELCOME" AND THEN "WELCOME BACK"!!!!!
        if username in usernames:
            message = f'Welcome back {username}!'
        else:
            message = f'Welcome {username}!'

            # Create and add profile to json file
            usernames[username] = {"classic": [" - ", " - ", " - "], "heist": [" - ", " - ", " - "], "escort": [" - ", " - ", " - "]}

            with open('usernames.json', 'w') as f:
                json.dump(usernames, f, indent=4)

        font = pygame.font.SysFont('Monospace', 30)
        welcome_text = font.render(message, True, WHITE)
        welcome_text_rect = welcome_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(welcome_text, welcome_text_rect)

        # Display classic scores
        pygame.draw.rect(screen, WHITE, [50, 100, 400, 150], 5)

        font = pygame.font.SysFont('Monospace', 30)
        classic_text = font.render('CLASSIC', True, WHITE)
        classic_text_rect = classic_text.get_rect(center=(150, 175))
        screen.blit(classic_text, classic_text_rect)

        # Easy difficulty
        font = pygame.font.SysFont('Monospace', 20)
        classic_easy_score = str(usernames[username]["classic"][0])
        classic_easy_text = font.render(f'Easy: {classic_easy_score}', True, GREEN)
        classic_easy_text_rect = classic_easy_text.get_rect(center=(350, 135))
        screen.blit(classic_easy_text, classic_easy_text_rect)

        # Medium difficulty
        classic_medium_score = str(usernames[username]["classic"][1])
        classic_medium_text = font.render(f'Medium: {classic_medium_score}', True, YELLOW)
        classic_medium_text_rect = classic_medium_text.get_rect(center=(350, 175))
        screen.blit(classic_medium_text, classic_medium_text_rect)

        # Hard difficulty
        classic_hard_score = str(usernames[username]["classic"][2])
        classic_hard_text = font.render(f'Hard: {classic_hard_score}', True, RED)
        classic_hard_text_rect = classic_hard_text.get_rect(center=(350, 215))
        screen.blit(classic_hard_text, classic_hard_text_rect)

        # Display heist scores
        pygame.draw.rect(screen, WHITE, [50, 250, 400, 150], 5)

        font = pygame.font.SysFont('Monospace', 30)
        heist_text = font.render('HEIST', True, WHITE)
        heist_text_rect = heist_text.get_rect(center=(150, 325))
        screen.blit(heist_text, heist_text_rect)

        # Easy difficulty
        font = pygame.font.SysFont('Monospace', 20)
        heist_easy_score = str(usernames[username]["heist"][0])
        heist_easy_text = font.render(f'Easy: {heist_easy_score}', True, GREEN)
        heist_easy_text_rect = heist_easy_text.get_rect(center=(350, 285))
        screen.blit(heist_easy_text, heist_easy_text_rect)

        # Medium difficulty
        heist_medium_score = str(usernames[username]["heist"][1])
        heist_medium_text = font.render(f'Medium: {heist_medium_score}', True, YELLOW)
        heist_medium_text_rect = heist_medium_text.get_rect(center=(350, 325))
        screen.blit(heist_medium_text, heist_medium_text_rect)

        # Hard difficulty
        heist_hard_score = str(usernames[username]["heist"][2])
        heist_hard_text = font.render(f'Hard: {heist_hard_score}', True, RED)
        heist_hard_text_rect = heist_hard_text.get_rect(center=(350, 365))
        screen.blit(heist_hard_text, heist_hard_text_rect)

        # Display escort scores
        pygame.draw.rect(screen, WHITE, [50, 400, 400, 150], 5)

        font = pygame.font.SysFont('Monospace', 30)
        heist_text = font.render('ESCORT', True, WHITE)
        heist_text_rect = heist_text.get_rect(center=(150, 475))
        screen.blit(heist_text, heist_text_rect)

        # Easy difficulty
        font = pygame.font.SysFont('Monospace', 20)
        escort_easy_score = str(usernames[username]["escort"][0])
        escort_easy_text = font.render(f'Easy: {escort_easy_score}', True, GREEN)
        escort_easy_text_rect = escort_easy_text.get_rect(center=(350, 435))
        screen.blit(escort_easy_text, escort_easy_text_rect)

        # Medium difficulty
        escort_medium_score = str(usernames[username]["escort"][1])
        escort_medium_text = font.render(f'Medium: {escort_medium_score}', True, YELLOW)
        escort_medium_text_rect = escort_medium_text.get_rect(center=(350, 475))
        screen.blit(escort_medium_text, escort_medium_text_rect)

        # Hard difficulty
        escort_hard_score = str(usernames[username]["escort"][2])
        escort_hard_text = font.render(f'Hard: {escort_hard_score}', True, RED)
        escort_hard_text_rect = escort_hard_text.get_rect(center=(350, 515))
        screen.blit(escort_hard_text, escort_hard_text_rect)

        # Next step instructions (fade in and out)
        font = pygame.font.SysFont('Monospace', 20)
        instructions_text = font.render('Press any key to continue.', True, WHITE)
        instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, HEIGHT - 30))
        screen.blit(instructions_text, instructions_text_rect)

        if alpha >= 255 or alpha <= 0:
            change *= -1
        alpha += change
        fade.set_alpha(alpha)
        screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, HEIGHT - 40))

        pygame.display.update()

    # MAIN MENU, GAME SELECTION
    elif main_menu is True:

        screen.fill(BACKGROUND_COLOUR)

        # Classic game mode
        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 50, RECT_WIDTH, RECT_HEIGHT], 3)
        font = pygame.font.SysFont('Monospace', 30)
        classic_text = font.render('Classic', True, WHITE)
        classic_rect = classic_text.get_rect(center=(WIDTH / 2, 100))
        screen.blit(classic_text, classic_rect)

        # Heist game mode
        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 200, RECT_WIDTH, RECT_HEIGHT], 3)
        font = pygame.font.SysFont('Monospace', 30)
        classic_text = font.render('Heist', True, WHITE)
        classic_rect = classic_text.get_rect(center=(WIDTH / 2, 250))
        screen.blit(classic_text, classic_rect)

        # Escort game mode
        pygame.draw.rect(screen, WHITE, [(WIDTH - RECT_WIDTH) / 2, 350, RECT_WIDTH, RECT_HEIGHT], 3)
        font = pygame.font.SysFont('Monospace', 30)
        classic_text = font.render('Escort', True, WHITE)
        classic_rect = classic_text.get_rect(center=(WIDTH / 2, 400))
        screen.blit(classic_text, classic_rect)

        # Back
        pygame.draw.rect(screen, WHITE, [(WIDTH - BACK_WIDTH) / 2, 500, BACK_WIDTH, BACK_HEIGHT], 3)
        font = pygame.font.SysFont('Monospace', 25)
        back_text = font.render('← BACK', True, WHITE)
        back_rect = back_text.get_rect(center=(WIDTH / 2, 525))
        screen.blit(back_text, back_rect)

        pygame.display.update()

    # CLASSIC MODE DIFFICULTY SELECTION
    elif classic_difficulty_selection is True:
        # Title
        font = pygame.font.SysFont('Monospace', 50)
        classic_text = font.render('Classic Mode', True, WHITE)
        classic_text_rect = classic_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(classic_text, classic_text_rect)

        # Easy
        pygame.draw.rect(screen, GREEN, [50, 100, 400, 100], 3)

        # Medium
        pygame.draw.rect(screen, YELLOW, [50, 210, 400, 100], 3)

        # Hard
        pygame.draw.rect(screen, RED, [50, 320, 400, 100], 3)

        # Back
        pygame.draw.rect(screen, WHITE, [50, 430, 185, 100], 3)

        # Tutorial
        pygame.draw.rect(screen, WHITE, [265, 430, 185, 100], 3)

        pygame.display.update()

    # HEIST MODE DIFFICULTY SELECTION
    elif heist_difficulty_selection is True:
        pass

    # ESCORT MODE DIFFICULTY SELECTION
    elif escort_difficulty_selection is True:
        pass

    clock.tick(30)
