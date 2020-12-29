'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open("program_file.txt", "w", encoding="UTF-8") as file_01:
    listing = input("Введите числа через пробел: ").split('_')
    file_01.writelines(listing)
with open("program_file.txt", "r", encoding="UTF-8") as file_02:
    listing = file_02.read()
    listing = (list(map(int, listing.split())))
    sum = 0
    for el in listing:
        sum = sum + el
    print("Сумма введенных чисел: ", sum)

