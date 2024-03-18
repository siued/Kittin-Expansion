from typing import Tuple, List

import numpy as np

num_kittin_shapes = 6
orientations = 4


def get_random_kittin_shape() -> Tuple[List[List[Tuple[float, float]]], float]:
    # angle in radians
    angle = np.random.choice([0, 0.5, 1.0, 1.5])
    index = np.random.randint(num_kittin_shapes)
    # for testing with 1 shape only
    index = 0
    vertices = get_kittin_shape(index)

    # enable this once it works
    # if np.random.rand() < 0.5:
    #     vertices = flip_shape(vertices)

    return vertices, angle


# TODO check that this works!
def flip_shape(vertices):
    return np.flip(vertices, 1)


def get_kittin_shape(idx):
    return kittin_funcs[idx]()


def get_kittin_shape_0():
    # l-shape for now
    return [
        [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)],
        [(1, 0), (1, 1), (2, 1), (2, 0)]
    ]


def get_kittin_shape_1():
    pass


def get_kittin_shape_2():
    pass


def get_kittin_shape_3():
    pass


def get_kittin_shape_4():
    pass


def get_kittin_shape_5():
    pass


kittin_funcs = [get_kittin_shape_0, get_kittin_shape_1, get_kittin_shape_2, get_kittin_shape_3, get_kittin_shape_4, get_kittin_shape_5]