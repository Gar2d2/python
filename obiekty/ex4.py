class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def Show(self):
        print(self.nazwa_produktu, end = '\n')
        print(self.ilosc, end = '\n')
        print(self.jednostka_miary, end = '\n')
        print(self.cena_jed, end = '\n')

    def ile_produktu(self):
        print(f"ilosc {self.ilosc} {self.jednostka_miary} ")
    
    def ile_kosztuje(self):
        print(f" koszt {self.ilosc} {self.jednostka_miary} {self.nazwa_produktu} to {self.ilosc * self.cena_jed} zł ")
    

ziemniak = NaZakupy("ziemniak", 3, "kg", 2)

ziemniak.ile_produktu()
ziemniak.Show()
ziemniak.ile_kosztuje()
ziemniak.ilosc = 10
ziemniak.ile_kosztuje()