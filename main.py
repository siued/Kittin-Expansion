import numpy as np
import pygame

import World
import Shapes

if __name__ == "__main__":
    pygame.init()
    world = World.World()

    shapes = Shapes.Shapes(world.screen, world)
    shape = shapes.add_shapes()

    world.start_game()