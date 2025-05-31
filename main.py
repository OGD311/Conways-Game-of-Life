import pygame
import sys

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 10

ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

FPS = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.rect(screen, (255, 255, 255), (x, y, CELL_SIZE, CELL_SIZE), 0)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()