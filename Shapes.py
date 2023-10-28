from constants import *
import pygame

class Square:
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
        self.square = pygame.Rect(x,y,width,width)

class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.circle = pygame.Rect(x-radius,y-radius,2*radius,2*radius)


class Snake:
    def __init__(self,color,segment):
        self.head = Square(RECT_X,RECT_Y,RECT_WIDTH)
        self.snake_squares = []
        self.snake_squares.append(self.head)
        for i in range(1,segment+1):
            self.snake_squares.append(Square(self.head.x,self.head.y+i*self.head.width,self.head.width))
        self.color=color
        self.width = self.head.width

    def moveUp(self):
        newHead = Square(self.head.x,self.head.y-self.width,self.width)
        self.snake_squares.insert(0,newHead)
        self.head=newHead

    def moveDown(self):
        newHead = Square(self.head.x,self.head.y+self.width,self.width)
        self.snake_squares.insert(0,newHead)
        self.head=newHead
    
    def moveLeft(self):
        newHead = Square(self.head.x-self.width,self.head.y,self.width)
        self.snake_squares.insert(0,newHead)
        self.head = newHead

    
    def moveRight(self):
        newHead = Square(self.head.x+self.width,self.head.y,self.width)
        self.snake_squares.insert(0,newHead)
        self.head=newHead


    def is_Snake_collide_with_himself(self):
            for other_square in self.snake_squares:
                if self.head != other_square:
                    if self.head.square.colliderect(other_square.square):
                        return True
            return False
    
    def is_Snake_in_frontier(self):
        if self.head.x <= 0 or self.head.x >= GAME_SCREEN_WIDTH or self.head.y <=0 or self.head.y >= GAME_SCREEN_HEIGHT:
            return False
        
        return True


        
    