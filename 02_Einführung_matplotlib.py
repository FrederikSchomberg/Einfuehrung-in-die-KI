#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


a_werte = [-5, -3, -1, 0, 2, 4]

x = np.linspace(-4, 4, 401)

fig, axs = plt.subplots(2, 3, figsize=(11.69, 8.27))

for i, a in enumerate(a_werte):
    y = x**3 -0.5 * a**2 * x  
    
    ax = axs[i // 3, i % 3]
    ax.plot(x, y)
    ax.set_title(f"a = {a}")
    ax.set_xlabel("x")
    ax.set_ylabel("f_a(x)")
    ax.set_xlim(-4, 4)
    
    
plt.tight_layout()

#plt.savefig('graphs.png')
plt.show()




a_werte = [-5, -3, -1, 0, 2, 4]

x = np.linspace(-4, 4, 401)

plt.figure(figsize=(8.27, 5.83))

for a in a_werte:
    y = x**3 - 0.5 * a**2 * x
    plt.plot(x, y, label=fr"$f_{{{a}}}(x)$")

plt.title(r"Funktionsschar $f_a(x)=x^3-\frac{1}{2}a^2x$", fontsize=18)
plt.xlabel("x", fontsize=12)
plt.ylabel(r"$y=f_a(x)$", fontsize=12)

plt.legend()

plt.tight_layout()

#plt.savefig('oneGraph.png')
plt.show()



