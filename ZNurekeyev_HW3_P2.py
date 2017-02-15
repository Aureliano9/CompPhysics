from math import sqrt
#input variables
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
#calculate roots
xA1=(-b+sqrt(b*b-4*a*c))/(2*a)
xA2=(-b-sqrt(b*b-4*a*c))/(2*a)
xB1=2*c/(-b-sqrt(b*b-4*a*c))
xB2=2*c/(-b+sqrt(b*b-4*a*c))
print("Method A (x1 and x2): ",xA1,";",xA2,"\nMethod B (x1 and x2): ",xB1,";",xB2)
#difference comes from subtraction -b+sqrt(b^2-4ac), but we can use the roots where we have summation only,
#which is x2 from Method A and x1 from Method B
print("Best x1 is: ",xA2,"; Best x2 is: ",xB1)
#answers are:
#Method A (x1 and x2):  -9.999894245993346e-07 ; -999999.999999
#Method B (x1 and x2):  -1.000000000001e-06 ; -1000010.5755125057
#Best x1 is:  -999999.999999 ; Best x2 is:  -1.000000000001e-06