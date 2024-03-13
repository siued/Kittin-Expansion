import World
import Shapes

if __name__ == "__main__":
    world = World.World()
    world.setup_world()

    shapes = Shapes.Shapes(world.screen, world.world)
    shapes.add_shapes()

    world.start_game()
