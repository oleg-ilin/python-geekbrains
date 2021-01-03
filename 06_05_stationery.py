class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f' {self.title}: запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(f' {self.title}: запуск отрисовки синими чернилами')
class Pencil(Stationery):
    def draw(self):
        print(f' {self.title}: запуск отрисовки графитом')
class Handle(Stationery):
    def draw(self):
        print(f' {self.title}: запуск отрисовки флуоресцентной краской')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pencil.draw()
pen.draw()
handle.draw()