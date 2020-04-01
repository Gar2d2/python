
class Ciag:
    
    __ciag__ = []
    __reszta__ = 0
    __pierwszy__ = 0
    __resztaIpierwszy__ = 0

    def wyswietl_dane(self):
        print(self.__ciag__)

    def pobierz_elementy(self, miejsceL, wartoscL):
        self.__ciag__ = [0] * (max(miejsceL) +1) 
        for i in range(len(miejsceL)):
            self.__ciag__[miejsceL[i]] = wartoscL[i]

    def pobierz_parametry(self, reszta, pierwszy, ilosc):
        self.__ciag__ = [i * reszta + pierwszy for i in range(ilosc)]
        self.__resztaIpierwszy__ = 1

    def policz_sume(self):
        return sum([i for i in self.__ciag__])

    def policz_elementy(self):
        if self.__resztaIpierwszy__:
            return len(self.__ciag__)
        return None
        



one = Ciag()
one.pobierz_elementy([0, 2, 3, 5], [2, 4 ,6, 8])
one.__ciag__[3] = 10
one.wyswietl_dane()
print(one.policz_sume())
one.pobierz_parametry(2, 1, 10)
one.wyswietl_dane()
print(one.policz_elementy())
    

