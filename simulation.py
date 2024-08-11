import pygame
import sys

pygame.init()

# Display Setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cargo Ship Port Simulation")


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# Vehical properties
vehicale_x = 100
vehicale_y = 270
vehicale_width = 50
vehicale_height = 30
vehicale_speed = 1




# main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if vehicale_x > screen_width:
        vehicale_x = 0

    vehicale_x += vehicale_speed

    screen.fill(white)

    pygame.draw.rect(screen, black, (100, 250, 600, 100))

    pygame.draw.rect(screen, red, (vehicale_x, vehicale_y, vehicale_width, vehicale_height))





    pygame.display.flip()

pygame.quit()
sys.exit()
