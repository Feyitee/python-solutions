# Problem 19

# Modify a list permanently by changing every negative number into a 0.


my_numbers = [4, -2, 7, -1, 9, -5]

def replace_negatives(data):
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    return data

print(replace_negatives(my_numbers))

# Problem 20
letters = ["A", "B", "C", "D", "E", "F"]

def get_even_index(data):
    result = []

    for i in range(0, len(data), 2):
        result.append(data[i])
    return result

print(get_even_index(letters))

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


print(running_sum(nums))
