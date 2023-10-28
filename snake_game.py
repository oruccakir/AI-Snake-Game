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
        self.start_button = Button(300, 750, 300, 50, "START as HUMAN",GRAY,self.start_button_action)
        self.start_ai_button = Button(300, 650, 300, 50, "START as ORUÇ",GRAY,self.start_ai_button_action)
        self.end_button = Button(300, 250, 200, 50, "END",GRAY,self.end_button_action)
        self.restart_button = Button(300, 100, 200, 50, "RESTART",GRAY,self.restart_button_action)
        self.pause_button = Button(25,25,150,40,"PAUSE",YELLOW,self.pause_button_action)
        self.settings_button = Button(375,25,150,40,"SETTINGS",BLUE,self.settings_button_action)
        self.return_game_button = Button(300,600,200,50,"RETURN",GRAY,self.return_game_button_action)
        self.score_rect = pygame.Rect(200,25,150,40)
        self.gamse_speed_rect = pygame.Rect(550,25,150,40)
        # Create the screen
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.settings_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.isLeft = False
        self.isDown = False
        self.isRight = False
        self.isUP = True
        self.isPaussed = False
        self.score = 0

        self.frontier = []
        self.frontier.append(Node(self.snake.head.x,self.snake.head.y))
        self.directions = []

        self.image = pygame.image.load("slytherin.jpg")
        self.image_surface = self.image.convert()

        self.headNode = Node(self.snake.head.x,self.snake.head.y)



    def start_button_action(self):
        self.STATE = GAME_STATE

    def end_button_action(self):
        self.RUNNING = False
    
    def start_ai_button_action(self):
        self.STATE = AI_STATE
    
    def settings_button_action(self):
        self.isPaussed = True
        self.STATE = SETTING_STATE
    
    def return_game_button_action(self):
        self.isPaussed = False
        self.STATE = GAME_STATE

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
        self.isPaussed = False
        self.score = 0

    def pause_button_action(self):
        if self.isPaussed == False:
            self.isPaussed = True
            self.pause_button.text = "Continue"
        else:
            self.isPaussed = False
            self.pause_button.text = "Pause"

    
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

                    self.start_ai_button.check_click(event)


                self.start_screen.fill(OLIVE)
                # Update the display
                self.start_button.draw_button(self.start_screen)
                self.start_ai_button.draw_button(self.start_screen)
                self.start_screen.blit(self.image_surface,(120,50))
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

                    if self.isPaussed == False:
                        if keys[pygame.K_LEFT] :
                            if not self.isRight:
                                self.isLeft=True
                                self.isUP = self.isDown = self.isRight = False
                        elif keys[pygame.K_RIGHT]:
                            if not self.isLeft:
                                self.isRight=True
                                self.isUP = self.isDown = self.isLeft = False
                        elif keys[pygame.K_UP]:
                            if not self.isDown:
                                self.isUP=True
                                self.isLeft = self.isDown = self.isRight = False
                        elif keys[pygame.K_DOWN]:
                            if not self.isUP:
                                self.isDown=True
                                self.isUP = self.isLeft = self.isRight = False
                            

                    for event in pygame.event.get():

                        self.pause_button.check_click(event)

                        self.settings_button.check_click(event)

                        if event.type == pygame.QUIT:
                            self.RUNNING = False
                        
                        elif event.type == pygame.USEREVENT and self.isPaussed == False:
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

                        RANDOM_X = random.randint(RECT_WIDTH+5,SCREEN_WIDTH-2*RECT_WIDTH-5)
                        RANDOM_Y = random.randint(5*RECT_WIDTH+10,SCREEN_HEIGHT-2*RECT_WIDTH-10)

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

                        self.score = self.score +1

                        if self.game_speed <= MAX_SPEED:
                            self.game_speed = MAX_SPEED

                        # enhance the speed of the game
                        pygame.time.set_timer(pygame.USEREVENT, self.game_speed)


                    # Fill the screen with a gray background
                    self.game_screen.fill(GRAY)

                    self.pause_button.draw_button(self.game_screen)

                    self.settings_button.draw_button(self.game_screen)

                    drawRect(self.game_screen,self.score_rect,f"Score : {self.score}",WHITE)
                    drawRect(self.game_screen,self.gamse_speed_rect, f"Speed : {self.game_speed}",WHITE)

                    drawSnake(self.game_screen,self.snake)

                   
                    pygame.draw.rect(self.game_screen,GREEN,(0,4*RECT_WIDTH,RECT_WIDTH,SCREEN_HEIGHT-4*RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(SCREEN_WIDTH-RECT_WIDTH,4*RECT_WIDTH,RECT_WIDTH,SCREEN_HEIGHT-4*RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(0,SCREEN_HEIGHT-RECT_WIDTH,SCREEN_WIDTH,RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(0,4*RECT_WIDTH,SCREEN_WIDTH,RECT_WIDTH))

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

            elif self.STATE == SETTING_STATE:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        self.RUNNING = False

                    self.end_button.check_click(event)

                    self.restart_button.check_click(event)

                    self.return_game_button.check_click(event)
                
                self.settings_screen.fill(TEAL)
                
                self.return_game_button.draw_button(self.settings_screen)
                self.end_button.draw_button(self.settings_screen)
                self.restart_button.draw_button(self.settings_screen)

                # Update the display
                pygame.display.flip()
            
            elif self.STATE == AI_STATE:

                if self.circle == None:
                        self.circle = Circle(RANDOM_X,RANDOM_Y,CIRCLE_RADIUS)
                
                for event in pygame.event.get():

                    self.pause_button.check_click(event)

                    self.settings_button.check_click(event)

                    if event.type == pygame.QUIT:
                            self.RUNNING = False

                    if event.type == pygame.USEREVENT and self.isPaussed == False:

                       print()

                    # Fill the screen with a gray background
                    self.game_screen.fill(GRAY)

                    self.pause_button.draw_button(self.game_screen)

                    self.settings_button.draw_button(self.game_screen)

                    drawRect(self.game_screen,self.score_rect,f"Score : {self.score}",WHITE)
                    drawRect(self.game_screen,self.gamse_speed_rect, f"Speed : {self.game_speed}",WHITE)

                    drawSnake(self.game_screen,self.snake)

                   
                    pygame.draw.rect(self.game_screen,GREEN,(0,4*RECT_WIDTH,RECT_WIDTH,SCREEN_HEIGHT-4*RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(SCREEN_WIDTH-RECT_WIDTH,4*RECT_WIDTH,RECT_WIDTH,SCREEN_HEIGHT-4*RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(0,SCREEN_HEIGHT-RECT_WIDTH,SCREEN_WIDTH,RECT_WIDTH))
                    pygame.draw.rect(self.game_screen,GREEN,(0,4*RECT_WIDTH,SCREEN_WIDTH,RECT_WIDTH))

                    #button.draw_button(screen)

                    
                    if self.circle != None:
                        pygame.draw.circle(self.game_screen, RED, (self.circle.x, self.circle.y), self.circle.radius)

                    # Update the display
                    pygame.display.flip()
                



                



            

        # Quit Pygame
        pygame.quit()
        sys.exit()




snake_game = Snake_Game()

snake_game.game()
            

    

















