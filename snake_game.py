import pygame
import sys
from helper_functions import *
from Shapes import *
from constants import *
import random
from button import *
import constants 

# Initialize Pygame
pygame.init()

# define a button
start_button = Button(300, 250, 200, 50, "START",start_button_action)
end_button = Button(300, 250, 200, 50, "END",end_button_action)

# Initialize the snake
snake = Snake(BLACK,20)

# Initialize the circle
circle = Circle(CIRCLE_X,CIRCLE_Y,CIRCLE_RADIUS)

# Create the screen
game_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
start_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
end_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

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

    if constants.STATE == START_STATE:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            start_button.check_click(event)

        start_screen.fill(GRAY)
        # Update the display
        start_button.draw_button(start_screen)
        pygame.display.flip()

    elif constants.STATE == GAME_STATE:

        if isGameOver(snake):
            constants.STATE = END_STATE
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

                RANDOM_X = random.randint(1,GAME_SCREEN_WIDTH-1)
                RANDOM_Y = random.randint(1,GAME_SCREEN_HEIGHT-1)

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


            # Fill the screen with a gray background
            game_screen.fill(GRAY)

            drawSnake(game_screen,snake)

            #button.draw_button(screen)

            
            if circle != None:
                pygame.draw.circle(game_screen, RED, (circle.x, circle.y), circle.radius)

            # Update the display
            pygame.display.flip()

    
    elif constants.STATE == END_STATE:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            end_button.check_click(event)
            
        end_screen.fill(GRAY)

        end_button.draw_button(end_screen)

        # Update the display
        pygame.display.flip()

    

# Quit Pygame
pygame.quit()
sys.exit()
