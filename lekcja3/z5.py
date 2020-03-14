def prosta(a1, a2):
    if a1==a2:
        return "proste równoległe"
    elif a1*a2==-1:
        return "proste prostopadłe"
    else:
        return "proste nie są w relacji"
    

print(prosta(1, -1))
print(prosta(1, 1))
print(prosta(-1, -2))
