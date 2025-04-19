def prime(num):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            print(f"{num} is not a prime number")
            break
    if is_prime:
        print(f"{num} is a prime number")

while True:
    num = int(input("Enter a number: "))
    prime(num)