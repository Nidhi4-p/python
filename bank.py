
balance=0
while True:
	a=input()
	b=a.split()
	
	if not a:
		break
	
	c=int(b[1])
	if (b[0]=='D'):
		balance=balance+c
	elif (b[0]=='W'):
		balance=balance-c
	else:
		break
print(balance)

