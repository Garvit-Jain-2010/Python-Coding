def classification(num):
    if num>0 and num%2 == 0:
        print("The number is even and positive")
    elif num>0 and num%2 != 0:
        print("The number is odd and positive")
    elif num<0 and num%2 == 0:
        print("The number is negative and even")
    else:
        print("The number is negative and odd")

while True:
    num = int(input("Enter the number: "))
    classification(num)