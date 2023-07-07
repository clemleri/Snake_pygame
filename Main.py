import pygame
from math import *
from random import *
from time import * 

from Variable import *
from Snake_classic import Snake_classic
from Snake_wall import Snake_wall
from Snake_level import Snake_level
from Snake_2_players import Snake_2_players

obj_snake_classic = Snake_classic()
obj_snake_wall = Snake_wall()
obj_snake_level = Snake_level()
obj_snake_player_1 = Snake_2_players(WIDTH/3,(-snake_speed,0),dict_button)
obj_snake_player_2 = Snake_2_players(WIDTH*(2/3),(snake_speed,0),dict_button_player2)


# Definition of the class of the main window it allows to create button more easily
class Main_window():
  def __init__(self,x, y, game_name, game_function, width = 400, height = 200) -> None:
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text, self.game_function = game_name, game_function
    self.last_coo_hover = []

  def draw_button(self):
    button_rect = pygame.Rect(self.x,self.y,self.width,self.height)
    pygame.draw.rect(screen,color_grey,button_rect,2,5)
    text = font_normal_size.render(self.text, True, color_green)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

  def hover_button(self, mouse_coo):
    if self.x <= mouse_coo[0] <= self.x + self.width and self.y <= mouse_coo[1] <= self.y+self.height:
      pygame.draw.rect(screen,color_white,(self.x,self.y,400,200),2,5)
      pygame.display.update((self.x ,self.y,400,200))
      if [self.x,self.x + self.width,self.y ,self.y +self.height] not in self.last_coo_hover:
        self.last_coo_hover.append([self.x,self.x + self.width,self.y ,self.y +self.height])
    if len(self.last_coo_hover) > 0:
      if (self.last_coo_hover[0][0] > mouse_coo[0] or self.last_coo_hover[0][2] > mouse_coo[1]) or (self.last_coo_hover[0][1] < mouse_coo[0] or self.last_coo_hover[0][3] < mouse_coo[1]):
        pygame.draw.rect(screen,color_grey,(self.last_coo_hover[0][0] ,self.last_coo_hover[0][2],400,200),2,5)
        pygame.display.update((self.last_coo_hover[0][0] ,self.last_coo_hover[0][2],400,200))
        self.last_coo_hover.pop(0)
      return True
    
  def click_button(self):
    if pygame.mouse.get_pressed()[0] == 1:
      click_button_sound_effect.play()
      screen.fill(color_grey_mid)
      if callable(self.game_function) == True:
        self.game_function()
      else:
        return True
    else:
      return False


def game_over_window(button_retry,score1, title_text, score2 = None):
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
          if button.click_button() == True:
            return
          else:
            continue
          


#------------------------------------function Game mode with the classic snake-------------------------------------
def Snake_classic_function():
  obj_snake_classic.snake_interface()
  obj_snake_classic.wait_start()

  obj_snake_classic.__init__()
  pygame.draw.rect(screen, color_yellow, (obj_snake_classic.food_x, obj_snake_classic.food_y, 20, 20))
  pygame.display.flip()

  while obj_snake_classic.running:
    clock.tick(FPS) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        obj_snake_classic.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          obj_snake_classic.running = False
          return

    if obj_snake_classic.x == obj_snake_classic.food_x and obj_snake_classic.y == obj_snake_classic.food_y:
      obj_snake_classic.food_spawn(color_yellow)

    obj_snake_classic.move_snake(color_green)
    
    if obj_snake_classic.snake_collision() == True:
      death_sound_effect.play()
      obj_snake_classic.running = False

  button_retry = Main_window(320,425,"Retry",Snake_classic_function)
  game_over_window(button_retry,obj_snake_classic.score,"GAME OVER")

  screen.fill(color_black)
  draw_main_window(lst_object_button)

  sleep(0.1)
  return
#-------------------------------------------function Game mode with wall-------------------------------------------
def Snake_wall_function():
  obj_snake_wall.snake_interface()
  obj_snake_wall.wait_start()

  obj_snake_wall.__init__()
  pygame.draw.rect(screen, color_yellow, (obj_snake_wall.food_x, obj_snake_wall.food_y, 20, 20))
  pygame.display.flip()

  while obj_snake_wall.running:
    clock.tick(FPS) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        obj_snake_wall.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          obj_snake_classic.running = False

    if obj_snake_wall.x == obj_snake_wall.food_x and obj_snake_wall.y == obj_snake_wall.food_y:
      obj_snake_wall.food_spawn(color_yellow)

    obj_snake_wall.move_snake(color_green)

    if obj_snake_wall.score > 0 and floor(obj_snake_wall.score/2) == len(obj_snake_wall.excluded_coo):
      obj_snake_wall.wall_creation()

    if obj_snake_wall.snake_colision_wall() == True or obj_snake_wall.snake_collision() == True:
      death_sound_effect.play()
      obj_snake_wall.running = False

  button_retry = Main_window(320,425,"Retry",Snake_wall_function)
  game_over_window(button_retry,obj_snake_wall.score,"GAME OVER")

  screen.fill(color_black)
  draw_main_window(lst_object_button)

  sleep(0.1)
  return
#------------------------------------------function Game mode with level--------------------------------------------
def Snake_level_function():
  obj_snake_level.snake_surface.fill(color_black)
  def new_level():
    succes_level_sound_effect.play()
    obj_snake_level.load_level()
    obj_snake_level.snake_surface.fill(color_black)
    obj_snake_level.snake_interface()
    obj_snake_level.draw_level()
    screen.blit(obj_snake_level.snake_surface,(0,0))
    obj_snake_level.reset()
    pygame.draw.rect(screen, color_yellow, (obj_snake_level.food_x, obj_snake_level.food_y, 20, 20))
    pygame.draw.rect(screen, color_red, (obj_snake_level.food_level_x, obj_snake_level.food_level_y, 20, 20))
    pygame.display.flip()

  obj_snake_level.num_level = 1
  obj_snake_level.snake_interface()
  obj_snake_level.draw_level()
  obj_snake_level.wait_start()

  obj_snake_level.__init__()
  pygame.draw.rect(screen, color_yellow, (obj_snake_level.food_x, obj_snake_level.food_y, 20, 20))
  pygame.draw.rect(screen, color_red, (obj_snake_level.food_level_x, obj_snake_level.food_level_y, 20, 20))
  pygame.display.flip()

  while obj_snake_level.running:
    clock.tick(FPS) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        obj_snake_level.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          obj_snake_level.running = False

    if obj_snake_level.x == obj_snake_level.food_x and obj_snake_level.y == obj_snake_level.food_y:
      if obj_snake_level.number_food >= obj_snake_level.food_eaten:
        obj_snake_level.food_spawn()
      else:
        food_sound_effect.play()
    elif obj_snake_level.x == obj_snake_level.food_level_x and obj_snake_level.y == obj_snake_level.food_level_y:
      if obj_snake_level.food_level_eaten == 10:
        food_sound_effect.play()
        if obj_snake_level.num_level == 1:
          obj_snake_level.num_level = 2
          new_level()
        elif obj_snake_level.num_level == 2:
          obj_snake_level.num_level = 3
          new_level()
        elif obj_snake_level.num_level == 3:
          obj_snake_level.running = False
      else:
        obj_snake_level.food_level_spawn()

    obj_snake_level.move_snake()
    
    if obj_snake_level.snake_collision() == True or obj_snake_level.verif_wall((obj_snake_level.x,obj_snake_level.y)) == True:
      death_sound_effect.play()
      obj_snake_level.running = False

  obj_snake_level.score_total += obj_snake_level.score
  button_retry = Main_window(320,425,"Retry",Snake_level_function)
  if  obj_snake_level.num_level < 3 or obj_snake_level.food_level_eaten < 11:
    game_over_window(button_retry,obj_snake_level.score_total,"GAME OVER")
  else:
    game_over_window(button_retry,obj_snake_level.score_total,"YOU WIN")

  screen.fill(color_black)
  draw_main_window(lst_object_button)

  sleep(0.1)
  return

#-----------------------------------------function Game mode with 2 players-----------------------------------------
def Snake_2_players_function():
  obj_snake_player_1.snake_interface()
  obj_snake_player_1.wait_start()

  obj_snake_player_1.__init__(WIDTH/3,(-snake_speed,0),dict_button)
  obj_snake_player_2.__init__(WIDTH*(2/3),(snake_speed,0),dict_button_player2)
  pygame.draw.rect(screen, color_yellow, (obj_snake_classic.food_x, obj_snake_classic.food_y, 20, 20))
  pygame.display.flip()

  while obj_snake_player_1.running and obj_snake_player_2.running:
    clock.tick(FPS) 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        obj_snake_player_1.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          obj_snake_player_1.running = False
          return

    if obj_snake_player_1.x == obj_snake_classic.food_x and obj_snake_player_1.y == obj_snake_classic.food_y:
      obj_snake_player_1.food_spawn(color_yellow)
    if obj_snake_player_2.x == obj_snake_classic.food_x and obj_snake_player_2.y == obj_snake_classic.food_y:
      obj_snake_player_2.food_spawn(color_yellow)

    obj_snake_player_1.move_snake(color_green)
    obj_snake_player_2.move_snake(color_red)
    
    if obj_snake_player_1.snake_collision() == True or obj_snake_player_1.player_colision(obj_snake_player_2.snake) == True:
      death_sound_effect.play()
      obj_snake_player_1.running = False
    if obj_snake_player_2.snake_collision() == True or obj_snake_player_2.player_colision(obj_snake_player_1.snake) == True:
      death_sound_effect.play()
      obj_snake_player_2.running = False


  button_retry = Main_window(320,425,"Retry",Snake_2_players_function)
  if obj_snake_player_1.running == False:
    game_over_window(button_retry,obj_snake_player_1.score,"PLAYER 2 WIN",obj_snake_player_2.score)
  elif obj_snake_player_2.running == False:
    game_over_window(button_retry,obj_snake_player_1.score,"PLAYER 1 WIN",obj_snake_player_2.score)

  screen.fill(color_black)
  draw_main_window(lst_object_button)

  sleep(0.1)
  return 

background_theme.play(-1)

button_Classic = Main_window(320,225,"Classic game mode",Snake_classic_function)
button_Wall = Main_window(760,225,"Wall game mode",Snake_wall_function)
button_Level = Main_window(320,465,"Level game mode",Snake_level_function)
button_2_Players = Main_window(760,465,"2 players game mode",Snake_2_players_function)

lst_object_button = [button_Classic,button_Wall,button_Level,button_2_Players]

button_quit = Main_window(760,425,"Quit",None)

#------------------------------------------function drawing the main window-----------------------------------------
def draw_main_window(lst_object):
  title_text = font_high_size.render('SNAKE', True, color_green)
  screen.blit(title_text,(520,50))

  for i in range(0,3):
    lst_object[i].draw_button()

  pygame.draw.rect(screen,color_grey,(760,465,400,200),2,3)
  screen.blit(font_normal_size.render('2 players', True, color_green),(870,505))
  screen.blit(font_normal_size.render('game mode', True, color_green),(850,555))

  pygame.display.update()

# Definition of the frame per second of the game 
clock = pygame.time.Clock()
FPS = 50

pygame.display.update()

#-----------------------------------------------Main loop of the game-----------------------------------------------
def main_loop(running,lst_object):
  draw_main_window(lst_object_button)
  while running:
    clock.tick(FPS) 
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      for object in lst_object:
        if object.hover_button(mouse) == True:
          object.click_button()

main_loop(True,lst_object_button)