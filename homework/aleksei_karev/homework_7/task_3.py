result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def extract_number(input_string: str):
    key, value = input_string.split(': ', maxsplit=1)
    return int(value)


def print_incremented_result(*args, increment=10):
    for number in args:
        print(extract_number(number) + increment)


print_incremented_result(result_1, result_2, result_3, result_4)
