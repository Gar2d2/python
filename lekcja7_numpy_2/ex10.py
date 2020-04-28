import numpy as np
m1 = np.arange(81).reshape(9,9)
print(m1)
print(m1.shape)
m1 = m1.ravel()
print(m1)
print(m1.shape)
m1 = m1.reshape(9,9)
m1 = m1.T
print(m1)
print(m1.shape)