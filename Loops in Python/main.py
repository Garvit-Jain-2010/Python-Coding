# # Program
# for j in range(2, 11):
#     for i in range(1, 11):
#         print(j*i)

# # Program
# for i in range(1, 101):
#     if i%2 == 0:
#         print(f"{i} - Even")
#     elif i%2 != 0:
#         print(f"{i} - Odd")

# # Program
# a = int(input("Enter the number: "))

# for i in range(2, a):
#     print(f"{a}/{i} = {a/i:.2f}")
    
# if a%i == 0:
#         print(f"{a} is not a prime number.")
# else:
#         print(f"{a} is a prime number.")

# # Program
num = int(input("Enter a number: "))
for i in range(2, num):
    for j in range(2, num):
        if i%j == 0:
            break
    else:
            print(i)