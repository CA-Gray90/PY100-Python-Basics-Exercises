# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result. How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

# range(start, stop, step) will produce a sequence of numbers from the start up to but not including the stop. 
# without a start specified it will default the start to 0, thus range(5) will produces numbers 0 - 4.

# solution:
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)