#import array
from numpy import array
#imput Z and A
atomic_num=int(input("Enter atomic number: "))
mass_num=int(input("Enter mass number: "))
#create arrays
atomic_nums=array([atomic_num,28,28,27],int)
mass_nums=array([mass_num,58,59,58],int)
#define a5 and figure out value
a5=array([0,0,0,0])
for k in range (0,4):
	if mass_nums[k]%2==1:
		a5[k]=0
	elif atomic_nums[k]%2==1:
		a5[k]=-12
	else:
		a5[k]=12
#calculate binding energies and and binding energies per nucleon
bind_en=15.67*mass_nums-17.23*(mass_nums**(2/3))-0.75*(atomic_nums**2)/(mass_nums**(1/3))-93.2*((mass_nums-2*atomic_nums)**2)/mass_nums-a5/(mass_nums**(1/2))
bind_en_nucl=bind_en/mass_nums
#print results
print("If Atomic Number is:",atomic_nums[0],"and Mass Number is:",mass_nums[0],", Then Binding Energy is:",bind_en[0],"and Binding Energy per nucleon is:",bind_en_nucl[0])
print("If Atomic Number is:",atomic_nums[1],"and Mass Number is:",mass_nums[1],", Then Binding Energy is:",bind_en[1],"and Binding Energy per nucleon is:",bind_en_nucl[1])
print("If Atomic Number is:",atomic_nums[2],"and Mass Number is:",mass_nums[2],", Then Binding Energy is:",bind_en[2],"and Binding Energy per nucleon is:",bind_en_nucl[2])
print("If Atomic Number is:",atomic_nums[3],"and Mass Number is:",mass_nums[3],", Then Binding Energy is:",bind_en[3],"and Binding Energy per nucleon is:",bind_en_nucl[3])