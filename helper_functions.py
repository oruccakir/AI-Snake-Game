import pygame
import sys
import constants
from constants import *
import serial

#arduinoData = serial.Serial("com6",9600)

def drawRows(screen,screen_width,screen_height,width,colour):
    ordinate=0
    while ordinate != screen_height :
        pygame.draw.line(screen,colour,(0,ordinate),(screen_width,ordinate),2)
        ordinate = ordinate + width


def drawCols(screen,screen_width,screen_height,width,colour):
    apsis=0
    while apsis != screen_width :
        pygame.draw.line(screen,colour,(apsis,0),(apsis,screen_height),2)
        apsis = apsis + width


def drawSnake(screen,snake):
    for square in snake.snake_squares:
        pygame.draw.rect(screen, snake.color, (square.x, square.y, square.width, square.width))


def isGameOver(snake):
    return snake.is_Snake_collide_with_himself() or not snake.is_Snake_in_frontier()

def drawRect(surface,rect,text,color):
    pygame.draw.rect(surface,color,rect)
    font = pygame.font.Font(None,36)
    text = font.render(text,True,(0,0,0))
    text_rect = text.get_rect(center = rect.center)
    surface.blit(text,text_rect)



def get_coordinates_and_draw(screen,rect,game):

    while True:

        dataPacket = arduinoData.readline()
        dataPacket = str(dataPacket,"utf-8")
        dataPacket.strip("\r\n")
        splitPacket = dataPacket.split(",")

        x = float(splitPacket[0])
        y = float(splitPacket[1])

        print(f"X : {x} Y : {y}")

        
            
        if x >= 0 and x <=200:
            game.isLeft = True
            game.isRight = game.isUp = game.isDown = False
        else:
            game.isLeft = False

        if x >= 800 and x <= 1023:
            game.isRight = True
            game.isLeft = game.isUp = game.isDown = False
        else:
            game.isRight = False


        
        
        print(game.isLeft)

    


