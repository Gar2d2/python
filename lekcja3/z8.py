import math as m
def ciag(a=1, r=1, ile=10 ):
    return sum(wyraz*r+a for wyraz in range (ile))

print(ciag(4, 0, 0))
print(ciag(5, 5, 3))
print(ciag(0, 5))
