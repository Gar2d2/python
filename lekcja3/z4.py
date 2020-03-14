def monotonicznosc(a):
    if a>0:
        print("funkcja rosnąca")
    elif a==0:
        print("funkcja stała")
    else:
        print("funkcja malejąca")

print(monotonicznosc(1))
print(monotonicznosc(0))
print(monotonicznosc(-1))