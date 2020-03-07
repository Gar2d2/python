#błąd przy podaniu wartości ujemnej do pierwiastka
while 1:
    try: 
      choice = int(input('podaj liczbę do spierwiastkowania: '))
      assert choice > 0 # sprawdź czy nie jest ujemna
      break
    except AssertionError :  #assert to wszechstronny sposób
      print("liczba jest ujemna")

print(choice**0.5)
input() #dodane, żeby konsolowe okienko nie uciekało 