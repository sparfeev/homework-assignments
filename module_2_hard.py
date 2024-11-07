list1_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2_ =[]
for i in list1_:
    for j in range(1,20):
        for n in range(2,20):
            if n <= j:
                continue
            if i % (j + n) == 0:
                print(f'{i} = {j}{n}')

