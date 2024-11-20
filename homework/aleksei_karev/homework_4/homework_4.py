import pprint

my_dict = {
    'tuple': (15, 'text', True, 1.0, 2),
    'list': [1, 1.5, None, False, 'Alex'],
    'dict': {'key': 'value', '1': 2, 'True': False, 'Object': None, 'Java': 'Not Python'},
    'set': {1, True, 5, 'test', 4}
}

tuple_last_element = my_dict.get('tuple')[-1]
print(tuple_last_element, end='\n\n')

list_to_change = my_dict.get('list')
print(list_to_change)
list_to_change.append(1)
list_to_change.pop(1)
print(list_to_change, end='\n\n')

dict_to_change = my_dict.get('dict')
print(dict_to_change)
dict_to_change[('i am a tuple',)] = ('tuple1', 12, 1.3)
dict_to_change.pop('1')
print(dict_to_change, end='\n\n')

set_to_change = my_dict.get('set')
print(set_to_change)
set_to_change.add('add')
set_to_change.discard(True)
print(set_to_change, end='\n\n')

pprint.pprint(my_dict)