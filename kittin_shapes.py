from typing import Tuple, List

import numpy as np
from vertices import *

num_kittin_shapes = 6
orientations = 4

scaling_factor = 0.33


def get_random_kittin_shape() -> Tuple[List[List[Tuple[float, float]]], float, str]:
    # angle in radians
    angle = np.pi * np.random.choice([0, 0.5, 1.0, 1.5])
    index = np.random.randint(num_kittin_shapes)
    color, vertices = get_kittin_shape(index)

    vertices = [[(x * 0.3, y * 0.3) for (x, y) in sub_array] for sub_array in vertices]


    # enable this once it works
    # if np.random.rand() < 0.5:
    #     vertices = flip_shape(vertices)

    return vertices, angle, color


# TODO check that this works!
def flip_shape(vertices):
    return np.flip(vertices, 1)


def get_kittin_shape(idx):
    func, color = kittin_funcs[idx]
    return color, func()

kittin_funcs = [(get_red, 'RED'), (get_yellow, 'YELLOW'), (get_green, 'GREEN'), (get_blue, 'BLUE'), (get_pink, 'PINK'), (get_orange, 'ORANGE')]