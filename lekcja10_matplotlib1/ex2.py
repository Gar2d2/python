#Na wykresie wyświetl wykres liniowy 
# funkcji f(x) = 1/x dla x ϵ [1, 20]. 
# Dodaj etykietę do linii wykresu i wyświetl
#  legendę. Dodaj odpowiednie etykiety do osi
#  wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1)
#  oraz (1, długość wektora x).
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 20, 20)
print(x)
plt.plot(x, x**-1, 'g--')
plt.plot(x, x**-1, 'g^')
plt.title("wykres x  F(x)")
plt.xlabel('f(x)')
plt.ylabel('x')

plt.show()