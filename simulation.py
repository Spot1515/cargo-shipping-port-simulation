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

# 2 lane road properties
road_x = 100
road_y = 100
road_width = 500
road_hight = 17



# Vehical properties
vehicale_x = road_x
vehicale_y = road_y + (road_hight //2) - 6
vehicale_width = 14
vehicale_height = 6
vehicale_speed = .1




# main loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if vehicale_x > screen_width:
    #    vehicale_x = 0

    vehicale_x += vehicale_speed

    if vehicale_x + vehicale_width > road_x + road_width:
        vehicale_x = road_x + road_width - vehicale_width

    screen.fill(white)

    pygame.draw.rect(screen, black, (road_x, road_y, road_width, road_hight))

    pygame.draw.rect(screen, red, (vehicale_x, vehicale_y, vehicale_width, vehicale_height))





    pygame.display.flip()

pygame.quit()
sys.exit()
