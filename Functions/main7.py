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

# Find the percentage of marks obtained by each student in the midterm exams and give the percentage what the name of the student is entered by the user.

def student_percentage(student_name):
    if student_name in x["student"]:
        student_index = x["student"].index(student_name)
        print(f"{name} has got {((x['midterm_marks'][student_index]['web-development'] + x['midterm_marks'][student_index]['python'] + x['midterm_marks'][student_index]['java'] + x['midterm_marks'][student_index]['c++']) / 400) * 100}%")
    else:
        print("Invalid name!")
    
name = input("Enter the student name: ")
student_percentage(name)

# To give the details of the student when the name is entered
def details(student):
    if student in x["student"]:
        student_index = x["student"].index(student)

        print("The name of the student is", name)
        print(f"{name} has got {((x['midterm_marks'][student_index]['web-development'] + x['midterm_marks'][student_index]['python'] + x['midterm_marks'][student_index]['java'] + x['midterm_marks'][student_index]['c++']) / 400) * 100}%")

        print(f"The percentage of {x['student'][student_index]}: {((x['midterm_marks'][student_index]['web-development'] + x['midterm_marks'][student_index]['python'] + x['midterm_marks'][student_index]['java'] + x['midterm_marks'][student_index]['c++']) / 400) * 100}%")

        print(f"The maximum marks of {name} is in {max(x['midterm_marks'][student_index])}")
        print(f"The minimun marks of {name} is in {min(x['midterm_marks'][student_index])}")
    else:
        print("Invalid name!")
    
name = input("Enter the student name: ")
details(name)