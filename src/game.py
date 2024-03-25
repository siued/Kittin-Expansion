import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from button import Button
from constants import *
from shapes import ShapeGenerator
from screen import ScreenManager
from world import WorldManager


class Game:
    """
    Singleton instance of the game.
    This contains logic for running the main game loop.
    """
    shapes = None
    button = Button()
    running = True
    shape_generator = ShapeGenerator()
    world_manager = WorldManager()
    screen_manager = ScreenManager()
    __clock = pygame.time.Clock()

    _instance = None

    def __new__(cls):
        """
        Singleton pattern initializer.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize_game()
        return cls._instance

    def initialize_game(self):
        """
        Initialize the game.
        :return:
        """
        pygame.display.set_caption(GAME_TITLE)

    def start_game(self):
        """
        Start the game loop.
        :return:
        """
        while self.running:
            self.tick_game()

        pygame.quit()

    def tick_game(self):
        """
        Perform one step of the game loop.
        :return:
        """
        self.handle_events()

        self.screen_manager.set_screen_background(COLORS['BLACK'])

        self.screen_manager.draw_button(self.button)

        objects = self.world_manager.get_drawable_objects()
        self.screen_manager.draw_objects(objects)

        self.screen_manager.refresh_screen()
        self.step_time()

    def step_time(self):
        """
        Step time forward one unit.
        Both physics time and game time are stepped forward.
        :return:
        """
        self.world_manager.step_physics_time()
        self.__clock.tick(TIME_MULTIPLIER * TARGET_FPS)

    def handle_events(self):
        """
        Handle events in the game loop.
        :return:
        """
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.stop_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_x, button_y, button_width, button_height = self.button.get_dims()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    self.button_pressed()

    def stop_game(self):
        """
        Stop the game loop.
        :return:
        """
        self.running = False

    def button_pressed(self):
        """
        Handle button press.
        :return:
        """
        self.world_manager.remove_all_dynamic_shapes_from_world()
        self.world_manager.add_kittin_to_world(KITTIN_SPAWN_POSITION, self.shape_generator.get_random_kittin_shape())

