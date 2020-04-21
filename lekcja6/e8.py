import numpy as np  
def funkcja(tablica, kierunek):
    x = int(np.size(tablica, 1)) #pionowo
    y = int(np.size(tablica, 0)) #poziomo
    if kierunek == 1:
        if x%2==0:
            return tablica[:, :x//2]
        raise Exception("liczba wierszy nie pozwala na podzielenie macierzy")
    else:
        if y%2==0:
            return tablica[:y//2]
        raise Exception("liczba kolumn nie pozwala na podzielenie macierzy")

        #casterror
    
    

tab = np.ones((2,4), dtype="float")
 
print(funkcja(tab, 0))