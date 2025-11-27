import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
print(type(a))
print(A)

print(A.ndim)
print(A.shape)
print(A.size)

print(A[1, 2])
print(A[1][2])

print(A[1][0:2])
print(A[0:2, 0:2])

X = np.array([[1, 0], [0, 1]])
print(X)
Y = np.array([[1, 0], [0, 1]])
Y = Y + 1
print(Y)
Z = X + Y
print(Z)

Z = 2 * Y
print(Z)
Z = X * Y
print(Z)

A = np.array([[1, 0, 1], [0, 1, 1]])
B = np.array([[1, 0], [0, 1], [1, 0]])
C = np.dot(A, B)
print()
print(C)
B = B.T
print(B)


