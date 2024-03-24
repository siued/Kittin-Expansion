from Box2D import b2_staticBody, b2_dynamicBody

PPM = 30.0  # pixels per meter

# increase target fps to make time run faster
TARGET_FPS = 300

# if this is 1 / target_fps, game runs at normal speed
TIME_STEP = 1.0 / 60

COLORS = {
    'GRAY': (70, 70, 70, 255),
    'YELLOW': (255, 216, 43, 255),
    'RED': (170, 51, 44, 255),
    'PINK': (255, 110, 162, 255),
    'GREEN': (20, 212, 184, 255),
    'BLUE': (26, 140, 232, 255),
    'ORANGE': (242, 117, 48, 255)
}

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
GAME_TITLE = 'Kittin Expansion 3000'
