class Material:
    

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc 

    def wyswietl_nazwe(self):
        print(self.rodzaj)



class Ubrania(Material):

    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    def wyswietl_dane(self):
        print(self.rozmiar," ", self.kolor, " ",self.dla_kogo)




class Swetry(Ubrania):
    
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
        Ubrania.__init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print(self.rodzaj_swetra)






ubranie = Ubrania("jedwab", 20, 20, 29, "czerwony", "kobiecy")
ubranie.wyswietl_dane()
ubranie.wyswietl_nazwe()

sfeter = Swetry("dziurawy", 20, 20, 29, "czerwony", "kobiecy", "duży")
sfeter.wyswietl_nazwe()
sfeter.wyswietl_dane()



