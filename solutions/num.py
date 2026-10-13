import numpy as np

# Numpy is Python lists, but built for fast numerical work.

numbers = [1, 2, 3, 4]
numbers = np.array([1, 2, 3, 4])

print(numbers * 2)

scores = np.array([
    [70, 80, 90],
    [60, 75, 85]
])
print(scores.shape)
(2, 3)

