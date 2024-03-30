from typing import Tuple, List, Dict
from collections import deque

import Box2D
import numpy as np

from src.constants import *
from src.shapes import Kittin


class WorldManager:
    def __init__(self):
        self.__world = Box2D.b2World(gravity=(0, -10), doSleep=True)
        self.__body_colors_dict = {}
        self.__body_past_velocities = {}
        self.__setup_walls()

    def __create_wall(self, position: Tuple[int, int], width: int, height: int):
        """
        Create a wall (box) in the world. Walls are static bodies.
        :param position:
        :param width:
        :param height:
        :return:
        """
        body = self.__world.CreateStaticBody(
            position=position,
            shapes=Box2D.b2PolygonShape(box=(width / 2, height / 2)),
        )
        self.__body_colors_dict[body] = COLORS['GRAY']

    def __setup_walls(self):
        """
        Create the walls of the world so that the kittins don't fall off.
        :return:
        """
        # Add bottom wall
        self.__create_wall((SCREEN_WIDTH / PPM / 2, 0), SCREEN_WIDTH / PPM, WALL_THICKNESS)
        # Add left wall
        self.__create_wall((0, SCREEN_HEIGHT / PPM / 2), WALL_THICKNESS, SCREEN_HEIGHT / PPM)
        # Add right wall
        self.__create_wall((SCREEN_WIDTH / PPM, SCREEN_HEIGHT / PPM / 2), WALL_THICKNESS, SCREEN_HEIGHT / PPM)

    def get_world_bodies(self) -> List[Box2D.b2Body]:
        """
        Get all the bodies in the world.
        :return: List[Box2D.b2Body]
        """
        return self.__world.bodies

    def get_drawable_objects(self) -> List[Tuple[List[Tuple[int, int]], Tuple[int, int, int, int]]]:
        """
        Get all the objects that can be drawn on the screen.
        :return: List of (vertex array, color) tuples
        """
        objects = []
        for body in self.get_world_bodies():
            for fixture in body.fixtures:
                shape = fixture.shape
                vertices = [(body.transform * v) * PPM for v in shape.vertices]
                vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
                color = self.get_body_color(body)
                objects.append((vertices, color))
        return objects

    def step_physics_time(self, time_multiplier=TIME_MULTIPLIER):
        """
        Take one step in time in the world.
        :return:
        """
        self.__world.Step(TIME_STEP * time_multiplier, VELOCITY_ITERATIONS, POSITION_ITERATIONS)

    def add_kittin_to_world(self, position: Tuple[int, int], kittin: Kittin) -> Box2D.b2Body:
        """
        Add a kittin to the world using its position, vertices, angle and color.
        :param position:
        :param kittin:
        :return: Box2D.b2Body
        """
        body = self.__world.CreateDynamicBody(position=position)
        for vert in kittin.vertices:
            shape = Box2D.b2PolygonShape(vertices=vert)
            body.CreateFixture(shape=shape, density=KITTIN_DENSITY, friction=KITTIN_FRICTION)
        body.angle = kittin.angle
        self.__body_colors_dict[body] = COLORS[kittin.color]
        return body

    def remove_all_dynamic_shapes_from_world(self):
        """
        Remove all the dynamic shapes from the world. This will not clear the walls.
        :return:
        """
        for body in self.get_world_bodies():
            if body.type == Box2D.b2_dynamicBody:
                self.__body_colors_dict.pop(body)
                self.__world.DestroyBody(body)

    def remove_body(self, body: Box2D.b2Body):
        """
        Remove a body from the world.
        :param body:
        :return:
        """
        self.__body_colors_dict.pop(body)
        self.__world.DestroyBody(body)

    def get_body_velocities(self) -> Dict[Box2D.b2Body, Tuple[float, float]]:
        """
        Get the velocities of all the dynamic bodies in the world.
        :return: Dict[Box2D.b2Body, Tuple[float, float]]
        """
        return {body: body.linearVelocity for body in self.__world.bodies if body.type == Box2D.b2_dynamicBody}

    def get_body_angles(self) -> Dict[Box2D.b2Body, float]:
        """
        Get the angles of all the dynamic bodies in the world.
        :return: Dict[Box2D.b2Body, float]
        """
        return {body: body.angle for body in self.__world.bodies if body.type == Box2D.b2_dynamicBody}

    def get_body_color(self, body: Box2D.b2Body) -> Tuple[int, int, int, int]:
        """
        Get the color of a body.
        :param body:
        :return: List[int]
        """
        return self.__body_colors_dict[body]

    def angle_changed(self, old_angles, new_angles):
        """
        Check if any angles have changed between the two angle arrays
        :param old_angles:
        :param new_angles:
        :return:
        """
        return [body for body in old_angles if old_angles[body] != new_angles[body]]

    def all_bodies_are_stationary(self) -> bool:
        """
        Check if all the bodies in the world are stationary.
        :return: bool
        """
        body_velocity_dict = self.get_body_velocities()
        # add these velocities to the body_past_velocities in order to keep the last 5 velocities
        for body in body_velocity_dict:
            if body not in self.__body_past_velocities:
                self.__body_past_velocities[body] = deque(maxlen=10)
            x, y = body_velocity_dict[body]
            self.__body_past_velocities[body].append((x, y))
        for body in body_velocity_dict:
            # check if all the past 5 velocities are less than epsilon
            if not all([np.linalg.norm(velocity) < VELOCITY_EPSILON for velocity in self.__body_past_velocities[body]]):
                return False
        return True

    def remove_unaligned_bodies(self):  # TODO: type this
        body_velocity_dict = self.get_body_velocities()
        # add these velocities to the body_past_velocities in order to keep the last 5 velocities
        for body in body_velocity_dict:
            if body not in self.__body_past_velocities:
                self.__body_past_velocities[body] = deque(maxlen=10)
            x, y = body_velocity_dict[body]
            self.__body_past_velocities[body].append((x, y))

        # check for any bodies that are not moving
        for body in body_velocity_dict:
            # check if all the past 5 velocities are less than epsilon
            if all([np.linalg.norm(velocity) < VELOCITY_EPSILON for velocity in self.__body_past_velocities[body]]):
                if (abs((np.degrees(body.angle)) + DEGREE_EPSILON) % 90) > 2 * DEGREE_EPSILON:
                    print("Body deleted")
                    print(np.degrees(body.angle))
                    print(abs((np.degrees(body.angle)) + DEGREE_EPSILON) % 90)
                    self.remove_body(body)

    def get_num_dynamic_shapes(self) -> int:
        """
        Get the number of dynamic shapes in the world.
        :return: int
        """
        return len([body for body in self.get_world_bodies() if body.type == Box2D.b2_dynamicBody])
