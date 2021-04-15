#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

esquerda = Motor(Port.B, Direction.COUNTERCLOCKWISE)
direita = Motor(Port.C, Direction.COUNTERCLOCKWISE)
MotorMA = Motor(Port.A)
MotorMD = Motor(Port.D)
melhorSensor = GyroSensor(Port.S2)

ev3 = EV3Brick
while True:
    if Button.CENTER in ev3.buttons.pressed():
        a = melhorSensor.angle()
        ev3.screen.print(a)
    if Button.LEFT in ev3.buttons.pressed():
        melhorSensor.reset_angle(0)