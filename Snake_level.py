import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic


class Snake_level(Snake_classic):
    def __init__(self):
        super().__init__()
        self.name_game_mode = "Level game mode"
        self.food_level_x, self.food_level_y = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  
        self.food_eaten, self.number_food = 0, randint(10,15)
        self.food_level_eaten = 1
        self.num_level = 1
        self.score_total = 0
        self.snake_body_add = []
        self.bool_food = True 
        self.score_added = 0

    def reset(self):
        self.x, self.y = self.snake_width/2, self.snake_height/2 
        self.snake = [(self.x,self.y),(self.x-20,self.y),(self.x-40,self.y)]
        self.tail_snake = (self.x-40.2,self.y)
        self.tuple_direction = (snake_speed,0)
        self.chg_tuple_direction = (snake_speed,0)
        self.verrou_change = False 
        self.food_x, self.food_y = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  
        self.bool_damier = False
        self.food_eaten, self.number_food = 0, randint(10,15)
        self.food_level_eaten = 1
        self.score_total += self.score 
        self.score = 0
        self.score = 0
        while self.verif_wall((self.food_level_x,self.food_level_y)) == True:
            self.food_level_x, self.food_level_y = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  
        while self.verif_wall((self.food_x,self.food_y)) == True:
            self.food_x, self.food_y = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  

    def verif_wall(self,coord):
        if self.num_level == 1:
            if coord[1] == 320 and 220<=coord[0]<= 1200:
                return True 
            else: 
                return False 
        elif self.num_level == 2:
            if (coord[1] == 260 and coord[0]<940) or (coord[1] == 520 and coord[0]>480):
                return True 
            else:
                return False
        elif self.num_level == 3:
            if (280<=coord[0]<=1140 and (coord[1] == 220 or coord[1] == 580)) or (260<=coord[1]<=540 and (coord[0] == 260 or coord[0] == 1140)): 
                return True
            else:
                return False
            
    def draw_snake(self):
        pygame.draw.rect(screen,color_green_snake,(self.snake[0][0],self.snake[0][1],20,20))
        if 1420 > self.tail_snake[0] > 0 and 720 > self.tail_snake[1] > 40 and self.bool_food == True:
            if self.bool_damier == True:
                pygame.draw.rect(screen,color_grey_mid,(self.tail_snake[0],self.tail_snake[1],20,20))
            elif self.bool_damier == False:
                pygame.draw.rect(screen,color_grey,(self.tail_snake[0],self.tail_snake[1],20,20))
        self.bool_damier = not self.bool_damier

    def move_snake(self):
        verif = pygame.key.get_pressed()
        for keys in dict_button:
            if verif[keys]:
                if (abs(dict_button[keys][0]),abs(dict_button[keys][1])) == (abs(self.tuple_direction[0]),abs(self.tuple_direction[1])):
                    break
                else:
                    self.chg_tuple_direction = dict_button[keys]

        self.x, self.y = round(self.x+self.tuple_direction[0],1), round(self.y+self.tuple_direction[1],1)

        if self.x == floor(self.x/20)*20 and self.y == floor(self.y/20)*20:
            if len(self.snake_body_add)>0 and self.tail_snake != self.snake[-1]:
                self.snake.append(self.snake_body_add[0])
                self.snake_body_add.pop(0)
            self.tuple_direction = self.chg_tuple_direction
            self.snake.insert(0,(self.x,self.y))
            self.tail_snake_rec = self.tail_snake
            self.tail_snake = self.snake.pop()
            if len(self.snake_body_add) == 0 and self.bool_food == False and self.score_added > 1:
                self.bool_food = True
            else: 
                self.score_added=2
            self.draw_snake()
                
            pygame.display.update((self.snake[0][0], self.snake[0][1], 20, 20))
            pygame.display.update((self.tail_snake[0], self.tail_snake[1], 20, 20))

    def food_spawn(self):
        self.food_eaten +=1
        self.score+=1*self.food_level_eaten
        self.score_added = 1*self.food_level_eaten
        food_sound_effect.play()
        pygame.draw.rect(screen,color_black,(120,20,80,38))
        score_text = font_little_size.render('Score: '+str(self.score), True, color_yellow)
        screen.blit(score_text,(20,20))

        for j in range(1*self.food_level_eaten):
            self.snake_body_add.append((self.snake[-1][0], self.snake[-1][1]))

        while (self.food_x,self.food_y) in self.snake or (self.food_x,self.food_y) == (self.food_level_x,self.food_level_y) or self.verif_wall((self.food_x,self.food_y)) == True:
            self.food_x, self.food_y = randrange(20, self.snake_width-40, 20), randrange(60,self.snake_height-60,20)  

        pygame.draw.rect(screen, color_yellow, (self.food_x, self.food_y, 20, 20))
        pygame.display.update((self.food_x, self.food_y, 20, 20))
        pygame.display.update((120,20,80,38))
        self.bool_food = False
        if 1*self.food_level_eaten%2 == 0:
            self.bool_damier = self.bool_damier
        else:
            self.bool_damier = not self.bool_damier

    def food_level_spawn(self):
        self.food_level_eaten+=1
        self.score+=1
        self.score_added = 1
        food_sound_effect.play()
        pygame.draw.rect(screen,color_black,(120,20,80,38))
        score_text = font_little_size.render('Score: '+str(self.score), True, color_yellow)
        screen.blit(score_text,(20,20))

        self.snake_body_add.append((self.snake[-1][0] , self.snake[-1][1]))
        
        while (self.food_level_x,self.food_level_y) in self.snake or (self.food_x,self.food_y) == (self.food_level_x,self.food_level_y) or self.verif_wall((self.food_level_x,self.food_level_y)) == True:
            self.food_level_x, self.food_level_y = randrange(20, self.snake_width-40, 20), randrange(60,self.snake_height-60,20)  

        pygame.draw.rect(screen, color_red, (self.food_level_x, self.food_level_y, 20, 20))
        pygame.display.update((self.food_level_x, self.food_level_y, 20, 20))
        pygame.display.update((120,20,80,38))
        self.bool_food = False
        self.bool_damier = not self.bool_damier

    def draw_level(self):
        def draw_rect(x,y,width,height):
            pygame.draw.rect(self.snake_surface,color_black,(x,y,width,height),0,5)
            pygame.draw.rect(self.snake_surface,color_green,(x,y,width,height),2,5)
        if self.num_level == 1:
            draw_rect(220,320,1000,20)
        elif self.num_level == 2:
            draw_rect(20,260,920,20)
            draw_rect(500,520,920,20)
        elif self.num_level == 3: 
            draw_rect(280,220,860,20)
            draw_rect(280,580,860,20)
            draw_rect(260,260,20,300)
            draw_rect(1140,260,20,300)
        level_text = font_little_size.render('Level '+str(self.num_level), True, color_yellow)
        self.snake_surface.blit(level_text,(1315,20))
        screen.blit(self.snake_surface,(0,0))
    
    def load_level(self):
        surface_loading = pygame.Surface((self.snake_width, self.snake_height),pygame.SRCALPHA)
        surface_loading.fill(color_black)

        loading_text = font_little_size.render("loading the next level", True, color_green)
        loading_text_rect = loading_text.get_rect(center=pygame.Rect(500, 300, 450, 100).center)

        surface_loading.set_alpha(150)
        screen.blit(surface_loading,(0,0))
        screen.blit(loading_text, loading_text_rect)
        pygame.display.flip()
        sleep(3)
    


