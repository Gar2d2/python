import numpy as np  
w1 = 1
w2 = 1
tab = np.arange(25)
tab[0]=tab[1]=1
for i in range(2, 25):
    tab[i] = w1+w2
    w1=w2
    w2=tab[i]
tab =tab.reshape((5,5))

print(tab)