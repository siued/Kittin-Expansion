"""
In short:
One static body:
    + One fixture: big polygon to represent the ground
Two dynamic bodies:
    + One fixture: a polygon
    + One fixture: a circle
And some drawing code that extends the shape classes.
"""
import pygame
import kittin_shapes
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)

import Box2D  # The main library
# Box2D.b2 maps Box2D.b2Vec2 to vec2 (and so on)
from Box2D import (b2World, b2PolygonShape, b2CircleShape, b2_staticBody, b2_dynamicBody)

# --- constants ---
# Box2D deals with meters, but we want to display pixels,
# so define a conversion factor:
PPM = 20.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640

# --- pygame setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Kittin Generator 3000')
clock = pygame.time.Clock()

# --- pybox2d world setup ---
# Create the world
world = b2World(gravity=(0, -10), doSleep=True)

# And a static body to hold the ground shape
ground_body = world.CreateStaticBody(
    position=(0, 0),
    shapes=b2PolygonShape(box=(50, 1)),
)

# Create a couple dynamic bodies
body = world.CreateDynamicBody(position=(20, 45))
circle = body.CreateCircleFixture(radius=0.5, density=1, friction=0.3)

body = world.CreateDynamicBody(position=(10, 45), angle=15)
box = body.CreatePolygonFixture(box=(2, 1), density=1, friction=0.3)

colors = {
    b2_staticBody: (70, 70, 70, 255),
    b2_dynamicBody: (127, 127, 127, 255),
}

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

# Let's play with extending the shape classes to draw for us.


def my_draw_polygon(polygon, body, fixture):
    vertices = [(body.transform * v) * PPM for v in polygon.vertices]
    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
    pygame.draw.polygon(screen, colors[body.type], vertices)
b2PolygonShape.draw = my_draw_polygon


def my_draw_circle(circle, body, fixture):
    position = body.transform * circle.pos * PPM
    position = (position[0], SCREEN_HEIGHT - position[1])
    pygame.draw.circle(screen, colors[body.type], [int(
        x) for x in position], int(circle.radius * PPM))
    # Note: Python 3.x will enforce that pygame get the integers it requests,
    #       and it will not convert from float.
b2CircleShape.draw = my_draw_circle

# --- main game loop ---

running = True
while running:
    # Check the event queue
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # The user closed the window or pressed escape
            running = False

    screen.fill(BLACK)
    # Draw the world
    for body in world.bodies:
        for fixture in body.fixtures:
            fixture.shape.draw(body, fixture)

    # Make Box2D simulate the physics of our world for one step.
    world.Step(TIME_STEP, 10, 10)

    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)

pygame.quit()