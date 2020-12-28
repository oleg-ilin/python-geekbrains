'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.'''

with open('user_file.txt', 'a', encoding='UTF-8') as file:
    while True:
        content = (input("Введите данные: "))
        file.writelines(content + '\n')
        if not content:
            break

