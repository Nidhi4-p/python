s=[]
n=input("enter the 4 digit binary numbers seperated by commas:\n").split(',')
for i in n:
	x=int(i,2)
	if (x%5==0):
		s.append(i)	
print(",".join(s))	

