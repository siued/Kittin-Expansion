import numpy as np

num_kittin_shapes = 6
orientations = 4


def get_random_kittin_shape():
    return get_kittin_shape(np.random.randint(num_kittin_shapes), np.random.randint(orientations))


def get_kittin_shape(idx, orientation):
    return kittin_funcs[idx](orientation)


def get_kittin_shape_0(orientation):
    pass


def get_kittin_shape_1(orientation):
    pass


def get_kittin_shape_2(orientation):
    pass


def get_kittin_shape_3(orientation):
    pass


def get_kittin_shape_4(orientation):
    pass


def get_kittin_shape_5(orientation):
    pass


kittin_funcs = [get_kittin_shape_0, get_kittin_shape_1, get_kittin_shape_2, get_kittin_shape_3, get_kittin_shape_4, get_kittin_shape_5]