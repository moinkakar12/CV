# Python program to find largest number in a list.

list1 = []

num = int(input("Enter number of elements in list: "))


for i in range(1, num + 1):
	elements = int(input("Enter elements: "))
	list1.append(elements)

print("Largest element is:", max(list1))

