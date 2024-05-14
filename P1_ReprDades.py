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

# Importam les funcions auxiliars desde una altra arxiu
import funcions as fun

from importlib import reload
reload(fun)

import matplotlib as mp

# Per a cambiar les lletres a l'estil que és te a latex
mp.rcParams['mathtext.fontset'] = 'stix'
mp.rcParams['font.family'] = 'STIXGeneral'
mp.rcParams.update({'font.size': 12})

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

# Representam el vent
fig, ax = plt.subplots(dpi=400, subplot_kw={'projection': 'polar'})
graf_vent = ax.scatter(data["w_dir"], data["w_speed"], 
                       c=data["time"], vmin=0, vmax=24, cmap="cividis")
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

cb = fig.colorbar(graf_vent)
cb.set_label("Hores")

plt.tight_layout()
plt.show()


################################################################
####################### Humitat relativa #######################
################################################################


q1 = fun.f_q(data['T'], data['p'], data['rel_H'])
q2 = fun.f_q(data['low_T'], data['p'], data['low_rel_H'])

plt.figure(dpi=300)
plt.plot(data.time, q1, label="2 m")
plt.plot(data.time, q2, label="0.26 m")
plt.title("Humitat especifica")
plt.legend()

################################################################
################### Resultats Teoria semblança #################
################################################################

ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                 data['T'], data['low_T'],
                                q1, q2)

fun.GrafiquesComp(data, data["ustar"], ustar, 
                  ylabel="$u_*$ (m$s^{-1}$)")
ax = plt.gca()
ax.set_title("Ustar")
# plt.figure(dpi=300)
# plt.plot(data.time, data["ustar"], label="Valors teorics")
# plt.plot(data.time, ustar, label="Teoria de Semblança")
# plt.title("U estrella")
# plt.xlabel("Temps (H)")
# plt.legend()

# plt.figure(dpi=300)
# plt.plot(data.time, Le, label="Valors teorics")
# plt.plot(data.time, Le_sem, label="Teoria de Semblança")
# plt.title("Calor Latent (LE)")
# plt.xlabel("Temps (H)")
# plt.legend()
fun.GrafiquesComp(data, Le, Le_sem, ylabel="LE (W $m^{-1}$)",
                  colorvar="goldenrod", colorsemb="lightsteelblue")

# plt.figure(dpi=300)
# plt.plot(data.time, H, label="Valors teorics")
# plt.plot(data.time, H_sem, label="Teoria de Semblança")
# plt.title("Calor sensible (H)")
# plt.xlabel("Temps (H)")
# plt.legend()

fun.GrafiquesComp(data, H, H_sem, ylabel="H (W $m^{-1}$)",
                  colorvar="maroon", colorsemb="mediumaquamarine")

################################################################
############ Adaptació dels parametres de la teoria ############
################################################################

ustar, H_sem, Le_sem = fun.TSemb(1, data["w_speed"], 
                                 data['T'], data['low_T'],
                                q1, q2, z0=0.08,
                                tht0=data['T'].mean()+273)

# plt.figure(dpi=300)
# plt.scatter(data.time, data["ustar"], label="Valors teorics", 
#             marker=".", color="seagreen")
# plt.plot(data.time, ustar, label="Teoria de Semblança",
#           color="steelblue")
# plt.title("U estrella")
# plt.xlabel("Temps (H)")
# plt.ylabel("$u_*$ (m$s^{-1}$)")
# plt.minorticks_on()
# plt.legend()

fun.GrafiquesComp(data, data["ustar"], ustar, 
                  ylabel="$u_*$ (m$s^{-1}$)")



# plt.figure(dpi=300)
# plt.scatter(data.time, Le, label="Valors teorics", 
#             marker=".")
# plt.plot(data.time, Le_sem, label="Teoria de Semblança")
# plt.title("Calor latent (LE)")
# plt.xlabel("Temps (H)")
# plt.minorticks_on()
# plt.legend()

fun.GrafiquesComp(data, Le, Le_sem, ylabel="LE (W $m^{-1}$)",
                  colorvar="goldenrod", colorsemb="lightsteelblue")

# plt.figure(dpi=300)
# plt.scatter(data.time, H, label="Valors teorics", 
#             marker=".")
# plt.plot(data.time, H_sem, label="Teoria de Semblança")
# plt.title("Calor sensible (H)")
# plt.legend()
# plt.xlabel("Temps (H)")

fun.GrafiquesComp(data, H, H_sem, ylabel="H (W $m^{-1}$)",
                  colorvar="maroon", colorsemb="mediumaquamarine")