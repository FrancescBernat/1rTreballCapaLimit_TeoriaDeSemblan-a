#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   funcions.py
@Date    :   2024/05/04 18:48:14
@Author  :   Francesc Bernat Bieri Tauler 
@Version :   1.0
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Grafiques(time: pd.core.series.Series,  
              var: pd.core.series.Series, titol: str):

    fig, ax = plt.subplots(figsize=(10, 8), dpi=600)

    ax.scatter(time, var)
    ax.set_xlabel("Temps (H)")
    ax.set_title(titol, fontsize=20)


def f_q(T, P, HR):

    alfa = 18.0153**(-3) / 28.9644**(-3)
    e_sat = 6.112 * np.exp( 17.67 +  T/(T + 243.5) )

    rsat = alfa * e_sat / (P - e_sat)

    q = 0.001 * HR / rsat

    return q

def ustar(U, k=0.4, z0=0.02, z2vent=2.15):

    ustar = k*U / ( np.log(z2vent/z0) )

    return ustar

def TSemb(z_L, U, k=0.4, z0=0.02, z2vent=2.15, tht0=300):

    ustar = k*U / ( np.log(z2vent/z0) )

    L = - (tht0 * ustar**3) / (k*g*wT)

    if z_L < 0:

        xlmo = (1 - 19.3*z_L)**0.25


