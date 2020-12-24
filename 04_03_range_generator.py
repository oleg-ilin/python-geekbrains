'''Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.'''

print(list(el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0))

# generator = list(el for el in range(20, 241))
# my_list_20 = [el for el in generator if el%20 == 0]
# my_list_21 = [el for el in generator if el%21 == 0]
# print("Числа, кратные 20: ", my_list_20)
# print("Числа, кратные 21: ", my_list_21)
