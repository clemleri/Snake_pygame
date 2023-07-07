import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic

class Snake_wall(Snake_classic):
    def __init__(self):
        super().__init__()
        self.name_game_mode = "Wall game mode"
        self.excluded_coo = []
        
    def wall_creation(self):
        self.excluded_coo.append((self.food_x,self.food_y))
        x_wall, y_wall = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20) 
        while (x_wall,y_wall) in self.excluded_coo:
            x_wall, y_wall = randrange(20,self.snake_width,20), randrange(40,self.snake_height,20)  
        self.excluded_coo.pop()
        self.excluded_coo.append((x_wall,y_wall))
        pygame.draw.rect(screen,color_black,(x_wall,y_wall,20,20))
        pygame.draw.rect(screen,color_green,(x_wall,y_wall,20,20),2,3)
        pygame.display.update((x_wall,y_wall,20,20))

    def snake_colision_wall(self):
        if (self.x,self.y) in self.excluded_coo:
            return True
        else:
            return False 