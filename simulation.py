import pygame
import sys

pygame.init()

# Display Setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cargo Ship Port Simulation")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (100, 250, 600, 100))

    pygame.display.flip()

pygame.quit()
sys.exit()
