import pygame
import random
import time

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra di gioco
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Creazione della finestra di gioco
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock per controllare la velocità del gioco
clock = pygame.time.Clock()

# Font per il testo
font = pygame.font.SysFont(None, 55)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

def game_over():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def main():
    snake = [[100, 50], [90, 50], [80, 50]]
    direction = [CELL_SIZE, 0]
    food = [random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != [0, CELL_SIZE]:
                    direction = [0, -CELL_SIZE]
                if event.key == pygame.K_DOWN and direction != [0, -CELL_SIZE]:
                    direction = [0, CELL_SIZE]
                if event.key == pygame.K_LEFT and direction != [CELL_SIZE, 0]:
                    direction = [-CELL_SIZE, 0]
                if event.key == pygame.K_RIGHT and direction != [-CELL_SIZE, 0]:
                    direction = [CELL_SIZE, 0]

        # Muovi il serpente
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        snake.insert(0, new_head)

        # Controlla se il serpente mangia il cibo
        if snake[0] == food:
            score += 1
            food = [random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]
        else:
            snake.pop()

        # Controlla le collisioni
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
            game_over()

        # Disegna tutto
        screen.fill(BLACK)
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        display_score(score)
        pygame.display.flip()

        # Controlla la velocità del gioco
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
