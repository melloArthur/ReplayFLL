#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Declaração das variaveis do robo:

esquerda = Motor(Port.B, Direction.COUNTERCLOCKWISE)
direita = Motor(Port.C, Direction.COUNTERCLOCKWISE)
MotorMA = Motor(Port.A)
MotorMD = Motor(Port.D)
# EsqCor = ColorSensor(Port.S1)
# DirCor = ColorSensor(Port.S4)

gabriel = DriveBase(esquerda, direita, wheel_diameter=100,axle_track=166.2) #Ajustar valores
ev3 = EV3Brick()





# Declaração das funções:

def Acelera_e_Curva(qp_max, qf, ang):
    
    
    # Dados iniciais 
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
    for i in range(0, len(vec_array)):
        gabriel.drive(vec_array[i],0)
        wait(dt*1000)
    else:
        gabriel.turn(ang)

def latencia():
    wait(200)

# Codigos:





# #Codigo saida 3

# Acelera_e_Curva(1, 1, 55)
# Acelera_e_Curva(600, 760, -55)
# Acelera_e_Curva(600, 450, 0)
# Acelera_e_Curva(1, 1, 20)
# Acelera_e_Curva(250, 50, 0)





#Codigo saida 4

# Acelera_e_Curva(250, 380, 22) #Anda ate o banco e derruba o banco
# Acelera_e_Curva(350, 20, 0)
# Acelera_e_Curva(-450, -330, -47) #Volta pra base e vira em direção a pista de dança
# Acelera_e_Curva(650, 960, 43) #Anda em diração a pista de dança
# Acelera_e_Curva(200, 90, 0)
# for i in range(4):
#     gabriel.turn(45) #Dansa gatinho dansa
#     latencia()
#     gabriel.turn(-45) #Dansa gatinho dansa
#     latencia()





#Motor control

# while True:


    # if Button.LEFT in ev3.buttons.pressed():
    #     MotorMA.run(-400)
    # if Button.RIGHT in ev3.buttons.pressed():
    #     MotorMA.run(400)
    # if Button.DOWN in ev3.buttons.pressed():
    #     MotorMD.run(-400)
    # if Button.UP in ev3.buttons.pressed():
    #     MotorMD.run(400)
    # if ev3.buttons.pressed() == []:
    #     MotorMD.stop()
    #     MotorMA.stop()
    # if Button.CENTER in ev3.buttons.pressed():
    #     MotorMD.reset_angle(0)
    #     MotorMA.reset_angle(0)