# This function sometimes works correctly, but other times it produces incorrect results. Can you help you fix the bug?

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = 0
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = min(numbers)
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98, outputs 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5, outputs 5
print(find_maximum([-10, -3, -20]))   # Expected -2, outputs 0