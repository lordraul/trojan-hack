from enum import Enum
import pygame

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def X(self):
        return [0, 0, -1, 1][self.value]
    
    def Y(self):
        return [-1, 1, 0, 0][self.value]
        

class Soldier:
    rect : pygame.Rect
    direction : Direction

    def __init__(self, rect : pygame.Rect, direction : Direction):
        self.rect = rect
        self.direction = direction