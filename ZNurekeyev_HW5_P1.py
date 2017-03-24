import numpy as np
import pylab as plt
from scipy.optimize import curve_fit
from scipy.signal import argrelextrema

#load data, find standard deviation, cut 3 standard deviations from temperature
data=np.loadtxt('munich.txt')
std_dev=np.std(data[:,1])
data=data[data[:,1]<3*std_dev]
data=data[data[:,1]>(-3)*std_dev]

#input parameters
guess_freq=1
guess_amp=3*np.std(data[:,1])/(2**0.5)
guess_phase=2.9
guess_offset=np.mean(data[:,1])
p0=[guess_freq, guess_amp, guess_phase, guess_offset]

#define function for fit
def my_fun(x,freq,amp,phase,offset):
	return np.cos(x*2*np.pi*freq+phase)*amp+offset

#fit
fit=curve_fit(my_fun, data[:,0], data[:,1], p0=p0)

data_first_guess=my_fun(data[:,0], *p0)
data_fit=my_fun(data[:,0], *fit[0])

#part b) calculating average, hottest and coldest temperatures predicted by model
#find local maxima and minima, then print aveages 
hottest=data_fit[argrelextrema(data_fit,np.greater)[0]]
coldest=data_fit[argrelextrema(data_fit,np.less)[0]]
print('Overal average temperature:',np.average(data_fit))
print('Hottest day:',np.average(hottest))
print('Coldest day:',np.average(coldest))

#plotting results
plt.plot(data[:,0],data[:,1], '.')
plt.plot(data[:,0],data_fit,'o',label='after fitting')
plt.plot(data[:,0],data_first_guess, label='first guess')
plt.xlim(2008,2012)
plt.legend()
plt.show()

#part a) best fit values are: Frequency=1, Phase=2.9
#part b) Average=8.9 ; Hottest=18.7 ; Coldest=-0.6
#part c) parameter b is phase, it characterizes seasons of year
#part c) if we are in antiphase, then model fits summer with winter, spring with autumn etc.