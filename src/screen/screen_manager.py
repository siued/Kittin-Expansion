import pygame

from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BIT_COLOR_DEPTH, COLORS


class ScreenManager:
    screen: pygame.Surface = None
    """
    This class manages the screen and the objects on it. 
    """

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), depth=BIT_COLOR_DEPTH)


    def draw_objects(self):
        pass


    def draw_button(self, button):
        """
        Draw a button on the screen.
        :param button:
        :return:
        """
        pygame.draw.rect(self.screen, button.color, button.get_dims())

        # Add text to the button
        font = pygame.font.Font(None, button.font_size)
        text = font.render(button.text, True, COLORS['BLACK'])
        text_rect = text.get_rect(center=(button.x + button.width // 2, button.y + button.height // 2))
        self.screen.blit(text, text_rect)