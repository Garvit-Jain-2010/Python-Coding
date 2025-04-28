# Basic Calculator
a = int(input("Enter the frist number: "))
b = int(input("Enter the secod number: "))

operation = input("Enter the operation you want to do (+, -, /, *): ")
if operation == "+":
    print(f"The addition or sum of the number {a} and {b} is {a+b}.")
elif operation == "-":
    print(f"The subtraction of the number {a} - {b} is {a-b}.")
elif operation == "*":
    print(f"The multiplication of the number {a} * {b} is {a*b}.")
else:
    print(f"The division of the numbers is {a/b}.")

# ATM
money = 1000

amount = int(input("Enter your value to be widrawl: "))
if amount > money:
    print("Insufficent money in the account")

elif amount == money:
    print("You have taken all of your money from your account.")

elif amount < money and amount%100 == 0:
    print(f"{amount}₹ has been widthrawled and you have {money - amount}₹ left in your account.")

else:
    print("Money entered should be a multiple of 100")

# Avarage Marks
marks = 0
students = [{"name": "Garvit", "math": 90, "science": 85, "english": 88},
            {"name": "Aarav", "math": 95, "science": 80, "english": 90},
            {"name": "Ram", "math": 85, "science": 90, "english": 92},
            {"name": "Shobhit", "math": 80, "science": 85, "english": 87},
            {"name": "Mohan", "math": 88, "science": 92, "english": 89}]

for i in students:
    marks += i["math"]
a_marks = marks/len(students)
print(f"The avarage marks of the maths subject is {a_marks}")

# Cart
total = 0
cart = [
    {"product": "Laptop", "price": 55000, "qty": 1},
    {"product": "Mouse", "price": 500, "qty": 2},
    {"product": "Keyboard", "price": 1500, "qty": 1},
]

for i in cart:
    total += i["price"]
print(f"The total price of all the projuct is ₹{total}.")