result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
total_result = 'результат работы программы: 9'


def extract_number(input_string: str):
    index = input_string.index(':')
    number = int(input_string[index + 2:])
    return number


increment = 10

number_1 = extract_number(result_1) + increment
number_2 = extract_number(result_2) + increment
number_3 = extract_number(total_result) + increment

print(number_1 + number_2 + number_3)
