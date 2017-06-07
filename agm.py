from quaternion import Quaternion

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



# AGM function definition
def agm(x, y=1):
    for _ in range(40): x, y = (x+y)*0.5, (x*y)**0.5
    return x



# Generate a lattice
X = Y = Z = 10
sx = sy = sz = 1
lattice = [(x*sx, y*sy, z*sy) for x in range(int(X/sx)) for y in range(int(Y/sy)) for z in range(int(Z/sz))]



# Transform the lattice with AGM
transformed = []
for p in lattice:
    q = Quaternion(1, p[0], p[1], p[2])
    Q = agm(q)
    transformed.append((Q.b/Q.a, Q.c/Q.a, Q.d/Q.a))



# Display the transformed lattice
ax.scatter(*zip(*transformed))
plt.show()
