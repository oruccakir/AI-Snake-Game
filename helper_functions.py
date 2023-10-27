import pygame
import sys

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
