from Box2D import b2PolygonShape
import Vertices
import math

from Game import Game
from kittin_shapes import get_random_kittin_shape


# this probably shouldn't be a class
class Shapes:
    def __init__(self, screen, world):
        self.screen = screen
        self.world = world

    def add_shapes(self):
        self.world.add_shape_to_world(Vertices.get_l_shape(), 10, 0, 46)
        self.world.add_shape_to_world(Vertices.get_l_shape(), 15, 15, 46)
        for i in range(4):
            vertices, angle = get_random_kittin_shape()
            self.world.add_shape_to_world(vertices, 11, 20 + 2 * i, angle)
        # self.add_l_shape(11, 30)
        pass

