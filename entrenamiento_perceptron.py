# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:28:17 2021

@materia: Inteligencia Artificial
@author: Uriel de Jesús Mendoza Castillo
"""

import numpy as np
import random
from funciones_activacion import hardLimit

def perceptron(W, p, b):
    '''
    Calcula el perceptron con la funcion de activacion hardlimit
    '''
    pw = np.dot(W,p) + b
    a = hardLimit(pw)
    return a

def calculaError(t, a):
    '''
    Calcula el error del target menos el valor obtenido
    '''
    e = t - a
    return e

def actualizaPesoSinaptico(p, W, b, e):
    '''
    Actualiza el peso sinaptico y el bias con el error
    '''
    W =  W + e * p
    b = b + e
    return W,b

def generaBiasAleatorio(t):
    '''
    Genera los bias aleatorio dependiendo del numero de neuronas
    '''
    b_l = []
    for i in range(t):
        b_l.append(random.random())
    b = np.array(b_l)
    return b

def generaPesoSinapticoAleatorio(S, R):
    '''
    Genera los pesos sinapticos aleatorios dependiendo del numero 
    de neuronas y de entradas
    '''
    W = np.zeros((S,R))
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            W[i,j] = random.random()   
    return W

def generaArray(d):
    '''
    Genera un numpy array apartir de una lista
    '''
    data = np.array(d)
    return data

def test(p, t, W, b):
    '''
    Realiza la prueba del entrenaimiento con 1 neurona
    '''
    print('Test: ')
    for i in range(len(p)):
        a = perceptron(W, p[i], b)
        print('Entrada = ', p[i])
        print('Target = ', t[i])
        print('a = ', a)
        
def testMulti(p, t, W, b):
    '''
    Realiza la prueba del entrenaimiento con n neuronas
    '''
    neurona = len(t[0])
    print('Test: ')
    for i in range(len(p)):
        a = []
        for j in range(neurona):
            a.append(perceptron(W[j], p[i], b[j]))
        print('Entrada = ', p[i])
        print('Target = ', t[i])
        print('a = ', a)

def infoInicio(W, b, neurona):
    '''
    Imprime la informacion de inicio, pesos sipticos iniciales, 
    bias inicial y numero de neuronas
    '''
    print('==========================================')
    print('Pesos sinapticos iniciales: ')
    print(W)
    print('Bias inicial: ')
    print(b)
    print('Neuronas: ',neurona)
    print('==========================================\n')

def infoFin(W, b, epocas):
    '''
    Imprime la informacion del final, pesos sipticos finales, 
    bias final y numero de epocas realizadas
    '''
    print('\n==========================================')
    print('Pesos sinapticos finales: ')
    print(W)
    print('Bias final: ')
    print(b)
    print('Epocas: ',epocas)
    print('==========================================\n')

def info(p, t, a, e):
    '''
    Imprime la informacion general por cada prueba en el entrenamiento
    '''
    print('\n')
    print('Entrada = ',p)
    print('a = ',a)
    print('target = ',t)
    print('error = ',e)

def infoError(W, b, e):
    '''
    Imprime la informacion general en caso de error diferente de 0
    '''
    print('Nuevos Pesos Sinapticos =')
    print(W)
    print('Nuevo bias =')
    print(b)
    print('Nuevo error = ', e)
    
def entrenaUniPerceptron(p, t):
    '''
    Entrenamiento de una red con 1 neurona y n entradas
    '''
    neurona = 1        
    W = generaPesoSinapticoAleatorio(neurona, len(p[0]))
    b = generaBiasAleatorio(neurona)
    
    infoInicio(W, b, neurona)
    
    epocas = 0
    error = True
    while error == True:
        error = False
        for i in range(len(p)):
            a = perceptron(W, p[i], b)
            e = calculaError(t[i], a)
            info(p[i], t[i], a, e)
            if e != 0:
                error = True
                e = calculaError(t[i], a)
                W, b = actualizaPesoSinaptico(p[i], W, b, e)
                a = perceptron(W, p[i], b)
                infoError(W, b, e)
                
        epocas += 1
        
    infoFin(W, b, epocas)
    
    return W, b

def entrenaRedPerceptron(p, t):   
    '''
    Entrenamiento de una red con n neuronas y n entradas
    ''' 
    neurona = len(t[0])        
    W = generaPesoSinapticoAleatorio(neurona, len(p[0]))
    b = generaBiasAleatorio(neurona)
    a = np.zeros((1, neurona))
    
    infoInicio(W, b, neurona)
    
    epocas = 0
    error = True
    while error == True:
        error = False
        for i in range(len(p)):
            for j in range(neurona):
                a[0,j] = perceptron(W[j], p[i], b[j])
                e = calculaError(t[i][j], a[0][j])
                info(p[i], t[i], a, e)
                if e != 0:
                    error = True
                    e = calculaError(t[i][j], a[0][j])
                    W[j], b[j] = actualizaPesoSinaptico(p[i], W[j], b[j], e)
                    a[0,j] = perceptron(W[j], p[i], b[j])
                    infoError(W, b, e)
                
        epocas += 1
        
    infoFin(W, b, epocas)
    
    return W,b

#============================================
# ENTRENAMIENTO PARA UN PERCEPTRON DE UNA CAPA
p = generaArray([[0,0],[0,1],[1,0],[1,1]])
# COMENTAR Y DESCOMENTAR t PARA DISTINTAS PRUEBAS DE TARGETS
# AND
t = generaArray([0,0,0,1])
# OR
#t = np.array([0,1,1,1])
# NOR
#t = np.array([1,0,0,0])
# XOR
#t = np.array([0,1,1,0])

W, b = entrenaUniPerceptron(p, t)
test(p, t, W, b)
#============================================

#============================================
# ENTRENAMIENTO PARA UNA RED PERCEPTRONES DE UNA CAPA
# COMENTAR Y DESCOMENTAR p y t PARA DISTINTAS PRUEBAS DE TARGETS Y ENTRADAS
# AND, OR y NOR
p = generaArray([[0,0],[0,1],[1,0],[1,1]])
t = generaArray([[0,0,1],[0,1,0],[0,1,0],[1,1,0]])
# %
#p = generaArray([[0,0,0],[0,1,0],[1,1,0],[1,1,1],[1,0,0]])
#t = np.array([[0],[1],[1],[1],[0]])

W, b = entrenaRedPerceptron(p, t)
testMulti(p, t, W, b)
#============================================
