numbers = [4, 7, 4, 2, 7, 9]


def first_duplicates(num):
    result = {}

    for value in num:
        result[value] = result.get(value,  0) + 1

    for value in num:
        if result[value] == 1:
            return value

print(first_duplicates(numbers))