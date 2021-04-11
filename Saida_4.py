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


def Acelera_e_Curva(qp_max, qf, ang):
    
    
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
    else:
        gabriel.turn(ang)

def latencia():
    wait(200)


# Codigo saida 4
Acelera_e_Curva(250, 380, 22) # Anda ate o banco e derruba o banco, levanta o encosto, coloca o projeto inovador no lugar e coloca as 4 bolsas de saude no lugar
Acelera_e_Curva(350, 20, -10) # Derruba os 4 cubos em seus respectivos lugares
Acelera_e_Curva(350, 10, 10)
Acelera_e_Curva(-450, -330, -47) # Volta pra base e vira em direção a pista de dança
Acelera_e_Curva(650, 960, 43) # Anda em diração a pista de dança e faz a curva na exata direção da pista de dança
Acelera_e_Curva(200, 90, 0) # Anda para dentro da pista de dança
for i in range(4): #O robo dança na pista de dança

    gabriel.turn(45) 
    latencia()
    gabriel.turn(-45) 
    latencia()