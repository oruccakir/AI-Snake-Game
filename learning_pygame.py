import pygame
import sys
from helper_functions import *
from Shapes import *
from constants import *
import random

# Initialize Pygame
pygame.init()

# Pop-up 
popup_width = 300
popup_height = 200
popup_color = (200, 200, 200)

popup_font = pygame.font.Font(None, 36)
popup_text = "Pop-up Window"

# Initialize the snake
snake = Snake(BLACK,20)

# Initialize the circle
circle = Circle(CIRCLE_X,CIRCLE_Y,CIRCLE_RADIUS)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pygame Example")

# set game speed 
game_speed = GAME_SPEED

# set timer
pygame.time.set_timer(pygame.USEREVENT, GAME_SPEED)


isLeft = False
isDown = False
isRight = False
isUP = True

# Game loop
running = True
while running:

    if isGameOver(snake):
        running = False
    else:

        if circle == None:
            circle = Circle(RANDOM_X,RANDOM_Y,CIRCLE_RADIUS)

        # Get the state of all keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if not isRight:
                isLeft=True
                isUP = isDown = isRight = False
        if keys[pygame.K_RIGHT]:
            if not isLeft:
                isRight=True
                isUP = isDown = isLeft = False
        if keys[pygame.K_UP]:
            if not isDown:
                isUP=True
                isLeft = isDown = isRight = False
        if keys[pygame.K_DOWN]:
            if not isUP:
                isDown=True
                isUP = isLeft = isRight = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.USEREVENT:
                if isUP:
                    snake.moveUp()
                    snake.snake_squares.pop()
                elif isDown:
                    snake.moveDown()
                    snake.snake_squares.pop()
                elif isLeft:
                    snake.moveLeft()
                    snake.snake_squares.pop()
                elif isRight:
                    snake.moveRight()
                    snake.snake_squares.pop()

            
        if circle != None and snake.head.square.colliderect(circle.circle):

            RANDOM_X = random.randint(1,SCREEN_WIDTH-1)
            RANDOM_Y = random.randint(1,SCREEN_HEIGHT-1)

            print(str(len(snake.snake_squares))+ " "+str(RANDOM_X)+" "+str(RANDOM_Y))

            if isUP:
                snake.moveUp()
            elif isDown:
                snake.moveDown()
            elif isLeft:
                snake.moveLeft()
            elif isRight:
                snake.moveRight()

            circle = None

            GAME_SPEED = GAME_SPEED - INCREMENT

            if GAME_SPEED <= MAX_SPEED:
                GAME_SPEED = MAX_SPEED

            # enhance the speed of the game
            pygame.time.set_timer(pygame.USEREVENT, GAME_SPEED)

            print("Game SPEED : ",GAME_SPEED)

        # Fill the screen with a gray background
        screen.fill(GRAY)

        drawSnake(screen,snake)

        
        if circle != None:
            pygame.draw.circle(screen, RED, (circle.x, circle.y), circle.radius)
                # Update the screen

        # Update the display
        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
