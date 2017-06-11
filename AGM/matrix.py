import math
import numpy as np
from scipy import linalg

I = np.array([[1,0,0],[0,1,0],[0,0,1]])

def agm(X, Y=I):
    for _ in range(10):
        X, Y = (X+Y)/2, linalg.sqrtm((np.dot(X,Y) + np.dot(Y,X))/2)
    return X

def logm(X):
    eps = 10.0**(-2)
    return math.log(4/eps)*I - math.pi/2 * linalg.inv(agm(eps*X)) 

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('A=')
print(A)
print()

print('Avg. value of A - e^linalg.logm(A)')
print(np.mean(A - linalg.expm(linalg.logm(A))))
print()

print('Avg. value of A - e^logm.agm(A)')
print(np.mean(A - linalg.expm(logm(A))))
print()
