from pylab import *
from scipy import *
import importlib
importlib.import_module('mpl_toolkits.mplot3d').__path__
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

X=40
Y=30

dx=0.1
dy=0.1
dt=0.0001

Ro=1.21
C=343
K=Ro*C*C

ang = arange(-pi,pi,2*pi/50)
sig = cos(ang)
sig += 1

P = zeros((X,Y),"float64")
Ux = zeros((X+1,Y),"float64")
Uy = zeros((X,Y+1),"float64")

fig = figure()
ax = axes3d.Axes3D(fig)

x = arange(0,dx*X,dx)
y = arange(0,dy*Y,dy)
xx,yy = meshgrid(y,x)

surf = ax.plot_surface(xx,yy,P,rstride=1, cstride=1, cmap=cmp.gray)
oldsurf=surf

Z=Ro*C

for t in range(40):
    if t<len(sig):
        P[X/2,Y/2] += sig[t]

    Ux[1:X,:]=Ux[1:X,:]-dt/Ro/dx*(P[1:X,:]-P[:X-1,:])
    Uy[:.1:Y]=Uy[:,1:Y]-dt/Ro/dy*(P[:,1:Y]-P[:,:Y-1])

    Ux[0,:]=P[0,:]/-Z
    Ux[-1,:]=P[0,:]/-Z

    Uy[:,0]=P[:,0]/-Z
    Uy[:,-1]=P[:,-1]/Z

    P[:X,:Y] = P[:X,:Y]-K*dt/dx*(Ux[1:X+1,:]-Ux[:X,:]) \
    -K*dt/dy*(Uy[:,1:Y+1]-Uy[:,:Y])

    surf = ax.plot_surface(xx,yy,P,rstride=1,cstride=1,cmap=cm.jet)
    ax.set_zlim3d(-1,1)
    ax.collections.remove(oldsurf)
    oldsurf=surf
    draw()
    fig.show()
