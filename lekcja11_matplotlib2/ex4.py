import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

colormap = ['b','g','r','c','m','y','k','w']
colormap2 = ['b','g','r','c','m','y']
# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 151 , projection = '3d' )
ax2 = fig.add_subplot( 152 , projection = '3d' )
ax3 = fig.add_subplot( 153 , projection = '3d' )
ax4 = fig.add_subplot( 154 , projection = '3d' )
ax5 = fig.add_subplot( 155 , projection = '3d' )
# fikcyjne dane
_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
print('xx, yy')
print(_xx)
print(_yy)
x, y = _xx.ravel(), _yy.ravel()
print('x, y')
print(x)
print(y)
top = x + y
print('top')
print(top)
bottom = np.zeros_like(top)
print('bottom')
print(bottom)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax2.set_title('Wykres przezroczysty zielony')
ax3.bar3d(x, y, bottom, width, depth, top, shade = True, color = 'g', alpha = 0.5)
ax3.set_title('Wykres nie zacieniony')
for i in range(len(y)):
    ax4.bar3d(x[i], y[i], bottom[i], width, depth, top[i],shade = False, color = colormap[i % len(colormap)]*len(y), alpha = 0.5)
ax4.set_title('Wykres 8kolorowy')
ax5.bar3d(x, y, bottom, width, depth, top, shade = False, color = colormap2*len(y) )
ax5.set_title('Każda ściana w innym kolorze')
plt.show()