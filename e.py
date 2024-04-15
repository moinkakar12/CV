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


