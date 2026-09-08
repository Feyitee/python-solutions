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

print(count_frequencies(words))