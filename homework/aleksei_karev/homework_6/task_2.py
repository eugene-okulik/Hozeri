seq = list(range(1, 101))

for elem in seq:
    if elem % 3 == 0 and elem % 5 == 0:
        print('FuzzBuzz')
    elif elem % 3 == 0:
        print('Fuzz')
    elif elem % 5 == 0:
        print('Buzz')
    else:
        print(elem)
