# (f) Print the following using for loop
#12345
#1234
#123
#12
#1

num = int(input("Enter Number of rows: "))  
for i in range(num):
	
	for j in range(num - i):
		print(j+1,end=" ")

	print()
	
	

