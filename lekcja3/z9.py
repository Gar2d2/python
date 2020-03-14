
def ciag(*liczby ): #gwiazdka pojawia się jeżeli może być wiele argumentów ( nie jest podana ilosc)
    if len(liczby) == 0:
        return 0
    suma=1
    for i in liczby:
        suma*=i
    return suma

print(ciag(1,2,3,4))
print(ciag())
