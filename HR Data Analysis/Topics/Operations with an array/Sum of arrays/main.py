import numpy as np


array = np.array([[[13, 14], [34, 35]], [[9, 9], [5, 0]]])

ax = int(input())
print(array.sum(axis=ax))
