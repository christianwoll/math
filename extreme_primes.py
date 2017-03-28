primes = [2]
extreme_primes = [2]
print('1: 2')

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
