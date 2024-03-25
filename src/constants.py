from typing import Tuple, Dict

TARGET_FPS = 60
"""
Target FPS for the screen refresh rate.
"""

TIME_MULTIPLIER = 5
"""
This controls the speed of time in game.
The physics FPS is this much faster than displayed FPS. 
"""

TIME_STEP = 1.0 / TARGET_FPS
"""
This is the time step for the physics engine.
"""

COLORS: Dict[str, Tuple[int, int, int, int]] = {
    'GRAY': (70, 70, 70, 255),
    'BLACK': (0, 0, 0, 255),
    'YELLOW': (255, 216, 43, 255),
    'RED': (170, 51, 44, 255),
    'PINK': (255, 110, 162, 255),
    'GREEN': (20, 212, 184, 255),
    'BLUE': (26, 140, 232, 255),
    'ORANGE': (242, 117, 48, 255)
}
"""
Colors for objects. 
"""

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
"""
Screen size in pixels.
"""

PPM = 30.0
"""
Pixels per meter. 
Used to convert screen coodrinates to physics coordinates.
"""

WALL_THICKNESS = 1
"""
Thickness of the walls around the screen in meters.
"""

BIT_COLOR_DEPTH = 32
"""
Display color depth.
"""

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

KITTIN_FRICTION = 0.15
"""
Friction of the kittin objects.
"""

KITTIN_DENSITY = 1
"""
Density of the kittin objects.
"""

KITTIN_SCALING_FACTOR = 0.33
"""
Scaling factor for the kittin objects.
"""

KITTIN_SPAWN_POSITION = (10, 20)
