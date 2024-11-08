# Write a function that returns the last element of a list provided as an argument.

def last_element(lst):
    return lst[-1] if lst else None

print(last_element(['Earth', 'Moon', 'Mars']))  # Mars 
print(last_element([])) # None 