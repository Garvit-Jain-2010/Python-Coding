# Q. Given a list of studens with there marks, find the avarage marks of eack subjects.

x = 0
students = [{"name": "Garvit", "math": 90, "science": 85, "english": 88},
            {"name": "Aarav", "math": 95, "science": 80, "english": 90},
            {"name": "Ram", "math": 85, "science": 90, "english": 92},
            {"name": "Shobhit", "math": 80, "science": 85, "english": 87},
            {"name": "Mohan", "math": 88, "science": 92, "english": 89}]

for i in students:
    # print(i.get("name"))
    # print(i.get("math"))
    x += i["math"]
print(x)
a = (x/len(students))
list = [a]
print(list)