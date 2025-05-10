# 1
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age   

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# p1 = person("Alice", 30)
# p1.greet()

# 2
# class student:
#     def __init__(self, name, age, clas):
#         self.name = name
#         self.age = age
#         self.class_name = clas

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old. I am in class {self.class_name}.")
    
# s1 = student("Alice", 30, "10th")
# s1.greet()

# 3
# class employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def bonus(self):
#         # With a 10% bonus
#         return self.salary * 0.10

# a = employee("Alice", 30, 50000)
# print(f"Bonus for {a.name}: {a.bonus()}")

# 4
# class car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#     def main(self):
#         print(f"Car model: {self.model}, Year: {self.year}, Color: {self.color}")

# a = car("Toyota", 2025, "Red")
# a.main()

# 5
# class bank_account:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient money in your bank account.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
    
# x = bank_account("Alice", 1000)
# x.deposit(500)
# x.withdraw(200)