words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_keys(words_to_print):
    for key, value in words_to_print.items():
        i = 0
        while i <= value:
            i += 1
            print(key, end='')
        print()


print_keys(words)
