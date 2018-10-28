'''
Question 4:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

#code:

a=input("enter the string:")
i=0
j=0
for k in a:
	if (k.isupper()):
		i+=1
		
	elif (k.islower()):
		j+=1
	else:
		pass	
	

print("UPPER CASE",i)
print("LOWER CASE",j)		
