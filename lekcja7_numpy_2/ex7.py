import numpy as np
m1 = np.arange(6).reshape(2,3)
a = np.sin(m1)
b = np.cos(m1)
c = np.add(a,b)
print(c)