"""
part a) p(x)=w(x)/integral(w(x)) from 0 to 1. 
Integral(x^(-1/2))=
2*x^(1/2)=
2*1^(1/2)-2*0^(1/2)=
2
p(x)=x^(-1/2)/2

Transforming formula:
z=Integral(p(x)dx)from 0 to x
Integral(x^(-1/2)/2)=
x^(1/2)=
x^(1/2)-0^(1/2)=
x^(1/2)
z^2=x
z is uniform random distribution from 0 to 1
"""
# part b) import functions
from math import exp
from random import random

#define constans
N=1000000
I=0
#Loop

for i in range(1,N):
	x=random()**2
	I+=2/(exp(x)+1)
I=I/N
print('The result is',I)

#result is 0.8387311270927638