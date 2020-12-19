def func(name, s_name, year, city, mail, phone):
    print(f"Пользователь: {name} {s_name}, Год рождения: {year}, Город проживания: {city}, "
          f"E-mail: {mail}, Телефон: {phone}")
name = input("Введите имя ")
s_name = input("Введите фамилию ")
year = input("Введите год рождения ")
city = input("Введите город проживания ")
mail = input("Введите E-mail ")
phone = input("Введите номер телефона ")
func(name, s_name,year,city,mail, phone)
