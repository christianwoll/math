import sys
import random

def norm(x):
    return [
        x[0]**2 - x[1]**2 + x[2]**2 - x[3]**2, 
        2*x[0]*x[1] + 2*x[2]*x[3]]

def mul(x, y):
    return [
        x[0]*y[0] - x[1]*y[1] - x[2]*y[2] + x[3]*y[3],
        x[0]*y[1] + x[1]*y[0] - x[2]*y[3] - x[3]*y[2],
        x[0]*y[2] - x[1]*y[3] + x[2]*y[0] - x[3]*y[1],
        x[0]*y[3] + x[1]*y[2] + x[2]*y[1] + x[3]*y[0]]

def neg(x):
    return [x[0], x[1], -x[2], -x[3]]

def sub(x, y):
    return [
        x[0] - y[0],
        x[1] - y[1],
        x[2] - y[2],
        x[3] - y[3]]

def f(X):
    if len(X) <= 1: return X
    return f([mul(X[0], X[1])] + X[2:]) + f([mul(neg(X[0]), X[1])] + X[2:])

X = [random.sample(range(1, 12), 4) for _ in range(10)]
Y = [mul(mul(x, x), mul(x, x)) for x in X]
Z = f(Y)

for x in X: print(x)
print()
for y in Y: print(y)
print()
for z in Z: print(z)

A = []
for i, z1 in enumerate(Z):
    for z2 in Z[i+1:]:
        A.append(sub(z1, z2))
print('A')
for a in A: 
    if A.count(a) > 1: print(a)
