# Write some code that creates and prints a string that contains each portion of the passcode separated by hyphens (-)

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

print('-'.join(passcode))

complete_passcode = ''
for string in passcode:
    complete_passcode += f'{string}-'

complete_passcode = complete_passcode.strip('-')

print(complete_passcode)

# joined_string = ''
# for i in range(len(passcode)):
#     if i > 0:
#         joined_string += '-'
    
#     joined_string += passcode[i]

joined_string = ''
for i in range(len(passcode)):
    joined_string += passcode[i]
    
    if i != len(passcode) - 1:
        joined_string += '-'

# joined_string = ''
# index = 0
# while index < len(passcode):
#     joined_string += passcode[index]
#     if index == len(passcode) - 1:
#         break
#     joined_string += '-'
#     index += 1

# joined_string = ''
# index = 0
# while index < len(passcode):
#     if index != 0:
#         joined_string += f'-{passcode[index]}'
#     else:
#         joined_string += passcode[index]

#     index += 1

print(joined_string)