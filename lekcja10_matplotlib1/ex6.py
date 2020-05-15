import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_excel('imiona.xlsx')
#1
grupa1 = df.groupby(['Plec'])['Liczba'].sum()
#2
grupaM  = df[df['Plec'] == 'M']
grupaK  = df[df['Plec'] == 'K']
grupaM = grupaM.groupby(['Rok'])['Liczba'].sum()
grupaK = grupaK.groupby(['Rok'])['Liczba'].sum()
#3
grupa3 = df.groupby(['Rok'])['Liczba'].sum()

#1
plt.subplot(1, 3, 1)
grupa1.plot.bar()

#2
plt.subplot(1, 3, 2)
grupaM.plot()
grupaK.plot()
#3
plt.subplot(1, 3, 3)
grupa3.plot.bar()

plt.show()
