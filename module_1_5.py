immutable_var = (12,'cat','dog',True)
print(immutable_var)
 #элементы кортежа не изменяются
mutable_list = [43,60,'sergey','ivan']
print(mutable_list)
mutable_list[0] = 88
print(mutable_list)
mutable_list.extend([True,146])
print(mutable_list)
mutable_list.remove('sergey')
print(mutable_list)