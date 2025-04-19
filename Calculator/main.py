num1 = int(input("Enter the first number: "))
x = input("Enter the operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if x == "+":
    print(num1+num2)
elif x == "-":
    print(num1-num2)
elif x == "/":
    print(num1/num2)
elif x == "*":
    print(num1*num2)
else:
    print("Invalid number!")