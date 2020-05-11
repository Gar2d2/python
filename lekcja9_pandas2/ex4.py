import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



df = pd.read_csv('iris.csv')


suma = df.groupby('class')['sepal width in cm'].mean()

mean =  df.groupby('class')['sepal length in cm'].mean()
a = mean*suma*10



colormap = np.array(['r','g','b'])
wykres = plt.scatter(suma, mean, c=colormap, s=a, cmap="Spectral")
plt.legend()
plt.ylabel("średnia sepal length")
plt.xlabel("Srednia sepal width ") #ach ten polishinglisz
plt.show()