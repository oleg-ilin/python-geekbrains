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
        self.value = value

    def calc(self):
        global textile_01
        textile_01 = 0
        textile_01 = round((self.value / 6.5 + 0.5), 2)
        return (f'Расход ткани на пальто: {textile_01}')


class Suit(ParentClass):
    def __init__(self, value):
        self.value = value

    def calc(self):
        global textile_02
        textile_02 = 0
        textile_02 = round((self.value * 2 + 0.2))
        return (f'Расход ткани на костюм: {textile_02}')

    def sum(self):
        sum = textile_01 + textile_02
        print(f'Общий расход ткани: {sum}')


c = Coat(50)
s = Suit(2)
sum = Suit(1)
print(c.calc())
print(s.calc())
sum.sum()

