class Even:
    """Iterator zwracajacy wartosci na parzystych indeksach"""
    def __init__(self, data):
        self.data = data
        self.index = -2 #zero też jest parzysta a pierwsza iteracja doda 2
        self.max = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 2
        if self.index >= self.max:
            raise StopIteration
        return self.data[self.index]

for i in Even([2,4,5,6,7,8]):
    print(i)

for i in Even(['ala', 'michal', 'agnieszka']):
    print(i)

for i in Even('karmazynoweniebo'):
    print(i)