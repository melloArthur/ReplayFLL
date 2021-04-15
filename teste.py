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


# ev3 = EV3Brick()


gabriel = DriveBase(esquerda, direita, wheel_diameter=100,axle_track=166.2)


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
        esquerda.run(vec_array[i])
        direita.run(vec_array[i])
        wait(dt*1000)


def Curva(qp_max, ang, direction='left'): # direction is 'left' or 'right'

    # Dados iniciais 
    qf = ((2 * 3.14 * 77.72)*ang)/360
    qi     =    0               # Posição inicial (em mm)
    
    # Primeiro cálculo
    Dq =  qf - qi           # Variação da posição (distância, em mm)
    
    # Determinação das outras variáveis 
    tf = 15*Dq/(8*qp_max)       # Tempo do movimento
    a3 = 16*qp_max/(3*tf**2)
    a4 = -8*qp_max/(tf**3)
    a5 = 16*qp_max/(5*tf**4)
    
    # Inicio do tempo
    t = 0
    dt = 0.01
    vec_array = []
    
    # Loop do cálculo dos valores de velocidade
    while t < tf:
        qp = round(3*a3*t**2 + 4*a4*t**3 + (5*a5*t**4), 2)
        t += dt
        vec_array.append(qp)

    # Loop do movimento

    # From https://docs.pybricks.com/en/latest/ev3devices.html#motors
    # --->>>>>> run_time(speed, time, then=Stop.HOLD, wait=True)
            # speed (rotational speed: deg/s) – Speed of the motor.
            # time (time: ms) – Duration of the maneuver.
            # then (Stop) – What to do after coming to a standstill.
                # Using a new mode from https://docs.pybricks.com/en/latest/parameters/stop.html
                # ---->>>>>>> Stop.COAST (Let the motor move freely) 
            # wait (bool) – Wait for the maneuver to complete before continuing with the rest of the program.
                # The first is False for simultaneus moviment

    for i in range(0, len(vec_array)-1):
        if direction == 'left':
            esquerda.run(vec_array[i])
            direita.run(-vec_array[i])
            wait(dt*1000)
        elif direction == 'right':
            esquerda.run(-vec_array[i])
            direita.run(vec_array[i])
            wait(dt*1000)

        else:
            esquerda.HOLD()
            direita.HOLD()


Acelera(300, 100)
Curva(300, 360, 'left')
Acelera(300, 100)
Curva(300, 360, 'right')