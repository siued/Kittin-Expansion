from Box2D import b2PolygonShape
import Vertices
import math

from World import World
from kittin_shapes import get_random_kittin_shape


# this probably shouldn't be a class
class Shapes:
    def __init__(self, screen, world):
        self.screen = screen
        self.world = world

    # def add_l_shape(self, pos_x, pos_y, orientation=0):
    #     l_body = self.world.CreateDynamicBody(position=(pos_x, pos_y))
    #
    #     verts = Vertices.get_l_shape()
    #     for vert in verts:
    #         l_shape = b2PolygonShape(vertices=vert)
    #         l_body.CreateFixture(shape=l_shape, density=1, friction=0.3)
    #     l_body.angle = math.radians(46)

    def add_shapes(self):
        self.world.add_shape(Vertices.get_l_shape(), 10, 0, 46)
        self.world.add_shape(Vertices.get_l_shape(), 15, 15, 46)
        for i in range(4):
            vertices, angle = get_random_kittin_shape()
            self.world.add_shape(vertices, 11, 20 + 2*i, angle)
        # self.add_l_shape(11, 30)
        pass

