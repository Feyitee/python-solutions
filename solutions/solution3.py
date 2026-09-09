# Phase 3: Dictionaries & Key-Value Pairs Problem

# 8 of 100: The Price CheckerGoal: Retrieve data from a dictionary using its key, and handle missing data safely.
# Instructions: Write a function called get_price(stock_dict, item_name) that looks up an item in a dictionary of prices.
# If the item exists, return its price.If the item does not exist in the dictionary, return the string: "Item not found".

menu = {"apple": 1.50, "banana": 0.75, "orange": 1.25}

def get_price(stock_dict, item_name):
    if item_name not in stock_dict:
        return "Item not found"
    else:
        return stock_dict[item_name]

# print(get_price(menu, "mango"))

# A better approach for getting value in a dictionary and returning error if the value doesn't exit.

def geet_price(stock_dict, item_name):
    return stock_dict.get(item_name, "Item not Found")

# print(geet_price(menu, "banana"))


# Problem 9 of 100: The Inventory UpdaterGoal: 
# Modify an existing dictionary by adding new key-value pairs or updating old ones
# .Instructions: Write a function called update_inventory(inventory, item, quantity)
# that takes an inventory dictionary, an item name, and a quantity number.
# If the item is already in the inventory, add the new quantity to the existing count.
# If the item is not in the inventory, add it to the dictionary with the given quantity.
# Return the updated inventory dictionary.

current_stock = {"apples": 5, "bananas": 2}

def update_inventory(inventory, item, quantity):
    if item not in inventory:
       inventory[item] = quantity
    else:
        inventory[item] = inventory[item] + quantity
    return inventory

# print(update_inventory(current_stock, "bananas", 2))

# Faster method

# This gives us access to the key and modifies it and if the value doesn't exists, it creates it and add the quantity to it
def updateinventory(inventory, item, quantity):
    inventory[item] = inventory.get(item, 0) + quantity
    return inventory

# print(updateinventory(current_stock, "yam", 2))




# Problem 10 of 100: 
# The Frequency CounterGoal: Count how many times items appear in a list and store the results in a dictionary.

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
def count_frequencies(elements):
    result = {}

    for val in elements:
        result[val] = result.get(val, 0) + 1
    return result

# print(count_frequencies(words))


numbers = [1, 2, 2, 3, 4, 4, 4, 5]

def remove_duplicates(data):
    result = list(set(data))
    return result

# print(remove_duplicates(numbers))

# Problem 12 of 100: The Common Interest Finder

list_x = ["Python", "JavaScript", "C++", "Java", "CSS"]
list_y = ["Java", "HTML", "CSS", "Python"]
list_z = ["C#", "CSS"]


def common_finder(dataa, datab):
    return list(set(dataa).intersection(datab))

# print(common_finder(list_x, list_y))


#Multiples
def common_finder_multiple(dataa, *others):
    return list(set(dataa).intersection(*others))

# print(common_finder_multiple(list_x, list_y, list_z))


# Problem 13 of 100: The Nested Grade FilterGoal: Filter a list of dictionaries based on a specific nested value. 
# (This is a fundamental skill for data cleaning in AI!)
# Instructions: Write a function called get_passing_students(student_list, passing_grade) 
# that takes a list of dictionaries
#  (where each dictionary represents a student with a name and a score) and a cutoff grade. 
# It should return a new list containing only the names (strings) 
# of the students who scored equal to or higher than the passing_grade.

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 60},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 70}
]

def get_passing_students(student_list, passing_grade):
    successful_students = []

    for student in student_list:
        if student["score"] >= passing_grade:
            successful_students.append(student["name"])
    return successful_students

# print(get_passing_students(students, 75))

# Problem 14 of 100: 
# The Price DoublerGoal: Transform a list of numbers using a list comprehension based on a condition.
# Instructions:Write a function called double_high_prices(prices, threshold) using a single-line list 
# comprehension inside your return statement. It should take a list of numbers (prices). 
# If a price is greater than or equal to the threshold, 
# double it (price * 2). If it is less than the threshold, leave it unchanged.

old_prices = [5, 12, 8, 20, 3]

def double_high_prices(prices, threshold):
    return [value * 2 if value >= threshold else value for value in prices]

# print(double_high_prices(old_prices, 10))


