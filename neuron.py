#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:30:42 2026

@author: fred
"""

import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    #initialisierung
    def __init__(self, w):
        self.w = w

    #aktivierung/ sigmoid
    def activation(self, z):
        return 1.0/(1 + np.exp(-z))
        
    #propagierungsfunktion
    def propa(self, x):
        return np.dot(x, self.w)
        
    # predict/berechnungsfunktion
    def prediction(self, x):
        return self.activation(self.propa(x))

if __name__== '__main__':
    a = np.array([1, -2, 2, -8, 0.5])      #gewichtsvektor
    b = np.array([0.5, 3, 3, 0.125, 1])    #eingabevektor
    
    myNeuron = Neuron(a)
    out = myNeuron.prediction(b)
    print('Das Neuron gibt %.3f aus' %out)

    