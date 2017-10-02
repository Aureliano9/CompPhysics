from math import sin,pi
from numpy import array,arange
from pylab import plot,xlabel,ylabel,show,text

#set constants and initial values including -174 degree in radians
g=9.81
l=0.13
theta0=-174*pi/180
omega0=1.0
user_time=float(input('Enter the time in seconds, when you want to know the angle:'))

#define function
def f(r,t):
	theta = r[0]
	omega = r[1]
	ftheta = omega
	fomega = -(g/l)*sin(theta)
	return array([ftheta,fomega],float)

#set range of time and increment
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N


time_s = arange(a,b,h)
theta_s = []
omega_s = []

r = array([theta0,omega0],float)
for t in time_s:
	theta_s.append(r[0])
	omega_s.append(r[1])
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t+0.5*h)
	k3 = h*f(r+0.5*k2,t+0.5*h)
	k4 = h*f(r+k3,t+h)
	r += (k1+2*k2+2*k3+k4)/6

r0=array(theta_s)
user_theta0=(r0[time_s==user_time])*180/pi
if user_theta0//180%2==1:
	user_theta=user_theta0%180-180
else:
	user_theta=user_theta0%180
name1=str('Angle in degree at ')
name2=str(user_time)
name3=str(' seconds is ')
name4=str(user_theta)

plot(time_s,theta_s,'.')
xlabel("time, s")
ylabel("theta, rad")
text(2,0,name1+name2+name3+name4)
show()