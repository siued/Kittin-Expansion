from typing import Tuple, List


class Kittin:
    """
    A class to represent a kittin shape.

    Attributes
    ----------
    vertices : List[List[Tuple[float, float]]]
        A list of lists of tuples representing the vertices of the shape.
    angle : float
        The angle of the shape in radians.
    color : str
        The color of the shape.
    """
    vertices: List[List[Tuple[float, float]]]
    center: Tuple[float, float]
    angle: float
    color: str

    def __init__(self, vertices, angle, color):
        self.vertices = vertices
        self.angle = angle
        self.color = color

    def scale_shape(self, scaling_factor) -> 'Kittin':
        """
        Scales the shape by a given scaling factor.
        :param scaling_factor:
        :return: Kittin
        """
        self.vertices = [
            [
                (x * scaling_factor, y * scaling_factor) for (x, y) in sub_array
            ] for sub_array in self.vertices
        ]
        return self

    def flip_shape(self) -> 'Kittin':
        """
        Flips the shape by negating the y-coordinate of each vertex.
        :return: Kittin
        """
        self.vertices = [
            [
                (x, -y) for (x, y) in sub_array
            ] for sub_array in self.vertices
        ]
        return self
