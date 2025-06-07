dict1 = {"x": 1, "y": 2}
dict2 = {"z": 3, "w": 4}
merged = dict1.copy()
for i in dict2:
    merged[i] = dict2[i]
print(merged)
