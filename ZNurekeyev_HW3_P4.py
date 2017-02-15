#import functions
from numpy import zeros
from math import exp
from pylab import show,plot,xlabel,ylabel
#define integrand function
def f(t):
	return exp(t**2)
#set limits and array for answer
N=10
a=0.0
answer=zeros([31,2])
#integrate using Simpson's rule
for i in range (0,31):
	x=i/10
	b=x
	h=(b-a)/N
	s=h*(f(a)+f(b))/3
	for k in range (1,int(N/2)+1):
		s+=4*h*f(a+h*(2*k-1))/3
	for k in range (1,int(N/2-1)+1):
		s+=2*h*f(a+2*k*h)/3
	answer[i,0]=x
	answer[i,1]=s
#plot the answer
plot(answer[:,0],answer[:,1])
xlabel("x")
ylabel("E(x)")
show()