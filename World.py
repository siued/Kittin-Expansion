import pygame
import Box2D
from Box2D import (b2_staticBody, b2_dynamicBody)
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)

# Constants
PPM = 30.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
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

        # Main game loop

    def start_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False

            self.screen.fill((0, 0, 0, 255))

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
