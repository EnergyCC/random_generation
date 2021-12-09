import pygame
import math
import time
from player_controller import Player
import random
from map_generation import Map
import numpy as np


game_width = 1600
game_height = 900
game_fps = 144
tile_size_x = 25
tile_size_y = 25
tile_size = 25
map_fill_percentage = 53
player_pos_top = 150
movement_speed = 0.5
player_size_x = 20
player_size_y = 20
player_pos_left = (game_width / 2) - player_size_x
player_pos_top = (game_height / 2) - player_size_y
screen_cubes = []
map_seed = "EnergyCore"

game_window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Test poop')


def cube(x, y):
    return pygame.draw.rect(game_window, (0, 0, 150), pygame.Rect(x - 5, y - 5, 10, 10))


map_gen = Map(game_window, game_width, game_height)
map_gen.generate_map(tile_size, map_fill_percentage, map_seed)
map_gen.map_smoothing(2)


player = Player(100, movement_speed, 10,
                player_pos_left, player_pos_top, player_size_x, player_size_y)


run = True
clock = pygame.time.Clock()

while run:
    clock.tick(game_fps)
    game_window.fill((100, 100, 100))

    player.player_body(game_window)
    player.player_movement(game_width, game_height)
    map_gen.draw_map()

    for (x, y) in screen_cubes:
        cube(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_r]:
        map_gen.generate_map(tile_size, map_fill_percentage)
        map_gen.map_smoothing(3)

    if keys[pygame.K_e]:
        map_gen.generate_map(tile_size, map_fill_percentage, map_seed)
        map_gen.map_smoothing(3)

    if keys[pygame.K_f]:
        map_gen.map_smoothing()

    if pygame.mouse.get_pressed()[0]:
        screen_cubes.append(
            (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    if pygame.mouse.get_pressed()[1]:
        screen_cubes.clear()

    pygame.display.update()
pygame.quit()
