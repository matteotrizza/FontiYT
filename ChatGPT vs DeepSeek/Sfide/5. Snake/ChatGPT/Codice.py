import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Arcade")

# Clock
clock = pygame.time.Clock()

# Snake and Food initialization
def initialize_game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    food = spawn_food(snake)
    return snake, direction, food, 0

def spawn_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y

# Draw the game objects
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Main game loop
def main():
    snake, direction, food, score = initialize_game()

    while True:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Control snake direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

        # Move snake
        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= CELL_SIZE
        if direction == "DOWN":
            head_y += CELL_SIZE
        if direction == "LEFT":
            head_x -= CELL_SIZE
        if direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Check for collisions
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake
        ):
            break

        # Check if food is eaten
        if new_head == food:
            score += 1
            food = spawn_food(snake)
        else:
            snake.pop()

        snake.insert(0, new_head)

        # Draw everything
        draw_snake(snake)
        draw_food(food)
        draw_score(score)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
