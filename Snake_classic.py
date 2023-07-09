import pygame
from math import *
from random import *
from time import * 

from Variable import *

class Snake_classic():
    def __init__(self):
      self.name_game_mode = "Classic game mode"
      self.running = True
      self.snake_width, self.snake_height = WIDTH, HEIGHT
      self.snake_surface = pygame.Surface((self.snake_width, self.snake_height))
      self.x, self.y = self.snake_width/2, self.snake_height/2 
      self.snake = [(self.x,self.y),(self.x-20,self.y),(self.x-40,self.y)]
      self.tail_snake = (self.x-40.2,self.y)
      self.dict_button = {pygame.K_LEFT:(-snake_speed,0),pygame.K_RIGHT:(snake_speed,0),pygame.K_UP:(0,-snake_speed),pygame.K_DOWN:(0,snake_speed)}
      self.tuple_direction = (snake_speed,0)
      self.chg_tuple_direction = (snake_speed,0)
      self.verrou_change = False 
      self.food_x, self.food_y = randrange(20,self.snake_width-20,20), randrange(60,self.snake_height-40,20)  
      self.score = 0
      self.bool_damier = False
      
    def snake_interface(self):

      boolean_damier = False 

      game_mode_rect = pygame.Rect(0,0,1440,60)
      name_game_mode = font_normal_size.render(self.name_game_mode, True, color_green)
      name_gm_rect = name_game_mode.get_rect(center=game_mode_rect.center)
      self.snake_surface.blit(name_game_mode, name_gm_rect)
      
      for i in range(20,1420,20):
        for y in range(60,720,20):
          if boolean_damier == False:
            pygame.draw.rect(self.snake_surface,color_grey_mid,(i,y,20,20))
          else:
            pygame.draw.rect(self.snake_surface,color_grey,(i,y,20,20))
          boolean_damier = not boolean_damier
          
      score_text = font_little_size.render('Score: 0', True, color_yellow)
      self.snake_surface.blit(score_text,(20,20))
      pygame.draw.rect(self.snake_surface,color_green,(18,58,self.snake_width-36,self.snake_height-96),2,7)
      pygame.display.flip()

    def wait_start(self):
      self.running = True
      surface_wait_start = pygame.Surface((self.snake_width, self.snake_height),pygame.SRCALPHA)
      surface_wait_start.fill(color_black)

      text = font_little_size.render("Press enter to start playing", True, color_green)
      text_rect = text.get_rect(center=pygame.Rect(500, 300, 450, 100).center)

      screen.blit(self.snake_surface,(0,0))
      surface_wait_start.set_alpha(150)
      screen.blit(surface_wait_start,(0,0))
      screen.blit(text, text_rect)
      pygame.display.flip()

      while self.running:
        for event in pygame.event.get():
          if pygame.key.get_pressed()[pygame.K_RETURN]:
            click_button_sound_effect.play()
            self.running = False

      screen.blit(self.snake_surface,(0,0))
      pygame.display.flip()

    def food_spawn(self,color_food):
      self.score+=1
      food_sound_effect.play()
      pygame.draw.rect(screen,color_black,(120,20,80,40))
      score_text = font_little_size.render('Score: '+str(self.score), True, color_yellow)
      screen.blit(score_text,(20,20))

      if self.snake[-1][0] == self.snake[-2][0]:
          self.snake.append((self.snake[-1][0] - 20, self.snake[-1][1]))
      else:
          self.snake.append((self.snake[-1][0], self.snake[-1][1] - 20))

      while (self.food_x,self.food_y) in self.snake:
        self.food_x, self.food_y = randrange(20, self.snake_width-40, 20), randrange(60,self.snake_height-60,20)  

      pygame.draw.rect(screen, color_food, (self.food_x, self.food_y, 20, 20))
      pygame.display.update((self.food_x, self.food_y, 20, 20))
      pygame.display.update((120,20,80,38))

      self.bool_damier = not self.bool_damier

    def draw_snake(self,color):
      pygame.draw.rect(screen,color,(self.snake[0][0],self.snake[0][1],20,20))
      if 1420 > self.tail_snake[0] > 0 and 720 > self.tail_snake[1] > 40:
        if self.bool_damier == True:
          pygame.draw.rect(screen,color_grey_mid,(self.tail_snake[0],self.tail_snake[1],20,20))
        elif self.bool_damier == False:
          pygame.draw.rect(screen,color_grey,(self.tail_snake[0],self.tail_snake[1],20,20))
      self.bool_damier = not self.bool_damier

    def move_snake(self,color):
      verif = pygame.key.get_pressed()
      for keys in self.dict_button:
        if verif[keys]:
          if (abs(self.dict_button[keys][0]),abs(self.dict_button[keys][1])) == (abs(self.tuple_direction[0]),abs(self.tuple_direction[1])):
            break
          else:
            self.chg_tuple_direction = self.dict_button[keys]
      
      self.x, self.y = round(self.x+self.tuple_direction[0],1), round(self.y+self.tuple_direction[1],1)

      if self.x == floor(self.x/20)*20 and self.y == floor(self.y/20)*20:
        self.tuple_direction = self.chg_tuple_direction
        self.snake.insert(0,(self.x,self.y))
        self.tail_snake = self.snake.pop()
        self.draw_snake(color)
      pygame.display.update((self.snake[0][0], self.snake[0][1], 20, 20))
      pygame.display.update((self.tail_snake[0], self.tail_snake[1], 20, 20))

    def snake_collision(self):
      if (self.x, self.y) in self.snake[1:]:
        return True 
      elif self.snake[0][0] < 20 or self.snake[0][0] > self.snake_width-40 or self.snake[0][1] < 60 or self.snake[0][1] > self.snake_height-60:
        return True
      else: 
        return False
      
def game_over_window(button_retry,button_quit,score1, title_text, score2 = None):
  surface_game_over = pygame.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
  surface_game_over.fill(color_black)
  alpha_game_over = 0
  game_over_text = font_high_size.render(title_text, True, color_green)
  game_over_text_rect = game_over_text.get_rect(center=pygame.Rect(0, 0, WIDTH, HEIGHT-500).center)
  rect_score1 = pygame.Rect(0,200,WIDTH,200)
  
  if type(score2) == int:
    score_text1 = font_normal_size.render("Player1 scored "+str(score1)+" points", True, color_green)
    score_text_rect1 = score_text1.get_rect(center=rect_score1.center)
    rect_score2 = pygame.Rect(0,250,WIDTH,200)
    score_text2 = font_normal_size.render("Player2 scored "+str(score2)+" points", True, color_green)
    score_text_rect2 = score_text2.get_rect(center=rect_score2.center)
  else:
    score_text1 = font_normal_size.render("You scored "+str(score1)+" points", True, color_green)
    score_text_rect1 = score_text1.get_rect(center=rect_score1.center)

  while alpha_game_over <= 15:
    button_retry.draw_button()
    button_quit.draw_button()
    screen.blit(game_over_text, game_over_text_rect)
    screen.blit(score_text1, score_text_rect1)
    if type(score2) == int:
      screen.blit(score_text2, score_text_rect2)
    surface_game_over.set_alpha(alpha_game_over)
    screen.blit(surface_game_over,(0,0))
    pygame.display.flip()
    alpha_game_over+=0.1
    
  lst_button = [button_retry,button_quit]
  running = True

  while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      for button in lst_button:
        if button.hover_button(mouse) == True:
          if button.click_button(event) == True:
            running = False
            return
          else:
            continue
