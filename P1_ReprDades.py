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

arxiu = "Dades/DADES_26SETEMBRE2020.dat"

colnames = ["time", "H", "LE", "ustar", "z_L", "w_speed",
            "w_dir", "T", "rel_H", "low_T", "low_rel_H",
            "p"]
data = pd.read_csv(arxiu, sep="\s+", engine='python', 
                   names=colnames, header=None)