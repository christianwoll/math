import sys
import numpy as np
import scipy
from scipy import linalg

if len(sys.argv) < 3:
    print('Usage: nasik_dimension.py <#dimension> <#order>')
    sys.exit(0)

# n dimensions
n = int(sys.argv[1])

# k order
k = int(sys.argv[2])

# Generate all vectors such that each one increments over a line-sum
# in the magic square.
vectors = []
for v in np.ndindex((3,)*n):
    v = tuple(1-x for x in v)
    if not any(v): continue
    if tuple(-x for x in v) in vectors: continue
    vectors.append(v)

# Use the line-sum vectors to iterate over all line-sums.
A = []
for v in vectors:
    # Iterate over over the free dimensions
    for coords in np.ndindex((k,)*(v.count(0))):
        u = [0 if x == 1 else k-1 if x == -1 else None for x in v]
        for x in coords: u[u.index(None)] = x

        start_v = np.array(u)
        step_v = np.array(v)
        points = [start_v + i * step_v for i in range(k)]

        row = np.zeros((k**n,), dtype=np.uint8)
        for point in points: row[sum([x * k**i for i, x in enumerate(point)])] = 1
        A.append(row)

A = np.array(A)
print('Line-sum matrix shape:', A.shape)

"""
from PIL import Image
Image.fromarray(A*255).show()
"""


from sympy import Matrix
M = Matrix([row.tolist() for row in A])
nullspace = M.nullspace()
for v in nullspace: print([x for x in v])
print('Dimension:', len(nullspace))
