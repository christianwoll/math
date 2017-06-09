primes = [2]
extreme_primes = [2]
print('1: 2')

"""
An extremem prime is defined recursively.
The (N+1)th extreme prime is the Pth prime
where P is the Nth prime.

2 is the first extreme prim
3 is the 2nd prime
5 is the 3rd prime
11 is the 5th prime
31 is the 11th prime
...
"""

next = 3
while True:
    is_prime = True
    root = next**(1/2)
    for p in primes:
        if next % p == 0:
            is_prime = False
            break
        if p > root:
            break
    if is_prime:
        primes.append(next)
        if len(primes) == extreme_primes[-1]:
            extreme_primes.append(next)
            print('%d: %d' % (len(extreme_primes), next))
    next += 2
