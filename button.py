import pygame
from constants import *

class Button:

    def __init__(self,x,y,width,height,text,color,action=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.color = color
        self.action = action
        self.is_hovered = False
    
    def draw_button(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
        font = pygame.font.Font(None,36)
        text = font.render(self.text,True,(0,0,0))
        text_rect = text.get_rect(center = self.rect.center)
        surface.blit(text,text_rect)

    
    def check_click(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

