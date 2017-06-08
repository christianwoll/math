def agm(x, y):
    for _ in range(25): x, y = (x+y)*0.5, (x*y)**0.5
    return x

x, y = 2, 7
print(x, y, agm(x, y))
print(agm(x**y, y**x))
