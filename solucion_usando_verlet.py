#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import pdb
import numpy as np
import matplotlib.pyplot as plt
VY0=0.3
condicion_inicial = np.array([10., 0, 0, VY0])

p = Planeta(condicion_inicial)

t_final =  3000.
numero_pasos = 2000+1
dt= t_final / (float)(numero_pasos)

x = np.zeros(numero_pasos)
y = np.zeros(numero_pasos)
vx = np.zeros(numero_pasos)
vy = np.zeros(numero_pasos)

energia = np.zeros(numero_pasos)

[x[0],y[0],vx[0],vy[0]] = condicion_inicial
energia[0] = p.energia_total()
for i in range (1,numero_pasos):
    #pdb.set_trace()
    p.avanza_verlet(dt)
    resultados = p.y_actual
    x[i] = resultados[0]
    y[i] = resultados[1]
    vx[i] = resultados[2]
    vy[i] = resultados[3]
    energia[i] = p.energia_total()
fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x , y, label = "Trayectoria")
plt.title("solucion usando Verlet")
plt.xlabel("X")
plt.ylabel("Y")
t_values = np.linspace(1,t_final,numero_pasos)
plt.subplot(2, 1, 2)
plt.plot(t_values,energia)
plt.title("Energia en cada instante")
plt.show()
