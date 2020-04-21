import numpy as np  
def funkcja(n):
    a=np.zeros((n, n))
    liczba = 1
    for wiersz in range(0, n):
        for miejsce in range(0, n):
            a[wiersz][miejsce] = liczba
            liczba +=1
        
    return a


print(funkcja(4))