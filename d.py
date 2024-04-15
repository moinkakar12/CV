# d) Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

a = int(input("Enter a Number: "))
sum = 0
for i in range(1, a+1): #inclusive
    sum+=i
    print(sum)
