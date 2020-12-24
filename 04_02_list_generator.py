'''
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
'''
my_list = [1, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 555]
new_list = [el for el in my_list if 0 < my_list.index(el) < (len(my_list)) and my_list[my_list.index(el)] > my_list[my_list.index(el) - 1]]
print(new_list)
# new_list = []
# for el in my_list:
#     if my_list.index(el) > 0:
#         if my_list.index(el) < (len(my_list)):
#             if my_list[my_list.index(el)] > my_list[my_list.index(el)-1]:
#                 new_list.append(el)
















# new_list = [el for el in my_list]




# print(f"Исходный список: {my_list}")
# print(f"Новый список: {new_list}")
# print(type(my_list[10]))
# print(my_list[10])