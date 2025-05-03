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

x = {3, 5, 8, 10}
b = {3, 5, 7, 9}

# c = x.difference(b) 
# print(c)

# c  = x.__and__(b)
# print(c)

# Same

c = x.intersection(b)
print(c)  # More preferable