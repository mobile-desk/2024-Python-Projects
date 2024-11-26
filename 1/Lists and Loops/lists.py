def sort_list(lst):
    return sorted(lst)

def average_of_numbers(lst):
    if len(lst) == 0:
        return 0  # Avoid division by zero
    return sum(lst) / len(lst)

def find_max(lst):
    return max(lst) if lst else None  # Return None if the list is empty

def find_min(lst):
    return min(lst) if lst else None  # Return None if the list is empty

def sum_of_list(lst):
    return sum(lst)


numbers = [5, 3, 8, 1, 4]

sorted_numbers = sort_list(numbers)
average = average_of_numbers(numbers)
maximum = find_max(numbers)
minimum = find_min(numbers)
total_sum = sum_of_list(numbers)

print("Sorted List:", sorted_numbers)
print("Average of Numbers:", average)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Sum of List:", total_sum)