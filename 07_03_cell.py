class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        new_cell = self.number + other.number
        return f'Результат слжоения двух клеток: {new_cell}'

    def __sub__(self, other):
        new_cell = self.number - other.number
        if new_cell < 0:
            return f'Результат вычетани отрицательный'
        else:
            return f'Результат вычетания второй клетки из первой: {new_cell}'

    def __mul__(self, other):
        new_cell = self.number * other.number
        return f'Результат умножения двух клеток: {new_cell}'

    def __truediv__(self, other):
        new_cell = round(self.number / other.number)
        return f'Результат деления: {new_cell}'

    def make_order(self, line):
        arr = ''
        for i in range(int(self.number / line)):
            arr += '*' * line + '\n'
        arr += '*' * (self.number % line) + '\n'
        return arr


cell_1 = Cell(56)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))

