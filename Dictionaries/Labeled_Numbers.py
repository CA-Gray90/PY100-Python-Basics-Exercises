# Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

# for pair in numbers.items():
#     a, b = pair
#     print(f'A {a} number is {b}')

# for key in numbers:
#     print(f'A {key} number is {numbers[key]}')

for key, value in numbers.items():
    print(f'A {key} number is {value}')

# Expected output:
# A high number is 100.
# A medium number is 50.
# A low number is 10.