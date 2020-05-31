
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca( projection = '3d' )
x = [0.0,0.2,0.2,0.2,0.2,0.5]
y = [0.2,0.2,0.4,0.4,0.6,0.6]
z = [0.4,0.4,0.4,0.6,0.6,0.6]
y = np.ravel(y)
ax.plot(x, y, zs = z , zdir = 'z' , label = 'snake' )
colors = ( 'r' , 'g' , 'b' , 'k' )
np.random.seed( 19680801 )





ax.scatter(0.6,0.6, zs = 0.6, c ='r', label = 'apple')


ax.legend()
ax.set_xlim( 0 , 1 )
ax.set_ylim( 0 , 1 )
ax.set_zlim( 0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
ax.view_init( elev = 20. , azim =- 80 )
plt.show()