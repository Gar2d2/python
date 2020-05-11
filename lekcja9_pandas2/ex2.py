import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_excel('imiona.xlsx')
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
grupa.rename(columns = {'sum':'suma urodzen'}, inplace = True)
wykres = grupa.plot.bar()
wykres.legend()


plt.title('Wykres słupkowy sumy urodzeń')
plt.show()