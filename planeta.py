#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
G=1
M=1
m=1
class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self,datos=np.array([0,0,0,0])):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        Recibe dx,dy,dvx dvy, elementos que se sumaran a la componente
        correspondiente de fx o fy
        '''

        x, y, vx, vy = self.y_actual

        dx = datos[0]
        dy = datos[1]
        dvx = datos[2]
        dvy = datos[3]

        x += dx
        y += dy
        vx += dvx
        vy += dvy

        fx = x*(G*M)*(((2.* self.alpha) / ((x**2 + y**2)**2)) - (1. / (np.sqrt(x**2 + y**2))**3))
        fy = y*(G*M)*(((2.* self.alpha) / ((x**2 + y**2)**2)) - (1. / (np.sqrt(x**2 + y**2))**3))

        return np.array([vx, vy, fx, fy])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        yn = self.y_actual + dt * (self.ecuacion_de_movimiento())
        self.y_actual = yn
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        k1 = self.ecuacion_de_movimiento()
        k2 = self.ecuacion_de_movimiento(dt/2. * k1)
        k3 = self.ecuacion_de_movimiento(dt/2. * k2)
        k4 = self.ecuacion_de_movimiento(dt * k3)

        yn = self.y_actual + dt/6. * (k1 + 2*k2 + 2*k3 + k4)

        self.y_actual = yn
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt, x_p,y_p):
        '''
        Similar a avanza_euler, pero usando Verlet.
        recibe las posiciones en el paso previo
        '''
        '''
        x , y, vx, vy = self.y_actual
        yn = np.array([ x , y ]) + np.array([ vx , vy ]) * dt + 1/2. * self.ecuacion_de_movimiento()[2:] * dt**2
        Yn = np.array([yn[0] , yn[1], 0, 0])
        vn = np.array([ vx , vy ]) + 1/2. * (self.ecuacion_de_movimiento()[2:] + self.ecuacion_de_movimiento(Yn)[2:]) * dt

        actual = np.array([yn[0], yn[1], vn[0], vn[1]])
        self.y_actual = actual
        self.t_actual += dt
        '''
        Y_previo = np.array([x_p,y_p])
        x , y, vx, vy = self.y_actual
        Y = np.array([x,y])
        Yn = 2 * Y - Y_previo + dt**2 * self.ecuacion_de_movimiento()[2:]
        Vn = (Yn - Y_previo) / (2*dt)

        actual = np.array([Yn[0],Yn[1],Vn[0], Vn[1]])
        self.y_actual = actual
        self.t_actual +=dt


        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        x, y, vx, vy = self.y_actual
        potencial = - G*M*m/(np.sqrt(x**2 + y**2))  + self.alpha*G*M*m /((x**2 + y**2))
        energia = (vx**2 +vy**2) * m/2. + potencial

        return energia
        pass
