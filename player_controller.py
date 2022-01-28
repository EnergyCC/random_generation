import pygame
import time


class Player:

    def __init__(self, health, movement_speed, damage, x, y, size_x, size_y):
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def player_body(self, windows):
        self.windows = windows
        pygame.draw.rect(self.windows, (150, 0, 0, 0.5), pygame.Rect(
            self.x, self.y, self.size_x, self.size_y))

    def get_player_pos(self):
        return round(self.x / 25), round(self.y / 25)

    def move_to(self):
        if pygame.mouse.get_pressed()[2]:
            if self.x <= pygame.mouse.get_pos()[0]:
                while self.x <= pygame.mouse.get_pos()[0]:
                    self.x += 1
            if self.x >= pygame.mouse.get_pos()[0]:
                while self.x >= pygame.mouse.get_pos()[0]:
                    self.x -= 1
            if self.y <= pygame.mouse.get_pos()[1]:
                while self.y <= pygame.mouse.get_pos()[1]:
                    self.y += 1
            if self.y >= pygame.mouse.get_pos()[1]:
                while self.y >= pygame.mouse.get_pos()[1]:
                    self.y -= 1

    def player_movement(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.x > 0:
                self.x -= self.movement_speed
        if keys[pygame.K_d]:
            if self.x < game_width - self.size_x:
                self.x += self.movement_speed
        if keys[pygame.K_w]:
            if self.y > 0:
                self.y -= self.movement_speed
        if keys[pygame.K_s]:
            if self.y < game_height - self.size_y:
                self.y += self.movement_speed
