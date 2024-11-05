# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.
string = 'Captain Ruby'

# lst = string.split()
# lst[1] = 'Python'
# new_string = ' '.join(lst)

# print(new_string)

# new_string = string.replace('Ruby', 'Python')

# new_string = string.split()[0] + ' Python'

new_string = string[:string.find('Ruby')] + 'Python'
print(new_string)