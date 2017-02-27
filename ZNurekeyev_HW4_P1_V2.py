#import functions
import numpy
from random import random
from pylab import show,plot,xlabel,ylabel,ylim

#define constans
NBi3=10000
NPb=0
NTi=0
NBi9=0
Total=10000
tauBi3=46*60
tauPb=3.3*60
tauTi=2.2*60
h=1.0
pBi3=1-2**(-h/tauBi3)
pPb=1-2**(-h/tauPb)
pTi=1-2**(-h/tauTi)
tmax=20000.0
tpoints=numpy.arange(0.0,tmax,h)
Bi3points=[]
Pbpoints=[]
Tipoints=[]
Bi9points=[]
Totalpoints=[]

#loop
for t in tpoints:
	Bi3points.append(NBi3)
	Pbpoints.append(NPb)
	Tipoints.append(NTi)
	Bi9points.append(NBi9)
	Totalpoints.append(Total)
	decayBi3=0
	decayTi=0
	decayPb=0

	Total=NBi3+NPb+NTi+NBi9
#Pb decay
	for l in range(NPb):
		if random()<pPb:
			decayPb+=1
	NPb-=decayPb
	NBi9+=decayPb
#Ti decay
	for j in range(NTi):
		if random()<pTi:
			decayTi+=1
	NTi-=decayTi
	NPb+=decayTi

#Bi313 decay
	for i in range(NBi3):
		if random()<pBi3:
			decayBi3+=1
	NBi3-=decayBi3
#choosing decay path
	for k in range(decayBi3):
		if random()<0.9791:
			NPb+=1
		else:
			NTi+=1

#plot the answer
plot(tpoints,Bi3points,tpoints,Tipoints,tpoints,Pbpoints,tpoints,Bi9points,tpoints,Totalpoints)
ylim(-1000,11000)
xlabel("Time")
ylabel("Number of atoms")
show()