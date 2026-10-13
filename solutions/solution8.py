numbers = [4, 7, 4, 2, 7, 9]


def first_unique(num):
    result = {}

    for value in num:
        result[value] = result.get(value,  0) + 1

    for value in num:
        if result[value] == 1:
            return value

print(first_unique(numbers))



numbers = [11, 2, 15, 7]
target = 9
def two_sum(numm, target):
    seen = {}

    for index, value in enumerate(numm):
        needed = target - value

        if needed in seen:
            return [seen[needed], index]

        seen[value] = index


print(two_sum(numbers, target))