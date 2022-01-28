import pygame
import numpy as np
import math
import time


class Monster:
    def __init__(self, health, damage, monster_speed):
        self.health = health
        self.damage = damage
        self.monster_speed = monster_speed
