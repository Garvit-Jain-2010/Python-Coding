while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        C = float(input("Enter temperature in degrees Celsius: "))
        F = (C * 9/5) + 32
        print(f"{C} degrees Celsius = {F} degrees Fahrenheit")
    elif choice == 2:
        F = float(input("Enter temperature in degrees Fahrenheit: "))
        C = (F - 32) * 5/9
        print(f"{F} degrees Fahrenheit = {C} degrees Celsius")

    else:
        print("Invalid Entry!")