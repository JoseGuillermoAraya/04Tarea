#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import pdb
import numpy as np
import matplotlib.pyplot as plt
VY0=0.3
condicion_inicial = np.array([10., 0, 0, VY0])

p = Planeta(condicion_inicial)

t_final =  1000.
numero_pasos = 500+1
dt= t_final / (float)(numero_pasos)

x = np.zeros(numero_pasos)
y = np.zeros(numero_pasos)
vx = np.zeros(numero_pasos)
vy = np.zeros(numero_pasos)


[x[0],y[0],vx[0],vy[0]] = condicion_inicial

for i in range (1,numero_pasos):
    #pdb.set_trace()
    p.avanza_verlet(dt)
    resultados = p.y_actual
    x[i] = resultados[0]
    y[i] = resultados[1]
    vx[i] = resultados[2]
    vy[i] = resultados[3]

plt.plot(x , y)
plt.show()
