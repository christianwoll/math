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

def alpha(p):
    return Param(p.c - p.a, p.b, p.c)

def alpha_inv(p):
    return alpha(p)

def beta(p):
    return Param(p.a, p.c - p.b, p.c)

def beta_inv(p):
    return beta(p)

def gamma(p):
    if p.c != 2 * p.b: return None
    return Param(p.a / 2, p.b - p.a / 2, p.b + Fraction(1,2))

def gamma_inv(p):
    if p.c != p.a + p.b + Fraction(1,2): return None
    return Param(p.a * 2, p.a + p.b, p.a * 2 + p.b * 2)

def delta(p):
    if p.c != (p.a + p.b + 1) / 2: return None
    return Param((p.a + 1) / 2, (p.b + 1) / 2, Fraction(3,2))

def zeta(p):
    return Param(p.a, p.b, p.a + p.b - p.c + 1)


# c = a + b - 1/2

def quad1(p):
    if p.c != p.a + p.b - Fraction(1,2): return None
    return Param(p.a * 2 - 1, p.b * 2 - 1, p.c)

def quad2(p):
    if p.c != p.a + p.b - Fraction(1,2): return None
    return Param(p.a * 2 - 1, p.a - p.b + Fraction(1,2), p.c)

def quad3(p):
    if p.c != p.a + p.b - Fraction(1,2): return None
    return Param(p.a * 2 - 1, p.a + p.b - 1, p.a * 2 + p.b * 2 - 2)



# c = a + b + 1/2

def quad4(p):
    if p.c != p.a + p.b + Fraction(1,2): return None
    return Param(p.a * 2, p.b * 2, p.c)

def quad5(p):
    if p.c != p.a + p.b + Fraction(1,2): return None
    return Param(p.a * 2, p.a - p.b + Fraction(1,2), p.c)

def quad6(p):
    if p.c != p.a + p.b + Fraction(1,2): return None
    return Param(p.a * 2, p.b * 2, p.c)



# c = a - b + 1

def quad7(p):
    if p.c != p.a - p.b + 1: return None
    return Param(p.a / 2, (p.a + 1) / 2 - p.b, p.c)

def quad8(p):
    if p.c != p.a - p.b + 1: return None
    return Param((p.a + 1) / 2, p.a / 2 - p.b + 1, p.c)

def quad9(p):
    if p.c != p.a - p.b + 1: return None
    return Param(p.a / 2, (p.a + 1) / 2, p.c)

def quad10(p):
    if p.c != p.a - p.b + 1: return None
    return Param((p.a + 1) / 2 - p.b, p.a / 2 - p.b + 1, p.c)

def quad11(p):
    if p.c != p.a - p.b + 1: return None
    return Param(p.a, p.a - p.b + Fraction(1,2), p.a * 2 - p.b * 2 + 1)



# c = (a + b + 1) / 2

def quad12(p):
    if p.c != (p.a + p.b + 1) / 2: return None
    return Param(p.a / 2, p.b / 2, p.c)

def quad13(p):
    if p.c != (p.a + p.b + 1) / 2: return None
    return Param((p.a + 1) / 2, (p.b + 1) / 2, p.c)

def quad14(p):
    if p.c != (p.a + p.b + 1) / 2: return None
    return Param(p.a / 2, (p.a + 1) / 2, p.c)

def quad15(p):
    if p.c != (p.a + p.b + 1) / 2: return None
    return Param(p.a, (p.a + p.b) / 2, p.a + p.b)



# b = a + 1/2

def quad16(p):
    if p.b != p.a + Fraction(1/2): return None
    return Param(p.a * 2, p.c * 2 - p.a * 2 - 1, p.c)

def quad17(p):
    if p.b != p.a + Fraction(1/2): return None
    return Param(p.a * 2, p.c - Fraction(1,2), p.c * 2 - 1)


def cubic(p):
    if p.b != p.a + Fraction(1,2) or p.c != (p.a * 4 + 2) / 3: return None
    return Param(p.a / 3, p.a / 3 + Fraction(1,2), (p.a * 4 + 5) / 6)

functions = [
    (alpha, 'A'),
    (beta, 'B'),
    (gamma, 'C'),
    (gamma_inv, 'C^-1'),
    (zeta, 'Z'),
    (cubic, 'U'),
    #((quad1, 'Q1'),
    #((quad2, 'Q2'),
    #((quad3, 'Q3'),
    #((quad4, 'Q4'),
    #((quad5, 'Q5'),
    #((quad6, 'Q6'),
    #((quad7, 'Q7'),
    #((quad8, 'Q8'),
    #((quad9, 'Q9'),
    #((quad10, 'Q10'),
    #((quad11, 'Q11'),
    #((quad12, 'Q12'),
    #((quad13, 'Q13'),
    #((quad14, 'Q14'),
    #((quad15, 'Q15'),
    #((quad16, 'Q16'),
    #(quad17, 'Q17'),
    ]

x = Param(Fraction(1,2), Fraction(1,2), Fraction(1))
x = gamma(x)
x = beta(x)
x = cubic(x)

triples = [x]
paths = [[]]

for dist in range(11):
    for trp, path in zip(triples, paths):
        if len(path) > dist: continue
        for f in functions:
            trp_ = f[0](trp)
            if not trp_ is None and not trp_ in triples:
                triples.append(trp_)
                paths.append(path + [f[1]])

for trp, path in zip(triples, paths):
    if trp.b == trp.c == Fraction(1): 
        print('EXPONENTIAL')
    if trp.a == trp.b == Fraction(1) and trp.c == Fraction(2): 
        print('LOGARITHM')
    if trp.a == trp.b == Fraction(1,2) and trp.c == Fraction(3,2):
        print('ARCSIN')
    print(path, trp)
            
print(len(triples))
