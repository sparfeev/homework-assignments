first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and third == first and third == second:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and third or second != third:
    print(0)
