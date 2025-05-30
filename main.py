#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

right_color = ColorSensor(Port.S1)
left_color = ColorSensor(Port.S2)
#distance = InfraredSensor(Port.S4)

r_reflect = 0
dist = 0
l_speed = 0
r_speed = 0
const_speed = 450


# Write your program here.
while True:
    l_reflect = left_color.reflection()
    r_reflect = right_color.reflection()
    #dist = distance.distance()
    l_speed = const_speed + (r_reflect - l_reflect)*8
    r_speed = const_speed + (l_reflect - r_reflect)*8

    left_motor.run(l_speed)
    right_motor.run(r_speed)

