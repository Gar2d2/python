with open("plik.txt", "w") as wplik:
    wejscie = input("wpisz tekst: ")
    while wejscie != "":
        wplik.write(wejscie + "\n")
        wejscie = input("wpisz tekst: ")

    
with open("plik.txt", "r") as rplik:
    for linia in rplik:
        print(linia, end="")