class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        new_arr = ''
        for el in self.arr:
            new_arr += (str(el) + '\n')
        return new_arr

    def __add__(self, other):
        new_arr = ''
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                self.arr[i][j] = self.arr[i][j] + other.arr[i][j]
        for el in self.arr:
            new_arr = new_arr + (str(el) + '\n')
        return new_arr


m_1 = Matrix([[31, 22, 1], [37, 43, 1], [51, 86, 1]])
m_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m_1)
m_3 = m_1 + m_2
print(m_3)
