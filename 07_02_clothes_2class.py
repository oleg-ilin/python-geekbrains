'''Вариант с двумя классами'''

from abc import ABC, abstractmethod

class ParentClass(ABC):

    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    def calc(self):
        pass


class Coat(ParentClass):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def calc(self):
        textile_01 = round((self.value / 6.5 + 0.5), 2)
        return (f'Расход ткани на пальто: {textile_01}')


class Suit(ParentClass):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def calc(self):
        textile_02 = round((self.value * 2 + 0.2), 2)
        return (f'Расход ткани на костюм: {textile_02}')


class Clothes:
    def sum(self, c, s):
        self.c = c
        self.s = s
        sum = round((self.c / 6.5 + 0.5), 2) + round((self.s * 2 + 0.2), 2)
        return (f'Общий расход ткани: {sum}')

v = 50
h = 2
c = Coat(v)
s = Suit(h)
sum = Clothes()
print(c.calc())
print(s.calc())
print(sum.sum(v, h))



