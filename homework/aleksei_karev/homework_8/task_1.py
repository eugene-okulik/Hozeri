from random import randrange, choice

salary = int(input("Введите вашу зарплату: "))
bonus = choice([True, False])
bonus_amount = randrange(500, 1000)
if bonus:
    print(f'{salary}, {bonus} - ${salary + bonus_amount}')
else:
    print(f'{salary}, {bonus} - ${salary}')
