while True:
    purchase_amount = float(input("Enter the total purchase amount: "))

    if purchase_amount < 100:
        discount = 0
    elif 100 <= purchase_amount <= 500:
        discount = 0.10
    elif 500 < purchase_amount <= 1000:
        discount = 0.20
    else:
        discount = 0.30

    final_price = purchase_amount - (purchase_amount * discount)

    discount_percentage = discount * 100

    print(f"Discount Applied: {discount_percentage}%")
    print(f"Final Price after Discount: ${final_price}")