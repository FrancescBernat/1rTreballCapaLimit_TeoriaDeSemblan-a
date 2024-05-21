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

