# 61
# list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = list(dict.fromkeys(list))
# print(unique_list)

# 62
# list1 = [1, 2, 3]
# list2 = [2, 3, 4, 5]
# merged_unique = list(dict.fromkeys(list1 + list2))
# print(merged_unique)

# 66
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# intersection = list(set(list1) & set(list2))
# print(intersection)

# 67
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# difference = list(set(list1) - set(list2))
# print(difference)

# 68
# import random

# list = [1, 2, 3, 4, 5]
# random.shuffle(list)
# print(list)

# 69
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 5]
# list3 = [3, 6, 2]

# common = list(set(list1) & set(list2) & set(list3))
# print(common)

# 71
# nested = [[1, 2], [3, 4], [5, 6]]
# print(nested[1][0])

# 72
# nested = [[1, 2], [3, 4], [5, 6]]

# for sublist in nested:
#     for item in sublist:
#         print(item)

# 74
# nested = [[1, 8], [3, 4], [5, 6]]

# max_val = nested[0][0]
# for sublist in nested:
#     for item in sublist:
#         if item > max_val:
#             max_val = item
# print(max_val)

# 75
# nested = [[1, 4], [3, 1], [5, 2]]
# nested.sort(key=lambda x: x[1])
# print(nested)

# 77
# nested = [[1, 2], [3, 4], [5, 6]]
# target = 4
# found = False

# for sublist in nested:
#     if target in sublist:
#         found = True
#         break
# print(found)

# 78
# nested = [[1, 2], [3, 4], [5, 6]]
# total = 0

# for sublist in nested:
#     for item in sublist:
#         total += item
# print(f"The total sum is: {total}")