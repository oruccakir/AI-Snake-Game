from constants import *
import pygame

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.parent = None
        self.childs = []
        self.node_square = pygame.Rect(x,y,RECT_WIDTH,RECT_WIDTH)

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
        if self.head.x <= 0 or self.head.x >= SCREEN_WIDTH-1*RECT_WIDTH or self.head.y <=4*RECT_WIDTH or self.head.y >= SCREEN_HEIGHT-1*RECT_WIDTH:
            return False
        
        return True
    
    def aboveControl(self,node):

        above_node = Node(node.x,node.y-RECT_WIDTH)

        isCollideWith_Himself = False

        for square in self.snake_squares:
            if above_node.node_square.colliderect(square.square):
                isCollideWith_Himself = True
                break

        isCollideWith_Frontier = False

        print(above_node.node_square.y)

        if above_node.node_square.y <= 4*RECT_WIDTH:
            isCollideWith_Frontier = True

        print("Fro " +str(isCollideWith_Frontier))
        print("Him "+str(isCollideWith_Himself))
        return not isCollideWith_Himself and not isCollideWith_Frontier
    
    
    def belowControl(self,node):

        below_node = Node(node.x,node.y+RECT_WIDTH)

        isCollideWith_Himself = False

        for square in self.snake_squares:
            if below_node.node_square.colliderect(square.square):
                isCollideWith_Himself = True
                break

        isCollideWith_Frontier = False

        if below_node.node_square.y >= SCREEN_HEIGHT-1*RECT_WIDTH:
            isCollideWith_Frontier = True

        return not isCollideWith_Himself and not isCollideWith_Frontier
    

    def leftControl(self,node):

        left_node = Node(node.x-RECT_WIDTH,node.y)

        isCollideWith_Himself = False

        for square in self.snake_squares:
            if left_node.node_square.colliderect(square.square):
                isCollideWith_Himself = True
                break

        isCollideWith_Frontier = False

        if left_node.node_square.x <= 0:
            isCollideWith_Frontier = True

        return not isCollideWith_Himself and not isCollideWith_Frontier
    

    def rightControl(self,node):

        right_node = Node(node.x+RECT_WIDTH+1,node.y)

        isCollideWith_Himself = False

        for square in self.snake_squares:
            if right_node.node_square.colliderect(square.square):
                isCollideWith_Himself = True
                break

        isCollideWith_Frontier = False

        if right_node.node_square.x >= SCREEN_WIDTH-RECT_WIDTH:
            isCollideWith_Frontier = True

        return not isCollideWith_Himself and not isCollideWith_Frontier

    

    def findTheGoal(self,target_circle):

        frontier = []
        frontier.append(Node(self.head.x,self.head.y))
        isFound = False

        while not isFound:

            currentNode = frontier.pop(0)

            if currentNode.square.colliderect(target_circle.circle):
                isFound = True
            else:

                if self.aboveControl(currentNode):
                    currentNode.childs.append(Node(currentNode.x,currentNode.y+RECT_WIDTH))

                if self.belowControl(currentNode):
                    currentNode.childs.append(Node(currentNode.x,currentNode.y-RECT_WIDTH))

                if self.leftControl(currentNode):
                    currentNode.childs.append(Node(currentNode.x-RECT_WIDTH,currentNode.y))
                
                if self.rightControl(currentNode):
                    currentNode.childs.append(Node(currentNode.x+RECT_WIDTH,currentNode.y))

                for node in currentNode.childs:
                    frontier.insert(0,node)





        
    