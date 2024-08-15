# (a) Print multiple messages using print statement.

print("Course = Introduction To Computer Vision")
print("Session = 2021-2025")
print("Semester = 6th Semester")


# (b) Take an integer and print whether it is odd or even.

a = int(input("Enter a Integer: "))
if (a % 2) == 0:
    print('The Number is Even')
else:
    print('The Number is Odd')
    

# (c) Write a program that prints a multiplication table for the given number.

table = int(input("Enter a number's table: "))
limit = 10
for i in range(1, limit + 1):
	print(str(table) + "x" + str(i) + "=" + str(i*table))
	
	
	
# d) Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

a = int(input("Enter a Number: "))
sum = 0
for i in range(1, a+1): #inclusive
    sum+=i
    print(sum)
    
    
    
# (e) Using python array list and take 6 courses number show the GP and GPA of that semester.

courses = 6
marks_lst = []

for i in range(1, courses + 1):
    marks = int(input(f"Obtained marks in course {i}: "))
    marks_lst.append(marks)
    
print("\t Course \t Obtained Marks \t Total Marks \t \t GP \t")

GPA = 0
for i, marks in enumerate(marks_lst):  
    total_marks = 100  

    if marks < 50:
        GP = 0
    elif marks >= 80:
        GP = 4.0
    else:
        GP = (marks - 50) / 10 + 1
    
    GPA += GP

    print(f"\t {i + 1} \t\t {marks} \t\t\t {total_marks} \t\t\t {GP}")

print("\n\t ************************************")
print(f"GPA is : {GPA / courses:.2f}")



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
	
	

# (g) Write a program that prints the next 20 leap years.

year = int(input("Enter the year: "))

leap_yr_found = 0
year += 1
while leap_yr_found < 20:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
        leap_yr_found += 1
    year += 1  


# Python program to find largest number in a list.

list1 = []

num = int(input("Enter number of elements in list: "))


for i in range(1, num + 1):
	elements = int(input("Enter elements: "))
	list1.append(elements)

print("Largest element is:", max(list1))



# (i) Write a program that checks whether an element occurs in a list.

List1 = [10, 22, 9, 17, 23, 92, 40, 77, 3, 56, 44]

number = int(input("Enter a Number: "))

if number in List1:
    print("Element exists in the list.")
else:
    print("Element does not exist in the list.")
    
    
#Compute the running of total numbers
    
def compute_running_total(numbers):
    running_sum = 0

    result = []

    for num in numbers:
        running_sum += num  
        result.append(running_sum)

    return result

input_numbers = input("Enter the numbers separated by spaces: ")
numbers = [int(num) for num in input_numbers.split()]

running_totals = compute_running_total(numbers)

print(running_totals)




# (k) Implement binary search you studied in Data Structures.  
          
          
def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


lst = [int(i) for i in input("Enter a list of numbers: ").strip().split()]
num = int(input("Enter the number you want to search in the list: "))

result = binary_search(sorted(lst), num)

if result != -1:
    print(f"{num} is in the list.")
else:
    print(f"{num} is not in the list.")
    








