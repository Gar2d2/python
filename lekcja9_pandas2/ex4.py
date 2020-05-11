import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#Wykres kołowy z wartościami % ukazującymi ilość 
# urodzonych chłopców i 
# dziewczynek w ostatnich 5 latach z datasetu.


df = pd.read_csv('iris.csv')


suma = df.groupby('class')['sepal width in cm'].mean()
print(suma)
mean =  df.groupby('class')['sepal length in cm'].mean()
print(mean)
print(df)

print(suma)
#scale = np.array([mean['sepal length in cm']])
colormap = np.array(['r','g','b'])
wykres = plt.scatter(suma, mean, c=colormap, s=400, cmap="Spectral")
plt.legend()
plt.ylabel("średnia sepal length")
plt.xlabel("Srednia sepal width ") #ach ten polishinglisz
plt.show()