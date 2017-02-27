"""
part a) For satellite in order to orbit earth, there should be force 
that will counter-act gravitaional force >> m*a=G*m*M/(r^2) >> a=G*M/(r^2). 
The force, obviously, must be tangential. a=v^2/r. Also, v=w*r=2*pi*f*r=2*pi*r/T. 
Then 4*pi^2*r/(T^2)=G*M/(r^2) >> r^3=G*M*T^2/(4*pi^2). 
Since r is distance between mass centers of each body (Earth and sattellite), 
we can take it as sum of Earth radius and distance to satellite from Earth surface r=R+h. 
Finally, R+h=(G*M*T^2/(4*pi^2))^1/3 >> h=(G*M*T^2/(4*pi^2))^1/3-R.
"""
#part b) first input desired period
user_period=float(input("Enter the period of satellite in minutes: "))
#import functions we need
from math import pow
from math import pi
from numpy import array
#create an array of periods including 90 min, 45 min etc. Converted to seconds
period=array([user_period, 24*60*60, 23.93*60*60, 90*60, 45*60], float)
#calculations
coef=pow(6.67*10**(-11)*5.97*10**24/(4*pi**2),(1/3))
altitude=pow(period,(2/3))*coef-6371000
#print all the results
print("The altitude of satellite in meters is: ",int(altitude[0]), \
      "\nIf period is 1 day: ",int(altitude[1]),\
      "\nIf period is 90 minutes: ",int(altitude[3]), \
      "\nIf period is 45 minutes: ",int(altitude[4]), \
      "\nThe difference between 24 hours and 23.93 hours: ",int(altitude[2]-altitude[1]))
"""
part c) If period is 45 minutes, satellite should orbit inside Earth. Therefore, this period is impossible.
part d) The period of Earth, spinning around itself, is 23.93 hours. 
That's why the period of geosyncrhonous satellite is 23.93 hours.
""" 