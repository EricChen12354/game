import pygame
import json
import sys
import random

pygame.init()


# ---------- FUNCTIONS ----------------
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


def win(score):
    # Win text
    font = pygame.font.SysFont('Monospace', 30)
    win_text = font.render('YOU WIN!', True, WHITE)
    win_text_rect = win_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(win_text, win_text_rect)

    # Score text
    score_text = font.render(f'Score: {score}', True, WHITE)
    score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(score_text, score_text_rect)

    pygame.display.update()

    pygame.time.delay(3000)

    fade_out()

    pygame.display.update()


def lose(score):
    # Lose text
    font = pygame.font.SysFont('Monospace', 30)
    loss_text = font.render('YOU LOSE', True, WHITE)
    loss_text_rect = loss_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(loss_text, loss_text_rect)

    # Score text
    score_text = font.render(f'Score: {score}', True, WHITE)
    score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(score_text, score_text_rect)

    pygame.display.update()

    pygame.time.delay(3000)

    fade_out()

    pygame.display.update()


# ---------- SCREEN VARIABLES ---------
WIDTH = 500
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# ---------- COLOURS ------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_PURPLE = (15, 0, 15)
BACKGROUND_COLOUR = DARK_PURPLE

# ---------- DISPLAY ------------------
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Space Fighters')
FONT_SIZE = 40
font = pygame.font.SysFont('Monospace', FONT_SIZE)

# ---------- GAME STATE ---------------
finished = False
loading_screen = True
log_in = False
profile_screen = False
main_menu = False

difficulty_selection = False
tutorial = False
easy = False
medium = False
hard = False
start = False

# ---------- BACKGROUND ASTEROIDS -----
asteroids_size = 30
menu_asteroids = [[-5, 0], [-18, 150], [200, -5], [-19, 400]]
menu_asteroids_original = [[-5, 0], [-18, 150], [200, -5], [-5, 400]]

# ---------- FADING MAIN MENU TEXT ----
FADE_WIDTH = 310
FADE_HEIGHT = 20
FADE_SIZE = (FADE_WIDTH, FADE_HEIGHT)
fade = pygame.Surface(FADE_SIZE)
fade.fill(BACKGROUND_COLOUR)
alpha = 1
change = 5

# ---------- USER LOG IN --------------
username = ''
BOX_WIDTH = 400
BOX_HEIGHT = 100
CLEAR_WIDTH = 175
CLEAR_HEIGHT = 50

# ---------- PROFILE PAGE -------------
with open('usernames.json', 'r') as f:
    usernames = json.load(f)

message = ''

# ---------- TUTORIAL -----------------
description = ['This is your space ship,',
               'use "A" and "D" to strafe',
               'left and right. Press',
               '"SPACE" to fire a laser.',
               '',
               'This is an enemy. They',
               'spawn and shoot randomly.',
               'They take one shot to kill.',
               'They protect the safe from',
               'your lasers.',
               '',
               'To win, you must destroy',
               'the safe at the top of the',
               'screen. If you run out of ',
               'lives, you lose!']

# ---------- GAME VARIABLES -----------
ship_x = WIDTH / 2 - 32
ship_y = 500
enemy_pos = []
enemy_speed = []
easy_speed = 2
ship_laser_pos = []
enemy_laser_pos = []
easy_lives = 3
easy_safe_health = 10000
laser_off_screen = False
easy_score = 0
ship_laser_del = []
enemy_ship_del = []
enemy_laser_off_screen = []
medium_speed = 3
medium_score = 0
medium_safe_health = 10000
medium_lives = 2
hard_score = 0
hard_safe_health = 15000
hard_lives = 1

# ---------- MAIN GAME LOOP -----------
while not finished:

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if loading_screen is True:
                loading_screen = False
                log_in = True
                fade_out()

            elif tutorial is True:
                fade_out()
                tutorial = False
                main_menu = True

            elif difficulty_selection is True:
                if 50 <= mouse_x <= 400:
                    if 100 <= mouse_y <= 200:
                        fade_out()
                        difficulty_selection = False
                        easy = True
                    elif 250 <= mouse_y <= 350:
                        fade_out()
                        difficulty_selection = False
                        medium = True
                    elif 400 <= mouse_y <= 500:
                        fade_out()
                        difficulty_selection = False
                        hard = True
                    elif 525 <= mouse_y <= 575:
                        fade_out()
                        difficulty_selection = False
                        main_menu = True

            elif main_menu is True:
                # Play button
                if 50 <= mouse_x <= 450 and 150 <= mouse_y <= 350:
                    fade_out()
                    main_menu = False
                    difficulty_selection = True

                # Profile button
                elif 50 <= mouse_x <= 225 and 400 <= mouse_y <= 500:
                    fade_out()
                    profile_screen = True
                    main_menu = False

                # Tutorial button
                elif 275 <= mouse_x <= 450 and 400 <= mouse_y <= 500:
                    fade_out()
                    tutorial = True
                    main_menu = False

            elif easy is True or medium is True or hard is True:
                if start is False:
                    start = True

            elif profile_screen is True:
                fade_out()
                profile_screen = False
                main_menu = True

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
                        usernames[username] = {"easy": 0, "medium": 0, "hard": 0}

                        with open('usernames.json', 'w') as f:
                            json.dump(usernames, f, indent=4)

        elif event.type == pygame.KEYDOWN:
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
                        usernames[username] = {"easy": 0, "medium": 0, "hard": 0}

                        with open('usernames.json', 'w') as f:
                            json.dump(usernames, f, indent=4)

            elif easy is True or medium is True or hard is True:
                if start is False:
                    start = True
                else:
                    if event.key == pygame.K_SPACE:
                        if len(ship_laser_pos) != 0 and ship_laser_pos[-1][1] >= ship_y - 40:
                            pass
                        else:
                            ship_laser_pos.append([ship_x + 27, ship_y])

            elif tutorial is True:
                fade_out()
                tutorial = False
                main_menu = True

            elif profile_screen is True:
                fade_out()
                profile_screen = False
                main_menu = True

            elif loading_screen is True:
                loading_screen = False
                log_in = True
                fade_out()

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

        # Draw rectangles
        pygame.draw.rect(screen, GREEN, [50, 100, 400, 100], 3)
        pygame.draw.rect(screen, YELLOW, [50, 250, 400, 100], 3)
        pygame.draw.rect(screen, RED, [50, 400, 400, 100], 3)

        # Display easy score
        easy_score = usernames[username]["easy"]
        easy_text = font.render(f'Easy: {easy_score}', True, GREEN)
        easy_text_rect = easy_text.get_rect(center=(WIDTH / 2, 150))
        screen.blit(easy_text, easy_text_rect)

        # Display medium score
        medium_score = usernames[username]["medium"]
        medium_text = font.render(f'Medium: {medium_score}', True, YELLOW)
        medium_text_rect = medium_text.get_rect(center=(WIDTH / 2, 300))
        screen.blit(medium_text, medium_text_rect)

        # Display hard score
        hard_score = usernames[username]["hard"]
        hard_text = font.render(f'Hard: {hard_score}', True, RED)
        hard_text_rect = hard_text.get_rect(center=(WIDTH / 2, 450))
        screen.blit(hard_text, hard_text_rect)

        # Next step instructions (fade in and out)
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

    # MAIN MENU
    elif main_menu is True:

        # Game title
        font = pygame.font.SysFont('Monospace', 55)
        title_text = font.render('SPACE FIGHTERS', True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, 100))
        screen.blit(title_text, title_text_rect)

        # Draw rectangles
        pygame.draw.rect(screen, WHITE, [50, 150, 400, 200], 3)
        pygame.draw.rect(screen, WHITE, [50, 400, 175, 100], 3)
        pygame.draw.rect(screen, WHITE, [WIDTH / 2 + 25, 400, 175, 100], 3)

        # Play text
        play_text = font.render('PLAY', True, WHITE)
        play_text_rect = play_text.get_rect(center=(WIDTH / 2, 250))
        screen.blit(play_text, play_text_rect)

        # Profile text
        font = pygame.font.SysFont('Monospace', 30)
        profile_text = font.render('Profile', True, WHITE)
        profile_text_rect = profile_text.get_rect(center=(135, 450))
        screen.blit(profile_text, profile_text_rect)

        # Tutorial text
        tutorial_text = font.render('Tutorial', True, WHITE)
        tutorial_text_rect = tutorial_text.get_rect(center=(365, 450))
        screen.blit(tutorial_text, tutorial_text_rect)

        pygame.display.update()

    # TUTORIAL
    elif tutorial is True:
        # Title
        font = pygame.font.SysFont('Monospace', 30)
        tutorial_text = font.render('Tutorial', True, WHITE)
        tutorial_text_rect = tutorial_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(tutorial_text, tutorial_text_rect)

        # Display description
        for i in range(len(description)):
            font = pygame.font.SysFont('Monospace', 17)
            description_text = font.render(description[i], True, WHITE)
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

    # DIFFICULTY SELECTION
    elif difficulty_selection is True:
        screen.fill(BACKGROUND_COLOUR)

        # Title
        font = pygame.font.SysFont('Monospace', 40)
        title_text = font.render('Select Difficulty', True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(title_text, title_text_rect)

        # Easy
        pygame.draw.rect(screen, GREEN, [50, 100, 400, 100], 3)

        font = pygame.font.SysFont('Monospace', 30)
        easy_text = font.render('EASY', True, GREEN)
        easy_text_rect = easy_text.get_rect(center=(WIDTH / 2, 130))
        screen.blit(easy_text, easy_text_rect)

        font = pygame.font.SysFont('Monospace', 20)
        easy_high_score = usernames[username]["easy"]
        easy_high_score_text = font.render(f'High score: {easy_high_score}', True, GREEN)
        easy_high_score_text_rect = easy_high_score_text.get_rect(center=(WIDTH / 2, 165))
        screen.blit(easy_high_score_text, easy_high_score_text_rect)

        # Medium
        pygame.draw.rect(screen, YELLOW, [50, 250, 400, 100], 3)

        font = pygame.font.SysFont('Monospace', 30)
        medium_text = font.render('MEDIUM', True, YELLOW)
        medium_text_rect = medium_text.get_rect(center=(WIDTH / 2, 280))
        screen.blit(medium_text, medium_text_rect)

        font = pygame.font.SysFont('Monospace', 20)
        medium_high_score = usernames[username]["medium"]
        medium_high_score_text = font.render(f'High Score: {medium_high_score}', True, YELLOW)
        medium_high_score_text_rect = medium_high_score_text.get_rect(center=(WIDTH / 2, 315))
        screen.blit(medium_high_score_text, medium_high_score_text_rect)

        # Hard
        pygame.draw.rect(screen, RED, [50, 400, 400, 100], 3)

        font = pygame.font.SysFont('Monospace', 30)
        hard_text = font.render('HARD', True, RED)
        hard_text_rect = hard_text.get_rect(center=(WIDTH / 2, 430))
        screen.blit(hard_text, hard_text_rect)

        font = pygame.font.SysFont('Monospace', 20)
        hard_high_score = usernames[username]["hard"]
        hard_high_score_text = font.render(f'High Score: {hard_high_score}', True, RED)
        hard_high_score_text_rect = hard_high_score_text.get_rect(center=(WIDTH / 2, 465))
        screen.blit(hard_high_score_text, hard_high_score_text_rect)

        # Back
        pygame.draw.rect(screen, WHITE, [50, 525, 400, 50], 3)

        font = pygame.font.SysFont('Monospace', 30)
        back_text = font.render('BACK', True, WHITE)
        back_text_rect = back_text.get_rect(center=(WIDTH / 2, 550))
        screen.blit(back_text, back_text_rect)

        pygame.display.update()

    # EASY MODE
    elif easy is True:

        screen.fill(BACKGROUND_COLOUR)

        if start is False:
            # ---------- GAME VARIABLES -----------
            ship_x = WIDTH / 2 - 32
            ship_y = 500
            enemy_pos = []
            enemy_speed = []
            easy_speed = 2
            ship_laser_pos = []
            enemy_laser_pos = []
            easy_lives = 3
            easy_safe_health = 5000
            laser_off_screen = False
            easy_score = 0
            ship_laser_del = []
            enemy_ship_del = []
            enemy_laser_off_screen = []

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

            # Enemy spawns
            num = random.randint(0, 50)
            if num == 0:
                enemy_pos.append([random.randint(0, WIDTH - 49), random.randint(120, 200)])
                enemy_speed.append(easy_speed)

            # Enemy movement
            for i in range(len(enemy_pos)):
                if enemy_pos[i][0] - easy_speed < 0 or enemy_pos[i][0] + 48 + easy_speed > WIDTH:
                    enemy_speed[i] *= -1
                enemy_pos[i][0] += enemy_speed[i]

            # Ship lasers
            ship_laser = pygame.image.load('laser.png')
            for i in range(len(ship_laser_pos)):
                if ship_laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    ship_laser_pos[i][1] -= 7
                    screen.blit(ship_laser, (ship_laser_pos[i][0], ship_laser_pos[i][1]))

                    # Collision with enemy
                    for j in range(len(enemy_pos)):
                        if enemy_pos[j][0] <= ship_laser_pos[i][0] <= enemy_pos[j][0] + 48:
                            if enemy_pos[j][1] <= ship_laser_pos[i][1] <= enemy_pos[j][1] + 48:
                                enemy_ship_del.append(j)
                                ship_laser_del.append(i)
                                easy_score += 100

                    # Collision with safe
                    if 218 <= ship_laser_pos[i][0] <= 282:
                        if 10 <= ship_laser_pos[i][1] <= 74:
                            easy_safe_health -= 100
                            easy_score += 100
                            ship_laser_del.append(i)

                            # If safe is down to 0 health
                            if easy_safe_health <= 0:
                                win(easy_score)
                                easy = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["easy"] < easy_score:
                                    usernames[username]["easy"] = easy_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if laser_off_screen is True:
                ship_laser_pos.pop(0)
                laser_off_screen = False
            if len(enemy_ship_del) != 0:
                for i in range(len(enemy_ship_del)):
                    enemy_pos.pop(enemy_ship_del[i - i])
                enemy_ship_del.clear()
            if len(ship_laser_del) != 0:
                for i in range(len(ship_laser_del)):
                    ship_laser_pos.pop(ship_laser_del[i - i])
                ship_laser_del.clear()

            # Enemy lasers
            for ship in enemy_pos:
                num = random.randint(0, 100)
                # Enemy shoots laser
                if num == 0:
                    enemy_laser_pos.append([ship[0], ship[1] + 40])

            # Enemy lasers
            enemy_laser = pygame.image.load('enemy laser.png')
            for i in range(len(enemy_laser_pos)):
                if enemy_laser_pos[i][1] > HEIGHT - 40:
                    enemy_laser_off_screen.append(i)
                else:
                    enemy_laser_pos[i][1] += 7
                    screen.blit(enemy_laser, (enemy_laser_pos[i][0], enemy_laser_pos[i][1]))

                    # Collision with player
                    if ship_x <= enemy_laser_pos[i][0] <= ship_x + 64:
                        if ship_y <= enemy_laser_pos[i][1] <= ship_y + 64:
                            easy_lives -= 1
                            easy_score -= 100
                            enemy_laser_off_screen.append(i)

                            if easy_lives <= 0:
                                lose(easy_score)
                                easy = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["easy"] < easy_score:
                                    usernames[username]["easy"] = easy_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if len(enemy_laser_off_screen) != 0:
                for i in range(len(enemy_laser_off_screen)):
                    enemy_laser_pos.pop(enemy_laser_off_screen[i])
                enemy_laser_off_screen.clear()

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw enemies
        for pos in enemy_pos:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw safe
        safe = pygame.image.load('safe.png')
        screen.blit(safe, (WIDTH / 2 - 32, 10))

        # Draw score
        font = pygame.font.SysFont('Monospace', 20)
        score_text = font.render(f'Score: {easy_score}', True, RED)
        screen.blit(score_text, (10, 10))

        # Draw safe health
        health_text = font.render(f'Safe: {easy_safe_health}', True, RED)
        screen.blit(health_text, (10, 40))

        # Draw player health
        player_text = font.render(f'Health: {easy_lives}', True, RED)
        screen.blit(player_text, (10, 70))

        pygame.display.update()

    # MEDIUM MODE
    elif medium is True:
        screen.fill(BACKGROUND_COLOUR)

        if start is False:
            # ---------- GAME VARIABLES -----------
            ship_x = WIDTH / 2 - 32
            ship_y = 500
            enemy_pos = []
            enemy_speed = []
            medium_speed = 3
            ship_laser_pos = []
            enemy_laser_pos = []
            medium_lives = 2
            medium_safe_health = 10000
            laser_off_screen = False
            medium_score = 0
            ship_laser_del = []
            enemy_ship_del = []
            enemy_laser_off_screen = []

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

            # Enemy spawns
            num = random.randint(0, 40)
            if num == 0:
                enemy_pos.append([random.randint(0, WIDTH - 49), random.randint(120, 300)])
                enemy_speed.append(medium_speed)

            # Enemy movement
            for i in range(len(enemy_pos)):
                if enemy_pos[i][0] - medium_speed < 0 or enemy_pos[i][0] + 48 + medium_speed > WIDTH:
                    enemy_speed[i] *= -1
                enemy_pos[i][0] += enemy_speed[i]

            # Ship lasers
            ship_laser = pygame.image.load('laser.png')
            for i in range(len(ship_laser_pos)):
                if ship_laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    ship_laser_pos[i][1] -= 7
                    screen.blit(ship_laser, (ship_laser_pos[i][0], ship_laser_pos[i][1]))

                    # Collision with enemy
                    for j in range(len(enemy_pos)):
                        if enemy_pos[j][0] <= ship_laser_pos[i][0] <= enemy_pos[j][0] + 48:
                            if enemy_pos[j][1] <= ship_laser_pos[i][1] <= enemy_pos[j][1] + 48:
                                enemy_ship_del.append(j)
                                ship_laser_del.append(i)
                                medium_score += 100

                    # Collision with safe
                    if 218 <= ship_laser_pos[i][0] <= 282:
                        if 10 <= ship_laser_pos[i][1] <= 74:
                            medium_safe_health -= 100
                            medium_score += 100
                            ship_laser_del.append(i)

                            # If safe is down to 0 health
                            if medium_safe_health <= 0:
                                win(medium_score)
                                medium = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["medium"] < medium_score:
                                    usernames[username]["medium"] = medium_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if laser_off_screen is True:
                ship_laser_pos.pop(0)
                laser_off_screen = False
            if len(enemy_ship_del) != 0:
                for i in range(len(enemy_ship_del)):
                    enemy_pos.pop(enemy_ship_del[i - i])
                enemy_ship_del.clear()
            if len(ship_laser_del) != 0:
                for i in range(len(ship_laser_del)):
                    ship_laser_pos.pop(ship_laser_del[i - i])
                ship_laser_del.clear()

            # Enemy lasers
            for ship in enemy_pos:
                num = random.randint(0, 50)
                # Enemy shoots laser
                if num == 0:
                    enemy_laser_pos.append([ship[0], ship[1] + 40])

            # Enemy lasers
            enemy_laser = pygame.image.load('enemy laser.png')
            for i in range(len(enemy_laser_pos)):
                if enemy_laser_pos[i][1] > HEIGHT - 40:
                    enemy_laser_off_screen.append(i)
                else:
                    enemy_laser_pos[i][1] += 7
                    screen.blit(enemy_laser, (enemy_laser_pos[i][0], enemy_laser_pos[i][1]))

                    # Collision with player
                    if ship_x <= enemy_laser_pos[i][0] <= ship_x + 64:
                        if ship_y <= enemy_laser_pos[i][1] <= ship_y + 64:
                            medium_lives -= 1
                            medium_score -= 100
                            enemy_laser_off_screen.append(i)

                            if medium_lives <= 0:
                                lose(medium_score)
                                medium = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["medium"] < medium_score:
                                    usernames[username]["medium"] = medium_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if len(enemy_laser_off_screen) != 0:
                for i in range(len(enemy_laser_off_screen)):
                    enemy_laser_pos.pop(enemy_laser_off_screen[i])
                enemy_laser_off_screen.clear()

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw enemies
        for pos in enemy_pos:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw safe
        safe = pygame.image.load('safe.png')
        screen.blit(safe, (WIDTH / 2 - 32, 10))

        # Draw score
        font = pygame.font.SysFont('Monospace', 20)
        score_text = font.render(f'Score: {medium_score}', True, RED)
        screen.blit(score_text, (10, 10))

        # Draw safe health
        health_text = font.render(f'Safe: {medium_safe_health}', True, RED)
        screen.blit(health_text, (10, 40))

        # Draw player health
        player_text = font.render(f'Health: {medium_lives}', True, RED)
        screen.blit(player_text, (10, 70))

        pygame.display.update()

    # HARD MODE
    elif hard is True:
        screen.fill(BACKGROUND_COLOUR)

        if start is False:
            # ---------- GAME VARIABLES -----------
            ship_x = WIDTH / 2 - 32
            ship_y = 500
            enemy_pos = []
            enemy_speed = []
            hard_speed = 4
            ship_laser_pos = []
            enemy_laser_pos = []
            hard_lives = 1
            hard_safe_health = 15000
            laser_off_screen = False
            hard_score = 0
            ship_laser_del = []
            enemy_ship_del = []
            enemy_laser_off_screen = []

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

            # Enemy spawns
            num = random.randint(0, 25)
            if num == 0:
                enemy_pos.append([random.randint(0, WIDTH - 49), random.randint(120, 300)])
                enemy_speed.append(medium_speed)

            # Enemy movement
            for i in range(len(enemy_pos)):
                if enemy_pos[i][0] - medium_speed < 0 or enemy_pos[i][0] + 48 + medium_speed > WIDTH:
                    enemy_speed[i] *= -1
                enemy_pos[i][0] += enemy_speed[i]

            # Ship lasers
            ship_laser = pygame.image.load('laser.png')
            for i in range(len(ship_laser_pos)):
                if ship_laser_pos[i][1] <= -20:
                    laser_off_screen = True
                else:
                    ship_laser_pos[i][1] -= 7
                    screen.blit(ship_laser, (ship_laser_pos[i][0], ship_laser_pos[i][1]))

                    # Collision with enemy
                    for j in range(len(enemy_pos)):
                        if enemy_pos[j][0] <= ship_laser_pos[i][0] <= enemy_pos[j][0] + 48:
                            if enemy_pos[j][1] <= ship_laser_pos[i][1] <= enemy_pos[j][1] + 48:
                                enemy_ship_del.append(j)
                                ship_laser_del.append(i)
                                hard_score += 100

                    # Collision with safe
                    if 218 <= ship_laser_pos[i][0] <= 282:
                        if 10 <= ship_laser_pos[i][1] <= 74:
                            hard_safe_health -= 100
                            hard_score += 100
                            ship_laser_del.append(i)

                            # If safe is down to 0 health
                            if hard_safe_health <= 0:
                                win(hard_score)
                                hard = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["hard"] < hard_score:
                                    usernames[username]["hard"] = hard_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if laser_off_screen is True:
                ship_laser_pos.pop(0)
                laser_off_screen = False
            if len(enemy_ship_del) != 0:
                for i in range(len(enemy_ship_del)):
                    enemy_pos.pop(enemy_ship_del[i - i])
                enemy_ship_del.clear()
            if len(ship_laser_del) != 0:
                for i in range(len(ship_laser_del)):
                    ship_laser_pos.pop(ship_laser_del[i - i])
                ship_laser_del.clear()

            # Enemy lasers
            for ship in enemy_pos:
                num = random.randint(0, 50)
                # Enemy shoots laser
                if num == 0:
                    enemy_laser_pos.append([ship[0], ship[1] + 40])

            # Enemy lasers
            enemy_laser = pygame.image.load('enemy laser.png')
            for i in range(len(enemy_laser_pos)):
                if enemy_laser_pos[i][1] > HEIGHT - 40:
                    enemy_laser_off_screen.append(i)
                else:
                    enemy_laser_pos[i][1] += 7
                    screen.blit(enemy_laser, (enemy_laser_pos[i][0], enemy_laser_pos[i][1]))

                    # Collision with player
                    if ship_x <= enemy_laser_pos[i][0] <= ship_x + 64:
                        if ship_y <= enemy_laser_pos[i][1] <= ship_y + 64:
                            hard_lives -= 1
                            hard_score -= 100
                            enemy_laser_off_screen.append(i)

                            if hard_lives <= 0:
                                lose(hard_score)
                                hard = False
                                difficulty_selection = True
                                start = False

                                # Save score
                                if usernames[username]["hard"] < hard_score:
                                    usernames[username]["hard"] = hard_score

                                    with open('usernames.json', 'w') as f:
                                        json.dump(usernames, f)

            if len(enemy_laser_off_screen) != 0:
                for i in range(len(enemy_laser_off_screen)):
                    enemy_laser_pos.pop(enemy_laser_off_screen[i])
                enemy_laser_off_screen.clear()

        # Draw space ship icon
        ship = pygame.image.load('ship.png')
        ship = pygame.transform.rotate(ship, 180)
        screen.blit(ship, (ship_x, ship_y))

        # Draw enemies
        for pos in enemy_pos:
            enemy = pygame.image.load('enemy.png')
            screen.blit(enemy, (pos[0], pos[1]))

        # Draw safe
        safe = pygame.image.load('safe.png')
        screen.blit(safe, (WIDTH / 2 - 32, 10))

        # Draw score
        font = pygame.font.SysFont('Monospace', 20)
        score_text = font.render(f'Score: {hard_score}', True, RED)
        screen.blit(score_text, (10, 10))

        # Draw safe health
        health_text = font.render(f'Safe: {hard_safe_health}', True, RED)
        screen.blit(health_text, (10, 40))

        # Draw player health
        player_text = font.render(f'Health: {hard_lives}', True, RED)
        screen.blit(player_text, (10, 70))

        pygame.display.update()

    clock.tick(30)
