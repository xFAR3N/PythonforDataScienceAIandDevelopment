import numpy as np

a = np.array([0, 1, 2, 3, 4])
print(a)
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)
print(type(a))
print(a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

print(b)

print(type(b))
print(b.dtype)

c = np.array([20, 1, 2, 3, 4])
c[0] = 100
print(c)

d = c[1:4]
print(d)

c[3:5] = 300, 400
print(c)

select = [0, 2, 3, 4]

print(select)

d = c[select]
c[select] = 10000

print(c)
print(d)


print()
print(a)
print(a.size)

print(a.ndim)

print(a.shape)

mean = a.mean()
print(mean)
standard_deviation = a.std()
print(standard_deviation)

x = np.array([-1, 2, 3, 4, 5])
print()
print(b)
max_b = b.max()
print(max_b)
min_b = b.min()
print(min_b)
print()

u = np.array([0, 1])
v = np.array([1, 0])
z = np.add(u, v)
print(z)
print()
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(arr1)
print(arr2)

arr3 = np.add(arr1, arr2)
print(arr3)
print()
i = np.array([1, 2])
y = np.array([2, 1])
z = np.multiply(i, y)

print(z)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

arr3 = np.divide(arr1, arr2)
print(arr3)
print()
X = np.array([1, 2])
Y = np.array([3, 2])

Z = np.dot(X, Y)

print(Z)

Arr1 = np.array([3, 5])
Arr2 = np.array([2, 4])
print(np.dot(Arr1, Arr2))


u = np.array([1, 2, 3, 4, -1])
print(u + 1)
print(np.pi)

r = np.array([0, np.pi/2, np.pi])
print(r)
n = np.sin(r)
print(n)
