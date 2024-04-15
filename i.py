# (i) Write a program that checks whether an element occurs in a list.

List1 = [10, 22, 9, 17, 23, 92, 40, 77, 3, 56, 44]

number = int(input("Enter a Number: "))

if number in List1:
    print("Element exists in the list.")
else:
    print("Element does not exist in the list.")
