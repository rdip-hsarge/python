class Complex:

    def __init__(self, a, b):
        self.real = a
        self.imagine = b

    def __str__(self):
        return f'{self.real} + ({self.imagine})*i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imagine + other.imagine)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imagine - other.imagine)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imagine * other.imagine,
                self.real * other.imagine + self.imagine * other.real)

num1 = Complex(2, 3)
num2 = Complex(3, 4)

# print(num1)
# print(num1 - num2)
# print(num1 * num2)