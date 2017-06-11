

# Vanilla AGM iteration
def agm(x, y=1):
    for _ in range(5): 
        x, y = (x+y)/2, (x*y)**(1/2)
        print(x, y)
    return x

# Cubically convergent 2-variable AGM-like iteration
def agm3(x, y=1):
    for _ in range(5):
        x, y = (x+2*y)/3, (y*(x*x+x*y+y*y)/3)**(1/3)
        print(x, y)
    return x

# Degree N convergent 2-variable AGM-like iteration
# From Borwein^2
def agmN(x, y=1, N=2):
    for _ in range(5):
        c = (x-y)/N
        x = (x + (N-1)*y)/N
        y = (x**N - c**N)**(1/N)
        print(x,y)
    return x

# 3-variable AGM-like iteration (cubic convergence)
# From math.stackexchange
def agmStack(a, b=1, c=1):
    for _ in range(5):
        R = (a**2*(b+c)+b**2*(c+a)+c**2*(a+b))/6
        I = (a-b)*(b-c)*(c-a) / (2 * (-27)**(1/2))
        a, b, c = (a+b+c)/3, (R+I)**(1/3), (R-I)**(1/3)
        print(a, b, c)
    return a

print('AGM:3')
agmN(10, N=3)
print()

print('AGMGuess')
agmGuess(10)
print()
