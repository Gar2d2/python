import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_excel('imiona.xlsx')

#2
grupaM  = df[df['Plec'] == 'M']
grupaK  = df[df['Plec'] == 'K']
grupaM = grupaM.groupby(['Rok'])['Liczba'].sum()
grupaK = grupaK.groupby(['Rok'])['Liczba'].sum()


#2

grupaM.plot.bar(color = 'blue')
grupaK.plot.bar(color = 'red', bottom = grupaM)


plt.show()
