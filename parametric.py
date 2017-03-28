import sys

def gen_terms(m, M, num_vars):
    if num_vars == 1:
        return [[n] for n in range(m, M)]
    return [[n] + l for n in range(m, M) for l in gen_terms(m, M, num_vars - 1)]

def nartitons(total, M, n):
    if total > M:
        return []
    if n == 1:
        return [total]
    for t in range(0, total):
        


print(gen_terms(-2, 2, 3))
