# test_weight.py

from weight_sensor import *
from time import sleep
set_zero()

while True:
    print(get_weight())
    sleep(0.5)