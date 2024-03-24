import pygame
import Box2D

from button import Button
from src.shapes import Kittin
from src.shapes import ShapeGenerator
from constants import *
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


class Game:
    screen = None
    clock = None
    world = None
    shapes = None
    button = Button()
    running = True
    shape_generator = ShapeGenerator()

    draw_colors = {}

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            self = cls._instance
            self.setup_world()
        return cls._instance

    def setup_world(self):
        # Pygame setup
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        # Box2D world setup
        self.world = Box2D.b2World(gravity=(0, -10), doSleep=True)

        def create_wall(x, y, width, height):
            body = self.world.CreateStaticBody(
                position=(x, y),
                shapes=Box2D.b2PolygonShape(box=(width, height)),
            )
            self.draw_colors[body] = COLORS['GRAY']

        create_wall(0, 0, 50, 1)
        create_wall(0, 0, 1, 50)
        create_wall(SCREEN_WIDTH / PPM, 0, 1, 50)

        # for coordinate-checking purposes, position is the center of the shape btw
        # self.world.CreateStaticBody(
        #     position=(2, 2),
        #     shapes=Box2D.b2PolygonShape(box=(0.5, 0.5)),
        # )

    def start_game(self):
        old_angles = self.get_body_angles()
        while self.running:
            new_angles = self.get_body_angles()
            if self.angle_changed(old_angles, new_angles):
                print("Alive")
            self.tick_game()
            old_angles = new_angles

        pygame.quit()

    def tick_game(self):
        self.handle_events()

        self.screen.fill((0, 0, 0, 255))

        self.button.draw_button(self.screen)

        # Draw the world
        for body in self.world.bodies:
            for fixture in body.fixtures:
                shape = fixture.shape
                vertices = [(body.transform * v) * PPM for v in shape.vertices]
                vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
                pygame.draw.polygon(self.screen, self.draw_colors[body], vertices)

        # Make Box2D simulate the physics for one step.
        self.world.Step(TIME_STEP, 10, 10)

        # Flip the screen and try to keep at the target FPS
        pygame.display.flip()
        self.clock.tick(TARGET_FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.stop_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_x, button_y, button_width, button_height = self.button.get_dims()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    self.button_pressed()

    def stop_game(self):
        self.running = False

    def add_shape_to_world(self, kittin: Kittin):
        body = self.world.CreateDynamicBody(position=(10, 20))
        for vert in kittin.vertices:
            shape = Box2D.b2PolygonShape(vertices=vert)
            body.CreateFixture(shape=shape, density=1, friction=0.3)
        body.angle = kittin.angle
        self.draw_colors[body] = COLORS[kittin.color]
        return body
    
    def button_pressed(self):
        # self.remove_all_shapes()
        self.add_shape_to_world(self.shape_generator.get_random_kittin_shape())
    
    def remove_all_shapes(self):
        for body in self.world.bodies:
            if body.type == Box2D.b2_dynamicBody:
                self.draw_colors.pop(body)
                self.world.DestroyBody(body)
        
    def get_body_angles(self):
        return {body: body.angle for body in self.world.bodies if body.type == Box2D.b2_dynamicBody}

    def angle_changed(self, old_angles, new_angles):
        return [body for body in old_angles if old_angles[body] != new_angles[body]]
