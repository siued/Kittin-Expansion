import math
from typing import List, Tuple

import pygame
import Box2D

from button import Button
from constants import *
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


class Game:
    screen = None
    clock = None
    world = None
    button = Button()
    running = True

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            self = cls._instance
            self.setup_world()
        return cls._instance

    def setup_world(self):
        # Pygame setup
        pygame.display.set_caption('Kittin Expansion 3000')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        # Box2D world setup
        self.world = Box2D.b2World(gravity=(0, -10), doSleep=True)

        # And a static body to hold the ground shape
        self.world.CreateStaticBody(
            position=(0, 0),
            shapes=Box2D.b2PolygonShape(box=(50, 1)),
        )

        self.world.CreateStaticBody(
            position=(0, 0),
            shapes=Box2D.b2PolygonShape(box=(1, 50)),
        )

        self.world.CreateStaticBody(
            position=(SCREEN_WIDTH / PPM, 0),
            shapes=Box2D.b2PolygonShape(box=(1, 50)),
        )

        # for coordinate-checking purposes, position is the center of the shape btw
        # self.world.CreateStaticBody(
        #     position=(2, 2),
        #     shapes=Box2D.b2PolygonShape(box=(0.5, 0.5)),
        # )

    def start_game(self):
        while self.running:

            self.handle_events()

            self.screen.fill((0, 0, 0, 255))

            self.button.draw_button(self.screen)

            # Draw the world
            for body in self.world.bodies:
                for fixture in body.fixtures:
                    shape = fixture.shape
                    vertices = [(body.transform * v) * PPM for v in shape.vertices]
                    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
                    pygame.draw.polygon(self.screen, COLORS[body.type], vertices)

            # Make Box2D simulate the physics for one step.
            self.world.Step(TIME_STEP, 10, 10)

            # Flip the screen and try to keep at the target FPS
            pygame.display.flip()
            self.clock.tick(TARGET_FPS)

        pygame.quit()

    def stop_game(self):
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.stop_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_x, button_y, button_width, button_height = self.button.get_dims()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    print("Button clicked!")

    def add_shape_to_world(self, vertices: List[List[Tuple[float, float]]], x, y, angle: float = 0.0):
        body = self.world.CreateDynamicBody(position=(x, y))
        for vert in vertices:
            shape = Box2D.b2PolygonShape(vertices=vert)
            body.CreateFixture(shape=shape, density=1, friction=0.3)
        body.angle = math.radians(angle)
        return body
