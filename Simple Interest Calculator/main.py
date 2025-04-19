while True:
    P = float(input("Enter the principal amount: "))
    R = float(input("Enter the rate of interest: "))
    T = float(input("Enter the time in years: "))

    simple_interest = (P * R * T) / 100

    if simple_interest < 1000:
        category = "Low Interest"
    elif 1000 <= simple_interest <= 5000:
        category = "Moderate Interest"
    else:
        category = "High Interest"

    print(f"Simple Interest: {simple_interest}")
    print(f"Category: {category}")