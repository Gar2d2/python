import pandas as pd
import numpy as np
import xlrd
import openpyxl
###########zadanie 1###########
df = pd.read_excel('./imiona.xlsx')
#print(df)

############zadani 2###########

#tylko rekordy gdzie iczba nadanych imion była większa niż 1000 w danym roku
print(df[pd.to_numeric(df['Liczba']) > 1000])


#tylko rekordy z imieniem takie jak twoje
print(df[(df['Imie']=='PIOTR')])

#sume wszystkich urodzonych dzieci w całym danym okresie//czyli z całego pliku?
print(df['Liczba'].sum())

#sume dzieci urodzonych w latach 2000-2005
dfex = df.where((df['Rok'] >= 2000) & (df['Rok'] <= 2005))
print(dfex['Liczba'].sum())

#sume urodzonych chlopcow i dziewczynek // ale kiedy? w całym pliku?
print(df['Liczba'].sum())

#najbardziej popularne imie dziewczynki i chopca w danym roku(czyli po 2 rekordy na rok)
dfex = df.groupby(['Rok', 'Plec'])['Liczba'].transform(max) == df['Liczba']

print(df[dfex])

#najbardziej popularne imie dziewczynki i chłopca w całym danym okresie
dfex = df.groupby(['Plec'])['Liczba'].transform(max) == df['Liczba']
print(df[dfex])