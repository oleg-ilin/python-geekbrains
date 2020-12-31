
class Worker:
    def __init__(self, name, surname, position, wage, bonus):

        d = {"wage": 100000, "bonus": 50000}

        self.name = name
        self.surname = surname
        self.position = position
        self._income = (d[wage]) + (d[bonus])



class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)
    def get_total_income(self):
        print(f'Доход с учетом премии:  {self._income}')

worker = Position('Дональд', 'Трамп', 'президент', 'wage', 'bonus')
worker.get_full_name()
worker.get_total_income()




