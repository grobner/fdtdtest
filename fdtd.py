from pylab import *
from scipy import *
from matplotlib import cm

X = 40
Y = 30

dx = 1
dy = 1
dt = 0.0001

Ro = 1.21
C = 343
K = Ro*C*C

Q = 0.5+0.5*cos(arange(-pi,pi,2*pi/200))

P = zeros((X,Y),"float64")
#P2 = zeros((X,Y),"float64")

Ux = zeros((X+1,Y),"float64")
#Ux2 = zeros((X+1,Y),"float64")

Uy = zeros((X,Y+1),"float64")
#Uy2 = zeros((X,Y+1),"float64")

mic = []

for n in range(5000):
    if n<len(Q):
        P[20,15] += Q[n]

    mic.append(P[0,0])

    for x in range(X-1):
        for y in range(Y):
            Ux[x+1,y] = Ux[x+1,y] -dt/Ro/dx*(P[x+1,y]-P[x,y])

    for x in range(X):
        for y in range(Y-1):
            Uy[x,y+1] = Uy[x,y+1]-dt/Ro/dy*(P[x,y+1]-P[x,y])

    for x in range(X):
        for y in range(Y):
            P[x,y] = P[x,y] - K*dt/dx*(Ux[x+1,y]-Ux[x,y]) \
             - K * dt/dy*(Uy[x,y+1]-Uy[x,y])

figure()
plot(mic)

xlabel("sample")
ylabel("Relative sound plessure")
show()
