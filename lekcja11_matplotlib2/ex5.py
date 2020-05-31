import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def rysuj(n,size, gestosc = 0.25):
    ax = fig.add_subplot(1,size,n+1, projection = '3d' )
    X = np.arange(- 5 , 5 , gestosc)
    Y = np.arange(- 5 , 5 , gestosc)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X** 2 + Y** 2 )
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, cmap =colormap[0],
    linewidth = 0 , antialiased = True )
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator( 10 ))
    ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
    fig.colorbar(surf, shrink = 0.5 , aspect = 5)

colormap = ['PiYG', 'PRGn', 'seismic', 'bwr', 'gist_rainbow']
fig = plt.figure(figsize=plt.figaspect(0.2))

rysuj(0, 2)
rysuj(1, 2, 0.1)
plt.show()