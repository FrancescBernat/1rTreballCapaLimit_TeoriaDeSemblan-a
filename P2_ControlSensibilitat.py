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

for i, zi in enumerate(z0):
    for j, kj in enumerate(k):
        ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                data['T'], data['low_T'],
                                q1, q2, k=kj, z0=zi)
        
        err_H[i, j] = fun.fRMSE(ustar, ustar_rea)
        err_Le[i, j] = fun.fRMSE(Le_sem, Le)
        err_H[i, j] = fun.fRMSE(H_sem, H)