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


output = ".jpg"

################################################################
##################### Grafiques singulars ######################
################################################################

# Calor sensible
H = data.H
H[H < -999] = np.nan
fun.Grafiques(data.time, H, "H (W $m^{-1})$", "sienna")
plt.savefig("Imatges/H_dades"+output)
plt.title("Calor sensible")

# Calor latent
Le = data.LE
Le[Le < -999] = np.nan
fun.Grafiques(data.time, Le, "LE (W $m^{-1}$)", "rosybrown")
plt.savefig("Imatges/LE_dades"+output)
plt.title("Calor latent")

# Pressió atmosferica
fun.Grafiques(data.time, data['p'], "p (hPa)")
plt.savefig("Imatges/Pressio"+output)
plt.title("Pressio")


################################################################
##################### Representam el vent ######################
################################################################

fig = plt.figure(dpi=400)

ax = plt.plot(data["time"], data["w_speed"], color="dimgray")
plt.ylabel("v (m/s)")
plt.xlabel("temps (H)")
plt.minorticks_on()
plt.show()

fig.savefig("Imatges/Vent" + output)

# Grafic polar
fig, ax = plt.subplots(dpi=400, subplot_kw={'projection': 'polar'})
graf_vent = ax.scatter(data["w_dir"], data["w_speed"], 
                       c=data["time"], vmin=0, vmax=24, cmap="cividis")
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_xlabel("v (m/s)")
cb = fig.colorbar(graf_vent)
cb.set_label("Hores")

plt.tight_layout()
plt.show()
fig.savefig("Imatges/RosaVent" + output)

################################################################
####################### Humitat relativa #######################
################################################################


q1 = fun.f_q(data['T'], data['p'], data['rel_H'])
q2 = fun.f_q(data['low_T'], data['p'], data['low_rel_H'])

plt.figure(dpi=400)
plt.plot(data.time, q1, label="2 m", color="cornflowerblue")
plt.plot(data.time, q2, label="0.26 m", color="peru")
plt.xlabel("Temps (H)")
plt.ylabel("q (g/kg)")
plt.minorticks_on()
plt.legend()

plt.savefig("Imatges/Humitat especifica" + output)
plt.title("Humitat especifica")

################################################################
################### Resultats Teoria semblança #################
################################################################

ustar, H_sem, Le_sem = fun.TSemb(2, data["w_speed"], 
                                 data['T'], data['low_T'],
                                q1, q2)

fun.GrafiquesComp(data, data["ustar"], ustar, 
                  ylabel="$u_*$ (m$s^{-1}$)")
plt.savefig("Imatges/ustar" + output)

fun.GrafiquesComp(data, Le, Le_sem, ylabel="LE (W $m^{-1}$)",
                  colorvar="goldenrod", colorsemb="lightsteelblue")
plt.savefig("Imatges/Le" + output)


fun.GrafiquesComp(data, H, H_sem, ylabel="H (W $m^{-1}$)",
                  colorvar="maroon", colorsemb="mediumaquamarine")
plt.savefig("Imatges/H" + output)

################################################################
############ Adaptació dels parametres de la teoria ############
################################################################

ustar, H_sem, Le_sem = fun.TSemb(1, data["w_speed"], 
                                 data['T'], data['low_T'],
                                q1, q2, z0=0.08,
                                tht0=data['T'].mean()+273)



fun.GrafiquesComp(data, data["ustar"], ustar, 
                  ylabel="$u_*$ (m$s^{-1}$)")
plt.savefig("Imatges/ustar_2" + output)

fun.GrafiquesComp(data, Le, Le_sem, ylabel="LE (W $m^{-1}$)",
                  colorvar="goldenrod", colorsemb="lightsteelblue")
plt.savefig("Imatges/Le_2" + output)

fun.GrafiquesComp(data, H, H_sem, ylabel="H (W $m^{-1}$)",
                  colorvar="maroon", colorsemb="mediumaquamarine")
plt.savefig("Imatges/H_2" + output)