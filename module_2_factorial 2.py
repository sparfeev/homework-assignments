a = int(input('Введите число,'))
def factorial(a):
    f = 1
    for i in range(2,a+1):
        f *= i
    print(f)

factorial(a)