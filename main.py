#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

esquerda = Motor(Port.B)
direita = Motor(Port.C)
MotorMA = Motor(Port.A)
MotorMD = Motor(Port.D)
EsqCor = ColorSensor(Port.S1)
DirCor = ColorSensor(Port.S4)

gabriel = DriveBase(esquerda, direita, wheel_diameter=100,axle_track=166.2) #Ajustar valores


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

def Acelera(qp_max, qf):
    
    
    # dados iniciais ----------------------
    qi     =    0               # posição inicial (em mm)
    
    # primeiro cálculo
    Dq =  qf - qi           # variação da posição (distância, em mm)
    
    # determinação das outras variáveis 
    tf = 15*Dq/(8*qp_max)       # tempo do movimento
    a3 = 16*qp_max/(3*tf**2)
    a4 = -8*qp_max/(tf**3)
    a5 = 16*qp_max/(5*tf**4)
    
    # inicio do tempo
    t = 0
    dt = 0.01
    vec_array = []
    
    # loop do cálculo dos valores de velocidade
    while t < tf:
        qp = round(3*a3*t**2 + 4*a4*t**3 + (5*a5*t**4), 2)
        t += dt
        vec_array.append(qp)

    # loop do movimento
    for i in range(0, len(vec_array)):
        gabriel.drive(vec_array[i],0)
        wait(dt*1000)


ev3.speaker.beep()