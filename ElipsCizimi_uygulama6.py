#düzlemde ELİPS gösterme kodu
import numpy as np
import matplotlib.pyplot as plt
a=5
b=3
#plot the ellipce
x = np.linspace(-5.0,5.0, num=300)
y=(b**2*(1-(x**2)/(a**2)))**.5
plt.plot(x,y)
plt.plot(x,-y)
plt.show()
#ax.pltaxes(projection= '3d')
