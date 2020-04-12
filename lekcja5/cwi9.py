def Even(data):
    for i in range(0, len(data), 2):
        yield data[i]



for i in Even([2,4,6,8,10]):
    print(i)