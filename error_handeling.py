# try:
#     a = int("abc")
# except ValueError:
#     print("Conversion failed: Not a number.")

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     result = a / b
#     print("Result:", result)
# except Exception as e:
#     print(f"An error occurred: {e}")

# try:
#     num = int(input("Enter an integer: "))
#     print(f"Your number is {num}.")
# except Exception as r:
#     print("Error:", r)

# try:
#     x = [23, 45, 67]
#     index = int(input("Enter index: "))
#     print("Value:", x[index])
# except Exception as s:
#     print(f"Error: {s}")

# list = [10, 20, 30, 40, 50]
# try:
#     num = int(input("Enter a number to search: "))
#     if num in list:
#         print(f"{num} is in the list.")
#     else:
#         raise ValueError
# except ValueError:
#     print(f"{num} is not in the list.")

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
# except:
#     print("Help me!")

# inventory = ["Apple", "Banana", "Mango", "Pineapple", "Cherry", "Watermelon"]
# try:
#     fruit = input("Enter the fruit name: ")
#     if fruit in inventory:
#         print(f"{fruit} is present in the storage")
#     else:
#         raise ValueError
# except ValueError:
#     print("Fruit is not in the storage.")