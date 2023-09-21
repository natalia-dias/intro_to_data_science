import numpy as np
list_to_array = []
for i in range(3):
    list_to_array.append(int(input()))

np_array = np.array(list_to_array)
max_np_array = max(np_array)
print(f'{max_np_array}\n{list_to_array.index(max_np_array)}')
