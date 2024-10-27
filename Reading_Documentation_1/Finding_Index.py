# Finding the index of an element in a list
# How would we find the index of `cherry`?

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

if 'cherry' in fruits:                      # Using an if conditional to avoid a value error if 'cherry' does not exist in the list
    cherry_index = fruits.index('cherry')
    print(f'The index of "cherry" is at {cherry_index}')
else:
    print('"cherry" is not in fruits')
