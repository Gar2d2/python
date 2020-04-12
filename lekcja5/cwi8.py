class Samogloski:
    """Iterator przyjmujacy tylko string i zwracajacy samogloski"""
    def __init__(self, data):
        if not(isinstance(data, str)):
            raise ValueError("passed value isnt string")
        self.data = data
        self.index = -1 #pierwsze wywoałanie next podbija o 1 wiec da 0
        self.max = len(data) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        self.index += 1
        for j in "aeyiou":
            if self.data[self.index] == j:
                self.index += 1
                return j
        return next(self)
                
        

        





for i in Samogloski('akarmazynoweniebo'):
    print(i)