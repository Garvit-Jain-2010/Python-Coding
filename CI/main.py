p = int(input("Enter the principal: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

ci = p * (((1+r)/100) ** t)

print(f"Compound Interest is: {ci:.2f}")