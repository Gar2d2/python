#!/usr/bin/env python3
short={"cze":"cześć",
"brb":"be right back",
"gtg":"got to go",
"cya":"see ya",
"cu later":"see you later"}
short_cpy=short.copy()
short_cpy["gtg"]="gotta goooo"
print(short,"\n",short_cpy)

#inna możliwośc za pomocą pętli albo 
#short_cpy=dict(short)\
#short_cpy=short stworzy wskaźnik a nie kopie