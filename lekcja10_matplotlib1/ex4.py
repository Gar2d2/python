#Na wykresie wyświetl wykres liniowy 
# funkcji f(x) = 1/x dla x ϵ [1, 20]. 
# Dodaj etykietę do linii wykresu i wyświetl
#  legendę. Dodaj odpowiednie etykiety do osi
#  wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1)
#  oraz (1, długość wektora x).
import math as m
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 30, 301)
s = [(m.sin(i) +2) for i in x]
c = [(m.sin(i + np.pi)) for i in x]

plt.plot(x, s, label = 'sin(x)')
plt.plot(x, c, label = 'sin(x)')
plt.legend(loc = 1,  bbox_to_anchor=(0.2,0.57))
plt.xlabel('x')
plt.ylabel('y')

plt.show()