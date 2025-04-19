def passing_students(grades):
    x = [i for i in grades if i > 40]
    print(f"{len(x)} students have passed")

grades = [35, 50, 70, 40, 90, 20, 45]
passing_students(grades)