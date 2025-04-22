# We have to take dictionary {}.

a = {3, 5, 8, 10}
b = {3, 5, 7, 9}

# c = a.difference(b) 
# print(c)

# c  = a.__and__(b)
# print(c)

# Same

c = a.intersection(b)
print(c)  # More preferable