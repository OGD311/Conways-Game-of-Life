import pygame
import sys

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 10

ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

FPS = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = (x // CELL_SIZE) * CELL_SIZE
            y = (y // CELL_SIZE) * CELL_SIZE

            state = screen.get_at((x, y))

            if state == ALIVE:
                pygame.draw.rect(screen, DEAD, (x, y, CELL_SIZE, CELL_SIZE), 0)
            else:
                pygame.draw.rect(screen, ALIVE, (x, y, CELL_SIZE, CELL_SIZE), 0)



    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):

            state = screen.get_at((x, y))

            # Get neighbour count - we do this regardless of state as there are both rules for 'Alive' and 'Dead' cells
            neighbourCount = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i >= 0 and j >= 0) and (i < WIDTH and j < HEIGHT) and (i != x and j != y):
                        neighbourState = screen.get_at((i, j))

                        if neighbourState == ALIVE:
                            neighbourCount += 1


            if state == ALIVE:

                # Rule 1 - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if neighbourCount < 2:
                    pygame.draw.rect(screen, DEAD, (x, y, CELL_SIZE, CELL_SIZE), 0)

                # Rule 2 - Any live cell with two or three live neighbours lives on to the next generation.
                # -- No need to do anything for this - the cell stays 'Alive' if we do not edit it

                # Rule 3 - Any live cell with more than three live neighbours dies, as if by overpopulation.
                if neighbourCount > 3:
                    pygame.draw.rect(screen, DEAD, (x, y, CELL_SIZE, CELL_SIZE), 0)
            

            if state == DEAD and neighbourCount == 3:

                pygame.draw.rect(screen, ALIVE, (x, y, CELL_SIZE, CELL_SIZE), 0)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()