import numpy as np  
def generuj(a, b):
    return np.logspace(1, b, base = a, num = b, dtype="int")
    
    

print(generuj(2, 6))