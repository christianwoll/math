import random
import numpy as np

a = 11
b = 3
c = 19
d = 66

T = a + b + c + d

K = 50
for e, i, g, f in np.ndindex((K,K,K,K)):
    e,i,g,f = e+1, i+1, g+1, f+1

    m = T - i - e - a
    j = T - m - g - d

    k = (d + 2*T - e - g - i - j - a) / 2 - f
    if k % 1: continue
    else: k = int(k)

    h = T - e - f - g
    l = T - i - j - k
    n = T - b - f - j
    o = T - c - g - k
    p = T - a - f - k

    if len(set([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])) < 16: continue
    if any(n <= 0 for n in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]): continue
    square = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]
    break

print('\n'.join(['\t'.join([str(n) for n in row]) for row in square]))
