import pygame
import sys
from helper_functions import *

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
RED = (255, 0, 0)


# Dairenin başlangıç konumu ve yarıçapı
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2
circle_radius = 15


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")



# Initialize the rectangle's position and size
rect_x = SCREEN_WIDTH // 2
rect_y = SCREEN_HEIGHT // 2
rect_width = 50
rect_height = 50

# Set the initial movement speed
speed = 0.2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the rectangle based on key input
    if keys[pygame.K_LEFT]:
        rect_x -= speed
        if rect_x <0:
            rect_x=0
    if keys[pygame.K_RIGHT]:
        rect_x += speed
        if rect_x + rect_width > SCREEN_WIDTH:
            rect_x = SCREEN_WIDTH - rect_width
    if keys[pygame.K_UP]:
        rect_y -= speed
        if rect_y <0:
            rect_y=0
    if keys[pygame.K_DOWN]:
        rect_y += speed
        if rect_y + rect_height > SCREEN_HEIGHT:
            rect_y = SCREEN_HEIGHT - rect_height
    

    # Fill the screen with a white background
    screen.fill(GREEN)

    # Draw the blue rectangle on the screen
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Draw rows
    drawRows(screen,SCREEN_WIDTH,SCREEN_HEIGHT,rect_width,BLACK)

    # Draw cols
    drawCols(screen,SCREEN_WIDTH,SCREEN_HEIGHT,rect_width,BLACK)

    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
            # Update the screen

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
