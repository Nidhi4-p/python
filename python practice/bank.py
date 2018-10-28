'''question1 :
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500 */'''

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

