import sys
import time
import random
import numpy as np
from PIL import Image

width = 360
height = 640

parents = 5
rule = [1 if random.random() > 0.5 else 0 for _ in range(2**parents)]

#parents = 3;rule = [0, 1, 1, 1, 0, 1, 1, 0]

states = [1 if random.random() > 0.5 else 0 for _ in range(width)]

#states = [0] * width;states[width // 2] = 1

data = []
for _ in range(height):
    data.append([[255]*3 if n==0 else [0]*3 for n in states])
    parent_states = states[-(parents // 2):] + states + states[:parents - parents // 2 - 1]
    states = [rule[sum([2**j * n for j, n in enumerate(parent_states[i:i+parents])])] for i in range(len(states))]

Image.fromarray(np.array(data, dtype=np.uint8)).show()
