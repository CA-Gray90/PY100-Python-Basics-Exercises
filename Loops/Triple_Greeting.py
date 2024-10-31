# Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'

for i in range(3):  # `i` can be replaced with `_` if your not using the loop variable in the loop. This is common python convention.
    print(greeting)

# Another solution (more memory intensive?):
greeting = 'Aloha!'

counter = 3
while counter > 0:
    print(greeting)
    counter -= 1

# Another solution:
[print(greeting) for _ in range(3)]
