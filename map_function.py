# Square the numbers in list.
# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared = map(square, numbers)
# squared_list = list(squared)
# print(squared_list)

# Convert all strings to uppercase.
# def uppercase(y):
#     return y.upper()
# name = ["Garvit", "Shobhit", "Raj"]
# captial = map(uppercase, name)
# c = list(captial)
# print(c)

# Add 5 to each number.
# def add(z):
#     return z + 5
# num = [4, 7, 3, 9, 5]
# add_5 = map(add, num)
# a = list(add_5)
# print(a)

# Get length of each string.
# def len_string(x):
#     return len(x)
# name = ["Garvit", "Shobhit", "Raj"]
# length = map(len_string, name)
# print(list(length))

# Remove whitespace from each string
# def trim(c):
#     return c.strip(" ")
# dirty_strings = [' a ', ' b  ', '   c']
# trims = map(trim, dirty_strings)
# print(list(trims))

# Convert list of floats to integers
# def integer(a):
#     return int(a)
# floats = [2.3, 3.7, 4.8]
# print(list(map(integer, floats)))

x = {
    "student":["Garvit", "Rahul", "Mohit", "Geeta", "Shobhit", "Anvi", "Shivam", "Ayushi", "Amit", "Piyush"],
    "attendance": [56, 78, 90, 45, 67, 89, 34, 45, 78, 90],
    "midterm_marks":[
        {"maths": 85, "science": 90, "hindi": 80, "english": 89},
        {"maths": 78, "science": 88, "hindi": 75, "english": 80},
        {"maths": 92, "science": 80, "hindi": 85, "english": 87},
        {"maths": 70, "science": 75, "hindi": 65, "english": 72},
        {"maths": 88, "science": 85, "hindi": 78, "english": 84},
        {"maths": 76, "science": 80, "hindi": 70, "english": 75},
        {"maths": 90, "science": 95, "hindi": 88, "english": 92},
        {"maths": 45, "science": 50, "hindi": 40, "english": 48},
        {"maths": 67, "science": 70, "hindi": 60, "english": 65},
        {"maths": 80, "science": 85, "hindi": 75, "english": 82}
    ],  
    "gender":["male", "male", "male", "female", "male", "female", "male", "male", "female", "male"],
}

def math_marks(x):
    pass