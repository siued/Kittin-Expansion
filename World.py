import math
from typing import List, Tuple

import pygame
import Box2D
from Box2D import b2_staticBody, b2_dynamicBody
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Constants
PPM = 30.0  # pixels per meter
# increase target fps to make time run faster
TARGET_FPS = 300
# if this is 1 / target_fps, game runs at normal speed
TIME_STEP = 1.0 / 60
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
EPSILON = 0.0001
COLORS = {
    b2_staticBody: (70, 70, 70, 255),
    b2_dynamicBody: (127, 127, 127, 255),
}


class World:
    screen = None
    clock = None
    world = None

    _instance = None

    # Singleton pattern
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()
        self.setup_world()

    def setup_world(self):
        # Pygame setup
        pygame.display.set_caption('Kittin Expansion 3000')

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

    def button_dims(self):
        button_width = 100
        button_height = 50
        button_x = (SCREEN_WIDTH - button_width) // 2
        button_y = (SCREEN_HEIGHT - button_height) // 2
        return button_x, button_y, button_width, button_height

    def draw_button(self):
        button_x, button_y, button_width, button_height = self.button_dims()

        pygame.draw.rect(self.screen, (130, 130, 130, 255), (button_x, button_y, button_width, button_height))

        # Add text to the button
        font = pygame.font.Font(None, 36)
        text = font.render("Button", True, (0, 0, 0, 255))
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        self.screen.blit(text, text_rect)

    def start_game(self, func=lambda: None):

        running = True
        while running:
            func()

            button_x, button_y, button_width, button_height = self.button_dims()

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                        print("Button clicked!")

            self.screen.fill((0, 0, 0, 255))

            self.draw_button()

            # Draw the world
            for body in self.world.bodies:
                for fixture in body.fixtures:
                    shape = fixture.shape
                    vertices = [(body.transform * v) * PPM for v in shape.vertices]
                    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
                    pygame.draw.polygon(self.screen, COLORS[body.type], vertices)

            # Make Box2D simulate the physics of our world for one step.
            self.world.Step(TIME_STEP, 10, 10)

            # Flip the screen and try to keep at the target FPS
            pygame.display.flip()
            self.clock.tick(TARGET_FPS)

        pygame.quit()

    def add_shape(self, vertices: List[List[Tuple[float, float]]], x, y, angle: float = 0.0):
        body = self.world.CreateDynamicBody(position=(x, y))
        for vert in vertices:
            shape = Box2D.b2PolygonShape(vertices=vert)
            body.CreateFixture(shape=shape, density=1, friction=0.3)
        body.angle = math.radians(angle)
        return body
