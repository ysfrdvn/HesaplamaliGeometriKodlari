from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-14,14,0.25)
y=np.arange(-14,14,0.25)
x,y=np.meshgrid(x,y)
r=x**2+y**2
z=np.sin(r)
x_plane=np.arange(-3,7,0.5)
y_plane=np.arange(-3,7,0.5)
x_plane,y_plane=np.meshgrid(x_plane,y_plane)
z_plane=-5+2*x_plane+4*y_plane
ax.plot_surface(x,y,r,rstride=1,cstride=1,cmap="hot")
ax.plot_surface(x_plane,y_plane,z_plane,rstride=1,cstride=1,cmap="hot")
plt.show()
