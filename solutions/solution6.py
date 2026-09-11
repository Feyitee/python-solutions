# Problem 28
# Write a function called prune_rare_items(transactions, min_count) 
# that takes a list of items and a threshold number.

orders = ["apple", "banana", "apple", "cherry", "banana", "apple", "pear"]

def prune_rare_items(transactions, min_count):
    counts = {}

    for item in transactions:
        counts[item] = counts.get(item, 0) + 1
#  This perfect instead of the if else, you set the value as the key and default thee value zero if not, add 1.
   
    return[item for item in transactions if counts[item] >= min_count]
    

print(prune_rare_items(orders, 2))
