import pygame
import time
import random

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 255, 0)
yellow = (255, 255, 102)
black = (0, 0, 0)
white = (255, 255, 255)

size_of_snake_block = 10

clock = pygame.time.Clock()

font1 = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 30)

def print_level(level):
    text = font2.render("Your Level: " + str(level), True, yellow)
    screen.blit(text, (200, 0))

def print_score(score):
    text = font2.render("Your Score: " + str(score), True, yellow)
    screen.blit(text, (0, 0))

def print_message(message, color):
    text = font1.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, text_rect)

def give_random_color(list_of_colors):
    random_color = random.choice(list_of_colors)
    return random_color

def timer(start_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 5:
        return True
    else:
        return False

def snake(size_of_snake_block, snake_list):
    for i in snake_list:
        x = i[0]
        y = i[1]
        pygame.draw.rect(screen, green, (x, y, size_of_snake_block, size_of_snake_block))

def game_loop():
    game_paused = False
    game_over = False

    color_is_given = False

    timer_is_started = False

    x = screen_width // 2
    y = screen_height // 2

    x_change = 0
    y_change = 0

    score = 0
    level = 1
    snake_speed = 10

    colors = [red, white]

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(size_of_snake_block, screen_width - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(40, screen_height - size_of_snake_block - size_of_snake_block) / 10.0) * 10.0

    inc_speed = pygame.USEREVENT + 1
    pygame.time.set_timer(inc_speed, 5000)

    while not game_over:
        while game_paused == True:
            screen.fill(black)
            print_message("You Lost! Press Q-Quit or P-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_paused = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_LEFT:
                    x_change = -size_of_snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = size_of_snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -size_of_snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = size_of_snake_block
            if event.type == inc_speed and level == 10:
                    snake_speed += 2

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_paused = True

        x += x_change
        y += y_change

        screen.fill(black)

        if color_is_given == False:
            random_color = give_random_color(colors)
            color_is_given = True
            if random_color == red:
                start_time = time.time()
                timer_is_started = True

        pygame.draw.rect(screen, random_color, (food_x, food_y, size_of_snake_block, size_of_snake_block))

        snake_list.append((x, y))

        if len(snake_list) > length_of_snake:
            del snake_list[0]