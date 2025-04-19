name = input("Enter your name: ")
a = int(input("Enter the marks of English: "))
b = int(input("Enter the marks of Hindi: "))
c = int(input("Enter the marks of Science: "))
d = int(input("Enter the marks of Mathematics: "))
e = int(input("Enter the marks of Social Science: "))

perc = (a+b+c+d+e)/5

if perc >90:
    print("You got A grade.")
elif 89>perc>80:
    print("You got B grade.")
else:
    print("You got C grade.")

print(f"Hello {name}!. Your percontage is {perc}%")