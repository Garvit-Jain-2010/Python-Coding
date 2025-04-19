a = int(input("Enter a number: "))
prime_numbers = []
for num in range(1, a+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print(prime_numbers)