import random as r
plik = open("mod4.txt", "w+")
i = 0
rand = r.randrange(0,1000)
while i < 4: 
    rand = r.randrange(0,1000)
    if (rand % 4) == 0:
        plik.write(str(rand) + " ")
        i += 1
plik.close()