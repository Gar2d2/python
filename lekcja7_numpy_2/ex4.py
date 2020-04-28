import numpy as np
m1 = np.arange(3, dtype='int64').reshape(1,3)
m2 = np.arange(3, 9, 2.5, dtype='float').reshape(1,3)

m4 = m1*m2
print(m1,'\n',m2, '\n', m4)