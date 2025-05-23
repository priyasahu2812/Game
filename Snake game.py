import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game by Priya")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

# Score function
def your_score(score):
    value = font.render(f"Your Score: {score}", True, green)
    screen.blit(value, [0, 0])

# Draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(message, [width / 6, height / 3])
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = [x, y]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
