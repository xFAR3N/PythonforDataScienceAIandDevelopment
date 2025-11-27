import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(2, -2, 9)
print(x)

y = np.linspace(0, 2*np.pi, 100)
print(y)
print(np.sin(y))

plt.plot(y, np.sin(y))
plt.show()

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
plt.plot(a, b)
plt.show()

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
for i in arr1:
    print(i)