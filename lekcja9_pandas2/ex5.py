import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



df = pd.read_csv('zamowienia.csv')


ilosc = df.groupby('Sprzedawca')['idZamowienia'].count()




label = ["ilość zamówień"]

wykres = ilosc.plot.bar()
plt.legend(labels = label )
plt.show()