# Write a function that checks whether a string is empty or not

# def is_empty(string):
#     return string == ''

def is_empty(string):
    return (not bool(string))

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True