import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from button import Button
from constants import *
from shapes import ShapeGenerator
from world import WorldManager


class Game:
    shapes = None
    button = Button()
    running = True
    shape_generator = ShapeGenerator()
    world_manager = WorldManager()

    draw_colors = {}

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize_game()
        return cls._instance

    def initialize_game(self):
        pygame.display.set_caption(GAME_TITLE)

    def start_game(self):
        old_angles = self.world_manager.get_body_angles()
        while self.running:
            new_angles = self.world_manager.get_body_angles()
            if self.angle_changed(old_angles, new_angles):
                print("Alive")
            self.tick_game()
            old_angles = new_angles

        pygame.quit()

    def tick_game(self):
        self.handle_events()

        self.world_manager.set_screen_background(COLORS['BLACK'])

        self.world_manager.draw_button_on_screen(self.button)

        # Draw the world
        for body in self.world_manager.get_world_bodies():
            for fixture in body.fixtures:
                shape = fixture.shape
                vertices = [(body.transform * v) * PPM for v in shape.vertices]
                vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
                color = self.world_manager.get_body_color(body)
                self.world_manager.draw_shape_on_screen(color, vertices)

        self.world_manager.step_time()
        self.world_manager.refresh_screen()

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

    def button_pressed(self):
        self.world_manager.remove_all_dynamic_shapes_from_world()
        self.world_manager.add_kittin_to_world(KITTIN_SPAWN_POSITION, self.shape_generator.get_random_kittin_shape())

    def angle_changed(self, old_angles, new_angles):
        return [body for body in old_angles if old_angles[body] != new_angles[body]]
