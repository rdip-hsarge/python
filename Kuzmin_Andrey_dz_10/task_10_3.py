class Cell:

    def __init__(self, num):
        self.num = num

    def make_order(self, cells_in_row = 10):
        all_cell = '*' * self.num
        self.cells_in_row = cells_in_row
        result_cell = ''
        for i in range(0, self.num, self.cells_in_row):
            result_cell += f'{all_cell[i:i + self.cells_in_row]}\n' # Если добавить \ перед n, вывод будет в одну строку
        return result_cell

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num >= other.num:
            return Cell(self.num - other.num)
        else:
            return f'Не корректная операция (нельзя от меньшего числа ({self.num}) отнять больше, чем оно само)'

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def __floordiv__(self, other):
        return Cell(self.num // other.num)

a = Cell(32)
b = Cell(64)
c = Cell(3)
print(a + b) # 96
print(a - b) # Не корректная операция (нельзя от меньшего числа (32) отнять больше, чем оно само)
print(a * c) # 96
print(a / c) # 10
print(a / c) # результат как и в прошлом вызове принта 10
print(c.make_order(15)) # ***