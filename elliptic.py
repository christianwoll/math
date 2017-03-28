n = 6
x1, y1 = 12, 36
C = []
print('Generating solutions...')
for _ in range(2**12):
    C.append((x1**2 + n**2) / y1)
    m = (3 * x1**2 - n**2) / (2 * y1)
    x2 = m**2 - 2 * x1
    y2 = m * (x2 - x1) + y1
    x1, y1 = x2, abs(y2)

best = 1
for c1 in C:
    for c2 in C:
        if c1 <= c2: continue
        b = 2 * c2**2 - c1**2
        for c3 in C:
            if abs(c3**2 - b) < best:
                best = abs(c3**2 - b)
                print('Error:', best)
                print(c1, c2, c3)
                print(c1**2 - c2**2, c2**2 - c3**2)
                print()
