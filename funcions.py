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

def GrafiquesComp(data, ustar):
    
    fig, ax = plt.subplots(dpi=300)

    ax.scatter(data.time, data["ustar"], label="Valors teorics", 
                marker=".", color="seagreen")
    ax.plot(data.time, ustar, label="Teoria de Semblança",
            color="steelblue")
    
    ax.set_title("U estrella")
    ax.set_ylabel("$u_*$ (m$s^{-1}$)")
    ax.set_xlabel("Temps (H)")
    ax.minorticks_on()
    ax.legend()

def f_q(T, P, HR):

    # alfa = 18.0153**(-3) / 28.9644**(-3)
    alfa = 18.0153e-3 / 28.9644e-3
    e_sat = 6.112 * np.exp( 17.67 * T/(T + 243.5) )

    rsat = alfa * e_sat / (P - e_sat)

    q = 0.001 * HR / rsat

    return q

def TSemb(z, U, t2m, ts, q2m, qs, k=0.4, z0=0.02, 
          z2vent=2.15, z0t=0.26, z2t=2, tht0=300):

    g = 9.81
    wT = 0.001

    # Primera iteració
    ustar = k*U / ( np.log(z2vent/z0) )
    L = - (tht0 * ustar**3) / (k*g*wT)

    
    phis = np.vectorize(f_phi)

    phi_m, phi_h, phi_q = phis(z, L)
    phi0_m, phi0_h, phi0_q = phis(z0, L)

    for i in range(20):

        ustar_new = k*U / ( np.log(z2vent/z0) + phi_m - phi0_m ) 
        wT = - ( (t2m - ts)*k*ustar ) / ( np.log( z2t/z0t ) 
                                                + phi_h - phi0_h  )  
                
        wq =  ( (q2m - qs)*k*ustar ) /  ( np.log( z2t/z0t ) 
                                        + phi_q - phi0_q  )
        
        # if all( abs(ustar - ustar_new) ) < 1e-50:
        #     print(i)
        #     break

        # else:
        ustar = ustar_new
        L = - (tht0 * ustar**3) / (k*g*wT)

    return ustar, 1231*wT, 3013.5*wq

def f_phi(z: int, L: pd.core.series.Series):

    z_L = z/L

    if z_L < 0:

        xlmo = (1 - 19.3*z_L)**0.25
        ylmo = 0.95*(1 - 11.6*z_L)**0.5

        phi_m = -np.log( (1 + xlmo**2)/2 ) + \
                -2*np.log( (1 + xlmo)/2 ) + 2*np.arctan(xlmo)  + \
                -np.pi/2
        phi_h = -2*np.log( (1 + ylmo)/2 )
        phi_q = phi_h

    elif z_L > 0:

        phi_m = -6*z_L
        phi_h = -7.8*z_L
        phi_q = phi_h

    return phi_m, phi_h, phi_q