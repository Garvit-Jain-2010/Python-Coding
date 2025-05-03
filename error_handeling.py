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

try:
    num = int(input("Enter an integer: "))
    print(f"Your number is {num}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
