# def get_quote(person):
#     if person == 'Yoda':
#         'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')

# Problem with the above code: There are no return values specified in the function, so it by default returns None. 

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    elif person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    elif person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
    else:
        return 'No quote for name entered'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')