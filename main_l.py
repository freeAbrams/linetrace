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

r_reflect = 0
dist = 0
l_speed = 0
r_speed = 0
const_speed = 150
N = 3

# forward by right color sensor only
def forward_by_right_reflect():
    r_reflect = right_color.reflection()
    l_speed = const_speed + (r_reflect - 25)*N
    r_speed = const_speed - (r_reflect - 25)*N
    left_motor.run(l_speed)
    right_motor.run(r_speed)

# forward by left color sensor only
def forward_by_left_reflect():
    l_reflect = left_color.reflection()
    l_speed = const_speed - (l_reflect - 25)*N
    r_speed = const_speed + (l_reflect - 25)*N
    left_motor.run(l_speed)
    right_motor.run(r_speed)

# forward by both color sensors
def forward_by_twin_reflect():
    l_reflect = left_color.reflection()
    r_reflect = right_color.reflection()
    l_speed = const_speed + (r_reflect - l_reflect)*N
    r_speed = const_speed + (l_reflect - r_reflect)*N
    left_motor.run(l_speed)
    right_motor.run(r_speed)

# backward by both motors with given angle
def backward(left,right):
    left_motor.run_angle(-const_speed,left,Stop.HOLD,False)
    right_motor.run_angle(-const_speed,right,Stop.HOLD,True)
    wait(300)

# spin by both motors with given angle
def spin(angle):
    left_motor.run_angle(-const_speed,angle*1.5,Stop.HOLD,False)
    right_motor.run_angle(const_speed,angle*1.5,Stop.HOLD,True)
    wait(300)




while True:
    forward_by_left_reflect()
    dist = distance.distance()
    if dist < 120:
        break

left_motor.stop()
right_motor.stop()
wait(3000)

const_speed = 300
N = 2.5

backward(300,300)
spin(180)
right_motor.reset_angle(0)
left_motor.reset_angle(0)
while right_motor.angle() < 1200:
    forward_by_twin_reflect()
left_motor.stop()
right_motor.stop()
wait(300)
spin(180)
right_motor.reset_angle(0)
left_motor.reset_angle(0)

const_speed = 150
N = 3

while right_motor.angle() < 1800:
    forward_by_right_reflect()

const_speed = 400
N = 3.5

right_motor.reset_angle(0)
left_motor.reset_angle(0)
while right_motor.angle() < 3000:
    forward_by_twin_reflect()
right_motor.reset_angle(0)
left_motor.reset_angle(0)
const_speed = 150
N = 3
while right_motor.angle() < 1500:
    forward_by_left_reflect()

const_speed = 300
N = 2.5
while True:
    forward_by_twin_reflect()
    dist = distance.distance()
    if dist < 120:
        break


