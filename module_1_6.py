my_dict = {'Sergey': 174,'Oly': 165,'Bob': 180}
print(my_dict)
my_dict['Anton'] = 150
print(my_dict)
my_dict.update({'Anna': 170,
                'Grin': 120})
print(my_dict)
a =my_dict.pop('Sergey')
print(a)

# множества
my_set = {1,1,56,45,56,'cat','dog',56,'cat'}
print(my_set)
my_set.update((755,88))
my_set.discard(56)
print(my_set)