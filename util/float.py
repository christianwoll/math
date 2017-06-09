"""
Arbitrary precision float class
"""

class Float:
    def __init__(self, n, d):
        self.n = n # n is usually a large int
        self.d = d # d is the places

    def __add__(self, other):
        a, b = self.n, other.n
        if self.n//10**self.K < other.n//10**other.K: 
            a,b = b, a
        b = b // 10**(other.K - self.K)
