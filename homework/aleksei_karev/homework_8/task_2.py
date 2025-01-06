def fibonacci_seq():
    num1 = 1
    num2 = 1
    while True:
        yield num2
        num1, num2 = num2, num1 + num2


index = int(input("Введите индекс числа: "))
count = 2
if index == 0:
    print(0)
elif index == 1:
    print(1)
else:
    for num in fibonacci_seq():
        if count == index:
            print(num)
            break
        count += 1
