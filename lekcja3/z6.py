import math as m
def okrag(x=0, y=0, a=0, b=0):
    return m.sqrt((x-a)**2 + (y-b)**2) #lub całość **0.5

print(okrag(1, 1))
print(okrag(1, 1, 1, 1))
print(okrag(4, 4, 6, 6))