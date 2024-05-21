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
from P1_ReprDades import data, q1, q2

from importlib import reload
reload(fun)

import matplotlib as mp

# Per a cambiar les lletres a l'estil que és te a latex
mp.rcParams['mathtext.fontset'] = 'stix'
mp.rcParams['font.family'] = 'STIXGeneral'
mp.rcParams.update({'font.size': 15})

