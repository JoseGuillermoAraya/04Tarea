#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import pdb
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
VY0=0.3
condicion_inicial = np.array([10., 0, 0, VY0])

p = Planeta(condicion_inicial, 10**(-2.844))

t_final =  180.*30
numero_pasos = 30000+1
dt= t_final / (float)(numero_pasos)

x = np.zeros(numero_pasos)
y = np.zeros(numero_pasos)
vx = np.zeros(numero_pasos)
vy = np.zeros(numero_pasos)
r = np.zeros(numero_pasos)

energia = np.zeros(numero_pasos)

perihelio = [[], [],[] ]

[x[0],y[0],vx[0],vy[0]] = condicion_inicial
r[0] = np.sqrt(x[0]**2+y[0]**2)
energia[0] = p.energia_total()

p.avanza_rk4(dt)
resultados = p.y_actual

x[1] = resultados[0]
y[1] = resultados[1]
vx[1] = resultados[2]
vy[1] = resultados[3]

r[1] = np.sqrt(x[1]**2+y[1]**2)

energia[1] = p.energia_total()
for i in range (2,numero_pasos):
    #pdb.set_trace()
    p.avanza_verlet(dt,x[i-2],y[i-2])
    resultados = p.y_actual
    x[i] = resultados[0]
    y[i] = resultados[1]
    vx[i] = resultados[2]
    vy[i] = resultados[3]
    energia[i] = p.energia_total()
    r[i] = np.sqrt(x[i]**2+y[i]**2)

    '''encontrando perhielio'''
    e = 0.000005
    valor =10
    if valor-e<r[i] and r[i]<valor+e:
        perihelio[0].append(p.t_actual)
        perihelio[1].append(x[i])
        perihelio[2].append(y[i])

'''calculo velocidad angular de precesion precesion'''
vel_angular = np.zeros(len(perihelio[0])-1)

phi_anterior =  np.tan(perihelio[2][0]/(perihelio[1][0]))
t_anterior = perihelio[0][0]
for i in range(1,len(perihelio[0])):
    phi = np.tan(perihelio[2][i]/(perihelio[1][i]))
    t = perihelio[0][i]
    dphi = phi - phi_anterior
    dt = t-t_anterior

    vel_angular[i-1] = dphi/dt

    t_anterior = t
    phi_anterior = phi

vel_angular = np.round(vel_angular,7)
velocidad_precesion = scipy.stats.mode(vel_angular)[0][0]
print("velocidad angular de precesion = "+(str)(vel_angular))
print("velocidad angular de precesion = "+(str)(velocidad_precesion))


fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x , y, label = "Trayectoria")
plt.title("Integracion Verlet para $\\alpha = 10^{-2.844}$")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(perihelio[1],perihelio[2],label="posicion perihelio")
plt.legend(loc="lower right",fontsize=10)


t_values = np.linspace(1,t_final,numero_pasos)
plt.subplot(2, 1, 2)
plt.plot(t_values,energia)
plt.title("Energia en cada instante")
plt.xlabel("Tiempo")
plt.ylabel("Energia")

plt.savefig("precesion.jpg", bbox_inches='tight')
plt.show()
