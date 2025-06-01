import pygame
import sys

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 10

ROWS = WIDTH // CELL_SIZE
COLUMNS = HEIGHT // CELL_SIZE

ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Conways GoL')
font = pygame.font.SysFont('Arial', 24)

grid = [[DEAD for _ in range(COLUMNS)] for _ in range(ROWS)]


def draw_grid():
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)


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

def get_pop():
    populationCount = 0

    for y in range(ROWS):
        for x in range(COLUMNS):
            if grid[y][x] == ALIVE:
                populationCount += 1


    return populationCount

paused = True
drag = False
running = True
generationCount = 0
while running:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_c:
                screen.fill(DEAD)
                grid = [[DEAD for _ in range(COLUMNS)] for _ in range(ROWS)]
                paused = True
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            drag = False

        

    if drag:
        FPS = 1000
        x, y = pygame.mouse.get_pos()
        x //= CELL_SIZE
        y //= CELL_SIZE

        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            grid[y][x] = DEAD if grid[y][x] == ALIVE else ALIVE
        
    else:
        FPS = 60


    if not paused:
        pygame.display.set_caption('Conways GoL')
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
    
    else:
        pygame.display.set_caption('Conways GoL - Paused')




    draw_grid()

    if paused:
        pauseText = font.render("Paused", True, (200, 0, 0))
        screen.blit(pauseText, (WIDTH - pauseText.get_width() - 10, HEIGHT - pauseText.get_height() - 10))
    
    else:
        generationCount += 1


    popText = font.render(f"Pop: {get_pop()}", True, (200, 0, 0))
    screen.blit(popText, (10, HEIGHT - popText.get_height() - 10))

    popText = font.render(f"Gen: {generationCount}", True, (200, 0, 0))
    screen.blit(popText, (10, HEIGHT - popText.get_height() - 40))
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()