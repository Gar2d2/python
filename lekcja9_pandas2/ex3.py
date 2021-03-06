import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_excel('imiona.xlsx')

df['Rok']= pd.to_numeric(df['Rok'])

data = df[df['Rok'].max() - df['Rok'] <= 5]

grupa = df.groupby(['Plec'])['Liczba'].sum()



wykres = grupa.plot.pie(
    subplots = True,
    autopct='%.2f %%',
    fontsize = 12
    )

label = ['Kobiety', 'Mężczyźni']
plt.legend(labels = label)
plt.show()
