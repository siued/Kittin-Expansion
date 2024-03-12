import pygame
from pygame.locals import *
from Box2D import *

# Define some constants for colors and dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BOX_SIZE = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Box2D Game')

# Create the Box2D world
world = b2World(gravity=(0, 10))

# Define a ground body
ground_body = world.CreateStaticBody(position=(50, 59), shapes=b2EdgeShape(vertices=[(-50, 0), (50, 0)]))

# Create a dynamic body (box)
box_body = world.CreateDynamicBody(position=(10, 10), fixedRotation=True)
box_shape = box_body.CreatePolygonFixture(box=(BOX_SIZE/2, BOX_SIZE/2), density=1, friction=0.3)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(WHITE)

    # Simulate the physics world
    world.Step(1/600, 6, 2)

    # Draw the ground
    for fixture in ground_body.fixtures:
        shape = fixture.shape
        vertices = [(ground_body.transform * v) * 10 for v in shape.vertices]
        pygame.draw.lines(screen, BLACK, True, vertices)

    # Draw the box
    box_position = box_body.position
    box_angle = box_body.angle
    box_vertices = [(box_position + b2Mul(box_body.transform, v)) * 10 for v in box_shape.shape.vertices]
    pygame.draw.polygon(screen, RED, box_vertices)

    pygame.display.flip()

pygame.quit()

