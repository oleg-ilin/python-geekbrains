class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехал(а)')
    def stop(self):
        print(f'{self.color} {self.name} совершил(а) остановку')
    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернул(а) {direction} ')
    def show_speed(self):
        print(f'текущая скорость {self.color} {self.name} {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превысил(а) скорость')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превысил(а) скорость')
class PoliceCar(Car):
    pass
car_1 = Car(100, 'белая', 'Тойота')
car_2 = TownCar(80, 'черная', 'Хонда')
car_3 = WorkCar(80, 'зеленый', 'Форд')
car_4 = SportCar(200, 'красная', 'Феррари')
car_5 = PoliceCar(160, 'синяя', 'Лада', True)
car_1.go()
car_1.show_speed()
car_1.stop()
car_1.turn("направо")
car_2.go()
car_2.show_speed()
car_3.go()
car_3.show_speed()
car_3.stop()
car_3 = WorkCar(0, 'зеленый', 'Форд')
car_3.show_speed()
car_4.go()
car_5.go()
car_5.show_speed()
