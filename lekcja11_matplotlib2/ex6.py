import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122 , projection = '3d' )
#plot
t = np.linspace( 0 , 1, 5 )
z = t
x = np.arange(5)
y = np.arange(5)

ax1.plot(x, y, z, label = 'wykres liniowy' )
ax1.legend()
ax1.set_title('Wykres zacieniony')
#scatter
xs = np.arange(20)
ys = np.arange(20)
zs = np.arange(20)
ax2.scatter(xs, ys, zs, c ='r', marker ='^', label = 'wykres punktowy')

ax2.legend()
plt.show()