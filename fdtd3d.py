from pylab import *
from scipy import *
from matplotlib import cm

X = 15
Y = 15
Z = 15

dx = 0.02
dy = 0.02
dz = 0.02
dt = 0.0001

Ro = 1.21
C = 343
K = Ro*C*C
Zp=Ro*C

Q = 0.5+0.5*cos(arange(-pi,pi,2*pi/200))

P = zeros((X,Y,Z),"float64")
#P2 = zeros((X,Y),"float64")

Ux = zeros((X+1,Y,Z),"float64")
#Ux2 = zeros((X+1,Y),"float64")

Uy = zeros((X,Y+1,Z),"float64")
#Uy2 = zeros((X,Y+1),"float64")

Uz = zeros((X,Y,Z+1),"float64")
mic = []

for n in range(5000):
    if n<len(Q):
        P[7,7,0] += Q[n]

    mic.append(P[7,7,14])

    for x in range(X-1):
        for y in range(Y):
            for z in range(Z):
                Ux[x+1,y,z] = Ux[x+1,y,z] -dt/Ro/dx*(P[x+1,y,z]-P[x,y,z])

    for x in range(X):
        for y in range(Y-1):
            for z in range(Z):
                Uy[x,y+1,z] = Uy[x,y+1,z]-dt/Ro/dy*(P[x,y+1,z]-P[x,y,z])
    for x in range(X):
        for y in range(Y):
            for z in range(Z-1):
                Uz[x,y,z+1] = Uz[x,y,z+1]-dt/Ro/dz*(P[x,y,z+1]-P[x,y,z])
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                P[x,y,z] = P[x,y,z] - K*dt/dx*(Ux[x+1,y,z]-Ux[x,y,z]) \
             - K * dt/dy*(Uy[x,y+1,z]-Uy[x,y,z]) \
             - K * dt/dz*(Uz[x,y,z+1]-Uz[x,y,z])

    for x in range(X):
        for y in range(Y):
            Uz[x,y,0]=P[x,y,0]/-Zp
            Uz[x,y,14]=P[x,y,14]/-Zp

    for y in range(Y):
        for z in range(Z):
            Ux[0,y,z]=P[0,y,z]/-Zp
            Ux[14,y,z]=P[14,y,z]/-Zp
    for z in range(Z):
        for x in range(X):
            Uy[x,0,z]=P[x,0,z]/-Zp
            Uy[x,14,z]=P[x,14,z]/-Zp
figure()
plot(mic)

xlabel("sample")
ylabel("Relative sound plessure")
show()

figure()
contourf(P.T,aspect="equal", cmap=cm.jet)
xlim(0,X-1)
ylim(0,Y-1)
xlabel("X [sample]")
ylabel("Y [sample]")
show()
