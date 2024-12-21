number_to_guess = 56

while True:
    input_number = int(input("Введите число: "))
    if number_to_guess == input_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print('Попробуйте снова')
