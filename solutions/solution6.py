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
    

# print(prune_rare_items(orders, 2))


# Problem 29
# Instructions:Write a function called sanitize_usernames(raw_users) that takes a list of names. 
# Some names have messy whitespace and mixed capitalization.Clean each name so it is 
# completely lowercase with no trailing/leading whitespace.
# Return a list of these cleaned names, but only keep the ones that appear exactly 
# once in the entire dataset after cleaning (remove any name that has a duplicate).

dirty_users = [" Alice ", "bob", "ALICE", "charlie", "  Bob  ", "david"]

def sanitize_usernames(raw_users):
    result = {}
    for value in raw_users:
        clean_word = value.lower().strip()
        result[clean_word] = result.get(clean_word, 0) + 1

    return[clean_word for clean_word in result if result[clean_word] == 1]

# print(sanitize_usernames(dirty_users))

# Problem 30   
# Write a function called aggregate_expensive_items(item_list, price_cutoff)
# that takes a list of dictionaries (representing inventory items) and a cutoff number.          

inventory = [
    {"name": "Laptop", "price": 1000, "qty": 2},
    {"name": "Mouse", "price": 25, "qty": 10},
    {"name": "Laptop", "price": 1000, "qty": 1},
    {"name": "Monitor", "price": 300, "qty": 4}
]
# {"Laptop": 3, "Monitor": 4}
# def aggregate_expensivee_items(item_list, price_cutoff):
#     return [obj for obj in item_list if obj["price"] >= price_cutoff]

  # "GET:  Give me the existing electronics total. If electronics doesn't exist yet, start me at 0."     
def aggregate_expensivee_items(item_list, price_cutoff):
    result = {}

    for obj in item_list:
        if obj["price"] > price_cutoff:
            name = obj["name"]
            price = obj["price"]

            result[name] = result.get(name, 0) + price

    return result
# print(aggregate_expensivee_items(inventory, 100))


# Problem 31 — Group Expensive Items by Name

inventory = [
    {"name": "Laptop", "price": 1000, "qty": 2},
    {"name": "Mouse", "price": 25, "qty": 10},
    {"name": "Laptop", "price": 1200, "qty": 1},
    {"name": "Monitor", "price": 300, "qty": 4},
    {"name": "Mouse", "price": 150, "qty": 3}
]

# def group_expensive_items(item_list, price_cutoff):
#     result = {}

#     for obj in item_list:
#         if obj["price"] >= price_cutoff:
#             price = obj["price"]
#             name = obj["name"]

#             result.setdefault(name, []).append(price)
#     return result
    
# print(group_expensive_items(inventory, 500))

# Problem 32 - Nested Dictionary Aggregation

inventory = [
    {"name": "Laptop", "category": "electronics", "qty": 2},
    {"name": "Mouse", "category": "electronics", "qty": 10},
    {"name": "Laptop", "category": "electronics", "qty": 1},
    {"name": "Chair", "category": "furniture", "qty": 4},
    {"name": "Desk", "category": "furniture", "qty": 2},
    {"name": "Chair", "category": "furniture", "qty": 3}
]

def group_inventory(item_list):
    result = {}

    for obj in item_list:
       category = obj["category"]
       name = obj["name"]
       qty = obj["qty"]

       inner = result.setdefault(category, {})
       inner[name] = inner.get(name, 0) + qty

    return result

# print(group_inventory(inventory))

# Problem 33 — Nested Dictionary + Filtering
inventory_2 = [
    {"name": "Laptop", "category": "electronics", "price": 1000, "qty": 2},
    {"name": "Mouse", "category": "electronics", "price": 25, "qty": 10},
    {"name": "Laptop", "category": "electronics", "price": 1200, "qty": 1},
    {"name": "Chair", "category": "furniture", "price": 150, "qty": 4},
    {"name": "Desk", "category": "furniture", "price": 500, "qty": 2},
    {"name": "Chair", "category": "furniture", "price": 200, "qty": 3}
]
def group_expensive_inventory(item_list, price_cutoff):
    result = {}

    for obj in item_list:
        if obj["price"] >= price_cutoff:
            name = obj["name"]
            category = obj["category"]
            qty = obj["qty"]

            inner = result.setdefault(category, {})
            inner[name] = inner.get(name, 0) + qty

    return result

# print(group_expensive_inventory(inventory_2, 200))


# Problem 34 — Nested Grouping Into Lists
sales = [
    {"region": "North", "product": "Laptop", "amount": 1000},
    {"region": "North", "product": "Mouse", "amount": 50},
    {"region": "South", "product": "Laptop", "amount": 1200},
    {"region": "North", "product": "Laptop", "amount": 900},
    {"region": "South", "product": "Mouse", "amount": 70},
    {"region": "South", "product": "Laptop", "amount": 1500}
]

def group_sales(sales_list):
    result = {}

    for obj in sales_list:
        region = obj["region"]
        product = obj["product"]
        amount = obj["amount"]

        inner = result.setdefault(region, {})
        inner.setdefault(product, []).append(amount)
    return result

# print(group_sales(sales))

# Problem 35 — Filter + Nested Grouping + Sum

def summarize_large_sales(sales_list, minimum_amount):
    result = {}

    for obj in sales_list:
        if obj["amount"] >= minimum_amount:
            region = obj["region"]
            product = obj["product"]
            amount = obj["amount"] 

            inner = result.setdefault(region, {})
            inner[product] = inner.get(product, 0) + amount

    return result

# print(summarize_large_sales(sales, 100))

# numbers = [4, 7, 2, 9, 7, 5, 2]

def first_duplicate(number):
    seen = set()

    for value in number:
        if value in seen:
            return value
        else:
            seen.add(value)

# print(first_duplicate(numbers))

# Problem 37 — DSA Pattern: Frequency Map

# numbers = [4, 7, 2, 7, 4, 7, 9]
def most_frequent(numbers):
    frequent = {}

    for value in numbers:
        frequent[value] = frequent.get(value, 0) + 1

    return max(frequent, key= frequent.get)
# print(most_frequent(numbers))

numbers = [4, 7, 2, 7, 4, 9, 2, 5]
def first_unique(numbers):
    result = {}

    for value in numbers:
        result[value] = result.get(value, 0) + 1

    for value in numbers:
        if result[value] == 1:
            return value

print(first_unique(numbers))
