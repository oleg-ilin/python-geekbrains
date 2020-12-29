'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.'''

with open("text4.txt", "r", encoding="UTF-8") as file:
    rus = ["Один", "Два", "Три", "Четыре"]
    eng = ["One", "Two", "Three", "Four"]
    with open('user_file.txt', 'w', encoding='UTF-8') as new_file:
        for i in range(4):
            content = file.readline()
            new_file.write(content.replace(eng[i], rus[i]))





