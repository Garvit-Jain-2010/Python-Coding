# A list contains student grades (0-100). Write a function to count the number of students who passed (above 40).

def passing_students(grades):
    count = []
    for i in grades:
        if i > 40:
            # print(i)
            count.append(i)
    print(len(count))    

grades = [35, 50, 70, 40, 90, 20, 45]
print(f"Number of passing students are: {passing_students(grades)}")
# print(len(grades))