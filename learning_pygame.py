import pygame
import sys
from helper_functions import *
from Shapes import *
from constants import *

# Initialize Pygame
pygame.init()

# Initialize the snake
snake = Snake(BLACK)

# Initialize the circle
circle = Circle(circle_x,circle_y,8)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# set timer
pygame.time.set_timer(pygame.USEREVENT, 800)


# Set the initial movement speed
speed = 50

isLeft = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == 769:
            newHead = Square(snake.head.x-snake.width,snake.head.y,snake.width)
            snake.snake_squares.insert(0,newHead)
            snake.snake_squares.pop()
        elif event.type == 768:
            newHead = Square(snake.head.x+snake.width,snake.head.y,snake.width)
            snake.snake_squares.insert(0,newHead)
            snake.snake_squares.pop()



    # Get the state of all keys
    keys = pygame.key.get_pressed()



    # Move the rectangle based on key input
    if isLeft == True :
        isLeft = False
        if snake.head.x  <0:
            snake.head.x =0
    if keys[pygame.K_RIGHT]:
        snake.head.x  += speed
        if snake.head.x  + snake.head.width > SCREEN_WIDTH:
            snake.head.x  = SCREEN_WIDTH - snake.head.width
    if keys[pygame.K_UP]:
        snake.head.y -= speed
        if snake.head.y <0:
            snake.head.y=0
    if keys[pygame.K_DOWN]:
        snake.head.y += speed
        if snake.head.y + snake.head.width > SCREEN_HEIGHT:
            snake.head.y = SCREEN_HEIGHT - snake.head.width
    

    
    # Fill the screen with a white background
    screen.fill(GRAY)

    # Draw the blue rectangle on the screen
    #pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    drawSnake(screen,snake)

    # Draw rows
    #drawRows(screen,SCREEN_WIDTH,SCREEN_HEIGHT,rect_width,BLACK)

    # Draw cols
    #drawCols(screen,SCREEN_WIDTH,SCREEN_HEIGHT,rect_width,BLACK)

    pygame.draw.circle(screen, RED, (circle.x, circle.y), circle.radius)
            # Update the screen

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
