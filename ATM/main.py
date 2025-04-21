while True:
    money = 5000

    amount = int(input("Enter your value to be widrawl: "))

    if amount > money:
        print("Insufficent money in the account")

    elif amount == money:
        print("You have taken all of your money from your account.")

    elif amount < money and amount%100 == 0:
        print(f"{amount}₹ has been widthrawled and you have {money - amount}₹ left in your account.")

    else:
        print("Money entered should be a multiple of 100")