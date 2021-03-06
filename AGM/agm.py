# Vanilla AGM iteration
def agm(x, y=1, verbose=0):
    for _ in range(5): 
        x, y = (x+y)/2, (x*y)**(1/2)
        if verbose: print(x, y)
    return x

# Cubically convergent 2-variable AGM-like iteration
def agm3(x, y=1, verbose=0):
    for _ in range(5):
        x, y = (x+2*y)/3, (y*(x*x+x*y+y*y)/3)**(1/3)
        if verbose: print(x, y)
    return x

# N-tic convergence 2-variable AGM-like iteration
# From Borwein^2
def agmN(x, y=1, N=2, verbose=0):
    for _ in range(8):
        c = (x-y)/N
        x = (x + (N-1)*y)/N
        y = (x**N - c**N)**(1/N)
        if verbose: print(x,y)
    return x

# 3-variable AGM-like iteration (cubic convergence)
# From math.stackexchange
def agmStack(a, b=1, c=1, verbose=0):
    for _ in range(5):
        R = (a**2*(b+c)+b**2*(c+a)+c**2*(a+b))/6
        I = (a-b)*(b-c)*(c-a) / (2 * (-27)**(1/2))
        a, b, c = (a+b+c)/3, (R+I)**(1/3), (R-I)**(1/3)
        if verbose: print(a, b, c)
    return a



if 0:
    x=10

    print('AGM3')
    agm3(x,1, verbose=1)
    print()

    print('AGMStack')
    agmStack(1, b=x, c=1, verbose=1)
    print()




import math
from scipy import special
import numpy as np

k = 1000
X = [5*n/k for n in range(1,k)]

import matplotlib.pyplot as plt
plt.plot(X,[math.pi/2/agmN(x,N=4) for x in X])
plt.plot(X,[special.ellipk((1-x**2)/2) for x in X])
plt.show()
