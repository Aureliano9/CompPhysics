#import functions
from numpy import zeros
from math import exp
from pylab import show,plot,xlabel,ylabel
#input temperature
userT=int(input("Enter the temperature: "))
#set variables
V=0.001
ro=6.022*10**28
kB=1.38*10**-23
TD=428
coef=9*V*ro*kB/(TD**3)
#set array
answer=zeros([496,2],float)
#define function to be integrated
def f(x):
	return x**4*exp(x)/((exp(x)-1)**2)
#integrate user defined temperature and calculate heat capacity
N=1000
a=0.0
b=TD/userT
h=(b-a)/N
s=0.5*f(b)
for k in range (1,N):
	s+=f(a+k*h)
user_answer=s*coef*userT**3
#print result
print("If temperature is: ",userT,", Then heat capacity is: ",user_answer)
#integrate from 5 Kelvin to 500 Kelvin
for T in range(5,501):
	b=TD/T
	h=(b-a)/N
	s=0.5*f(b)
	for k in range (1,N):
		s+=f(a+k*h)
	answer[T-5,0]=T
	answer[T-5,1]=s*coef*T**3
#plot the answer
plot(answer[:,0],answer[:,1])
xlabel("Temperature")
ylabel("Heat capacity")
show()