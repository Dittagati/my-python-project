import numpy as np
arr_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2 = np.array([[2, 3, 4], [5, 6, 7]])

adding = np.concatenate((arr_1, arr_2), axis=1)
print(adding)

add_2 = np.stack((arr_1, arr_2), axis=1)
print(add_2)

matrix = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]])
for ndx, x in np.ndenumerate(matrix):
    print(ndx, x)

x = 10
y = 23

z = x.__add__(y)
print(z)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

add_3 = np.hstack((x, y))
print(add_3)

add_4 = np.vstack((x, y))
print(add_4)

add_5 = np.dstack((x, y))
print(add_5)
