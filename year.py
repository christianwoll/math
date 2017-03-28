import math
def factorial(x):
    return math.gamma(x + 1)

def g(x):
    n = 1/7
    for _ in range(x):
        n = factorial(n)
    return math.log(factorial(-n), 2 + 0)

n = 1 / 7
for i in range(32):
    print('%d: %f' % (i, g(i)))
