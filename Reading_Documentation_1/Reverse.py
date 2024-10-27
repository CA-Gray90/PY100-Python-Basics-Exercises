# Is there a method to reverse a string?

string = 'hello'

print(string[::-1]) # Using index slicing

reversed_string_list = reversed(string)         # Using reversed function, which must be evaluated to a list, then converted back to a string using .join() method
reversed_string = ''.join(reversed_string_list)

print(reversed_string)

reversed_string = ''

for char in reversed(string):
    reversed_string += char

print(reversed_string)
