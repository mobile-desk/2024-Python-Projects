# approach 1
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Convert the list to a set to remove duplicates
unique_list = list(set(mylist))
print(unique_list)


# approach 2
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_list = []
for item in mylist:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)