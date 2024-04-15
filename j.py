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

