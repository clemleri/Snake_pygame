import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic


class Snake_2_players(Snake_classic):
    def __init__(self):
        super().__init__()
        self.snake_player_1 = Snake_classic(WIDTH/3,dict_button,(snake_speed,0))
        self.snake_player_2 = Snake_classic(WIDTH*(2/3),dict_button_player2, (snake_speed,0))
        self.name_game_mode = "2 players game mode"
        self.food_x_2s, self.food_y_2s = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  


    def player_colision_1(self):
        if (self.snake_player_1.x,self.snake_player_1.y) in self.snake_player_2.snake:
            return True
        
    def player_colision_2(self):
        if (self.snake_player_2.x,self.snake_player_2.y) in self.snake_player_1.snake:
            return True
        
    def move_snakes(self):
        self.snake_player_1.move_snake(color_green)
        self.snake_player_2.move_snake(color_red)

    def print_scores(self):
        pygame.draw.rect(screen,color_black,(120,20,80,40))
        score_text = font_little_size.render('Scores: '+str(self.snake_player_1.score)+' VS '+str(self.snake_player_2.score), True, color_yellow)
        screen.blit(score_text,(20,20))

    def food_spawn(self,color_food,snake_eating,snake_hungry):
        snake_eating.score+=1
        food_sound_effect.play()
        self.print_scores()

        self.food_x_2s, self.food_y_2s = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  


        if snake_eating.snake[-1][0] == snake_eating.snake[-2][0]:
             snake_eating.snake.append((snake_eating.snake[-1][0] - 20, snake_eating.snake[-1][1]))
        else:
            snake_eating.snake.append((snake_eating.snake[-1][0], snake_eating.snake[-1][1] - 20))

        while (self.food_x_2s,self.food_y_2s) in self.snake or (self.food_x_2s,self.food_y_2s) in snake_hungry.snake:
            self.food_x_2s, self.food_y_2s = randrange(20, self.snake_width-40, 20), randrange(60,self.snake_height-60,20)  

        pygame.draw.rect(screen, color_food, (self.food_x_2s, self.food_y_2s, 20, 20))
        pygame.display.update((self.food_x_2s, self.food_y_2s, 20, 20))
        pygame.display.update((120,20,180,38))

        snake_eating.bool_damier = not snake_eating.bool_damier




