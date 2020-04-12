from itertools import combinations

t = [1,2,3,4,5,6,7,8,9,0]
c = list(combinations(t, 3))
unq = set(c)
print(unq)