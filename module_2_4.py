numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    prime = 0
    for i in range(1,num+1):
        if num % i == 0:
            prime += 1
    if prime == 2:
        primes.append(num)
    else:
        not_primes.append(num)
print (primes)
print(not_primes)
