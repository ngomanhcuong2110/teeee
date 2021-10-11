from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt
xmin, xmax,xstep=-4.5,4.5,0.2
ymin, ymax,ystep=-4.5,4.5,0.2
x,y=np.meshgrid(np.arange(xmin,xmax,xstep),np.arange(xmin,xmax,xstep))
z=x**2+y**2
fig=plt.figure(figsize=(8,5))
ax=plt.axes(projection='3d',elev=50,azim=-50)
ax.plot_surface(x,y,z,norm=LogNorm(),rstride=1,cstride=1,edgecolor='none',alpha=.9,cmap=plt.cm.jet)
ax.set_ylabel('$')
ax.set_xlabel('$')
ax.set_zlabel('$')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
plt.show()