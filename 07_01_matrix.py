class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        for el in self.arr:
            print(f'{el}')

    def __add__(self, other):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                self.arr[i][j] = self.arr[i][j] + other.arr[i][j]
        for result in self.arr:
            print(result)


m_1 = Matrix([[31, 22, 1], [37, 43, 1], [51, 86, 1]])
m_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m_1.__str__()
print(m_1 + m_2)


