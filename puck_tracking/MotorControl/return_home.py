from __future__ import print_function

import odrive
from odrive.enums import *
import time
import math

# Find a connected ODrive (this will block until you connect one)
print("finding an odrive...")
my_drive = odrive.find_any()

my_drive.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
time.sleep(0.1)
my_drive.axis0.controller.config.input_mode = INPUT_MODE_POS_FILTER
time.sleep(0.1)

my_drive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
time.sleep(0.1)
my_drive.axis1.controller.config.input_mode = INPUT_MODE_POS_FILTER
time.sleep(0.1)

start_m0 = my_drive.axis0.controller.input_pos
start_m1 = my_drive.axis1.controller.input_pos

print(str(my_drive.axis0.controller.input_pos) + "," + str(my_drive.axis1.controller.input_pos))

while (True):
    if (abs(my_drive.axis0.controller.input_pos) < 1):
        my_drive.axis0.controller.input_pos = 0
        start_m0 = 0
    if (abs(my_drive.axis1.controller.input_pos) < 1):
        my_drive.axis1.controller.input_pos = 0
        start_m1 = 0
    if (abs(start_m0)>1 ):
        if (start_m0 > 0):
            my_drive.axis0.controller.input_pos = start_m0 - 1
            start_m0 = start_m0 - 1
        else:
            my_drive.axis0.controller.input_pos = start_m0 + 1
            start_m0 = start_m0 + 1

    if (abs(start_m1)>1):
        if (start_m1 > 0):
            my_drive.axis1.controller.input_pos = start_m1 - 1
            start_m1 = start_m1 - 1
        else:
            my_drive.axis1.controller.input_pos = start_m1 + 1
            start_m1 = start_m1 + 1

    time.sleep(0.5)
    print(str(my_drive.axis0.controller.input_pos) + "," + str(my_drive.axis1.controller.input_pos))
    if (start_m0 == 0 and start_m1 == 0):
        break
