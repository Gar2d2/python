import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.rename(columns = {'sum':'suma urodzeń'}, inplace = True)
wykres = grupa.plot()
wykres.legend()

plt.title('Wykres liniowy sumy urodzeń do roku')
plt.show()