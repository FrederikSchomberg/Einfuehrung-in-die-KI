# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:58:45 2026

@author: fred
"""

import numpy as np

class Neuron:
    #initialisierung
    def __init__(self, w):
        self.w = w

    # aktivierungsfunktion
    def activation(self, z):
        return 1.0/(1 + np.exp(-z))
        
    #propagierungsfunktionb
    def propa(self, x):
        return np.dot(x, self.w)
        
    # prediction or feedforward
    def prediction(self, x):
        return self.activation(self.propa(x))


if __name__== '__main__':

    w11 = np.array([3.5689712, 6.092813, -6.255747])    #gewichte für neuron11 + bias
    w12 = np.array([3.5879905, 6.3442955, -1.4534572])  #gewichte für neuron12 + bias
    w21 = np.array([8.658071, -7.7893, 3.6128955])      #gewichte für neuron 21 + bias
    
    neuron11 = Neuron(w11) # erstes neuron des hidden layers erzeugen
    neuron12 = Neuron(w12) # zweites neuron des hidden layers erzeugen 
    neuron21 = Neuron(w21) # ausgabeneuron erzeugen
    
    erg = np.zeros((101, 101, 1), np.double) # matrix für alle ausgaben vom netz
    
    for i1 in range(101):
        x1 = i1 * 0.01
        
        for i2 in range(101):
            x2 = i2 * 0.01
            
            out11 = neuron11.prediction(np.array([x1, x2, 1.0])) #ausgabe hidden neuron1
            out12 = neuron12.prediction(np.array([x1, x2, 1.0])) #ausgabe hidden neuron2
            
            y = neuron21.prediction(np.array([out11, out12, 1.0])) #ausgabe XNOR netz
            
            erg[i1, i2, 0] = y # ausgabe in matrix speichern
        
    print(erg)