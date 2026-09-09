# Problem 15 of 100: The Key-Value InverterGoal: Swap the keys and values of a dictionary.
# (This is highly useful in AI when you want to convert predictions back into human-readable labels!)
#  Instructions:Write a function called invert_dictionary(my_dict)
#    that takes a dictionary and returns a new dictionary where the original keys become values,
#      and the original values become keys.
#  (Assume all values in the starting dictionary are unique).
#  Example Input:Problem 15 of 100: The Key-Value InverterGoal: 
#  Swap the keys and values of a dictionary. (This is highly useful in AI when you want to convert predictions back into human-readable labels!)
# Instructions:Write a function called invert_dictionary(my_dict) that takes a dictionary and returns a new dictionary where
#  the original keys become values, and the original values become keys.
# (Assume all values in the starting dictionary are unique).Example Input:

user_roles = {"admin": 1, "editor": 2, "guest": 3}

def invert_dictionary(my_dict):
    return {value: key for key, value in my_dict.items()}
# print(invert_dictionary(user_roles))



# Problem 16 of 100: The Substring Dictionary 
# FilterGoal: Filter down a dictionary based on text matches inside its keys.
# Instructions:Write a function called filter_by_keyword(dataset, keyword) that takes a dictionary and a string keyword.
# It should return a new dictionary containing only 
# the key-value pairs where the key contains the keyword string (case-sensitive)


file_sizes = {
    "project_final.py": 1500,
    "notes.txt": 450,
    "script_final.py": 2300,
    "image.png": 8000
}

def filter_by_keyword(dataset, keyword):
    return {key: value for key, value in dataset.items() if keyword in key}

print(filter_by_keyword(file_sizes, "final"))


# Tier 2: Advanced Transformations & Filtering
# Problem 17 of 100: The Category GrouperGoal: Transform a flat list of items into an organized dictionary grouped by category.
# Instructions:Write a function called group_by_category(items) that takes a list of dictionaries, 
# where each dictionary has a "name" and a "category".


products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Jeans", "category": "Clothing"}
]

# Logic one
def group_by_category(items):
    result = {}

    for products in items:
        cat = products["category"]
        name = products["name"]

        if cat not in result:
            result[cat] = []

        result[cat].append(name)

    return result
       
print(group_by_category(products))

# Logic two

def group_by_cat(items):
    result = {}

    for products in items:
        result.setdefault(products["category"], []).append(products["name"])
    return result

print(group_by_cat(products))
