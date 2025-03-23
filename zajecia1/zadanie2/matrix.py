class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, om):
        return Matrix(self.a + om.a, self.b + om.b,
                      self.c + om.c, self.d + om.d)

    def __mul__(self, om):
        return Matrix(self.a * om.a + self.b * om.c, self.a * om.b + self.b * om.d,
                      self.c * om.a + self.d * om.c, self.c * om.b + self.d * om.d)

    def __str__(self):
        return f'\t|\t{self.a}\t|\t{self.b}\t|\n\t|\t{self.c}\t|\t{self.d}\t|\n'

    def __repr__(self):
        return f'Matrix({self.a}, {self.b}, {self.c}, {self.d})'


m1 = Matrix(1,2,3,4)
m2 = Matrix(2,0,1,2)
m3 = m1 + m2
m4 = m1 * m2

print(m1)
print(m2)
print(m3)
print(m4)

print(repr(m1))
print(repr(m2))
print(repr(m3))
print(repr(m4))

