#import array
from numpy import array
#imput v/c and distance
speed_ratio=float(input("Enter 'velocity/speed of ligth' ratio (less than 1): "))
distance=float(input("Enter distance in light years: "))
#create arrays
velocities=array([speed_ratio,0.9,0.98,0.999],float)
distances=array([distance,10,10,10],float)
#calculate times
time_passenger=distances/velocities
time_observer=(time_passenger+(distances*velocities))/((1-velocities**2)**(1/2))
#print results
print("If 'v/c' is:",velocities[0],"and distance is:",distances[0],", Then fligth duration measured by passenger is:",time_passenger[0],"and by observer:",time_observer[0])
print("If 'v/c' is:",velocities[1],"and distance is:",distances[1],", Then fligth duration measured by passenger is:",time_passenger[1],"and by observer:",time_observer[1])
print("If 'v/c' is:",velocities[2],"and distance is:",distances[2],", Then fligth duration measured by passenger is:",time_passenger[2],"and by observer:",time_observer[2])
print("If 'v/c' is:",velocities[3],"and distance is:",distances[3],", Then fligth duration measured by passenger is:",time_passenger[3],"and by observer:",time_observer[3])