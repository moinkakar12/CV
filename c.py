# (c) Write a program that prints a multiplication table for the given number.

table = int(input("Enter a number's table: "))
limit = 10
for i in range(1, limit + 1):
	print(str(table) + "x" + str(i) + "=" + str(i*table))
