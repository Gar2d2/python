class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x

    def __add__(self, _Kwadrat):  #overload operatora dodawania
        return Kwadrat(self.x + _Kwadrat.x) 
    #ge >=
    def __ge__(self, _Kwadrat):
        if self.x >= _Kwadrat.x:
            return 1
        
        return 0

    def __gt__(self, _Kwadrat):
        if self.x > _Kwadrat.x:
            return 1
        
        return 0

    def __le__(self, _Kwadrat):
        if self.x <= _Kwadrat.x:
            return 1
        
        return 0

    def __lt__(self, _Kwadrat):
        if self.x < _Kwadrat.x:
            return 1
        
        return 0
    



class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8 * self.x

    def pole(self):
        return 3 * self.x * self.y



kwadracik1 = Kwadrat(10)
kwadracik2 = Kwadrat(10)
sumakwadratow = kwadracik1 + kwadracik2
print(str(sumakwadratow.pole()))
print(str(kwadracik2 >= kwadracik1))
print(str(kwadracik2 > kwadracik1))
print(str(kwadracik2 <= kwadracik1))
print(str(kwadracik2 < kwadracik1))