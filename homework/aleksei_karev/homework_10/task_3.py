first_num, second_num = map(int, input("Введите два числа через пробел: ").split())


def new_calc(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second > 0 and first > 0:
            return func(second, first, '-')
        elif second > first > 0 and second > 0:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@new_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(first_num, second_num))
