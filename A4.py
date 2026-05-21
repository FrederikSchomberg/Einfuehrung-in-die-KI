# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:58:55 2026

@author: fred
"""

import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    #initialisierung
    def __init__(self, w):
        self.w = w

    #Activation
    def activation(self, z):
        return 1.0/(1 + np.exp(-z))
        
    #Sum funciton
    def weighted_sum(self, x):
        return np.dot(x, self.w)
        
    # prediction or feedforward
    def prediction(self, x):
        return self.activation(self.weighted_sum(x))


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
    
    plt.gray()  
    plt.imshow(erg)  
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.colorbar(label="Netzasusgabe")
    plt.show()
    
    
    
    
    
    # das bild zeigt die ausgaben des xnor-netzes für alle kombinationen von x1 und x2 zwischen 0.0 und 1.0. helle stellen bedeuten ausgabe nahe 1, dunkle stellen ausgabe nahe 0. graue übergänge entstehen weil auch zwischenwerte berechnet werden.
    # ist plausibel, da bei xnor ist die ausgabe 1, wenn beide eingaben gleich sind. und wenn die eingaben unterschiedlich sind ist die ausgabe 0.