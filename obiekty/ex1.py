import random as r
plik = open("mod4.txt", "w+")
i = 0
rand = r.randrange(0,1000)
while i < 10:    #generuje 10 liczb z przedziału 0 - 1000 podzielnych przez 4 
    rand = r.randrange(0,1000)
    if (rand % 4) == 0:
        plik.write(str(rand) + " ")
        i += 1
plik.close()