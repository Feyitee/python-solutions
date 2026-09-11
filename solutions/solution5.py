# Problem 19

# Modify a list permanently by changing every negative number into a 0.
my_numbers = [4, -2, 7, -1, 9, -5]

def replace_negatives(data):
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    return data

# print(replace_negatives(my_numbers))

# Problem 20
letters = ["A", "B", "C", "D", "E", "F"]

def get_even_index(data):
    result = []

    for i in range(0, len(data), 2):
        result.append(data[i])
    return result

# print(get_even_index(letters))

# Problem 21
# Write a function called running_sum(data) that modifies a list of numbers.
# Each position in the returned list should represent the sum of all numbers 
# from the start of the list up to that position.

nums = [1, 2, 3, 4]

def running_sum(data):
    result = []
    total = 0

    for i in data:     
        total += i
        result.append(total)

    return result

# print(running_sum(nums))

#Problem 22
# Write a function called extract_column(matrix, col_index) 
# that takes a 2D list (a list of lists) and a column index number. 
# It should extract the numbers sitting at that specific
# column position from every row and return them as a flat list.

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def extract_column(matrix, col_index):
    result = []

    for box in matrix:
        result.append(box[col_index])

    return result


# print(extract_column(grid, 0))

# Problem 23
# Instructions:Write a function called merge_and_sum(dict1, dict2) that merges two dictionaries containing item counts. 
# If an item exists in both dictionaries, do not overwrite it—instead, add their values together.
# If an item only exists in one dictionary, include it in the final result as-is.

store_a = {"apples": 10, "bananas": 5, "oranges": 8}
store_b = {"bananas": 3, "oranges": 2, "grapes": 15}


def merge_and_sum(dict1, dict2):
   result = dict1.copy()
   for key, value in dict2.items():
    if key in result:
         result[key] = result.get(key,0) + value
    else:
        result[key] = value 
        return result

print(merge_and_sum(store_a, store_b))

nums = [2, 4, 8, 1, 3, 9, 6]
def transform_alternating_elements(data):
    return[ data[i] * 10 if data[i] > 5 else data[i] for i in range(0, len(data), 2) ]
 
# print(transform_alternating_elements(nums))


prices = [5, 12, 8, 20]

def map_high_values(prices):
   return {f"index_{i}": value * 2 if value > 10 else value for i, value in enumerate(prices)}


# print(map_high_values(prices))

# Problem 25
# Instructions:Write a function called track_votes(votes_list) that takes a list of names (strings) representing votes.
# It should return a dictionary with the total vote counts for each candidate.

ballot = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

def track_votes(votes_list):
    result = {}
    for value in votes_list:
        if value in result:
            result[value] = result.get(value, 0) + 1
        else:
            result[value] = 1

    return result
 
# print(track_votes(ballot))

# Problem 27
# Instructions:Write a function called build_roster(player_data) that takes a list of tuples: (team_name, player_name). 
# It should return a dictionary where the keys are the teams, and the values are a list of player names on that team.
# Constraint: You must use the .setdefault(key, []) pattern inside a traditional loop.

players = [
    ("Lions", "Alex"),
    ("Tigers", "Ben"),
    ("Lions", "Chris"),
    ("Tigers", "David")
]

# // Setdefault says if key doesn't exist, create one, if it does, append to its value to it
def build_roster(player_data):
    result = {}

    for key, value in player_data:
        result.setdefault(key, []).append(value)
# For Tuple you can access the key and value without having to do enumerate or .items()
    return result
