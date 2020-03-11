#python comprehensions 
litery = [print(znak) for znak in "Wojtek"]

print(type(litery))
print(litery)

M = [
    [1, 2],
    [3, 4]]

[print(liczba) for wiersz in M for liczba in wiersz]


import this #pep 20 -python manifest
index = 0
#krotka nie jest mutowalna - jak zadeklaruje nie moge zmmienić elementu, można przypisać całej nową wartość
#pakowanie krotki
punkt = (0, 0)
#rozpakowanie krotk
x, y = (120, 130)


{krotka[0]:krotka[1] for krotka in enumerate('Wojtek')} # enumerate zwraca indeks i wartość w postaci krotki
{indeks:litera for indeks, litera in enumerate('Wojtek')} 

#for _ in slownik: #funkcja items() nie widzialna tutaj , ona tam jest
 #   print(_)

slownik = {'imie':'Marian', 'nazwisko':'Bąbel'}
{wartosc:klucz for klucz, wartosc in slownik.items()} #zapisuje w kolejności odwrotnej .items() zwraca krotke
#nie podając dodatkowych opcji w slownik -będzie zwracany slownik.keys()

#timeit -- pakiet pozwalający sprawdzić czas wykonywania jakiejś operacji
#jaka jest różnicza przy inicjalizacji 
lista = list()
lista2 = []


wielkie = [str.upper(znak) for znak in "Wojtek"]
print(wielkie)

#funkcje argumenty pozycyjne
def dodaj(liczba1, liczba2):
    return liczba1 + liczba2

print(dodaj(1, 2))

#wartości domyślne 
def witaj(imie='Jan', nazwisko = 'Kowalski'):
    print(f"witaj {imie} {nazwisko}!")



print(witaj("andrzej"))

def dodaj(* liczby):
    return sum([liczba for liczba in liczby]) #funkcja sum zwraca sume wartości numerycznych w danej kolekcji

print(dodaj(1, 2, 3 , 5, 6, 7, 8, 9, 10))
    

#import start
#from start import coś