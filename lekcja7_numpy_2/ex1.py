import numpy as np
m1 = np.arange(3).reshape(1,3)
m2 = np.arange(3, 9, 2).reshape(1,3)
m3 = m1*m2

print(m1,'\n',m2, '\n', m3)