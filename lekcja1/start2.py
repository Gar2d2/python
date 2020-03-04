#!/usr/bin/env python3
#a = input()   #wprowadzanie danych
#print(f"wprowadziłeś: {a}")
#print(type(a))
#int("100")
# <class 'str>
liczba=100

if liczba < 100 and liczba >0:
    print("liczba mniejsza niż 100")
elif liczba >0:
    print("liczba większa od 0")
else:
    print("")


if 0 < liczba < 100:
    print("liczba mniejsza niż 100")


#pętla for

imie = "Amanda"
#for jako foreach
for litera in imie:
    print(litera, end='')
print("\n")

for litera in imie:
    print(litera)

print("\n")

for liczba in range(10):
    print(liczba)

print("\n")

for liczba in range(1,11):
    print(liczba)

print("\n")
for liczba in range(1, 11, 2):
    print(liczba)

print("\n")


#range to generator 
print(list(range(1, 11, 2)))
print(list(range(11, 1, -2)))

#slice
print(imie[0:2:2])  #do zmiennej imie = "Amanda"
print(imie[::2]) #pomijając parametry ustawiam wartości domyślne [start:stop:step]