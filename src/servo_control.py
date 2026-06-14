import time
import board
import busio
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)

pca = PCA9685(i2c)
pca.frequency = 50

BASE = 0
SHOULDER = 1
ELBOW = 2
GRIPPER = 3

SERVO_MIN = 500
SERVO_MAX = 2500

current = {
    BASE: 90,
    SHOULDER: 100,
    ELBOW: 100,
    GRIPPER: 60
}


def set_servo(channel, angle):
    angle = max(0, min(180, angle))
    pulse = SERVO_MIN + (angle / 180.0) * (SERVO_MAX - SERVO_MIN)
    duty = int((pulse / 1000000.0) * 50 * 65535)
    pca.channels[channel].duty_cycle = duty
    current[channel] = angle

def smooth_move(channel, target, step=2, delay=0.02):
    start = current[channel]
    if target > start:
        rng = range(start, target, step)
    else:
        rng = range(start, target, -step)
    for angle in rng:
        set_servo(channel, angle)
        time.sleep(delay)
    set_servo(channel, target)

HOME = {
    "base": 90,
    "shoulder": 100,
    "elbow": 100,
    "gripper": 60
}

PICK = {
    "base": 90,
    "shoulder": 110,
    "elbow": 30,
    "open": 65,
    "close": 20
}

BIN_POSITIONS = {
    "black_small_circle_light": (10, 110, 25),
    "white_small_circle_light": (10, 130, 60),
    "black_big_circle_light": (60, 130, 60),
    "white_big_circle_light": (40, 140, 100),
    "black_small_circle_heavy": (75, 170, 130),
    "white_small_circle_heavy": (75, 170, 110),
    "black_big_circle_heavy": (100, 160, 110),
    "white_big_rectangle_heavy": (100, 160, 110),
    "black_small_rectangle_heavy": (125, 160, 120),
    "white_small_rectangle_heavy": (125, 160, 120),
    "white_big_rectangle_light": (150, 160, 120),
    "black_big_rectangle_light": (140, 130, 60),
    "black_small_rectangle_light": (170, 130, 35),
    "white_small_rectangle_light": (170, 130, 75)
}


def arm_home():

    smooth_move(BASE, HOME["base"])
    smooth_move(SHOULDER, HOME["shoulder"])
    smooth_move(ELBOW, HOME["elbow"])
    smooth_move(GRIPPER, HOME["gripper"])

    time.sleep(1)


def pick_object():

    smooth_move(BASE, PICK["base"])
    smooth_move(SHOULDER, PICK["shoulder"])
    smooth_move(ELBOW, PICK["elbow"])
    smooth_move(GRIPPER, PICK["close"])
    time.sleep(0.5)
    lift_after_pick()
    
def drop_category(category):

    if category not in BIN_POSITIONS:
        print("Unknown Category:", category)
        return
    base, shoulder, elbow = BIN_POSITIONS[category]
    smooth_move(BASE, base)
    smooth_move(SHOULDER, shoulder)
    smooth_move(ELBOW, elbow)
    time.sleep(0.5)
    smooth_move(GRIPPER, PICK["open"])
    time.sleep(0.5)
    raise_after_drop()
def lift_after_pick():
    smooth_move(ELBOW, 120)
    time.sleep(0.5)
def raise_after_drop():
    smooth_move(ELBOW, 120)
    time.sleep(0.5)

def cleanup():
    pca.deinit()
