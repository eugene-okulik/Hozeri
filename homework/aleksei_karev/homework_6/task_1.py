text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()

for word in words:
    if ',' not in word and '.' not in word:
        print(f'{word}ing ', end='')
    elif ',' in word:
        word = word.replace(',', '')
        print(f'{word}ing, ', end='')
    elif '.' in word:
        word = word.replace('.', '')
        print(f'{word}ing. ', end='')
    else:
        print('There are other punctuation marks')
