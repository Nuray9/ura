class Operation:

    def plus(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def umnoj(self, x, y):
        print(x * y)

    def delenie(self, x, y):
        print(x / y)

    def modul(self, x, y):
        print(abs(7 + 8j))

    def stepen(self, x, y):
        print(pow(x + y, 2))


obj1 = Operation()
x = complex(9, 2)
y = complex(4, 5)

obj1.plus(x, y)

obj1.minus(x, y)

obj1.umnoj(x, y)

obj1.modul(x, y)

obj1.delenie(x, y)

obj1.stepen(x, y)

#Основа
class ComplexNumber:
    def __init__(self, z, v, *args):
        self.z = z
        self.v = v
        self.c = 'z + v * i'

    def __add__(self, other):
        print(f' Cумма c1 и c2 равна:')
        return f'c = {self.z + other.z} + {self.v + other.v}i'

    def __mul__(self, other):
        print(f' Произведение c1 и c2 равно:')
        return f'c = {self.z * other.z - (self.v * other.v)} + {self.v * other.z}i'

    def __str__(self):
        return f'c = {self.z} + {self.v}i'


c_1 = ComplexNumber(5, -9)

c_2 = ComplexNumber(2, 7)

print(c_1 + c_2)
print(c_1 * c_2)
print(c_1)
