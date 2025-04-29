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

def max_attendence(x):
    max_attendence = max(x["attendance"])
    index = x["attendance"].index(max_attendence)
    return x["student"][index], max_attendence
result = max_attendence(x)
print(result)