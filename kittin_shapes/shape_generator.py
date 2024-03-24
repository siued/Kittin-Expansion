import numpy as np
from vertices import *
from kittin_shapes.kittin import Kittin


class ShapeGenerator:
    FLIP_CHANCE = 0.5
    ANGLES = [0, 90, 180, 270]
    SCALING_FACTOR = 0.33
    VERTICES_FUNCS = [
        (get_red, 'RED'),
        (get_yellow, 'YELLOW'),
        (get_green, 'GREEN'),
        (get_blue, 'BLUE'),
        (get_pink, 'PINK'),
        (get_orange, 'ORANGE')
    ]

    def get_random_kittin_shape(self) -> Kittin:
        """
        Generates a random kittin shape with a random angle, and color.
        :return: Kittin
        """
        angle = np.random.choice(self.ANGLES)
        angle = np.radians(angle)
        index = np.random.randint(len(self.VERTICES_FUNCS))
        vertices = self.VERTICES_FUNCS[index][0]()
        color = self.VERTICES_FUNCS[index][1]

        kittin = Kittin(vertices, angle, color)
        kittin.scale_shape(self.SCALING_FACTOR)
        if np.random.rand() < self.FLIP_CHANCE:
            kittin.flip_shape()

        return kittin
