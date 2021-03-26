import pygame
import sys
import json
import time

pygame.init()

# ---------- GAME MODES ----------------
# Game mode 1: Classic
#   Classic space invaders, one life, enemies have health, enemies cannot shoot lasers, only shoot one laser at
#   a time, one enemies reach the bottom of your screen you lose, enemies move side to side and down as a group.
#     - Easy:
#     - Medium:
#     - Hard:
#   Tutorial:
#       This is your space ship, use "A" and "D"
#       to strafe left and right. Press "SPACE" or
#       left click your mouse to fire a laser. You
#       have a certain number of lives depending on
#       the difficulty.
#
#       This is an enemy. They come in waves and
#       move left and right as a group. They cannot
#       shoot you back. They take a certain amount
#       of shots to kill, depending on the difficulty.
#
#       To win, you must clear the airspace of enemies
#       and complete all the waves. Good luck!.

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


def difficulty_selection(mode):
    # Title
    font = pygame.font.SysFont('Monospace', 50)
    title_text = font.render(f'{mode.title()} Mode', True, WHITE)
    title_text_rect = title_text.get_rect(center=(WIDTH / 2, 50))
    screen.blit(title_text, title_text_rect)

    # Easy
    pygame.draw.rect(screen, GREEN, [50, 100, 400, 100], 5)

    font = pygame.font.SysFont('Monospace', 30)
    easy_text = font.render('Easy', True, GREEN)
    easy_text_rect = easy_text.get_rect(center=(WIDTH / 2, 130))
    screen.blit(easy_text, easy_text_rect)

    font = pygame.font.SysFont('Monospace', 20)
    mode_easy_high_score = usernames[username][mode][0]
    easy_high_score = font.render(f'High score: {mode_easy_high_score}', True, GREEN)
    easy_high_score_rect = easy_high_score.get_rect(center=(WIDTH / 2, 165))
    screen.blit(easy_high_score, easy_high_score_rect)

    # Medium
    pygame.draw.rect(screen, YELLOW, [50, 210, 400, 100], 5)

    font = pygame.font.SysFont('Monospace', 30)
    medium_text = font.render('Medium', True, YELLOW)
    medium_text_rect = medium_text.get_rect(center=(WIDTH / 2, 240))
    screen.blit(medium_text, medium_text_rect)

    font = pygame.font.SysFont('Monospace', 20)
    mode_medium_high_score = usernames[username][mode][1]
    medium_high_score = font.render(f'High score: {mode_medium_high_score}', True, YELLOW)
    medium_high_score_rect = medium_high_score.get_rect(center=(WIDTH / 2, 275))
    screen.blit(medium_high_score, medium_high_score_rect)

    # Hard
    pygame.draw.rect(screen, RED, [50, 320, 400, 100], 5)

    font = pygame.font.SysFont('Monospace', 30)
    hard_text = font.render('Hard', True, RED)
    hard_text_rect = hard_text.get_rect(center=(WIDTH / 2, 350))
    screen.blit(hard_text, hard_text_rect)

    font = pygame.font.SysFont('Monospace', 20)
    mode_hard_high_score = usernames[username][mode][2]
    hard_high_score = font.render(f'High score: {mode_hard_high_score}', True, RED)
    hard_high_score_rect = hard_high_score.get_rect(center=(WIDTH / 2, 385))
    screen.blit(hard_high_score, hard_high_score_rect)

    # Back
    pygame.draw.rect(screen, WHITE, [50, 450, 185, 100], 5)

    font = pygame.font.SysFont('Monospace', 30)
    back_text = font.render('BACK', True, WHITE)
    back_text_rect = back_text.get_rect(center=(142, 500))
    screen.blit(back_text, back_text_rect)

    # Tutorial
    pygame.draw.rect(screen, WHITE, [265, 450, 185, 100], 5)

    tutorial_text = font.render('TUTORIAL', True, WHITE)
    tutorial_text_rect = tutorial_text.get_rect(center=(357, 500))
    screen.blit(tutorial_text, tutorial_text_rect)

    pygame.display.update()


def game_over():
    font = pygame.font.SysFont('Monospace', 30)
    game_over_text = font.render('GAME OVER', True, WHITE)
    game_over_text_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(game_over_text, game_over_text_rect)

    pygame.display.update()

    time.sleep(3)
    fade_out()


def win():
    font = pygame.font.SysFont('Monospace', 30)
    win_text = font.render('YOU WIN', True, WHITE)
    win_text_rect = win_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(win_text, win_text_rect)

    pygame.display.update()

    time.sleep(3)
    fade_out()


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
finished = False
loading_screen = True
log_in = False
profile_screen = False
main_menu = False

classic_difficulty_selection = False
heist_difficulty_selection = False
escort_difficulty_selection = False

classic_easy = False
classic_medium = False
classic_hard = False
classic_tutorial = False

heist_easy = False
heist_medium = False
heist_hard = False
heist_tutorial = False

escort_easy = False
escort_medium = False
escort_hard = False
escort_tutorial = False

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

# ---------- GAME MODE TUTORIALS -------
classic_description = ['This is your space ship,',
                       'use "A" and "D" to strafe',
                       'left and right. Press "SPACE"',
                       'to fire a laser.',
                       '',
                       'This is an enemy. They come',
                       'in waves and move left and right ',
                       'as a group. They cannot shoot.',
                       'They take a certain amount of ',
                       'shots to kill, depending on the ',
                       'difficulty.',
                       '',
                       'To win, you must clear the ',
                       'airspace of enemies and complete ',
                       'all the waves. Don\'t run out of ',
                       'lives! Good luck!.',
                       ]

# ---------- CLASSIC EASY --------------
start = False
ship_x = WIDTH / 2 - 32
ship_y = 500
enemy_pos_easy = [[10, -38], [10, 10], [10, 58], [10, 106], [10, 154],
             [68, -38], [68, 10], [68, 58], [68, 106], [68, 154],
             [126, -38], [126, 10], [126, 58], [126, 106], [126, 154],
             [184, -38], [184, 10], [184, 58], [184, 106], [184, 154],
             [242, -38], [242, 10], [242, 58], [242, 106], [242, 154],
             [300, -38], [300, 10], [300, 58], [300, 106], [300, 154]
             ]
enemy_speed_easy = 2
laser_pos = []
laser_off_screen = False
laser_del = []
enemy_del = []
classic_easy_score = 0

# ---------- CLASSIC MEDIUM ------------
enemy_pos_medium = [[10, -86], [10, -38], [10, 10], [10, 58], [10, 106], [10, 154],
             [68, -86], [68, -38], [68, 10], [68, 58], [68, 106], [68, 154],
             [126, -86], [126, -38], [126, 10], [126, 58], [126, 106], [126, 154],
             [184, -86], [184, -38], [184, 10], [184, 58], [184, 106], [184, 154],
             [242, -86], [242, -38], [242, 10], [242, 58], [242, 106], [242, 154],
             [300, -86], [300, -38], [300, 10], [300, 58], [300, 106], [300, 154],
             [358, -86], [358, -38], [358, 10], [358, 58], [358, 106], [358, 154]
             ]
enemy_speed_medium = 3
classic_medium_score = 0

# ---------- CLASSIC HARD --------------
enemy_pos_hard = [[10, 10], [10, 58], [10, 106],
             [68, 10], [68, 58], [68, 106],
             [126, 10], [126, 58], [126, 106],
             [184, 10], [184, 58], [184, 106],
             [242, 10], [242, 58], [242, 106],
             [300, 10], [300, 58], [300, 106],
             ]
enemy_speed_hard = 5
classic_hard_score = 0

# ---------- MAIN GAME LOOP-------------
while not finished:

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

            elif classic_easy is True:
                if start is False:
                    start = True

            elif classic_medium is True:
                if start is False:
                    start = True

            elif classic_hard is True:
                if start is False:
                    start = True

            elif classic_tutorial is True:
                fade_out()
                classic_tutorial = False
                classic_difficulty_selection = True

            elif classic_difficulty_selection is True:
                if 50 <= mouse_x <= 450 and 100 <= mouse_y <= 200:
                    fade_out()
                    classic_difficulty_selection = False
                    classic_easy = True
                elif 50 <= mouse_x <= 450 and 210 <= mouse_y <= 310:
                    fade_out()
                    classic_difficulty_selection = False
                    classic_medium = True
                elif 50 <= mouse_x <= 450 and 320 <= mouse_y <= 420:
                    fade_out()
                    classic_difficulty_selection = False
                    classic_hard = True
                elif 50 <= mouse_x <= 235 and 450 <= mouse_y <= 550:
                    fade_out()
                    classic_difficulty_selection = False
                    main_menu = True
                elif 265 <= mouse_x <= 450 <= mouse_y <= 550:
                    fade_out()
                    classic_difficulty_selection = False
                    classic_tutorial = True

            elif heist_difficulty_selection is True:
                if 50 <= mouse_x <= 450 and 100 <= mouse_y <= 200:
                    fade_out()
                    heist_difficulty_selection = False
                    heist_easy = True
                elif 50 <= mouse_x <= 450 and 210 <= mouse_y <= 310:
                    fade_out()
                    heist_difficulty_selection = False
                    heist_medium = True
                elif 50 <= mouse_x <= 450 and 320 <= mouse_y <= 420:
                    fade_out()
                    heist_difficulty_selection = False
                    heist_hard = True
                elif 50 <= mouse_x <= 235 and 450 <= mouse_y <= 550:
                    fade_out()
                    heist_difficulty_selection = False
                    main_menu = True
                elif 265 <= mouse_x <= 450 <= mouse_y <= 550:
                    fade_out()
                    heist_difficulty_selection = False
                    classic_tutorial = True

            elif escort_difficulty_selection is True:
                if 50 <= mouse_x <= 450 and 100 <= mouse_y <= 200:
                    fade_out()
                    escort_difficulty_selection = False
                    escort_easy = True
                elif 50 <= mouse_x <= 450 and 210 <= mouse_y <= 310:
                    fade_out()
                    escort_difficulty_selection = False
                    escort_medium = True
                elif 50 <= mouse_x <= 450 and 320 <= mouse_y <= 420:
                    fade_out()
                    escort_difficulty_selection = False
                    escort_hard = True
                elif 50 <= mouse_x <= 235 and 450 <= mouse_y <= 550:
                    fade_out()
                    escort_difficulty_selection = False
                    main_menu = True
                elif 265 <= mouse_x <= 450 <= mouse_y <= 550:
                    fade_out()
                    escort_difficulty_selection = False
                    escort_tutorial = True

            elif log_in is True:
                # Clear button
                if 50 <= mouse_x <= 225 and 400 <= mouse_y <= 450:
                    username = ''

                # Save button
                elif 275 <= mouse_x <= 450 and 400 <= mouse_y <= 450:
                    fade_out()
                    log_in = False
                    profile_screen = True

                    if username in usernames:
                        message = f'Welcome back {username}!'
                    else:
                        message = f'Welcome {username}!'

                        # Create and add profile to json file
                        usernames[username] = {"classic": [0, 0, 0], "heist": [0, 0, 0],
                                               "escort": [0, 0, 0]}

                        with open('usernames.json', 'w') as f:
                            json.dump(usernames, f, indent=4)

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

                    if username in usernames:
                        message = f'Welcome back {username}!'
                    else:
                        message = f'Welcome {username}!'

                        # Create and add profile to json file
                        usernames[username] = {"classic": [" - ", " - ", " - "], "heist": [" - ", " - ", " - "],
                                               "escort": [" - ", " - ", " - "]}

                        with open('usernames.json', 'w') as f:
                            json.dump(usernames, f, indent=4)

            elif classic_easy is True and start is True or classic_medium is True and start is True or classic_hard is True and start is True:
                if event.key == pygame.K_SPACE:
                    if len(laser_pos) != 0 and laser_pos[-1][1] >= ship_y - 30:
                        pass
                    else:
                        laser_pos.append([ship_x + 27, ship_y])
                        if classic_medium is True:
                            classic_medium_score = int(classic_medium_score)
                            classic_medium_score -= 10
                        elif classic_hard is True:
                            classic_hard_score = int(classic_hard_score)
                            classic_hard_score -= 50

            elif classic_easy is True or classic_medium is True or classic_hard is True:
                if start is False:
                    start = True

            elif classic_tutorial is True:
                fade_out()
                classic_tutorial = False
                classic_difficulty_selection = True

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
        screen.fill(BACKGROUND_COLOUR)
        difficulty_selection("classic")

    # CLASSIC MODE TUTORIAL
    elif classic_tutorial is True:
        # Tutorial
        font = pygame.font.SysFont('Monospace', 50)
        tutorial_text = font.render('Tutorial', True, WHITE)
        tutorial_text_rect = tutorial_text.get_rect(center=(WIDTH / 2, 60))
        screen.blit(tutorial_text, tutorial_text_rect)

        # Display description
        for i in range(len(classic_description)):
            font = pygame.font.SysFont('Monospace', 17)
            description_text = font.render(classic_description[i], True, WHITE)
            description_text_rect = description_text.get_rect(center=(200, 150 + 20 * i))
            screen.blit(description_text, description_text_rect)

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (390, 160))

        # Draw enemy ship icon
        enemy = pygame.image.load('enemy.png')
        screen.blit(enemy, (400, 300))

        # Draw star
        star = pygame.image.load('star.png')
        screen.blit(star, (400, 415))

        # Back (fade in and out)
        font = pygame.font.SysFont('Monospace', 20)
        instructions_text = font.render('Press any key to continue.', True, WHITE)
        instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, 550))
        screen.blit(instructions_text, instructions_text_rect)

        if alpha >= 255 or alpha <= 0:
            change *= -1
        alpha += change
        fade.set_alpha(alpha)
        screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, 540))

        pygame.display.update()

    # CLASSIC MODE EASY
    elif classic_easy is True:
        screen.fill(BACKGROUND_COLOUR)

        # Start
        if start is False:
            # Next step instructions (fade in and out)
            font = pygame.font.SysFont('Monospace', 20)
            instructions_text = font.render('Press any key to continue.', True, WHITE)
            instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(instructions_text, instructions_text_rect)

            if alpha >= 255 or alpha <= 0:
                change *= -1
            alpha += change
            fade.set_alpha(alpha)
            screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, (HEIGHT - FADE_HEIGHT) / 2))
        else:
            # Ship movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if ship_x >= 0:
                    ship_x -= 5
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if ship_x <= WIDTH - 64:
                    ship_x += 5

            # Enemy movement
            if enemy_pos_easy[-1][0] + 48 + enemy_speed_easy > WIDTH or enemy_pos_easy[0][0] + enemy_speed_easy < 0:
                enemy_speed_easy *= -1
                for i in range(len(enemy_pos_easy)):
                    enemy_pos_easy[i][1] += 48
                    # If enemies reach past your ship, you lose
                    if enemy_pos_easy[i][1] >= ship_y:
                        game_over()
                        classic_easy = False
                        classic_difficulty_selection = True
                        start = False
                        enemy_pos_easy = [[10, -38], [68, -38], [126, -38], [184, -38], [242, -38], [300, -38],
                                     [10, 10], [68, 10], [126, 10], [184, 10], [242, 10], [300, 10],
                                     [10, 58], [68, 58], [126, 58], [184, 58], [242, 58], [300, 58],
                                     [10, 106], [68, 106], [126, 106], [184, 106], [242, 106], [300, 106],
                                     [10, 154], [68, 154], [126, 154], [184, 154], [242, 154], [300, 154]
                                     ]
                        ship_x = WIDTH / 2 - 32
                        ship_y = 500
                        laser_pos = []
                        laser_off_screen = False

                        if classic_easy_score > usernames[username]["classic"][0]:
                            usernames[username]["classic"][0] = classic_easy_score

                            with open('usernames.json', 'w') as f:
                                json.dump(usernames, f)

                        classic_easy_score = 0

                        screen.fill(BACKGROUND_COLOUR)
                        # process score

            for i in range(len(enemy_pos_easy)):
                enemy_pos_easy[i][0] += enemy_speed_easy

            # Laser movement
            laser = pygame.image.load('laser.png')
            for i in range(len(laser_pos)):
                if laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    laser_pos[i][1] -= 7
                    screen.blit(laser, (laser_pos[i][0], laser_pos[i][1]))

                    # Laser collision with enemy
                    for j in range(len(enemy_pos_easy)):
                        if enemy_pos_easy[j][0] <= laser_pos[i][0] <= enemy_pos_easy[j][0] + 48:
                            if enemy_pos_easy[j][1] <= laser_pos[i][1] <= enemy_pos_easy[j][1] + 48:
                                enemy_del.append(j)
                                laser_del.append(i)
                                classic_easy_score = int(classic_easy_score)
                                classic_easy_score += 100

            if laser_off_screen:
                laser_pos.pop(0)
                laser_off_screen = False

            if len(enemy_del) != 0:
                enemy_pos_easy.pop(enemy_del[0])
                enemy_del.clear()
            if len(laser_del) != 0:
                laser_pos.pop(laser_del[0])
                laser_del.clear()

            # If all enemies are dead
            if len(enemy_pos_easy) == 0:
                win()
                classic_easy = False
                classic_difficulty_selection = True
                start = False
                enemy_pos_easy = [[10, -38], [68, -38], [126, -38], [184, -38], [242, -38], [300, -38],
                             [10, 10], [68, 10], [126, 10], [184, 10], [242, 10], [300, 10],
                             [10, 58], [68, 58], [126, 58], [184, 58], [242, 58], [300, 58],
                             [10, 106], [68, 106], [126, 106], [184, 106], [242, 106], [300, 106],
                             [10, 154], [68, 154], [126, 154], [184, 154], [242, 154], [300, 154]
                             ]
                ship_x = WIDTH / 2 - 32
                ship_y = 500
                laser_pos = []
                laser_off_screen = False

                if classic_easy_score > usernames[username]["classic"][0]:
                    usernames[username]["classic"][0] = classic_easy_score

                    with open('usernames.json', 'w') as f:
                        json.dump(usernames, f)

                classic_easy_score = 0

                screen.fill(BACKGROUND_COLOUR)

        # Draw enemies
        for pos in enemy_pos_easy:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw score
        font = pygame.font.SysFont('Monospace', 30)
        score_text = font.render(str(classic_easy_score), True, RED)
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(score_text, score_text_rect)

        pygame.display.update()

    # CLASSIC MODE MEDIUM
    elif classic_medium is True:
        screen.fill(BACKGROUND_COLOUR)

        # Start
        if start is False:
            classic_medium_score = 0
            # Next step instructions (fade in and out)
            font = pygame.font.SysFont('Monospace', 20)
            instructions_text = font.render('Press any key to continue.', True, WHITE)
            instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(instructions_text, instructions_text_rect)

            if alpha >= 255 or alpha <= 0:
                change *= -1
            alpha += change
            fade.set_alpha(alpha)
            screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, (HEIGHT - FADE_HEIGHT) / 2))
        else:
            # Ship movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if ship_x >= 0:
                    ship_x -= 7
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if ship_x <= WIDTH - 64:
                    ship_x += 7

            # Enemy movement
            if enemy_pos_medium[-1][0] + 48 + enemy_speed_medium > WIDTH or enemy_pos_medium[0][0] + enemy_speed_medium < 0:
                enemy_speed_medium *= -1
                for i in range(len(enemy_pos_medium)):
                    enemy_pos_medium[i][1] += 48
                    # If enemies reach past your ship, you lose
                    if enemy_pos_medium[i][1] >= ship_y:
                        game_over()
                        classic_medium = False
                        classic_difficulty_selection = True
                        start = False
                        enemy_pos_medium = [[10, -86], [10, -38], [10, 10], [10, 58], [10, 106], [10, 154],
                                            [68, -86], [68, -38], [68, 10], [68, 58], [68, 106], [68, 154],
                                            [126, -86], [126, -38], [126, 10], [126, 58], [126, 106], [126, 154],
                                            [184, -86], [184, -38], [184, 10], [184, 58], [184, 106], [184, 154],
                                            [242, -86], [242, -38], [242, 10], [242, 58], [242, 106], [242, 154],
                                            [300, -86], [300, -38], [300, 10], [300, 58], [300, 106], [300, 154],
                                            [358, -86], [358, -38], [358, 10], [358, 58], [358, 106], [358, 154]
                                            ]
                        ship_x = WIDTH / 2 - 32
                        ship_y = 500
                        laser_pos = []
                        laser_off_screen = False

                        if classic_medium_score > usernames[username]["classic"][1]:
                            usernames[username]["classic"][1] = classic_medium_score

                            with open('usernames.json', 'w') as f:
                                json.dump(usernames, f)

                        classic_medium_score = 0

                        screen.fill(BACKGROUND_COLOUR)
                        # process score

            for i in range(len(enemy_pos_medium)):
                enemy_pos_medium[i][0] += enemy_speed_medium

            # Laser movement
            laser = pygame.image.load('laser.png')
            for i in range(len(laser_pos)):
                if laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    laser_pos[i][1] -= 7
                    screen.blit(laser, (laser_pos[i][0], laser_pos[i][1]))

                    # Laser collision with enemy
                    for j in range(len(enemy_pos_medium)):
                        if enemy_pos_medium[j][0] <= laser_pos[i][0] <= enemy_pos_medium[j][0] + 48:
                            if enemy_pos_medium[j][1] <= laser_pos[i][1] <= enemy_pos_medium[j][1] + 48:
                                enemy_del.append(j)
                                laser_del.append(i)
                                classic_medium_score += 100

            if laser_off_screen:
                laser_pos.pop(0)
                laser_off_screen = False

            if len(enemy_del) != 0:
                enemy_pos_medium.pop(enemy_del[0])
                enemy_del.clear()
            if len(laser_del) != 0:
                laser_pos.pop(laser_del[0])
                laser_del.clear()

            # If all enemies are dead
            if len(enemy_pos_medium) == 0:
                win()
                classic_medium = False
                classic_difficulty_selection = True
                start = False
                enemy_pos_medium = [[10, -86], [10, -38], [10, 10], [10, 58], [10, 106], [10, 154],
                                    [68, -86], [68, -38], [68, 10], [68, 58], [68, 106], [68, 154],
                                    [126, -86], [126, -38], [126, 10], [126, 58], [126, 106], [126, 154],
                                    [184, -86], [184, -38], [184, 10], [184, 58], [184, 106], [184, 154],
                                    [242, -86], [242, -38], [242, 10], [242, 58], [242, 106], [242, 154],
                                    [300, -86], [300, -38], [300, 10], [300, 58], [300, 106], [300, 154],
                                    [358, -86], [358, -38], [358, 10], [358, 58], [358, 106], [358, 154]
                                    ]
                ship_x = WIDTH / 2 - 32
                ship_y = 500
                laser_pos = []
                laser_off_screen = False

                if classic_medium_score > usernames[username]["classic"][1]:
                    usernames[username]["classic"][1] = classic_medium_score

                    with open('usernames.json', 'w') as f:
                        json.dump(usernames, f)

                classic_medium_score = 0

                screen.fill(BACKGROUND_COLOUR)

        # Draw enemies
        for pos in enemy_pos_medium:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw score
        font = pygame.font.SysFont('Monospace', 30)
        score_text = font.render(str(classic_medium_score), True, RED)
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(score_text, score_text_rect)

        pygame.display.update()

    # CLASSIC MODE HARD
    elif classic_hard is True:
        screen.fill(BACKGROUND_COLOUR)

        # Start
        if start is False:
            classic_hard_score = 0
            # Next step instructions (fade in and out)
            font = pygame.font.SysFont('Monospace', 20)
            instructions_text = font.render('Press any key to continue.', True, WHITE)
            instructions_text_rect = instructions_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(instructions_text, instructions_text_rect)

            if alpha >= 255 or alpha <= 0:
                change *= -1
            alpha += change
            fade.set_alpha(alpha)
            screen.blit(fade, ((WIDTH - FADE_WIDTH) / 2, (HEIGHT - FADE_HEIGHT) / 2))
        else:
            # Ship movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if ship_x >= 0:
                    ship_x -= 7
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if ship_x <= WIDTH - 64:
                    ship_x += 7

            # Enemy movement
            if enemy_pos_hard[-1][0] + 48 + enemy_speed_hard > WIDTH or enemy_pos_hard[0][0] + enemy_speed_hard < 0:
                enemy_speed_hard *= -1
                for i in range(len(enemy_pos_hard)):
                    enemy_pos_hard[i][1] += 48
                    # If enemies reach past your ship, you lose
                    if enemy_pos_hard[i][1] >= ship_y:
                        game_over()
                        classic_hard = False
                        classic_difficulty_selection = True
                        start = False
                        enemy_pos_hard = [[10, 10], [10, 58], [10, 106],
                                          [68, 10], [68, 58], [68, 106],
                                          [126, 10], [126, 58], [126, 106],
                                          [184, 10], [184, 58], [184, 106],
                                          [242, 10], [242, 58], [242, 106],
                                          [300, 10], [300, 58], [300, 106],
                                          [358, 10], [358, 58], [358, 106]
                                          ]
                        ship_x = WIDTH / 2 - 32
                        ship_y = 500
                        laser_pos = []
                        laser_off_screen = False

                        if classic_hard_score > usernames[username]["classic"][2]:
                            usernames[username]["classic"][2] = classic_hard_score

                            with open('usernames.json', 'w') as f:
                                json.dump(usernames, f)

                        classic_hard_score = 0

                        screen.fill(BACKGROUND_COLOUR)

            for i in range(len(enemy_pos_hard)):
                enemy_pos_hard[i][0] += enemy_speed_hard

            # Laser movement
            laser = pygame.image.load('laser.png')
            for i in range(len(laser_pos)):
                if laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    laser_pos[i][1] -= 7
                    screen.blit(laser, (laser_pos[i][0], laser_pos[i][1]))

                    # Laser collision with enemy
                    for j in range(len(enemy_pos_hard)):
                        if enemy_pos_hard[j][0] <= laser_pos[i][0] <= enemy_pos_hard[j][0] + 48:
                            if enemy_pos_hard[j][1] <= laser_pos[i][1] <= enemy_pos_hard[j][1] + 48:
                                enemy_del.append(j)
                                laser_del.append(i)
                                classic_hard_score += 100

            if laser_off_screen:
                laser_pos.pop(0)
                laser_off_screen = False

            if len(enemy_del) != 0:
                enemy_pos_hard.pop(enemy_del[0])
                enemy_del.clear()
            if len(laser_del) != 0:
                laser_pos.pop(laser_del[0])
                laser_del.clear()

            # If all enemies are dead
            if len(enemy_pos_hard) == 0:
                win()
                classic_hard = False
                classic_difficulty_selection = True
                start = False
                enemy_pos_hard = [[10, 10], [10, 58], [10, 106],
                                  [68, 10], [68, 58], [68, 106],
                                  [126, 10], [126, 58], [126, 106],
                                  [184, 10], [184, 58], [184, 106],
                                  [242, 10], [242, 58], [242, 106],
                                  [300, 10], [300, 58], [300, 106],
                                  [358, 10], [358, 58], [358, 106]
                                  ]
                ship_x = WIDTH / 2 - 32
                ship_y = 500
                laser_pos = []
                laser_off_screen = False

                if classic_hard_score > usernames[username]["classic"][2]:
                    usernames[username]["classic"][2] = classic_hard_score

                    with open('usernames.json', 'w') as f:
                        json.dump(usernames, f)

                classic_hard_score = 0

                screen.fill(BACKGROUND_COLOUR)

        # Draw enemies
        for pos in enemy_pos_hard:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw score
        font = pygame.font.SysFont('Monospace', 30)
        score_text = font.render(str(classic_hard_score), True, RED)
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(score_text, score_text_rect)

        pygame.display.update()

    # HEIST MODE DIFFICULTY SELECTION
    elif heist_difficulty_selection is True:
        difficulty_selection("heist")

    # HEIST MODE TUTORIAL
    elif heist_tutorial is True:
        pass

    # ESCORT MODE DIFFICULTY SELECTION
    elif escort_difficulty_selection is True:
        difficulty_selection("escort")

    # ESCORT MODE TUTORIAL
    elif escort_tutorial is True:
        pass

    clock.tick(30)
