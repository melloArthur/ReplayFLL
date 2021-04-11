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
# EsqCor = ColorSensor(Port.S1)
# DirCor = ColorSensor(Port.S4)

gabriel = DriveBase(esquerda, direita, wheel_diameter=100,axle_track=166.2) #Ajustar valores
ev3 = EV3Brick()

while True:


    if Button.LEFT in ev3.buttons.pressed():
        MotorMA.run(-400)
    if Button.RIGHT in ev3.buttons.pressed():
        MotorMA.run(400)
    if Button.DOWN in ev3.buttons.pressed():
        MotorMD.run(-400)
    if Button.UP in ev3.buttons.pressed():
        MotorMD.run(400)
    if ev3.buttons.pressed() == []:
        MotorMD.stop()
        MotorMA.stop()
    if Button.CENTER in ev3.buttons.pressed():
        MotorMD.reset_angle(0)
        MotorMA.reset_angle(0)