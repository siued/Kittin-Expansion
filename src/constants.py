PPM = 30.0  # pixels per meter

# increase target fps to make time run faster
TARGET_FPS = 300

# if this is 1 / target_fps, game runs at normal speed
TIME_STEP = 1.0 / 60

COLORS = {
    'GRAY': (70, 70, 70, 255),
    'BLACK': (0, 0, 0, 255),
    'YELLOW': (255, 216, 43, 255),
    'RED': (170, 51, 44, 255),
    'PINK': (255, 110, 162, 255),
    'GREEN': (20, 212, 184, 255),
    'BLUE': (26, 140, 232, 255),
    'ORANGE': (242, 117, 48, 255)
}

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640

WALL_THICKNESS = 1

BIT_COLOR_DEPTH = 32

POSITION_ITERATIONS = 10
"""
This controls how accurately the physics engine calculates the positions of objects after collisions or other physical
interactions. Higher values will make the physics engine more accurate, but will also make the game run slower.
"""

VELOCITY_ITERATIONS = 10
"""
This controls how accurately the physics engine calculates the velocities of objects after collisions or other physical
interactions. Higher values will make the physics engine more accurate, but will also make the game run slower.
"""

GAME_TITLE = 'Kittin Expansion 9000'

KITTIN_FRICTION = 0.3

KITTIN_DENSITY = 1

KITTIN_SCALING_FACTOR = 0.33

KITTIN_SPAWN_POSITION = (10, 20)
