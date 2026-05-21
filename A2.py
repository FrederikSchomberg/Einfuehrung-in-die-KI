import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    
    #initialisierung
    def __init__(self, w):
        self.w = w

    #aktivierungsfunktion
    def activation(self, z):
        return 1.0/(1 + np.exp(-z))
        
    #propagierungsfunktion
    def propa(self, x):
        return np.dot(x, self.w)
        
    # predict/berechnungsfunktion
    def predict(self, x):
        return self.activation(self.propa(x))

if __name__== '__main__':
    
    w11 = np.array([3.5689712, 6.092813, -6.255747])    #gewichte für neuron11 + bias
    w12 = np.array([3.5879905, 6.3442955, -1.4534572])  #gewichte für neuron12 + bias
    w21 = np.array([8.658071, -7.7893, 3.6128955])      #gewichte für neuron 21 + bias
    
    neuron11 = Neuron(w11) # erstes neuron des hidden layers erzeugen
    neuron12 = Neuron(w12) # zweites neuron des hidden layers erzeugen 
    neuron21 = Neuron(w21) # ausgabeneuron erzeugen
    
    eingaben = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    for a, b in eingaben:
        x = np.array([a, b, 1.0])  #eingabevektor mit biaseingang 1.0
        
        out11 = neuron11.predict(x) # ausgabe von neuron11 berechnen
        out12 = neuron12.predict(x) # ausgabe von neuron12 berechnen
        
        hiddenout= np.array([out11, out12, 1.0]) # ausgaben der versteckten schicht + bias für die ausgabeneuron
        
        out21 = neuron21.predict(hiddenout) # ausgabe des netzes berechnen 
        
        xnor = int(out21 >= 0.5)  # sigmoidausgabe in 0 oder 1 umwandeln

        print("%d %d | %d   (%.3f)" % (a, b, xnor, out21))
    

