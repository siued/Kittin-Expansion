import pygame
import Box2D
from Box2D import (b2World, b2PolygonShape, b2CircleShape, b2_staticBody, b2_dynamicBody)
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)

# Constants
PPM = 30.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640

# Pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('L Shape Body')
clock = pygame.time.Clock()

# Box2D world setup
world = Box2D.b2World(gravity=(0, -10), doSleep=True)

# And a static body to hold the ground shape
world.CreateStaticBody(
    position=(0, 0),
    shapes=Box2D.b2PolygonShape(box=(50, 1)),
)

# Create L-shaped body
l_body = world.CreateDynamicBody(position=(10, 20))

# Create two polygon fixtures for the L shape
l_shape1 = b2PolygonShape(vertices=[(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)])
l_shape2 = b2PolygonShape(vertices=[(1, 0), (1, 1), (2, 1), (2, 0)])

l_body.CreateFixture(shape=l_shape1, density=1, friction=0.3)
l_body.CreateFixture(shape=l_shape2, density=1, friction=0.3)


# Create L-shaped body
l_body2 = world.CreateDynamicBody(position=(11, 30))

l_body2.CreateFixture(shape=l_shape1, density=1, friction=0.3)
l_body2.CreateFixture(shape=l_shape2, density=1, friction=0.3)

# Colors
colors = {
    b2_staticBody: (70, 70, 70, 255),
    b2_dynamicBody: (127, 127, 127, 255),
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    screen.fill((0, 0, 0, 255))

    # Draw the world
    for body in world.bodies:
        for fixture in body.fixtures:
            shape = fixture.shape
            vertices = [(body.transform * v) * PPM for v in shape.vertices]
            vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
            pygame.draw.polygon(screen, colors[body.type], vertices)

    # Make Box2D simulate the physics of our world for one step.
    world.Step(TIME_STEP, 10, 10)

    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)

pygame.quit()
