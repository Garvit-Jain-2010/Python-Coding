while True:
    a = int(input("Enter a number: "))

    squares = [x+x for x in range(a+1)]
    print(squares)