import pygame
import sys
from helper_functions import *
from Shapes import *
from constants import *
import random
from button import *
import constants 
import time

# Initialize Pygame
pygame.init()

class Snake_Game:

    def __init__(self):
        self.game_speed = GAME_SPEED
        self.STATE = START_STATE
        self.RUNNING = True
        self.snake = Snake(BLACK,20)
        self.circle = Circle(CIRCLE_X,CIRCLE_Y,CIRCLE_RADIUS)
        # define a button
        self.start_button = Button(300, 400, 200, 50, "START",GRAY,self.start_button_action)
        self.end_button = Button(300, 250, 200, 50, "END",GRAY,self.end_button_action)
        self.restart_button = Button(300, 100, 200, 50, "RESTART",GRAY,self.restart_button_action)
        # Create the screen
        self.game_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        self.start_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        self.end_screen = pygame.display.set_mode((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        self.isLeft = False
        self.isDown = False
        self.isRight = False
        self.isUP = True


    def start_button_action(self):
        self.STATE = GAME_STATE

    def end_button_action(self):
        self.RUNNING = False

    def restart_button_action(self):
        self.game_speed = GAME_SPEED
        self.RUNNING = True
        self.STATE = GAME_STATE
        self.snake = Snake(BLACK,20)
        self.circle = Circle(CIRCLE_X,CIRCLE_Y,CIRCLE_RADIUS)
        self.isDown = False
        self.isLeft = False
        self.isRight = False
        self.isUP = True
        pygame.time.set_timer(pygame.USEREVENT, self.game_speed)


    
    def game(self):

        pygame.display.set_caption("Simple Pygame Example")

         # set timer
        pygame.time.set_timer(pygame.USEREVENT, self.game_speed)

        while self.RUNNING:

            if self.STATE == START_STATE:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        self.RUNNING = False

                    self.start_button.check_click(event)

                self.start_screen.fill(OLIVE)
                # Update the display
                self.start_button.draw_button(self.start_screen)
                pygame.display.flip()

            elif self.STATE == GAME_STATE:

                if isGameOver(self.snake):
                    self.STATE = END_STATE
                    pygame.time.delay(100)
                    
                else:

                    if self.circle == None:
                        self.circle = Circle(RANDOM_X,RANDOM_Y,CIRCLE_RADIUS)

                    # Get the state of all keys
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_LEFT]:
                        if not self.isRight:
                            self.isLeft=True
                            self.isUP = self.isDown = self.isRight = False
                    if keys[pygame.K_RIGHT]:
                        if not self.isLeft:
                            self.isRight=True
                            self.isUP = self.isDown = self.isLeft = False
                    if keys[pygame.K_UP]:
                        if not self.isDown:
                            self.isUP=True
                            self.isLeft = self.isDown = self.isRight = False
                    if keys[pygame.K_DOWN]:
                        if not self.isUP:
                            self.isDown=True
                            self.isUP = self.isLeft = self.isRight = False

                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            self.RUNNING = False
                        
                        elif event.type == pygame.USEREVENT:
                            if self.isUP:
                                self.snake.moveUp()
                                self.snake.snake_squares.pop()
                            elif self.isDown:
                                self.snake.moveDown()
                                self.snake.snake_squares.pop()
                            elif self.isLeft:
                                self.snake.moveLeft()
                                self.snake.snake_squares.pop()
                            elif self.isRight:
                                self.snake.moveRight()
                                self.snake.snake_squares.pop()

                        
                    if self.circle != None and self.snake.head.square.colliderect(self.circle.circle):

                        RANDOM_X = random.randint(1,GAME_SCREEN_WIDTH-1)
                        RANDOM_Y = random.randint(1,GAME_SCREEN_HEIGHT-1)

                        if self.isUP:
                            self.snake.moveUp()
                        elif self.isDown:
                            self.snake.moveDown()
                        elif self.isLeft:
                            self.snake.moveLeft()
                        elif self.isRight:
                            self.snake.moveRight()

                        self.circle = None

                        self.game_speed = self.game_speed - INCREMENT

                        if self.game_speed <= MAX_SPEED:
                            self.game_speed = MAX_SPEED

                        # enhance the speed of the game
                        pygame.time.set_timer(pygame.USEREVENT, self.game_speed)


                    # Fill the screen with a gray background
                    self.game_screen.fill(GRAY)

                    drawSnake(self.game_screen,self.snake)

                    #button.draw_button(screen)

                    
                    if self.circle != None:
                        pygame.draw.circle(self.game_screen, RED, (self.circle.x, self.circle.y), self.circle.radius)

                    # Update the display
                    pygame.display.flip()

            
            elif self.STATE == END_STATE:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        self.RUNNING = False
                    
                    self.end_button.check_click(event)

                    self.restart_button.check_click(event)
                    
                self.end_screen.fill(MAROON)

                self.end_button.draw_button(self.end_screen)
                self.restart_button.draw_button(self.end_screen)


                # Update the display
                pygame.display.flip()

            

        # Quit Pygame
        pygame.quit()
        sys.exit()




snake_game = Snake_Game()

snake_game.game()
            

    

















