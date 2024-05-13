#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P1_ReprDades.py
@Date    :   2024/05/04 13:26:29
@Author  :   Francesc Bernat Bieri Tauler 
@Version :   1.0
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import funcions as fun

from importlib import reload

reload(fun)

arxiu = "Dades/DADES_26SETEMBRE2020.dat"

colnames = ["time", "H", "LE", "ustar", "z_L", "w_speed",
            "w_dir", "T", "rel_H", "low_T", "low_rel_H",
            "p"]

# Llegim les dades de l'arxiu
data = pd.read_csv(arxiu, sep="\s+", engine='python', 
                   names=colnames, header=None)

H = data.H
H[H < -999] = np.nan

fun.Grafiques(data.time, H, "Humitat")

Le = data.LE
Le[Le < -999] = np.nan
fun.Grafiques(data.time, Le, "LE")

## %% Humitat relativa
q1 = fun.f_q(data['T'], data['p'], data['rel_H'])
q2 = fun.f_q(data['low_T'], data['p'], data['low_rel_H'])

plt.figure(dpi=300)
plt.plot(data.time, q1, label="2 m")
plt.plot(data.time, q2, label="0.26 m")
plt.title("Humitat especifica")
plt.legend()

#%% Resultats Teoria semblança

ustar, H_sem, Le_sem = fun.TSemb(1, data["w_speed"], 
                                 data['T'], data['low_T'],
                                data["rel_H"], data["low_rel_H"])

plt.figure(dpi=300)
plt.plot(data.time, Le, label="Valors teorics")
plt.plot(data.time, Le_sem, label="Teoria de Semblança")
plt.title("LE")
plt.legend()

plt.figure(dpi=300)
plt.plot(data.time, H, label="Valors teorics")
plt.plot(data.time, H_sem, label="Teoria de Semblança")
plt.title("Humitat")
plt.legend()

# %%

ustar, H_sem, Le_sem = fun.TSemb(1, data["w_speed"], 
                                 data['T'], data['low_T'],
                                data["rel_H"], data["low_rel_H"])

plt.figure(dpi=300)
plt.plot(data.time, Le, label="Valors teorics")
plt.plot(data.time, Le_sem, label="Teoria de Semblança")
plt.title("LE")
plt.legend()

plt.figure(dpi=300)
plt.plot(data.time, H, label="Valors teorics")
plt.plot(data.time, H_sem, label="Teoria de Semblança")
plt.title("Humitat")
plt.legend()