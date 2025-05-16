a = [34, 12, 4, 48]

a.sort()  # Sorts the list in ascending order
print(a)
a.reverse()  # Reverses the order of the list
print(a) 
a.append(100)  # Adds an element to the end of the list
print(a)
a.pop()  # Removes the last element from the list
print(a)
a.remove(12)  # Removes the first occurrence of the specified value from the list
print(a)
a.insert(2, 99)  # Inserts an element at the specified position in the list
print(a)
a.clear()  # Removes all elements from the list
print(a)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]