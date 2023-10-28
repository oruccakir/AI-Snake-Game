import pygame
import sys
import constants
from constants import *
import snake_game

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
    

def start_button_action():
    constants.STATE = GAME_STATE

def end_button_action():
    snake_game.running = False