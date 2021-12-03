import numpy as np

string = np.array(['apple', 'coconut', 'banana'])
print(string)
print(string.dtype)

matrix = np.array([1.1, 2.0, 3.1, 4.6, 5.4, 3.3])
new_array = matrix.astype('i')
print(matrix.dtype)
print(new_array)
print(new_array.dtype)
