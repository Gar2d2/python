#python comprehensions 
import random as r

#random.radint(zakres min, zakres max
b = r.randint(1, 50)

A = [[r.randint(1, 50) for wiersz in range(4)] for liczba in range(4)]

print(A)

[print(A[i][i]) for i in range(4)]
