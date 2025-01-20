PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')
items, prices = [x.split()[0] for x in new_list], [y.split()[1] for y in new_list]
prices = list(map(lambda x: int(x.rstrip('р')), prices))
print(dict(zip(items, prices)))
