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

print(get_price(menu, "mango"))

# A better approach for getting value in a dictionary and returning error if the value doesn't exit.

def geet_price(stock_dict, item_name):
    return stock_dict.get(item_name, "Item not Found")

print(geet_price(menu, "banana"))