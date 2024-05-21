#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P2_ControlSensibilitat.py
@Date    :   2024/05/21 19:18:18
@Author  :   Francesc Bernat Bieri Tauler 
@Version :   1.0
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importam les funcions auxiliars desde una altra arxiu
import funcions as fun

from importlib import reload
reload(fun)

import matplotlib as mp

# Per a cambiar les lletres a l'estil que és te a latex
mp.rcParams['mathtext.fontset'] = 'stix'
mp.rcParams['font.family'] = 'STIXGeneral'
mp.rcParams.update({'font.size': 15})

output = ".jpg"

##############################################################
##################### Dades necessaries ######################
##############################################################
arxiu = "Dades/DADES_26SETEMBRE2020.dat"

colnames = ["time", "H", "LE", "ustar", "z_L", "w_speed",
            "w_dir", "T", "rel_H", "low_T", "low_rel_H",
            "p"]

# Llegim les dades de l'arxiu
data = pd.read_csv(arxiu, sep="\s+", engine='python', 
                   names=colnames, header=None)

q1 = fun.f_q(data['T'], data['p'], data['rel_H'])
q2 = fun.f_q(data['low_T'], data['p'], data['low_rel_H'])

H = data.H
H[H < -999] = np.nan

Le = data.LE
Le[Le < -100] = np.nan

ustar_rea = data['ustar']

##############################################################
# Calculs
##############################################################

ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                 data['T'], data['low_T'],
                                q1, q2)

z0 = np.linspace(0.02, 0.08)
k = np.linspace(0.25, 0.4)
tht0 = np.linspace(290, 310)

err_H  = np.zeros( (50, 50) )
err_Le = np.zeros((50, 50))
err_u  = np.zeros((50, 50))

##### RMSE variant z0 i k

for i, zi in enumerate(z0): # files
    for j, kj in enumerate(k): # columnes
        ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                data['T'], data['low_T'],
                                q1, q2, k=kj, z0=zi)
        
        err_u[i, j] = fun.fRMSE(ustar, ustar_rea)
        err_Le[i, j] = fun.fRMSE(Le_sem, Le)
        err_H[i, j] = fun.fRMSE(H_sem, H)

fun.GraficsErrors(z0, k, err_H)
plt.savefig("Imatges/RMSE_H_zk"+output)
plt.title("H, variant z0 i k")

fun.GraficsErrors(z0, k, err_Le)
plt.savefig("Imatges/RMSE_Le_zk"+output)
plt.title("Le, variant z0 i k")

fun.GraficsErrors(z0, k, err_u)
plt.savefig("Imatges/RMSE_U_zk"+output)
plt.title("U estrella, variant z0 i k")

##### RMSE variant z0 i tht0

for i, zi in enumerate(z0): # files
    for j, tj in enumerate(tht0): # columnes
        ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                data['T'], data['low_T'],
                                q1, q2, z0=zi, tht0=tj)
        
        err_u[i, j] = fun.fRMSE(ustar, ustar_rea)
        err_Le[i, j] = fun.fRMSE(Le_sem, Le)
        err_H[i, j] = fun.fRMSE(H_sem, H)

fun.GraficsErrors(z0, tht0, err_H, color="twilight", ylab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_H_zt"+output)
plt.title("H, variant z0 i t")

fun.GraficsErrors(z0, tht0, err_Le, color="twilight", ylab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_Le_zt"+output)
plt.title("Le, variant z0 i t")

fun.GraficsErrors(z0, tht0, err_u, color="twilight", ylab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_U_zt"+output)
plt.title("U estrella, variant z0 i t")

##### RMSE variant k i tht0

for i, ti in enumerate(tht0): # files
    for j, kj in enumerate(k): # columnes
        ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                data['T'], data['low_T'],
                                q1, q2, k=kj, tht0=ti)
        
        err_u[i, j] = fun.fRMSE(ustar, ustar_rea)
        err_Le[i, j] = fun.fRMSE(Le_sem, Le)
        err_H[i, j] = fun.fRMSE(H_sem, H)

fun.GraficsErrors(tht0, k, err_H, color="CMRmap", xlab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_H_tk"+output)
plt.title("H, variant t0 i k")

fun.GraficsErrors(tht0, k, err_Le, color="CMRmap", xlab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_Le_tk"+output)
plt.title("Le, variant t0 i k")

fun.GraficsErrors(tht0, k, err_u, color="CMRmap", xlab=r"$\theta_0$")
plt.savefig("Imatges/RMSE_U_tk"+output)
plt.title("U estrella, variant t0 i k")