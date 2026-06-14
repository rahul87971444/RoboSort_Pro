from hx711 import HX711
import time

DT_PIN = 5
SCK_PIN = 6

hx = HX711(DT_PIN, SCK_PIN)

hx.set_reading_format("MSB", "MSB")

# Your calibrated value
hx.set_reference_unit(780)

hx.reset()


def set_zero():
    print("Keep platform empty...")
    time.sleep(2)

    hx.tare()

    print("Scale Ready")


def get_weight():

    weight = hx.get_weight(31)

    if abs(weight) < 2:
        weight = 0

    hx.power_down()
    hx.power_up()

    return round(weight, 2)


def classify_weight():

    weight = get_weight()

    if weight < 20:
        return "LESS_THAN_20", weight
    else:
        return "GREATER_THAN_20", weight


def cleanup():
    pass
