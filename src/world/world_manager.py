import Box2D
import pygame

from src.constants import *
from src.shapes import Kittin


class WorldManager:
    def __init__(self):
        self.__world = Box2D.b2World(gravity=(0, -10), doSleep=True)
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), depth=BIT_COLOR_DEPTH)
        self.__clock = pygame.time.Clock()
        self.__body_colors_dict = {}
        self.setup_world()

    def __create_wall(self, x, y, width, height):
        body = self.__world.CreateStaticBody(
            position=(x, y),
            shapes=Box2D.b2PolygonShape(box=(width/2, height/2)),
        )
        self.__body_colors_dict[body] = COLORS['GRAY']

    def setup_world(self):
        # Add bottom wall
        self.__create_wall(SCREEN_WIDTH / PPM / 2, 0, SCREEN_WIDTH / PPM, WALL_THICKNESS)
        # Add left wall
        self.__create_wall(0, SCREEN_HEIGHT / PPM / 2, WALL_THICKNESS, SCREEN_HEIGHT / PPM)
        # Add right wall
        self.__create_wall(SCREEN_WIDTH / PPM, SCREEN_HEIGHT / PPM / 2, WALL_THICKNESS, SCREEN_HEIGHT / PPM)

    def set_screen_background(self, color):
        self.__screen.fill(color)

    def draw_button_on_screen(self, button):
        button.draw_button(self.__screen)

    def get_world_bodies(self):
        return self.__world.bodies

    def draw_shape_on_screen(self, color, vertices):
        pygame.draw.polygon(self.__screen, color, vertices)

    def step_time(self):
        self.__world.Step(TIME_STEP, VELOCITY_ITERATIONS, POSITION_ITERATIONS)

    def refresh_screen(self):
        pygame.display.flip()
        self.__clock.tick(TARGET_FPS)

    def add_kittin_to_world(self, position, kittin: Kittin):
        body = self.__world.CreateDynamicBody(position=position)
        for vert in kittin.vertices:
            shape = Box2D.b2PolygonShape(vertices=vert)
            body.CreateFixture(shape=shape, density=KITTIN_DENSITY, friction=KITTIN_FRICTION)
        body.angle = kittin.angle
        self.__body_colors_dict[body] = COLORS[kittin.color]
        return body

    def remove_all_dynamic_shapes_from_world(self):
        for body in self.get_world_bodies():
            if body.type == Box2D.b2_dynamicBody:
                self.__body_colors_dict.pop(body)
                self.__world.DestroyBody(body)

    def get_body_angles(self):
        return {body: body.angle for body in self.__world.bodies if body.type == Box2D.b2_dynamicBody}

    def get_body_color(self, body):
        return self.__body_colors_dict[body]
