single_ways = [1] + [0 for _ in range(180)]
for n in range(20):
    n += 1
    single_ways[n] += 1
    single_ways[2 * n] += 1
    single_ways[3 * n] += 1

single_ways[25] += 1
single_ways[50] += 1

def trititions(n):
    partitions = []
    for i in range(int((n + 2) / 3), n + 1):
        for j in range(int((n - i + 1) / 2), min(i, n - i) + 1):
            partitions.append([i, j, n - i - j])
    return partitions

double = [0, 1, 3, 6]
triple = [0, 1, 4, 10]

ways = []

for n in range(181):
    partitions = trititions(n)
    
    ways.append(0)
    for p in partitions:
        if p[0] == p[1] == p[2]:
            ways[-1] += triple[single_ways[p[0]]]
        else:
            if p[0] == p[1]:
                ways[-1] += double[single_ways[p[0]]] * single_ways[p[2]] 
            elif p[1] == p[2]:
                ways[-1] += single_ways[p[0]] * double[single_ways[p[1]]]
            else:
                ways[-1] += single_ways[p[0]] * single_ways[p[1]] * single_ways[p[2]]

    print('%d: %d' % (n, ways[-1]))

perfect = 0
for n in range(151, 181):
    perfect += ways[n] * ways[301 - n]
print('%d perfect games' % perfect)
