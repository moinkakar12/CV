# (g) Write a program that prints the next 20 leap years.

# Prompt the user to enter the year
year = int(input("Enter the year: "))

# Check if the entered year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

