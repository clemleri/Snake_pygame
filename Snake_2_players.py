import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic


class Snake_2_players(Snake_classic):
    def __init__(self,x,direction,dict_button):
        super().__init__()
        self.name_game_mode = "2 players game mode"
        self.x = x
        self.tuple_direction = direction 
        self.dict_button = dict_button
    
    def player_colision(self,snake_player):
        if (self.x,self.y) in snake_player:
            return True
        
    def food_spawn(self, color_food):
        return super().food_spawn(color_food)





