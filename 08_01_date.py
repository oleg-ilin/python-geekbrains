class Date:
    # def __init__(self, date):
    #     self.date = date
    #     print(date)


    @classmethod
    def get_int(cls, date):
        cls.date = date
        d = int(cls.date[0:2])
        m = int(cls.date[3:5])
        y = int(cls.date[6:10])
        return d, m, y

    @staticmethod
    def validation(date):
        d = int(date[0:2])
        m = int(date[3:5])
        y = int(date[6:10])
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            d_max = 31
        elif m == 2:
            print(f'{y} год')
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                d_max = 29
                print(f'Это високосный год, в феврале 29 дней')
            else:
                d_max = 28
                print("Это не високосный год, в феврале 28 дней")
        elif m == 4 or m == 6 or m == 9 or m == 11:
            d_max = 30
        if m >= 1 and m <= 12 and d >= 1 and d <= d_max:
            print("Дата корректна")
        else:
            print("Дата некорректна")


print(Date.get_int('12-01-2020'))
Date.validation('29-02-2001')


