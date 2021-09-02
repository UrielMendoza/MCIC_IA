# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 9:10:11 2021

@materia: Inteligencia Artificial
@author: Uriel de Jesús Mendoza Castillo
"""

import numpy as np
#import math
import matplotlib.pyplot as plt

def hardLimit(n):
    if n < 0 :
        return 0
    elif n >= 0 :
        return 1

def symmetricalHardLimit(n):
        if n < 0:
            return -1
        elif n >= 0:
            return 1

def linear(n):
    return n

def saturatingLinear(n):
    if n < 0:
        return 0
    elif 0 <= n <= 1:
        return n
    elif n > 1:
        return 1 

def symmetricSaturatingLinear(n):
    if n < -1:
        return -1
    elif -1 <= n <= 1:
        return n
    elif n > 1:
        return 1 

def logSigmoid(n):
    return 1 / (1+np.power(np.e,-n))

def hyperbolicTangentSigmoid(n):
    return (np.power(np.e,n) - np.power(np.e,-n)) / (np.power(np.e,n) + np.power(np.e,-n))

def positiveLinear(n):
    if n < 0:
        return 0
    elif 0 <= n:
        return n

def competitive(n,m):
    if max(n) == m:
        return 1
    else:
        return 0

def funcionesActivacion(rango,funcion):
    data = []
    for i in rango:
        if funcion == 'hardLimit':
            data.append(hardLimit(i))

        elif funcion == 'symmetricalHardLimit':
            data.append(symmetricalHardLimit(i))

        elif funcion == 'linear':
            data.append(linear(i))

        elif funcion == 'saturatingLinear':
            data.append(saturatingLinear(i))

        elif funcion == 'symmetricSaturatingLinear':
            data.append(symmetricSaturatingLinear(i))

        elif funcion == 'logSigmoid':
            data.append(logSigmoid(i))

        elif funcion == 'hyperbolicTangentSigmoid':
            data.append(hyperbolicTangentSigmoid(i))

        elif funcion == 'positiveLinear':
            data.append(positiveLinear(i))

        elif funcion == 'competitive':
            data.append(competitive(rango,i))
    return data

def plotFunciones(rango,data,title):
    plt.figure(figsize=(10,10))
    plt.plot(rango, data)
    plt.title(title)
    plt.savefig(title+'.png')
    #fig.tight_layout()

#funcionActivacion = 'positiveLinear'
#rango = np.linspace(-10,10).reshape([50,1])
#data = funcionesActivacion(rango,funcionActivacion)
#plotFunciones(rango,data,funcionActivacion)