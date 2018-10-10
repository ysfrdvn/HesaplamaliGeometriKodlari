import numpy as np
import matplotlib.pyplot as plt ##########defterde skaler çarpma . iken kodda * dýr
from mpl_toolkits.mplot3d import Axes3D

point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])

point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])

d1 = -np.sum(point1*normal1) #dot product
d2 = -np.sum(point2*normal2) #dot product
d3 = -np.sum(point3*normal3) #dot product
print(d1,d2,d3)

xx,yy = np.meshgrid(range(5),range(5))### ##3 boyutlu düzlem olusturcam. xyz degerleri var. z yi x ve y ye baglý olarak -
                                         ## -düsünüyorum. x ve y degerleri 30 rangeine atandi
                                          ## hep x hem ye 0,1,2,3,4 iceren(sol) ve 5 tane içeren(sol) dizi
        
z1 = (-normal1[0]*xx - normal1[1]*yy -d1)*1./normal1[2]  ## z = (-d -ax-by)/c
%matplotlib inline
plt3d = plt.figure().gca(projection ='3d')
plt3d.plot_surface(xx,yy,z1, color='red')
##############################################################################################


#########    VÝDA ÞEKLÝ ÇÝZME########

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#plot a helix along the x-axis
n=1000
theta_max = 8*np.pi
theta=np.linspace(0,theta_max,n)
z=theta
y=np.cos(theta)
x=np.sin(theta)
ax.plot(x,y,z,'b',lw=2)
