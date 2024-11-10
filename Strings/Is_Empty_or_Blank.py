# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces:

def is_empty_or_blank(s):
    return not (bool(s) and any(s.split(' ')))

# def is_empty_or_blank(s):
#     if bool(s):
#         is_space_list = [char == ' ' for char in s]
#         return any(is_space_list)
#     else:
#         return not s
    
# LS Solution using string method .strip(' ')
# def is_empty_or_blank(s):
#     return not s.strip()

# LS Student solutions:

# def is_empty_or_blank(word):
#     return word == ' '*len(word)          # Creates a string consisting of spaces that is the length of the word and checks against that.

# def is_empty_or_blank(str):
#     return not str or str.isspace()       # Uses the inbuilt method .isspace() to return a boolean if the string consists only of white space.

 
print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True