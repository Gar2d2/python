import os
commit= input("wprowadź treść commita")
os.system("git add . ")
os.system("git commit -m '" + commit + "'")
os.system("git push origin master")
input()