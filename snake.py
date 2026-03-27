import pygame as pg
import random as rd
import sys

pg.init()
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10  # Controlling game speed
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()
font = pg.font.Font(None, 36)


def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food = (rd.randrange(0, WIDTH, GRID_SIZE), rd.randrange(0, HEIGHT, GRID_SIZE))
    # ensure food does not spawn on the snake
    while food in snake:
        food = (rd.randrange(0, WIDTH, GRID_SIZE), rd.randrange(0, HEIGHT, GRID_SIZE))
    score = 0

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pg.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pg.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pg.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        # move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        # collision with walls or self
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
            or new_head in snake
        ):
            running = False
            continue

        snake.insert(0, new_head)

        # eating food logic
        if new_head == food:
            score += 1
            food = (rd.randrange(0, WIDTH, GRID_SIZE), rd.randrange(0, HEIGHT, GRID_SIZE))
            while food in snake:
                food = (rd.randrange(0, WIDTH, GRID_SIZE), rd.randrange(0, HEIGHT, GRID_SIZE))
        else:
            snake.pop()

        # draw
        screen.fill(BLACK)
        for segment in snake:
            pg.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE - 1, GRID_SIZE - 1))
        pg.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE - 1, GRID_SIZE - 1))

        # score
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (5, 5))

        pg.display.flip()
        clock.tick(FPS)

    # game over
    print(f"Game over! Final score: {score}")
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
