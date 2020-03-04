#!/usr/bin/env python3
print("Witaj świecie!")
a = 'Ala'
b = 'Marek'
c = 'Jarek'

print(a)
print(b)
print(c)

#blok kodu
# for element in kolekcja:
#     for element2 in kolekcja2:
d = """Ala
ma
dużego 
kota"""
print(d)
# def funkcja():
#     """ dokumentacja """
print(type(a)) #wyswietla typ <class 'nazwa'>
print(a + ' ' + b) #__add__
print(4 + 2)
print(4 - 2)
print(4 * 2)
print(9 / 2)
print(9 // 2) #dzielenie bez reszty
print(4 % 2) #modulo
print(4 ** 2) #potęgowanie
print(3.35 + 33.35) #kropka zamiast przecinka

import math as m    #lub    from math pi, pow, etc.

print("Ala ma " + str(4)+ " lata") #rzutowanie str(1), int(1), float(1)
print("{1} ma {2} lat".format(4, c, 6, "lat")) #lista parametrow
wiek = 3 
print(f"Marek ma {wiek} lata") #fstring
imie = 'Ala'
print(dir(imie))
imie = imie.upper()

print(imie[2])

#LISTY
lista = [1, 2, 3, 4, 'Ala']
print(lista)
lista2 = list() # to samo co lista=[]
lista2.append(12542) #dodaje na koniec listy
print(lista2)
lista[0] = 75 #w listach mozna
lista3 = lista + lista + lista2
print(lista3)

slownik = {"imie": "Andrzej", "wzrost": 185}
print(slownik["imie"]) #odwolanie przez klucz
print(slownik.keys())
print(slownik.values())