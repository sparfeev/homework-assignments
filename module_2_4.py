
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
    if prime:
        primes.append(num)
print (primes)

