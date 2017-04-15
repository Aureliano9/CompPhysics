#import functions
from math import cos,sin,pi,sqrt
from numpy import array,arange,size
from pylab import plot,xlabel,ylabel,show,text,legend

#set constants and initial values
g = 9.81
R = 0.02
ro = 1.28
roPb = 11.3*1000
roAu = 19.3*1000
roK = 0.9*1000
C = 0.47
m0 = [0, 0, 0]
m0[0] = roPb*(4/3)*pi*R**3
m0[1] = roAu*(4/3)*pi*R**3
m0[2] = roK*(4/3)*pi*R**3
velx0 = 130*cos(47*pi/180)
vely0 = 130*sin(47*pi/180)
x0 = 0.0
y0 = 3.0

#define function
def f(r,t):
	x = r[0]
	y = r[1]
	velx = r[2]
	vely = r[3]
	fcoordx = velx
	fcoordy = vely
	fvelx = -pi*R**2*ro*C/(2*m)*velx*sqrt(velx**2+vely**2)
	fvely = -g-pi*R**2*ro*C/(2*m)*vely*sqrt(velx**2+vely**2)
	return array([fcoordx,fcoordy,fvelx,fvely],float)

#set range of time and increment
a = 0.0
b = 20.0
N = 1000
h = (b-a)/N

#"for" loop to calculate distances for all materials
xcor = 'xcor'
ycor = 'ycor'
for i in range(3):
#create arrrays
	m=m0[i]
	time_s = arange(a,b,h)
	coordx_s = []
	coordy_s = []
	velx_s = []
	vely_s = []
	r = array([x0,y0,velx0,vely0],float)

#solve using 4th order Runge-Kutta method, use break function to stop running when ball hits the ground y=0
	for t in time_s:
		if r[1]<0.0:
			break
		coordx_s.append(r[0])
		coordy_s.append(r[1])
		velx_s.append(r[2])
		vely_s.append(r[3])
		k1 = h*f(r,t)
		k2 = h*f(r+0.5*k1,t+0.5*h)
		k3 = h*f(r+0.5*k2,t+0.5*h)
		k4 = h*f(r+k3,t+h)
		r += (k1+2*k2+2*k3+k4)/6
#to get 6 distinct names (3 coordinates + 3 times) for arrays of each material
	a1 = str(i)
	a2 = xcor+a1
	a3 = ycor+a1
	exec(a2+"=coordx_s")
	exec(a3+"=coordy_s")
	i+=1

#if coordinate array size is smaller than time array, we have to equalize them
time_s0 = time_s[:size(ycor0)]
time_s1 = time_s[:size(ycor1)]
time_s2 = time_s[:size(ycor2)]

#plot coordinates versus time with legend and textbox with distance travelled for Pb
plot(time_s0,xcor0,label='X coordinate')
plot(time_s0,ycor0,label='Y coordinate')
xlabel("Time, s")
ylabel("Coordinates, m")
legend(loc='upper left')
name1 = 'Distance travelled is '
name2 = str(xcor0[size(xcor0)-1])
name5 = ' meters'
name6 = ' (Pb)'
text(0.5,xcor0[size(xcor0)-1]/1.25,name1+name2+name5+name6)
show()

#plot coordinates versus time with legend and textbox with distance travelled for Pb, Au, K
plot(time_s0,xcor0,label='Pb')
plot(time_s1,xcor1,label='Au')
plot(time_s2,xcor2,label='K')
xlabel("Time, s")
ylabel("Coordinates, m")
legend(loc='upper left')
name2 = str(xcor0[size(xcor0)-1])
name3 = str(xcor1[size(xcor1)-1])
name4 = str(xcor2[size(xcor2)-1])
name7 = ' (Au)'
name8 = ' (K)'
text(0.5,900,name1+name2+name5+name6)
text(0.5,850,name1+name3+name5+name7)
text(0.5,800,name1+name4+name5+name8)
show()