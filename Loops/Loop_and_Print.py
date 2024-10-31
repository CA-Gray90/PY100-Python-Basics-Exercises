# Add some code inside the following for loop to print the current value of num on each iteration. 
# Before you execute the code: What sequence of numbers do you expect to be printed?

for num in range(0, 11, 2):
    print(num)


# The sequence of numbers produced by range produces numbers from `0` up to and including `10`. 
# A third argument is passed to range, which is the step. The step is `2`, therefore range will produce the numbers 0, 2, 4, 6, 8, 10, going up in increments of 2.

# Therefore the expected output on each loop will be:
#     => `0`
#     => `2`
#     => `4`
#     => `6`
#     => `8`
#     => `10`
