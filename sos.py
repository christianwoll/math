def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

def dot(p, q):
    return tuple(sorted([abs(p[0]*q[0]+p[1]*q[1]), abs(p[0]*q[1]-p[1]*q[0])]))

def square(p):
    return dot(p, (p[0], -p[1]))

def congruum(p):
    return 4*p[0]*p[1]*(p[1]*p[1]-p[0]*p[0])

def merge(P):
    if len(P) == 1: return P
    return merge([dot(P[0], P[1])] + P[2:]) + merge([dot(P[0], (P[1][0], -P[1][1]))] + P[2:])

P = [(m, n) for m in range(2, 2**5) for n in range(1, m)]
S = [square(square(p)) for p in P]

print(len(P))
for i in range(2, len(S)):
    for j in range(1, i):
        for k in range(j):
            a, b = S[i]
            c, d = S[j]
            e, f = S[k]
            T = [P[i], P[j], P[k]]
            M = merge(T)
            if len(set(M)) < len(M): continue
            C = sorted([abs(a*c*f+b*d*f+a*d*e-b*c*e),
                abs(a*c*f-b*d*f+a*d*e+b*c*e),
                abs(a*c*f+b*d*f-a*d*e+b*c*e),
                abs(a*c*f-b*d*f-a*d*e-b*c*e)])
            if C[2]-C[0]==C[1]: print('low', C)
            if C[2]+C[0]==C[3]: print('high', C)
