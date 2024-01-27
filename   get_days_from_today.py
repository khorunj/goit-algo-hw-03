from datetime import datetime
def get_days_from_today(date):
    while True:
        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
            nt = datetime.today() - dt
            return nt.days
            break

        except ValueError:
            print("Не корректний ввід дати. Спробуй ще")
            date = input('Введіть дату у форматі РРРР-ММ-ДД')

    
date = input('Введіть дату у форматі РРРР-ММ-ДД')
print(get_days_from_today(date))
