slownik = {
"mleko":"l", "ziemniaki":"kg","czosnek":"szt", "brokuł":"szt", "kapusta":"szt"}

print(slownik.keys())
print(slownik.values())


slownik2 = {key:value for key, value in slownik.items() if value=="szt"}


print(slownik2.items())

