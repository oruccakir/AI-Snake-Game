from constants import *

class Square:
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width

class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius


class Snake:
    def __init__(self,color):
        self.head = Square(rect_x,rect_y,rect_width)
        self.snake_squares = []
        self.snake_squares.append(self.head)
        self.color=color

        
    