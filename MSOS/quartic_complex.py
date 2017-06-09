from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def fourth(z):
    x, y = z
    return (x**4-6*x**2*y**2+y**4,4*x*y*(x**2-y**2))

def add(Z):
    x, y = 0,0
    for z in Z:
        x += z[0]
        y += z[1]
    return x,y

k = 6
points = [(x,y) for x in range(1-k,k) for y in range(1-k,k)]

F = [fourth(z) for z in points]
plt.scatter(*zip(*[add([a,b,c]) for a in F for b in F for c in F]))
plt.show()
