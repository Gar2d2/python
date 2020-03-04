#!/usr/bin/env python3
andżej = ["Andrzej","Andżej"]
przezwiska = {"andż":andżej,
    "przez1":"imie nazwisko1",
    "przez2":"imie nazwisko2",
    "przez3":"imie nazwisko3",
    "przez4":"imie nazwisko4",
    "przez5":"imie nazwisko5"
}
print(przezwiska["andż"]) #odwolanie przez klucz

print("Andrzej zwany również  ", przezwiska["andż"],
 " spotkał się dzisiaj z przez1 zwanym {0}".format(przezwiska["przez1"]),
 ' kolegą przez2 %(zm1)s' % {'zm1':przezwiska["przez2"]} )
 #różne możliwości zapisu  ^^
 
 
#c