import pygame

screen_size_x = 1600
screen_size_y = 800
wall_size = screen_size_x / 2 / 20
wall_group = pygame.sprite.Group()
ray_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

real_wall_height = 8000
wall_height_scale = 90000
camera_height = screen_size_y // 1.5  # middle of the screen (adjust if needed)
slice_width = 6