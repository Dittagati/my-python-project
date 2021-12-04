import numpy as np
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([2, 3, 4])

adding = np.concatenate((arr_1, arr_2))
print(adding)

matrix = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]])
for ndx, x in np.ndenumerate(matrix):
    print(ndx, x)

