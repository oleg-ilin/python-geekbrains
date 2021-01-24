'''Вариант с одним общим классом'''

from abc import ABC, abstractmethod

class ParentClass(ABC):
    def sum(self):
        sum = textile_01 + textile_02
        print(f'Общий расход ткани: {sum}')

    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class Clothes(ParentClass):
    def __init__(self, value):
        self.value = value

    def coat(self):
        global textile_01
        textile_01 = 0
        textile_01 = round((self.value / 6.5 + 0.5), 2)
        return (f'Расход ткани на пальто: {textile_01}')

    def suit(self):
        global textile_02
        textile_02 = 0
        textile_02 = round((self.value * 2 + 0.2))
        return (f'Расход ткани на костюм: {textile_02}')


c = Clothes(50)
s = Clothes(2)
sum = Clothes(1)
print(c.coat())
print(s.suit())
sum.sum()
