class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print("jestem na x = ", self.x, " i y = ", self.y)
    
    def __del__(self):
        print("brlerlelggeekekheeee (robak zdechł)")
    



biedronka = Robaczek(20, 20, 2)
biedronka.idz_w_gore(5)
biedronka.pokaz_gdzie_jestes()
biedronka.idz_w_dol(2)
biedronka.pokaz_gdzie_jestes()
biedronka.idz_w_prawo(5)
biedronka.pokaz_gdzie_jestes()
biedronka.idz_w_lewo(2)
biedronka.pokaz_gdzie_jestes()