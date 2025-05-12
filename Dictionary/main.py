a = {
    "name" : ["Garvit", "Shobhit", "Aarav", "Mohan"], # Here "name" is the key and ["Garvit", "Shobhit", "Aarav", "Mohan"] is the value.
    "age" : 70
    }
print(a.get("name"))
# or
print(a["name"])

print(a.get("age"))
# or
print(a["age"])


x = {3, 5, 8, 6}
b = {3, 5, 7, 9}

# c = x.difference(b) 
# print(c)

# c  = x.__and__(b)
# print(c)

# Same

c = x.intersection(b)
print(c)  # More preferable