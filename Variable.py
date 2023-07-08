import pygame


pygame.init()
pygame.mixer.init()

(WIDTH, HEIGHT) = (1440, 760)

color_red = (255,0,0)
color_white = (255,255,255)
color_yellow = (255,255,0)
color_black = (0,0,0)
color_green_snake = (0,250,0)
color_green = (0,255,0)
color_grey_mid = (20,20,20)
color_grey = (60,60,60)

font_little_size = pygame.font.Font('Assets/Font/Exo-Black.ttf', 32)
font_normal_size = pygame.font.Font('Assets/Font/Exo-Black.ttf', 40)
font_high_size = pygame.font.Font('Assets/Font/Exo-Black.ttf', 128)

image_sound = pygame.image.load('Assets/Images/sound.png')
image_volume = pygame.image.load('Assets/Images/volume.png')



death_sound_effect = pygame.mixer.Sound('Assets/Sound_effect/Death_sound_effect.wav')
food_sound_effect = pygame.mixer.Sound('Assets/Sound_effect/Food_sound_effect.wav')
click_button_sound_effect = pygame.mixer.Sound('Assets/Sound_effect/Click_button_sound_effect.wav')
background_theme = pygame.mixer.Sound('Assets/Sound_effect/Background_theme.wav')
succes_level_sound_effect =  pygame.mixer.Sound('Assets/Sound_effect/succes_level_sound_effect.wav')

game_volume = 0.5
def set_volume_function(volume):
    death_sound_effect.set_volume(volume)
    food_sound_effect.set_volume(volume)
    click_button_sound_effect.set_volume(volume)
    background_theme.set_volume(volume)
set_volume_function(game_volume)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

snake_speed = 5
dict_button = {pygame.K_LEFT:(-snake_speed,0),pygame.K_RIGHT:(snake_speed,0),pygame.K_UP:(0,-snake_speed),pygame.K_DOWN:(0,snake_speed)}

dict_button_player2 = {pygame.K_q:(-snake_speed,0),pygame.K_d:(snake_speed,0),pygame.K_z:(0,-snake_speed),pygame.K_s:(0,snake_speed)}


pygame.display.set_caption('Snake_game')
screen.fill(color_black)
pygame.display.flip()