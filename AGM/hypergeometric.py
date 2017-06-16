from fractions import Fraction

class Param:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        X = [(f.numerator, f.denominator) for f in (self.a, self.b, self.c)]
        return '(' + ', '.join([str(n) + '/' + str(d) for n,d in X]) + ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

def omega(p):
    return Param(p.b, p.a, p.c)

def alpha(p):
    return Param(p.c - p.a, p.b, p.c)

def beta(p):
    # return omega(alpha(omega(p))) # Same thing.
    return Param(p.a, p.c - p.b, p.c)

def gamma(p):
    return Param(p.a, p.b, Fraction(1) + p.a + p.b - p.c)

def zeta(p):
    if p.c != 2 * p.b: return None
    return Param(p.a / 2, p.b - p.a / 2, p.b + Fraction(1,2))

functions = (alpha, beta, gamma, zeta)

x = Param(Fraction(1,2), Fraction(1,2), Fraction(1))
x = zeta(x)
x = gamma(x)
x = zeta(x)
x = gamma(x)
x = alpha(x)
x = beta(x)

print(x)
print()

for f in functions: print(f(x), f, f(x) is None or x == f(x))
