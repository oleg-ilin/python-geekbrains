class CheckZero(Exception):
    def __init__(self, param_1):
        self.param_1 = param_1


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if b == 0:
        raise CheckZero('Вы пытаетесь разделить на ноль')
    else:
        c = a / b
        print(c)
except CheckZero as error:
    print(error)



