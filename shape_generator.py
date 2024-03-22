from kittin_shapes import get_random_kittin_shape


class ShapeGenerator:
    def __init__(self, world):
        self.world = world

    def get_shapes(self):
        vertices, angle, color = get_random_kittin_shape()
        return vertices, 10, 20, angle, color

