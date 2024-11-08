# Write a function that returns the first element of a list provided as an argument

def first_element(lst):
    return lst[0] if lst else 'Empty List'

print(first_element(['Earth', 'Moon', 'Mars']))  # Earth
print(first_element([])) # Empty List