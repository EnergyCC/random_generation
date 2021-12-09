import pygame
import random
import time


class Map():

    def __init__(self, game_window, game_width, game_height):
        self.game_window = game_window
        self.game_width = game_width
        self.game_height = game_height

    def generate_map(self, tile_size, map_fill_percentage=40, seed=None):
        self.map_fill_percentage = map_fill_percentage
        self.seed = seed
        self.tile_size = tile_size
        if self.seed == None:
            self.seed = time.time()
        random.seed(self.seed)
        self.map = [[random.randrange(0, 100) for i in range(
            0, self.game_width, self.tile_size)] for j in range(0, self.game_height, self.tile_size)]

        for index_y in range(len(self.map)):
            for index_x in range(len(self.map[0])):
                if index_y == 0 or index_y == len(self.map) - 1 or index_x == 0 or index_x == len(self.map[0]) - 1:
                    self.map[index_y][index_x] = 1
                elif self.map[index_y][index_x] <= self.map_fill_percentage:
                    self.map[index_y][index_x] = 1
                elif self.map[index_y][index_x] >= self.map_fill_percentage:
                    self.map[index_y][index_x] = 0
                # smoothing

    def map_smoothing(self, iterations=1):
        self.iterations = iterations
        for index in range(self.iterations):
            wall_count = 0

            # up -> down, left -> right
            for index_y in range(round(len(self.map) / 2) + 1):
                for index_x in range(round(len(self.map[0]) / 2) + 1):
                    if index_x > 0 and index_y > 0:
                        wall_count = self.map[index_y - 1][index_x - 1] + self.map[index_y - 1][index_x] + self.map[index_y - 1][index_x + 1] + self.map[index_y][index_x -
                                                                                                                                                                  1] + self.map[index_y][index_x + 1] + self.map[index_y + 1][index_x - 1] + self.map[index_y + 1][index_x] + self.map[index_y + 1][index_x + 1]
                        if wall_count > 5:
                            self.map[index_y][index_x] = 1
                        elif wall_count < 4:
                            self.map[index_y][index_x] = 0

            # up -> down, right -> left
            for index_y in range(round(len(self.map) / 2) + 1):
                for index_x in range(len(self.map[0]), round(len(self.map[0]) / 2) - 1, -1):
                    if index_x > 0 and index_x < len(self.map[0]) - 1 and index_y > 0:
                        wall_count = self.map[index_y - 1][index_x - 1] + self.map[index_y - 1][index_x] + self.map[index_y - 1][index_x + 1] + self.map[index_y][index_x -
                                                                                                                                                                  1] + self.map[index_y][index_x + 1] + self.map[index_y + 1][index_x - 1] + self.map[index_y + 1][index_x] + self.map[index_y + 1][index_x + 1]
                        if wall_count > 5:
                            self.map[index_y][index_x] = 1
                        elif wall_count < 4:
                            self.map[index_y][index_x] = 0

            # bottom -> up, left -> right

            for index_y in range(len(self.map), round(len(self.map) / 2) - 1, -1):
                for index_x in range(round(len(self.map[0]) / 2) + 1):
                    if index_x > 0 and index_x < len(self.map[0]) - 1 and index_y > 0 and index_y < len(self.map) - 1:
                        wall_count = self.map[index_y - 1][index_x - 1] + self.map[index_y - 1][index_x] + self.map[index_y - 1][index_x + 1] + self.map[index_y][index_x -
                                                                                                                                                                  1] + self.map[index_y][index_x + 1] + self.map[index_y + 1][index_x - 1] + self.map[index_y + 1][index_x] + self.map[index_y + 1][index_x + 1]
                        if wall_count > 5:
                            self.map[index_y][index_x] = 1
                        elif wall_count < 4:
                            self.map[index_y][index_x] = 0

            # bottom -> up, right -> left

            for index_y in range(len(self.map), round(len(self.map) / 2) - 1, -1):
                for index_x in range(len(self.map[0]), round(len(self.map[0]) / 2) - 1, -1):
                    print(index_x, len(self.map[0]))
                    if index_x > 0 and index_x < len(self.map[0]) - 1 and index_y > 0 and index_y < len(self.map) - 1:
                        wall_count = self.map[index_y - 1][index_x - 1] + self.map[index_y - 1][index_x] + self.map[index_y - 1][index_x + 1] + self.map[index_y][index_x -
                                                                                                                                                                  1] + self.map[index_y][index_x + 1] + self.map[index_y + 1][index_x - 1] + self.map[index_y + 1][index_x] + self.map[index_y + 1][index_x + 1]
                        if wall_count > 5:
                            self.map[index_y][index_x] = 1
                        elif wall_count < 4:
                            self.map[index_y][index_x] = 0

    def draw_tiles(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        pygame.draw.rect(self.game_window, (140, 80, 10), pygame.Rect(
            self.pos_x, self.pos_y, self.tile_size, self.tile_size))

    def draw_map(self):
        for index_y in range(len(self.map)):
            for index_x in range(len(self.map[0])):
                if self.map[index_y][index_x] == 1:
                    self.draw_tiles(index_x * self.tile_size,
                                    index_y * self.tile_size)
