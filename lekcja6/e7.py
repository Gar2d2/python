import numpy as np  
def funkcja(n):
    mat = np.arange(2, n*n*2 + 2, 2)
    return mat.reshape((n,n))
    


 
print(funkcja(5))