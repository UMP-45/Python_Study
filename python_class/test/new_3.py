import numpy as np

a = np.arange(4).reshape(2,2)
print(a)
b = a.sum(axis = 1)/2
print(b)
c = b.reshape(2,1)
print(c)
print(a-c)



