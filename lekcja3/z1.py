#python comprehensions 
A=[1/x for x in range(1, 11)]
print(A)

B=[2**x for x in range(1,11)]
print(B)

C = [x%4 for x in (B)]
print(C)