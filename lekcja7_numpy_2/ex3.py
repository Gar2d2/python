import numpy as np
m1 = np.arange(3).reshape(1,3)
m2 = np.arange(3, 9, 2).reshape(3,1)

m4 = np.dot(m1, m2)
print(m1,'\n',m2, '\n', m4)