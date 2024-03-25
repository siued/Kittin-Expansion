from typing import Tuple, List

import pygame

from src.constants import *


class ScreenManager:
    """
    This class manages the screen and the objects on it.
    """
    __screen: pygame.Surface

    def __init__(self):
        """
        Initialize the screen manager.
        Use constants from constants.py to set the screen size and color depth.
        """
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), depth=BIT_COLOR_DEPTH)

    def draw_objects(self, objects: List[Tuple[List[Tuple[int, int]], Tuple[int, int, int, int]]]):
        """
        Draw objects on the screen.
        :param objects: List of (vertex array, color) tuples
        :return:
        """
        for vertices, color in objects:
            self.draw_shape_on_screen(color, vertices)

    def set_screen_background(self, color: Tuple[int, int, int, int]):
        """
        Set the background color of the screen.
        :param color:
        :return:
        """
        self.__screen.fill(color)

    def draw_button(self, button):
        """
        Draw a button on the screen.
        :param button:
        :return:
        """
        pygame.draw.rect(self.__screen, COLORS[button.color], button.get_dims())

        # Add text to the button
        font = pygame.font.Font(None, button.font_size)
        text = font.render(button.text, True, COLORS['BLACK'])
        text_rect = text.get_rect(center=(button.x + button.width // 2, button.y + button.height // 2))
        self.__screen.blit(text, text_rect)

    def draw_shape_on_screen(self, color: Tuple[int, int, int, int], vertices: List[Tuple[float, float]]):
        """
        Draw a shape on the screen.
        :param color:
        :param vertices:
        :return:
        """
        pygame.draw.polygon(self.__screen, color, vertices)

    def refresh_screen(self):
        """
        Refresh the screen. The flip() function is called to update the contents displayed on the screen.
        :return:
        """
        pygame.display.flip()