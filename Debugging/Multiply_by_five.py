# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

# This code assigns number to a string type object rather than an int or float on line 7. Therefore during the invocation of multiply_by_five on line 9,
# a string object is passed to the function and concatenated with itself 5 times, then that string is returned.
# The fix would be:

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")