#błąd przy podaniu wartości ujemnej do pierwiastka
while 1:
    try:
        n=float(input("wprowadź liczbę: "))
        break
    except ValueError:
        print("nieprawidłowe dane wejściowe ")
input() #dodane, żeby konsolowe okienko nie uciekało 