def print_params (a = 1,b = 'str',c = True):
    print(a,b,c)


print_params(1,'str',True)
print_params(1)
print_params(1,'1')
print_params(b=25)
print_params(c=[1,2,3])

values_list = [2,'str',5.5]
values_dict = {'a' : 45, 'b' : 'str','c' : 55.66}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [8.4,'str']
print_params(*values_list_2,42)