class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

for i in Wspak([2,4,5,6,7,8]):
    print(i)

for i in Wspak(['ala', 'michal', 'agnieszka']):
    print(i)

for i in Wspak('karmazynoweniebo'):
    print(i)