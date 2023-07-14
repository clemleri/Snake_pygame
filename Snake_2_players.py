import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic


class Snake_2_players(Snake_classic):
    def __init__(self):
        super().__init__()
        self.snake_player_1 = Snake_classic()
        self.snake_player_2 = Snake_classic(dict_button_player2, (-snake_speed,0))
        self.name_game_mode = "2 players game mode"

    
    def player_colision(self,snake_player):
        if (self.x,self.y) in snake_player:
            return True
        
    def food_spawn(self, color_food,snake_2):
        self.score+=1
        food_sound_effect.play()
        pygame.draw.rect(screen,color_black,(120,20,80,40))
        score_text = font_little_size.render('Score: '+str(self.score), True, color_yellow)
        screen.blit(score_text,(20,20))

        if self.snake[-1][0] == self.snake[-2][0]:
             self.snake.append((self.snake[-1][0] - 20, self.snake[-1][1]))
        else:
            self.snake.append((self.snake[-1][0], self.snake[-1][1] - 20))

        while (self.food_x,self.food_y) in self.snake or (self.food_x,self.food_y) in snake_2:
            self.food_x, self.food_y = randrange(20, self.snake_width-40, 20), randrange(60,self.snake_height-60,20)  

        pygame.draw.rect(screen, color_food, (self.food_x, self.food_y, 20, 20))
        pygame.display.update((self.food_x, self.food_y, 20, 20))
        pygame.display.update((120,20,80,38))

        self.bool_damier = not self.bool_damier




