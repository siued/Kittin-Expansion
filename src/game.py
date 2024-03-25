from collections import deque
from typing import List

import numpy as np
import pygame
from Box2D import Box2D
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from button import Button
from constants import *
from shapes import ShapeGenerator
from screen import ScreenManager
from world import WorldManager


class Game:
    shapes = None
    button = Button()
    running = True
    shape_generator = ShapeGenerator()
    world_manager = WorldManager()
    screen_manager = ScreenManager()
    __clock = pygame.time.Clock()

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
        body_past_velocities = {}
        while self.running:
            body_velocity_dict = self.world_manager.get_body_velocities()
            # add these velocities to the body_past_velocities in order to keep the last 5 velocities
            for body in body_velocity_dict:
                if body not in body_past_velocities:
                    body_past_velocities[body] = deque(maxlen=10)
                x, y = body_velocity_dict[body]
                body_past_velocities[body].append((x, y))

            # check for any bodies that are not moving
            for body in body_velocity_dict:
                # check if all the past 5 velocities are less than epsilon
                if all([np.linalg.norm(velocity) < VELOCITY_EPSILON for velocity in body_past_velocities[body]]):
                    if (abs(np.degrees(body.angle) + DEGREE_EPSILON) % 90) > 2 * DEGREE_EPSILON:
                        print("Body deleted")
                        print(np.degrees(body.angle))
                        print(abs(np.degrees(body.angle) + DEGREE_EPSILON) % 90)
                        self.world_manager.remove_body(body)

            self.tick_game()

        pygame.quit()

    def tick_game(self):
        self.handle_events()

        self.screen_manager.set_screen_background(COLORS['BLACK'])

        self.screen_manager.draw_button(self.button)

        # Draw the world
        objects = self.world_manager.get_drawable_objects()
        self.screen_manager.draw_objects(objects)

        self.screen_manager.refresh_screen()
        self.step_time()

    def step_time(self):
        self.world_manager.step_physics_time()
        self.__clock.tick(TIME_MULTIPLIER * TARGET_FPS)

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
        # self.world_manager.remove_all_dynamic_shapes_from_world()
        self.world_manager.add_kittin_to_world(KITTIN_SPAWN_POSITION, self.shape_generator.get_random_kittin_shape())

    def angle_changed(self, old_angles, new_angles):
        return [body for body in old_angles if old_angles[body] != new_angles[body]]
