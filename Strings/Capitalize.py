# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'

s = 'launch school tech & talk'

print(s.title())

def capitalize_words(s):
    new_string = ' '.join([word.capitalize() for word in s.split()])
    return new_string

print(capitalize_words(s))
