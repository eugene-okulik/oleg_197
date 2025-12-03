my_dict = {
    'tuple': (56, 2, False, '4', 5),
    'list': ['text', 50.2, 531, 21, True],
    'dict': {'Name': 'Oliver', 'Second Name': 'Brown' ,'Age': 13, 'Height': 143, 'Sex': 'male'},
    'set': {None, 'text', 39, 15, 'last'}
    }

print(my_dict['tuple'][-1])

my_dict['list'].append('new_element')
print(my_dict['list'])

my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict']['i am a tuple'] = 'some value'
print(my_dict['dict'])

my_dict['dict'].pop('Sex')
print(my_dict['dict'])

my_dict['set'].add(True)
print(my_dict['set'])

my_dict['set'].discard(None)
print(my_dict['set'])
