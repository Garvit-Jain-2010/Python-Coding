# square = lambda x:x*x
# print(square(25))

# x = lambda x : x % 2 == 0
# print(x(10))

# def si(p, t, r):
#     print(f"SI: {(p*r*t)/100}.")
# a = int(input("Enter the principal: "))
# b = int(input("Enter the rate of interest: "))
# c = int(input("Enter the time period: "))
# si(a, b, c)

# OR

# si= lambda p,r,t : (p*r*t)/100
# print(si(1000,3,4))

# students = [('John', 90), ('Jane', 85), ('Dave', 95)]
# students.sort(key=lambda x: x[1])
#  print(students)  # Output: [('Jane', 85), ('John', 90), ('Dave', 95)]

# name = [('John', 28), ('Jane',34), ('Dave', 30)]
# name.sort(key=lambda y: y[1], reverse=True)
# print(name)

# Filter Products Cheaper Than 1000
# product = [('Apple', 1023), ('Banana', 522), ('Cherry', 1744)]
# a = filter(lambda x: x[1] < 1000, product)
# print(a)

# Get Names of Students Scoring More Than 90
# students = [('John', 90), ('Jane', 85), ('Dave', 95)]
# b = filter(lambda x: x[1] > 90, students)
# print(b)

# reverse = lambda s: s[::-1]
# print(reverse("hello"))