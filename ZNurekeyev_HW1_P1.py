#take the input from user in decimal
decnum=int(input("Enter your number in decimal: "))
#set variable for answer in binary as string so we can keep adding 0 and 1
answer='0'
#while loop for taking modulus of decimal number and putting it in front of answer as string
while decnum>=1:
	answer=str(decnum%2)+answer
	decnum=int(decnum/2)
#I have to switch to integer and then divide it by two in order to get proper answer
print("Your number in binary is:",int(int(answer)/10))