total_marks = 400
x = {
    "student":["Garvit", "Shyam", "Mohit", "Geeta", "Shobhit", "Ravi", "Shivam", "Saurabh", "Amit", "Piyush"],
    "current_sem": [1, 3, 2, 4, 3, 2, 1, 4, 2, 4],
    "attendance": [56, 78, 90, 45, 67, 89, 34, 45, 78, 90],
    "syllabus": ["Full", "Partial", "Full", "Partial", "Full", "Partial", "Full", "Partial", "Full", "Partial"],
    "previous_sem_marks": [45, 67, 89, 23, 88, 76, 90, 45, 67, 80],
    "previous_sem_attendance":[67, 78, 90, 45, 80, 85, 90, 70, 75, 80],
    "presentation":[3, 2, 6 , 7, 5, 4, 3, 2, 1, 0],
    "midterm_marks":[
        {"python": 85, "java": 90, "c++": 80, "web-development": 89},
        {"python": 78, "java": 88, "c++": 75, "web-development": 80},
        {"python": 92, "java": 80, "c++": 85, "web-development": 87},
        {"python": 70, "java": 75, "c++": 65, "web-development": 72},
        {"python": 88, "java": 85, "c++": 78, "web-development": 84},
        {"python": 76, "java": 80, "c++": 70, "web-development": 75},
        {"python": 90, "java": 95, "c++": 88, "web-development": 92},
        {"python": 45, "java": 50, "c++": 40, "web-development": 48},
        {"python": 67, "java": 70, "c++": 60, "web-development": 65},
        {"python": 80, "java": 85, "c++": 75, "web-development": 82}
    ],  
    "gender":["male", "male", "male", "female", "female", "female", "male", "male", "female", "male"],
    "pass":["yes", "no", "no", "yes", "yes", "no", "yes", "no", "yes", "no"],
    "fail":[0, 2, 1, 0, 0, 1, 0, 1, 0, 1],
    "working_total_day":[67, 89, 34, 45, 56, 89, 23, 88, 49, 47],
    "working_day_teacher":[89, 89, 89, 89, 89, 89, 89, 89, 89, 89],
}

marks = x["midterm_marks"][0]
print(marks)

for i in range(1, len(x["midterm_marks"])):
    print(x["midterm_marks"][i]["web-development"], end=" ")
    print(x["midterm_marks"][i]["python"], end=" ")
    print(x["midterm_marks"][i]["java"], end=" ")
    print(x["midterm_marks"][i]["c++"]) 

    # Average marks of each student.
    print(f"The average of {x['student'][i]} is {(x['midterm_marks'][i]['web-development'] + x['midterm_marks'][i]['python'] + x['midterm_marks'][i]['java'] + x['midterm_marks'][i]['c++']) / 4}") 

    # Percentage of each student.
    print(f"The percentage of {x['student'][i]}: {((x['midterm_marks'][i]['web-development'] + x['midterm_marks'][i]['python'] + x['midterm_marks'][i]['java'] + x['midterm_marks'][i]['c++']) / total_marks) * 100}%")

    # Find the subject in which the student has scored the highest marks
    highest_subject = max(x["midterm_marks"][i], key=x["midterm_marks"][i].get)
    print(f"{x['student'][i]} scored the highest in {highest_subject} with {x['midterm_marks'][i][highest_subject]} marks.")


for i in x:
    print(f"{i}: {x[i][0]}", end=" ")
    
for j in range(len(x["student"])):
    # print(f'{x["student"][j]} : {x["midterm_marks"][j]}')
    print(j)