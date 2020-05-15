import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd

def rzut(n, b):

    for i in range(n):
        c =rd.randrange(1,7,1)
        a =rd.randrange(1,7,1)
        b.append(int(a+c))

b = []
n = 200
rzut(n, b)
# bins oznacza ilość "koszy" czyli słupków, do których mają wpadać wartości z wektora x
# facekolor oznacza kolor słupków
# alpha to stopień przezroczystości wykresu
# density oznacza czy suma ilości zostanie znormalizowana do rozkładu prawdopodobieństwa (czyli przedział 0, 1)
plt.hist(b, bins=11, facecolor='b', alpha=0.75, density=True)


plt.xlabel('Sumy')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram Sumy rzutów')
# wyświatlanie siatki
plt.grid(True)
plt.show()
