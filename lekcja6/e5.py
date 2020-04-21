import numpy as np  
def funkcja(n):
    vector = np.arange(n, 0, -1)
        
    return np.diag(vector)


print(funkcja(4))