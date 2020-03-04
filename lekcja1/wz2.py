#!/usr/bin/env python3
a=2
b=3
c=4
print(f"dzielenie= {c/a}")
print("dodawanie- " + str(a+b+c))
print(f"odejmowanie- {a-b-c}")
print( f"dzielenie całkowite {a} i {b} = " + str(b//a))
print("potęga {0} do {1}=  ".format(a,b) + str(a**b)  
+ f" funkcją power {b} do {a} = {pow(b,a)} " )
reszta= b%a
print("3%2 = "  + str(reszta))