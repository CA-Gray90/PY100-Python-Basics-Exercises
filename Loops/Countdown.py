# The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers from 10 to 1 in descending order, followed by 'Launch!'.

# for i in range(1, 11):
#     print(i)

for i in range(10, 0, -1):
    print(i)
print('Launch!')

# Another solution:

reversed_range = reversed(range(1, 11))
for i in reversed_range:
    print(i)
print('Launch!')