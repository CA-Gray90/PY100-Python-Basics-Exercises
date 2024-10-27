# Use .rjust() to print a string right justified in a string of specified width. First, print with default padding, then change the default padding to '*'

s = 'string'
width = 10

print(s.rjust(width))
print(s.rjust(width, '*'))