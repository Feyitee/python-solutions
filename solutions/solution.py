# Modify a list by swapping the first and last elements.Instructions:
# Write a function called swap_extremes(data) that takes a list as an input. 
# It should swap the very first element with the very last element of that list and return the modified list.


my_list = [10, 20, 30, 40, 50]

def swap_extremes(data):
    data[0], data[-1]= data[-1], data[0]
    return data

print(swap_extremes(my_list))
