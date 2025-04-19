while True:
    side1 = float(input("Enter the length of first side: "))
    side2 = float(input("Enter the length of second side: "))
    side3 = float(input("Enter the length of third side: "))

    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print("The given sides form a valid triangle.")

        if (side1 == side2 == side3):
            print("It is an Equilateral Triangle.")
        elif (side1 == side2) or (side1 == side3) or (side2 == side3):
            print("It is an Isosceles Triangle.")
        else:
            print("It is a Scalene Triangle.")
    else:
        print("The given sides do not form a triangle.")