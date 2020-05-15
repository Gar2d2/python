import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



df = pd.read_csv('iris.csv')


a = [abs(i) for i in df['sepal width in cm'] - df['sepal length in cm']]
print(len(a))
print(len(df['sepal width in cm']))
colormap = np.random.randint(0,150, 150)
wykres = plt.scatter(df['sepal length in cm'],df['sepal width in cm'], c=colormap, s=a, cmap="Spectral")
plt.legend()
plt.ylabel("średnia sepal length")
plt.xlabel("Srednia sepal width ") #ach ten polishinglisz
plt.show()