from typing import Tuple, List

import numpy as np
import pygame

from src.constants import *
from src.shapes import Kittin


class ScreenManager:
    """
    This class manages the screen and the objects on it.
    """
    __screen: pygame.Surface
    __icons: Dict[str, pygame.Surface] = {}

    def __init__(self):
        """
        Initialize the screen manager.
        Use constants from constants.py to set the screen size and color depth.
        """
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), depth=BIT_COLOR_DEPTH)
        self.load_icons()

    def load_icons(self):
        """
        Load icons for the screen.
        :return:
        """
        for color in KITTIN_COLORS:
            icon = pygame.image.load(f'resources/{color}.png')
            icon_size = icon.get_size()
            icon = pygame.transform.scale(icon, (icon_size[0] // 25, icon_size[1] // 25))
            self.__icons[color] = icon

    def draw_kittins(self, kittins: List[Kittin], positions: [Tuple[float, float]]):
        """
        Draw objects on the screen.
        :param objects: List of (vertex array, color) tuples
        :return:
        """
        for (kittin, position) in zip(kittins, positions):
            self.draw_shape_on_screen(COLORS[kittin.color], kittin.vertices)
            self.draw_icon_on_screen(position, kittin.angle, kittin.color)

    def draw_walls(self, walls):
        """
        Draw walls on the screen.
        :param walls: list of lists of wall vertices
        :return:
        """
        for vertices, color in walls:
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

    def draw_icon_on_screen(self, center: tuple[float, float], angle: float, color: str):
        """
        Draw an icon on the screen.
        :param center: center of the icon
        :param angle: angle of the icon
        :param color: color of the kittin, user to retrieve correct icon
        :return:
        """
        icon = self.__icons[color]
        rotated_icon = pygame.transform.rotate(icon, -angle * 180 / np.pi)
        icon_rect = rotated_icon.get_rect(center=center)
        self.__screen.blit(rotated_icon, icon_rect)
