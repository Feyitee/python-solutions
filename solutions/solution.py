# Phase 1: Lists & Basic Data Structures

# Modify a list by swapping the first and last elements.Instructions:
# Write a function called swap_extremes(data) that takes a list as an input. 
# It should swap the very first element with the very last element of that list and return the modified list.

my_list = [10, 20, 30, 40, 50]
def swap_extremes(data):
    data[0], data[-1]= data[-1], data[0]
    return data

# print(swap_extremes(my_list))

# Problem 2 of 100: The Outlier RemoverGoal: Clean up a list by removing the highest and lowest values, regardless of where they sit in the list.Instructions:Write a function called remove_outliers(data) that takes a list of numbers. It needs to find the absolute minimum value and the absolute maximum value, 
# remove them both from the list, and return the cleaned list.(Assume all numbers in the list are unique for now).
scores = [12, 45, 2, 89, 34]
def remove_outliers(data):
    highest = data[0]
    lowest = data[0]
    for num in data:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    data.remove(highest)
    data.remove(lowest)
    return data

# fastest_solution
def remove_outliers2(data):
    highest = max(data)
    lowest = min(data)

    data.remove(highest)
    data.remove(lowest)
    return data

# print(remove_outliers2(scores))


# Problem 3 (The Sub-list Slicer)
items = ["A", "B", "C", "D", "E", "F", "G"]
def sub_listslicer(data):
    return data[2:5]

# print(sub_listslicer(items))

# Problem 4 of 100: The Evens CombinerGoal: Take two separate lists of numbers, 
# combine them into one list, but only keep the even numbers.
# Instructions:Write a function called combine_evens(list1, list2)that takes two lists of integers. 
# Combine them together and return a new list containing only the even numbers.Example

a = [1, 2, 3]
b = [4, 5, 6]

def combine_goals(data1, data2 ):
    combine = data1 + data2
    result = []
    for num in combine:
        if num % 2 == 0:
            result.append(num)
    return result

# print(combine_goals(a, b))

# Problem 5 of 100: The Short Word FilterGoal: Filter a list of strings using a single line of code
# (List Comprehension).Instructions:Write a function called filter_short_words(words) that takes a list of strings.
# It should return a new list containing only the words that have 4 characters or more.Challenge requirement: 
# Write the filtering logic inside the function using a list comprehension instead of a traditional multi-line for loop.


# The traditional For_Loop style
my_words = ["cat", "dog", "apple", "bird", "go", "python"]
def filter_goal(data):
    result = []
    for char in my_words:
        if len(char) >= 4:
            result.append(char)
    return result
# print(filter_goal(my_words))

#List comprehension

def filter_goall(data):
    return [char for char in data if len(char) >= 4]

# print(filter_goall(my_words))


