import math
import numpy as np
from scipy import linalg

I = np.array([[1,0,0],[0,1,0],[0,0,1]])

def sqrtm(A):
    X = A
    Y = (A + I) // 2
    for _ in range(4):
        X, Y = Y, (Y + A // Y) // 2
    return X

def agm(X, Y=I, verbose=0):
    for _ in range(4):
        X, Y = (X + Y) / 2, linalg.sqrtm((np.dot(X,Y)+np.dot(Y,X)) / 2)
        if verbose: print(X, '\n')
    return X

def logm(X):
    eps = 10.0**(-2)
    return math.log(4/eps)*I - math.pi/2 * linalg.inv(agm(eps*X)) 

A = np.array([[1,2,3],[4,5,6],[7,8,7]]) / 16

f = I
F = I
a,b,c = 1/2,1/2,1
for i in range(250):
    f = np.dot(f, A) * ((a+i)*(b+i)/(c+i)/(i+1))
    F = F + f

print(F)
print()

F = linalg.inv(agm(linalg.sqrtm(I-A)))
print(F)
print()
