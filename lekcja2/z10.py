#!/usr/bin/env python3

a=11
while a>10:
    a=int(input("podaj wysokosc piramidy nie wieksza niz 10: "))

for i in range(0,a,1):
    for j in range(0,i,1):
        print('A', end='')
    print()

