import pygame
import sys

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 10

ROWS = WIDTH // CELL_SIZE
COLUMNS = HEIGHT // CELL_SIZE

ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

FPS = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid = [[DEAD for _ in range(COLUMNS)] for _ in range(ROWS)]


def draw_grid():
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def count_neighbours(x, y):
    neighbourCount = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (0 <= i < COLUMNS and 0 <= j < ROWS):
                if not (i == x and j == y):
                    neighbourState = grid[j][i]

                    if neighbourState == ALIVE:
                        neighbourCount += 1


    return neighbourCount

paused = True
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = (x // CELL_SIZE)
            y = (y // CELL_SIZE)

            grid[y][x] = DEAD if grid[y][x] == ALIVE else ALIVE


    if not paused:
        new_grid = [[DEAD for _ in range(COLUMNS)] for _ in range(ROWS)]
        
        
        for x in range(COLUMNS):
            for y in range(ROWS):
                state = grid[y][x]

                # Get neighbour count - we do this regardless of state as there are both rules for 'Alive' and 'Dead' cells
                neighbourCount = count_neighbours(x, y)

                if state == ALIVE:

                    # Rule 1 - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                    if neighbourCount < 2:
                        new_grid[y][x] = DEAD

                    # Rule 3 - Any live cell with more than three live neighbours dies, as if by overpopulation.
                    elif neighbourCount > 3:
                        new_grid[y][x] = DEAD

                    # Rule 2 - Any live cell with two or three live neighbours lives on to the next generation.
                    else:
                        new_grid[y][x] = ALIVE

                if state == DEAD and neighbourCount == 3:

                    new_grid[y][x] = ALIVE

        grid = new_grid
    
    draw_grid()
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()