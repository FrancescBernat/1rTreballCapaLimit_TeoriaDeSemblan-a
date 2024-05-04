#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   funcions.py
@Date    :   2024/05/04 18:48:14
@Author  :   Francesc Bernat Bieri Tauler 
@Version :   1.0
'''

import matplotlib.pyplot as plt

def Grafiques(time, var):

    fig, ax = plt.subplots(figsize=(10, 8), dpi=600)

    ax.plot(time, var)
    ax.set_xlabel("Temps (H)")