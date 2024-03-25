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
