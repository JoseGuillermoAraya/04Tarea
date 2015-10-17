#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import pdb
import numpy as np
import matplotlib.pyplot as plt
VY0=0.2
condicion_inicial = [10, 0, 0, VY0]

p = Planeta(condicion_inicial)

t_final =  100.
numero_pasos = 100
dt= t_final / (float)(numero_pasos)

x = np.zeros(numero_pasos)
y = np.zeros(numero_pasos)
vx = np.zeros(numero_pasos)
vy = np.zeros(numero_pasos)

resultados = [[x , y , vx , vy]]
resultados[0] = condicion_inicial

for i in range (1,numero_pasos+1):
    pdb.set_trace()
    p.avanza_euler(dt)
    resultados[i] = p.y_actual

plt.scatter(resultados[0] , resultados[1])
plt.show()
