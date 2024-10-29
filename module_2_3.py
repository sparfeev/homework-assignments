my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
index = 0
while index < len(my_list):
    if my_list[index] == 0:
        my_list.pop(index)
        continue
    elif my_list[index] < 0:
        break
    else:
        print(f"{my_list[index]} ")
    index += 1

