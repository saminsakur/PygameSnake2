import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange= (255, 165, 0)

WIDTH, HEIGHT = 600, 400

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('Ubuntu', 25)

def draw_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    window.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, white, int(pixel[0]), int(pixel[1]), snake_size, snake_size)

def run_game():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(black)
            GameOverMessage = message_font.render("Game Over!", True, red)
            window.blit(GameOverMessage, [WIDTH / 3, HEIGHT / 3])
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.envent.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        window.fill(black)
        pygame.draw.rect(window, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        draw_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round (random.randrange (0, WIDTH - snake_size) / 10.0) * 10.0
            target_y = round (random.randrange (0, HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()
