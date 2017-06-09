import sys
import math

# sqrt is an integet square root function using
# Newton's method.
def sqrt(n):
    x = n
    y = (x+1) // 2
    while y < x: x, y = y, (y + n // y) // 2
    return x

# K is the number of digits to calculate.
# 3 is added for a precision loss buffer.
K = int(sys.argv[1]) + 3

# Initial values
a, b = 10**K, sqrt(2 * 10**(2*K)) // 2
t = 10**K // 4

# Iterate using Gauss Legendre-algorithm
for i in range(int(math.log(K, 2))):
    t = t - 2**i * ((a - b) // 2)**2 // 10**K
    a, b = (a + b) // 2, sqrt(a * b)

# All done
pi = (a + b)**2 // (4 * t)
print('3.' + str(pi)[1:-3])

print('1.' + str(sqrt(pi * 10**K))[1:-3])
