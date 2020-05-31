import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from random import seed
from random import randint


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 19680801 )


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )


# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
# zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
for c, m, zlow, zhigh in [( 'r' , 'H' ,  randint(-10, 100) , randint(-10, 100) ),
( 'b' , 'v' , randint(-10, 100) , randint(-10, 100) ),
( 'c' , '>' , randint(-10, 100) , randint(-10, 100) ),
( 'y' , '8' , randint(-10, 100) , randint(-10, 100) ),
( 'g' , '.' , randint(-10, 100) , randint(-10, 100) )]:
    n = randint(1,100)
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()