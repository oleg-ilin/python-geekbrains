class CheckInt(ValueError):
    def __init__(self, param_1):
        self.param_1 = param_1

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

my_list = []
while True:
    try:
        a = input('Введите число: ')
        if a == "stop":
            break
        if a.isdigit():
            my_list.append(int(a))
        if isfloat(a):
            my_list.append(float(a))
        else:
            raise CheckInt ('Вы ввели строку')
    except CheckInt as error:
        print(error)
print(my_list)

