import pygame
from constants import COLORS


class Button:
    width: int
    height: int
    x: int
    y: int
    font_size: int
    color: str
    text: str

    def __init__(self, x=50, y=50, width=100, height=50, font_size=36, color='GRAY', text="Button"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.color = color
        self.text = text

    def get_dims(self):
        return self.x, self.y, self.width, self.height

    def draw_button(self, screen):
        button_x, button_y, button_width, button_height = self.get_dims()

        pygame.draw.rect(screen, COLORS[self.color], (button_x, button_y, button_width, button_height))

        # Add text to the button
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, True, COLORS['BLACK'])
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)
