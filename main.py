import pygame

import Game
import Shapes

if __name__ == "__main__":
    pygame.init()
    game = Game.Game()

    shapes = Shapes.Shapes(game.screen, game)
    shape = shapes.add_shapes()

    game.start_game()