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
distance = UltrasonicSensor(Port.S4)

"""
const_speed = 300
left_motor.reset_angle(0)
right_motor.reset_angle(0)

left_motor.run_angle(-const_speed,1400,Stop.HOLD,False)
right_motor.run_angle(-const_speed,1400,Stop.HOLD,False)
while True:
    ev3.screen.clear()
    #ev3.screen.print(left_sensor.reflection())
    #ev3.screen.print(right_sensor.reflection())
    #ev3.screen.print(distance.distance())
    ev3.screen.print(left_motor.angle())
    ev3.screen.print(right_motor.angle())
    ev3.screen.print(distance.distance())
    wait(100)
"""

const_speed = 300
N = 6
def forward_by_twin_reflect():
    l_reflect = left_color.reflection()
    r_reflect = right_color.reflection()
    l_speed = const_speed + (r_reflect - l_reflect)*N
    r_speed = const_speed + (l_reflect - r_reflect)*N
    left_motor.run(l_speed)
    right_motor.run(r_speed)

def spin():
    left_motor.run_angle(-const_speed,270,Stop.HOLD,False)
    right_motor.run_angle(const_speed,270,Stop.HOLD,True)
    wait(300)

left_motor.run_angle(-const_speed,200,Stop.HOLD,False)
right_motor.run_angle(-const_speed,200,Stop.HOLD,True)
spin()

left_motor.reset_angle(0)
right_motor.reset_angle(0)
while right_motor.angle() < 1300:
    forward_by_twin_reflect()

left_motor.stop()
right_motor.stop()
wait(500)
spin()

while True:
    forward_by_twin_reflect()
    dist = distance.distance()
    if dist < 120:
        break






