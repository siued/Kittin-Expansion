from Box2D import b2_staticBody, b2_dynamicBody

PPM = 30.0  # pixels per meter

# increase target fps to make time run faster
TARGET_FPS = 300

# if this is 1 / target_fps, game runs at normal speed
TIME_STEP = 1.0 / 60

COLORS = {
    b2_staticBody: (70, 70, 70, 255),
    b2_dynamicBody: (127, 127, 127, 255),
}

SCREEN_WIDTH, SCREEN_HEIGHT = 480, 640
