class Slowa:
    __slowa__ = []

    def wprowadz_slowa(self, *slowa):
        self.__slowa__.clear()
        for arg in slowa:
            self.__slowa__.append(arg)
        
    def Show(self):
        print(self.__slowa__)

    def Sprawdz_czy_palindrom(self):
        for slowo in self.__slowa__:
            print(slowo + " to")
            if slowo == ''.join(reversed(slowo)):
                print(" palindrom")
            else:
                print(" nie jest palindrom")

    def Sprawdz_czy_metagramy(self):
        roznica = 0
        for n in range(len(self.__slowa__[0])):
            if self.__slowa__[0][n] != self.__slowa__[1][n]:
                roznica += 1
            if roznica == 2:
                break

        if roznica < 2:
            print("wyrazy są metagramami")
        else:
            print("wyrazy nie są metagramami")

    def Sprawdz_czy_anagramy(self):
        word1 = list(self.__slowa__[0])
        word2 = list(self.__slowa__[1])
        for letter1 in self.__slowa__[0]:
            for letter2 in word2:
                if letter1 == letter2:
                    word2.remove(letter1)
                    word1.remove(letter1)
                    break
    
        if word1 == word2:
            print("wyrazy sa anagramami")
        else:
            print("wyrazy nie są anagramami")
        





words = Slowa()
words.wprowadz_slowa("andrzej", "marcin")
words.Show()
words.Sprawdz_czy_metagramy()
words.wprowadz_slowa("mamtam", "tammamm")
words.Show()
words.Sprawdz_czy_palindrom()
words.Sprawdz_czy_metagramy()
words.Sprawdz_czy_anagramy()
words.wprowadz_slowa("mata", "tama")
words.Sprawdz_czy_palindrom()
words.Sprawdz_czy_metagramy()
words.Sprawdz_czy_anagramy()

lis = ['a', 'a', 'b', 'a']
lis.remove('a')
print(lis)