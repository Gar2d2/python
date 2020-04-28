import numpy as np
m1 = np.arange(16).reshape(4,4)
m2 = np.arange(9).reshape(3,3)

print(m1)
print(m2)
print(m1.min(axis = 0))
print(m1.min(axis = 1))
print(m2.min(axis = 0))
print(m2.min(axis = 1))