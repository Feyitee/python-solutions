# Phase 1: Lists & Basic Data Structures

# Modify a list by swapping the first and last elements.Instructions:
# Write a function called swap_extremes(data) that takes a list as an input. 
# It should swap the very first element with the very last element of that list and return the modified list.

my_list = [10, 20, 30, 40, 50]
def swap_extremes(data):
    data[0], data[-1]= data[-1], data[0]
    return data

print(swap_extremes(my_list))

# Problem 2 of 100: The Outlier RemoverGoal: Clean up a list by removing the highest and lowest values, regardless of where they sit in the list.Instructions:Write a function called remove_outliers(data) that takes a list of numbers. It needs to find the absolute minimum value and the absolute maximum value, 
# remove them both from the list, and return the cleaned list.(Assume all numbers in the list are unique for now).
scores = [12, 45, 2, 89, 34]
# def remove_outliers(data):
#     highest = data[0]
#     lowest = data[0]
#     for num in data:
#         if num > highest:
#             highest = num
#         if num < lowest:
#             lowest = num
#     data.remove(highest)
#     data.remove(lowest)
#     return data

# fastest_solution
def remove_outliers2(data):
    highest = max(data)
    lowest = min(data)

    data.remove(highest)
    data.remove(lowest)
    return data

print(remove_outliers2(scores))


