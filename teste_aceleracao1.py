#!/usr/bin/env pybricks-micropython

#Imports

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#Declaração das portas

esquerda = Motor(Port.B)
direita = Motor(Port.C)
EsqCor = ColorSensor(Port.S3)
DirCor = ColorSensor(Port.S4)

gabriel = DriveBase(esquerda, direita, wheel_diameter=88,axle_track=90) #Ajustar valores

#Código


#Funções
def Acelera(qp_max, qf)
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
    # while t < tf:
    #     qp = round(3*a3*t**2 + 4*a4*t**3 + (5*a5*t**4), 2)
    #     t += dt
    #     vec_array.append(qp)

    # # loop do movimento
    # for i in range(0, len(vec_array)):
    #     gabriel.drive(vec_array[i],0)
    #     wait(dt*1000)

    # tentativa de fazer o loop pela posição e não pela velocidade #########################################
    q_ant = 0
    space_array = []
    while t < tf:
        # qp = round(3*a3*t**2 + 4*a4*t**3 + (5*a5*t**4), 2)
        
        q = a3*t**3 + a4*t**4 + a5*t**5
        dist = q - q_ant
        
        vec_array.append(dist)
        t += dt
        q_ant = q

    for i in range(0, len(space_array)):
        gabriel.straight(space_array[i])
        wait(dt*1000)
    # tentativa de fazer o loop pela posição e não pela velocidade #########################################

    # tentativa p/ o giro sem gyro ##################################################
    # gabriel.turn(ang, vel)

    # tentativa p/ o giro sem gyro ##################################################


def SegLinhaPID(potencia, vezes)
    #Definir valores de calibração
    kp =
    ki =
    kd = 

    UltErro = 0
    erro = 0
    contador = 0
    
    while contador < vezes: #Loop para o movimento.
        erro = EsqCor.reflection() - DirCor.reflection()
        integral = integral + erro
        derivativa = erro - UltErro
        curva = erro * kp + integral * ki + derivativa * kp
        gabriel.drive(potencia,curva)