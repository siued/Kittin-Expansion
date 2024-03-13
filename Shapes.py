import pygame
import Box2D
from Box2D import (b2World, b2PolygonShape, b2CircleShape, b2_staticBody, b2_dynamicBody)
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)


class Shapes:
    screen = None
    world = None

    def __init__(self, screen, world):
        self.screen = screen
        self.world = world

    def add_shapes(self):
        # Create L-shaped body
        l_body = self.world.CreateDynamicBody(position=(10, 20))

        # Create two polygon fixtures for the L shape
        l_shape1 = b2PolygonShape(vertices=[(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)])
        l_shape2 = b2PolygonShape(vertices=[(1, 0), (1, 1), (2, 1), (2, 0)])

        l_body.CreateFixture(shape=l_shape1, density=1, friction=0.3)
        l_body.CreateFixture(shape=l_shape2, density=1, friction=0.3)

        # Create L-shaped body
        l_body2 = self.world.CreateDynamicBody(position=(11, 30))

        l_body2.CreateFixture(shape=l_shape1, density=1, friction=0.3)
        l_body2.CreateFixture(shape=l_shape2, density=1, friction=0.3)
