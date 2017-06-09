class Quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if isinstance(other, Quaternion):
            return Quaternion(
                self.a + other.a,
                self.b + other.b,
                self.c + other.c,
                self.d + other.d)
        else:
            return Quaternion(
                self.a + other,
                self.b,
                self.c,
                self.d)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            # return (q1 * q2 + q2 * q1) / 2
            return Quaternion(
                self.a*other.a-self.b*other.b-self.c*other.c-self.d*other.d,
                self.a*other.b+self.b*other.a,
                self.a*other.c+self.c*other.a,
                self.a*other.d+self.d*other.a)
        else:
            return Quaternion(
                self.a * other,
                self.b * other,
                self.c * other,
                self.d * other)

    def __pow__(self, other):
        # __pow__ returns the square root every time
        A = ((self.a+(self.a**2+self.b**2+self.c**2+self.d**2)**0.5)/2)**0.5
        return Quaternion(A,0.5*self.b/A,0.5*self.c/A,0.5*self.d/A)

    def __str__(self):
        return str(self.a)+' + ('+str(self.b)+')i + ('+str(self.c)+')j + ('+str(self.d)+')k'

    def __repr__(self):
        return self.__str__()
