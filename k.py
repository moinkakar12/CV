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

