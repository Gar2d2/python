import pandas as pd
import numpy as np
#Zadanie 3
df = pd.read_csv('zamowienia.csv', sep=';')
#listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)

print(df.Sprzedawca.unique())
print('\n\n\n')
#5 najwyższych wartości zamówień

print(df.sort_values('Utarg', ascending = False).head(5))
print('\n\n\n')
#ilość zamówień złożonych przez każdego sprzedawcę

print(df.groupby(['Sprzedawca'], as_index= False)['idZamowienia'].count())
print('\n\n\n')
#sumę zamówień dla każdego kraju
print(df.groupby(['Kraj'], as_index= False)['idZamowienia'].count())
print('\n\n\n')
#sumę zamówień dla roku 2005, dla sprzedawców z Polski
print(df[(df['Data zamowienia'].str.slice(start = 6)=='2005') & (df['Kraj']=="Polska")].agg({'Kraj':['count']})) #mój plik csv się rózni
print('\n\n\n')

#średnią kwotę zamówienia w 2004 roku,
dfx = df[(df['Data zamowienia'].str.slice(start = 6)=='2004')]
print(pd.to_numeric(dfx['Utarg']).mean())
print('\n\n\n')
