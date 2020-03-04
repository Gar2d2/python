#!/usr/bin/env python3
#tworzenie  przykładowej listy
lista=["ala", 3.14, 2, 1e30, [1, 2, 3]]
print('zadeklarowana lista\n ', lista, "\n")
#dodajemy element na koniec
lista.append("ostatni")
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#dodajemy element na indeksowanym miejscu 
lista.insert(1,"kot")
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#usuwanie ostatniego elementu
lista.pop() # dodając indeks w środku pop(2) usuwamy wybraną pozycję
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#usunięcie po wartości 
lista.remove(3.14)
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#zamiast przez pop możemy usunąć o tak \/\/
del lista[2]
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#dodawanie sekwencji do listy
lista.extend((1,2,3,4,5))
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#zmiana wartości wybranego elementu
lista[0]="ela"
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#usuwanie fragmentu lissty po indeksach 
del lista[3:5]
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#przypisanie nowyCh wartości do podanego wycinka
lista [3:7] = [1,2,3,4]
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#odwracanie kolejności
lista.reverse()
print('zadeklarowana lista po zmianach\n ', lista,"\n" )
#sortowanie
nowa=[5 ,4 ,2 ,0 ,8 ,23 ,42]
print('nowa lista\n ', nowa,"\n" )
nowa.sort()
print('nowa lista po sortowaniu\n ', nowa,"\n" )