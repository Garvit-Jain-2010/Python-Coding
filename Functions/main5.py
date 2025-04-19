names = ["Rahul", "Amit", "Ravi", "Ajay", "Ramesh"]

def name_start_with():
    for name in names:
        if name.startswith("R"):
            print(name)
        else:
            print(f"{name}'s name is not starting with R")
name_start_with()
