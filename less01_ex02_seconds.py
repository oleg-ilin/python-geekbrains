number_sec = int(input("Введите количество секунд "))
hours = number_sec // 3600
minutes = (number_sec % 3600) // 60
seconds = number_sec - hours * 3600 - minutes * 60
print("%02d:%02d:%02d" %(hours, minutes, seconds))
