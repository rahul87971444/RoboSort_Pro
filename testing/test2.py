import time
import board
import busio
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL, board.SDA)

pca = PCA9685(i2c)
pca.frequency = 50

SERVO_MIN = 500
SERVO_MAX = 2500

BASE = 0
SHOULDER = 1
ELBOW = 2
GRIPPER = 3

current = {
    BASE: 90,
    SHOULDER: 100,
    ELBOW: 100,
    GRIPPER: 70
}

def set_servo(channel, angle):
    angle = max(0, min(180, angle))

    pulse = SERVO_MIN + (angle / 180.0) * (SERVO_MAX - SERVO_MIN)

    duty = int((pulse / 1000000.0) * 50 * 65535)

    pca.channels[channel].duty_cycle = duty


def move_arm(base, shoulder, elbow, gripper, delay=0.02):
    max_steps = max(
        abs(base - current[BASE]),
        abs(shoulder - current[SHOULDER]),
        abs(elbow - current[ELBOW]),
        abs(gripper - current[GRIPPER])
    )

    if max_steps == 0:
        return

    for i in range(max_steps + 1):

        b = current[BASE] + (base - current[BASE]) * i / max_steps
        s = current[SHOULDER] + (shoulder - current[SHOULDER]) * i / max_steps
        e = current[ELBOW] + (elbow - current[ELBOW]) * i / max_steps
        g = current[GRIPPER] + (gripper - current[GRIPPER]) * i / max_steps

        set_servo(BASE, b)
        set_servo(SHOULDER, s)
        set_servo(ELBOW, e)
        set_servo(GRIPPER, g)

        time.sleep(delay)

    current[BASE] = base
    current[SHOULDER] = shoulder
    current[ELBOW] = elbow
    current[GRIPPER] = gripper


print("Smooth Calibration Mode")

while True:
    try:
        print("\nCurrent:", current)

        b = int(input("Base: "))
        s = int(input("Shoulder: "))
        e = int(input("Elbow: "))
        g = int(input("Gripper: "))

        move_arm(b, s, e, g)

    except KeyboardInterrupt:
        break

pca.deinit()