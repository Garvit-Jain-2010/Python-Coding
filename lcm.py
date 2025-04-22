# LCM of two numbers.

import math

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

lcm = x * y / math.gcd(x, y)

print(f"The L.C.M. of {x} and {y} is {lcm}")